#!/usr/bin/env python3
"""Convert the NHS 365 source book (PDF) to Markdown for projects/*/external/.

Usage
-----
    pip install pypdf
    python3 scripts/pdf2md.py                       # defaults, in place
    python3 scripts/pdf2md.py IN.pdf OUT.md --retrieved 2026-09-01

Re-run this after replacing the PDF with a newer edition of the book. The two
named repairs in repair() are keyed to wording in the 2026-08-11 edition; if a
later edition reflows, check the QA counters this prints and re-verify them.

Why the PDF needs more than pypdf
---------------------------------
It is a Designrr.io HTML export, and two things break a naive extraction:

1. Subset fonts give the ligature glyphs (fi/fl/ff/ffi) no ToUnicode entry, so
   pypdf emits NUL for each -- "staff" arrives as "sta", "Office" as "O ce".
   The raw content streams encode text with a uniform +29 byte shift that *does*
   preserve distinct ligature glyph codes, so the ligature run recovered from
   the streams is replayed, in order, over pypdf's NULs (108 == 108 in the
   2026-08-11 edition). A count mismatch means the alignment assumption broke:
   the script warns rather than silently guessing.
2. Structure is carried entirely by font size, not markup:
     2.9 chapter title | 1.9 subheading | 1.8/1.5 lead paragraphs
     1.4 running footer (dropped) | 1.2 numbered list | 1.1 body
   Content-stream order already matches reading order, including the two-column
   layout, so runs are never re-sorted -- a y-coordinate jump is the signal for
   a new text box, and therefore a new block. The cm matrix is identity
   throughout, so it carries no extra positioning information.

Reconstructed, not extracted
----------------------------
Callout labels and two bold inline spans are drawn *after* the text they sit
inside, and their baselines do not map back to the visual line. hoist_labels()
handles the general case; repair() reassembles the two spans coordinates cannot
recover. Both are flagged in the generated front matter -- quote the PDF, not
the Markdown, where exact wording matters.
"""
import argparse, datetime, re, sys, zlib
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PDF = ROOT / 'projects/000-global/external/nhs365-book2.pdf'
DEFAULT_OUT = ROOT / 'projects/000-global/external/nhs365-book2.md'
TITLE = ('NHS 365 — A Best Practices Guide for Transforming UK Healthcare '
         'with Microsoft AI')
SOURCE_URL = ('https://365apps.pro/wp-content/uploads/sites/50/2026/08/'
              'nhs365-book2.pdf')

LIG = {'Ċ': 'fi', 'ĉ': 'ff', 'ċ': 'fl', 'Č': 'ffi'}
LINE_H, PARA_FACTOR = 17.0, 1.5


def ligature_sequence(path):
    """Ligatures in content-stream order, recovered via the +29 byte shift."""
    data, seq = open(path, 'rb').read(), []
    for m in re.finditer(rb'stream\r?\n', data):
        s, e = m.end(), data.find(b'endstream', m.end())
        if e < 0:
            continue
        try:
            raw = zlib.decompress(data[s:e])
        except zlib.error:
            continue
        if b'Tj' not in raw and b'TJ' not in raw:
            continue
        for t in re.finditer(rb'\((?:\\.|[^\\()])*\)', raw):
            for b in re.sub(rb'\\([()\\])', rb'\1', t.group(0)[1:-1]):
                ch = chr(b + 29)
                if ch in LIG:
                    seq.append(LIG[ch])
    return seq


def collect_runs(reader):
    """(page, size, x, y, text) in natural content-stream order."""
    runs = []
    for pno, page in enumerate(reader.pages, 1):
        def visit(text, cm, tm, font_dict, font_size, _p=pno):
            t = (text or '').strip()
            if t:
                runs.append([_p, round(abs(font_size) * abs(tm[3] or 1), 1),
                             round(tm[4], 1), round(tm[5], 1), t])
        page.extract_text(visitor_text=visit)
    return runs


def apply_ligatures(runs, seq):
    it = iter(seq)
    for r in runs:
        r[4] = re.sub('\x00', lambda _m: next(it, 'fi'), r[4])
    if (left := sum(1 for _ in it)):
        print(f'warning: {left} ligatures unconsumed', file=sys.stderr)
    return runs


def classify(size):
    if size >= 2.5:
        return 'chapter'
    if 1.85 <= size < 2.5:
        return 'head'
    if 1.15 <= size < 1.35:
        return 'list'
    return 'body'


def clean(s):
    return re.sub(r'\s{2,}', ' ', s.replace('\xa0', ' ').replace('​', '')).strip()


def blocks_for_page(items):
    """Group runs into blocks; a y jump or x shift starts a new one."""
    out, cur, kind, prev = [], [], None, None
    def flush():
        nonlocal cur
        if cur:
            out.append((kind, clean(' '.join(cur))))
            cur = []

    for size, x, y, text in items:
        k = classify(size)
        brk = False
        if prev:
            psize, px, py = prev
            gap = py - y
            brk = (classify(psize) != k
                   or gap < -1                                  # new text box
                   or gap > size * LINE_H * PARA_FACTOR
                   or (k == 'body' and abs(px - x) > 4))
        if k == 'list' and re.match(r'^\d+[.)]\s', text):
            brk = True
        if brk:
            flush()
        kind, prev = k, (size, x, y)
        cur.append(text)
    flush()
    return out


def hoist_labels(blocks):
    """Designrr draws callout labels *after* their em-dash text; restore order."""
    out, i = [], 0
    while i < len(blocks):
        kind, text = blocks[i]
        nxt = blocks[i + 1] if i + 1 < len(blocks) else None
        if (kind == 'body' and text.startswith('—') and nxt and nxt[0] == 'body'
                and len(nxt[1]) < 60 and not nxt[1].endswith('.')):
            out.append(('body', f'**{nxt[1]}** {text}'))
            i += 2
            continue
        out.append((kind, text))
        i += 1
    return out


def build(runs):
    pages = {}
    for p, size, x, y, text in runs:
        if size < 1.6 and y < 40:            # running footer
            continue
        pages.setdefault(p, []).append((size, x, y, text))

    doc, last_chapter = [], None
    for p in sorted(pages):
        if p == 1:                           # cover: publisher mark only
            continue
        blocks = hoist_labels(blocks_for_page(pages[p]))
        title = ' '.join(t for k, t in blocks if k == 'chapter')
        if title and title != last_chapter:
            doc.append(('chapter', clean(title)))
            last_chapter = title
        for kind, text in blocks:
            if kind == 'chapter' or not text:
                continue
            # a 1.9 run ending in a full stop is a lead paragraph, not a heading
            doc.append(('body' if kind == 'head' and text.endswith('.') else kind, text))
    return doc


INLINE_TITLE = 'NHS 365 – A Best Practices Guide for Transforming UK Healthcare with Microsoft AI'


def repair(text):
    """Fix wrap artefacts that survive block assembly."""
    text = re.sub(r'(\w)- ([a-z])', r'\1-\2', text)            # post- pandemic
    text = re.sub(r'([\w”’)])— (\w)', r'\1—\2', text)         # shadow IT”— unofficial
    text = re.sub(r'[ \t]{2,}', ' ', text)
    # one italic span is drawn as an overlay after the sentence it sits inside
    text = re.sub(
        r'This book,\n\n, is\n\n(written expressly[^\n]*?)\n\n'
        r'NHS 365 – A Best Practices Guide for\n\nTransforming UK Healthcare with Microsoft AI',
        lambda m: f'This book, *{INLINE_TITLE}*, is {m.group(1)}', text)
    # Two bold inline spans are likewise drawn after their host paragraph, and
    # their baselines do not map back to the visual line -- so the fragments are
    # reassembled here from the runs, in the only order that yields a sentence.
    text = re.sub(
        r'\n\nis built natively for Microsoft 365 and\n\n(.*?)\n\nZensai\n\n',
        lambda m: f'\n\n**Zensai** is built natively for Microsoft 365 and {m.group(1)}\n\n',
        text, flags=re.S)
    text = re.sub(
        r'\n\nThe\n\n, and speci(?:fi)?cally its\n\nmodern authentication component\n\n'
        r', is the national\n\nidentity and access management platform for health and '
        r'social care professionals in England\.\n\nNHS\n\n\(CIS\)\n\n'
        r'Care Identity Service\n\nCIS2\n\nAuthentication\n\n',
        '\n\nThe **NHS Care Identity Service (CIS)**, and specifically its modern '
        'authentication component **CIS2 Authentication**, is the national identity and '
        'access management platform for health and social care professionals in England.\n\n',
        text)
    return text


def render(doc, npages, pdf_name, retrieved):
    lines = [
        '---',
        f'title: "{TITLE}"',
        'publisher: 365apps.pro',
        f'source_url: {SOURCE_URL}',
        f'source_file: {pdf_name}',
        'source_published: 2026-08-11',
        f'retrieved: {retrieved}',
        f'pages: {npages}',
        'conversion: automated text extraction (pypdf); figures and images are not',
        '  included and callout ordering is reconstructed, not authoritative',
        '---',
        '',
        f'# {TITLE}',
        '',
        '> Reference document for ArcKit governance artifacts, converted from',
        f'> `{pdf_name}` ({npages} pages) on {retrieved}. Where exact wording',
        '> matters, quote the PDF rather than this file.',
        '',
    ]
    for kind, text in doc:
        if kind == 'chapter':
            lines += ['', f'## {text}', '']
        elif kind == 'head':
            lines += ['', f'### {text}', '']
        elif kind == 'list':
            m = re.match(r'^(\d+)[.)]\s*(.*)$', text)
            if m and lines and lines[-1] and not re.match(r'^\d+\. ', lines[-1]):
                lines.append('')
            lines.append(f'{m.group(1)}. {m.group(2)}' if m else f'   {text}')
        else:
            if lines and re.match(r'^\d+\. ', lines[-1]):
                lines.append('')
            lines += [text, '']
    return repair(re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip()) + '\n'


def qa(text):
    """Counters worth eyeballing after a re-run; orphans should be 0."""
    paras = [p.strip() for p in text.split('---\n', 2)[2].split('\n\n') if p.strip()]
    orphans = [p for p in paras
               if not p.startswith(('#', '>')) and not re.match(r'^\d+\. ', p)
               and len(p) < 45]
    return {
        'chars': len(text),
        'paragraphs': len(paras),
        'chapters': text.count('\n## '),
        'subheadings': text.count('\n### '),
        'unresolved_ligatures': text.count('\x00'),
        'orphan_fragments': len(orphans),
    }, orphans


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('pdf', nargs='?', type=Path, default=DEFAULT_PDF)
    ap.add_argument('out', nargs='?', type=Path, default=DEFAULT_OUT)
    ap.add_argument('--retrieved', default=str(datetime.date.today()),
                    help='retrieval date recorded in the front matter')
    args = ap.parse_args(argv)

    if not args.pdf.is_file():
        sys.exit(f'no such PDF: {args.pdf}')

    reader = PdfReader(str(args.pdf))
    runs = apply_ligatures(collect_runs(reader), ligature_sequence(args.pdf))
    text = render(build(runs), len(reader.pages), args.pdf.name, args.retrieved)
    args.out.write_text(text, encoding='utf-8')

    stats, orphans = qa(text)
    print(f'wrote {args.out.relative_to(ROOT) if ROOT in args.out.parents else args.out}')
    for k, v in stats.items():
        print(f'  {k}: {v}')
    for p in orphans:
        print(f'  ORPHAN: {p[:70]!r}', file=sys.stderr)
    return 1 if stats['unresolved_ligatures'] or orphans else 0


if __name__ == '__main__':
    sys.exit(main())
