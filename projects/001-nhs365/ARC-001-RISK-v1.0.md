# Risk Register: NHS 365

> **Template Origin**: Official | **ArcKit Version**: 6.11.0 | **Command**: `/arckit:risk`

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ARC-001-RISK-v1.0 |
| **Document Type** | Risk Register (HM Treasury Orange Book 2023) |
| **Project** | NHS 365 (Project 001) |
| **Classification** | OFFICIAL |
| **Status** | DRAFT |
| **Version** | 1.0 |
| **Created Date** | 2026-08-19 |
| **Last Modified** | 2026-08-19 |
| **Review Cycle** | Monthly |
| **Next Review Date** | 2026-09-18 |
| **Owner** | Mark Craddock, Enterprise Architect |
| **Reviewed By** | PENDING |
| **Approved By** | PENDING |
| **Distribution** | NHS 365 programme board; Trust executive team; Audit and Risk Committee; Clinical Safety Officer; Caldicott Guardian; SIRO; staff-side representatives |

## Revision History

| Version | Date | Author | Changes | Approved By | Approval Date |
|---------|------|--------|---------|-------------|---------------|
| 1.0 | 2026-08-19 | ArcKit AI | Initial creation from `/arckit:risk` command. Consolidates R-1…R-7 from `ARC-001-STKE-v1.0` and RQ-1…RQ-7 from `ARC-001-REQ-v1.0` into a single Orange Book register, and adds 8 risks not previously captured. | PENDING | PENDING |

---

## Executive Summary

### Risk Profile Overview

**Total risks identified**: 20, across all six Orange Book categories.

This register supersedes two earlier, overlapping risk sets that were beginning to drift apart: `R-1…R-7` in the stakeholder analysis and `RQ-1…RQ-7` in the requirements. Those nine distinct risks are carried forward here with their original references preserved; eleven further risks were identified during consolidation, principally in the compliance, reputational, and technology categories, which the earlier sets under-covered.

| | Inherent | Residual |
|---|---|---|
| 🟥 Critical (20-25) | 2 | 0 |
| 🟧 High (13-19) | 6 | 0 |
| 🟨 Medium (6-12) | 12 | 18 |
| 🟩 Low (1-5) | 0 | 2 |
| **Aggregate score** | **265** / 500 | **148** / 500 |

**Risk reduction from controls**: 44% (265 → 148)

### ⚠ Control Maturity Caveat — read before relying on the residual scores

**The residual scores above assume the specified controls are implemented and verified. Almost none of them are yet.**

The controls credited in this register are, in the main, requirements in `ARC-001-REQ-v1.0` that have been *specified* rather than *built* — the technical safety gate (FR-018), the human review enforcement (FR-002), the identifier-sharing controls (FR-011), the retention configuration (FR-012), and the drift detection (FR-004) are all design commitments at this point. Several depend on a Clinical Safety Officer who has not been appointed (dependency D-1).

Until each control is implemented and its effectiveness evidenced, the organisation's actual exposure sits much closer to the **inherent** column than the residual one. Every control in this register therefore carries an explicit maturity marker:

- **Implemented** — in place and evidenced
- **Designed** — specified in requirements, not yet built
- **Proposed** — identified here, not yet specified anywhere

At v1.0, of the 71 controls credited across the register: **zero are Implemented**, 54 are Designed, and 17 are Proposed. Treat the residual column as a target state, not a current position, and re-score at each monthly review as controls move to Implemented.

### Risk Category Distribution

| Category | Risks | Avg Inherent | Avg Residual | Control Reduction |
|----------|-------|--------------|--------------|-------------------|
| STRATEGIC | 4 | 14.0 | 7.5 | 46% |
| OPERATIONAL | 4 | 12.0 | 6.3 | 48% |
| FINANCIAL | 2 | 10.5 | 7.0 | 33% |
| COMPLIANCE | 4 | 14.8 | 8.0 | 46% |
| REPUTATIONAL | 2 | 12.0 | 6.5 | 46% |
| TECHNOLOGY | 4 | 14.3 | 8.5 | 40% |

### Overall Risk Assessment

**Overall risk profile: CONCERNING**

No risk remains Critical or High once designed controls are credited, which on its face is reassuring. Three findings qualify that:

1. **Six risks exceed provisional risk appetite** (see below), and three of those six concern patient safety, where appetite is necessarily lowest.
2. **Control maturity is zero.** Nothing has yet been built. The 44% reduction is a forecast.
3. **Two risks are Critical at inherent level and both concern patient safety** — R-001 (assurance gate overridden) and R-017 (clinical error accepted into the record). These are the risks the programme exists to manage, and neither can be tolerated at inherent level.

### Risks Exceeding Appetite

No ratified organisational risk appetite statement exists for this programme. The thresholds below are **provisional**, proposed here for board ratification, and calibrated to an NHS clinical context — where appetite for patient-safety risk is materially lower than for delivery or financial risk.

| Category | Provisional Threshold | Risks Within | Risks Exceeding |
|----------|----------------------|--------------|-----------------|
| Clinical safety / patient harm | Very Low (≤ 4) | 0 | 3 (R-001, R-013, R-017) |
| COMPLIANCE / Regulatory | Low (≤ 6) | 1 | 3 (R-011, R-013, R-014) |
| REPUTATIONAL | Low (≤ 6) | 1 | 1 (R-015) |
| TECHNOLOGY | Medium (≤ 9) | 4 | 0 |
| OPERATIONAL | Medium (≤ 12) | 4 | 0 |
| FINANCIAL | Medium (≤ 12) | 2 | 0 |
| STRATEGIC | Medium (≤ 12) | 4 | 0 |

**6 unique risks exceed provisional appetite**: R-001, R-011, R-013, R-014, R-015, R-017. All require escalation to the Trust Board with a documented acceptance decision, or further treatment.

> **Action required**: the Audit and Risk Committee should ratify or amend these thresholds. Until it does, "exceeds appetite" is an architect's judgement rather than an organisational position, and the six escalations above cannot be formally closed.

### Top 5 Risks Requiring Immediate Attention

| Rank | ID | Title | Category | Inherent | Residual | Owner |
|------|-----|-------|----------|----------|----------|-------|
| 1 | R-017 | Generated clinical error accepted into the record | TECHNOLOGY | 🟥 20 | 🟨 10 | Clinical Safety Officer |
| 2 | R-001 | Clinical safety gate overridden by delivery pressure | STRATEGIC | 🟥 20 | 🟨 10 | Trust Chief Executive |
| 3 | R-013 | Drift into clinical use triggers unapproved SaMD status | COMPLIANCE | 🟧 15 | 🟨 10 | Clinical Safety Officer |
| 4 | R-015 | AI-attributable harm becomes a national news story | REPUTATIONAL | 🟧 15 | 🟨 10 | Trust Chief Executive |
| 5 | R-005 | Assurance and RA capacity unfunded, becoming the bottleneck | OPERATIONAL | 🟧 16 | 🟨 9 | Trust Chief Executive |

### Key Findings and Recommendations

1. **The top four risks share one root cause**: the gap between what a tool is approved to do and what staff actually use it for. R-001, R-013, R-015, and R-017 are four faces of clinical drift. The single highest-value intervention is not four separate mitigations but one working drift-detection capability (FR-004) — which is itself at risk (R-018).

2. **Three risks are concentrated on an unappointed post.** R-001, R-013, and R-017 all name the Clinical Safety Officer as owner or action owner, and no CSO has been appointed (D-1). Until that appointment is made and funded, the programme's three highest-scoring risks have no effective owner — which is itself the most urgent finding in this register.

3. **Risk ownership is heavily concentrated.** The Trust Chief Executive owns 3 of the 20 risks and is the escalation point for a further 4 — and is owner or escalation point for **all five** of the top five. This is appropriate for accountability but makes one person the single decision bottleneck on the programme's critical path; the Audit and Risk Committee should consider whether escalation for R-011 and R-014 could rest with the SIRO alone.

4. **The controls the register credits do not yet exist.** Prioritise moving the six controls behind the top five risks from Designed to Implemented before wave 1, rather than spreading effort evenly across all 35.

5. **Ratify the appetite statement.** Six exceedances cannot be formally escalated or accepted against thresholds nobody has approved.

---

## A. Risk Matrix Visualization

### Inherent Risk Matrix (Before Controls)

```text
                                          IMPACT
              1-Negligible  2-Minor   3-Moderate    4-Major      5-Catastrophic
            ┌────────────┬───────────┬───────────┬──────────────┬──────────────┐
5-Almost    │            │           │           │              │              │
Certain     │     5      │    10     │    15     │      20      │      25      │
            ├────────────┼───────────┼───────────┼──────────────┼──────────────┤
            │            │  R-007    │  R-002    │  R-005 R-011 │  R-001       │
4-Likely    │            │           │  R-006    │  R-012 R-020 │  R-017       │
            │     4      │     8     │    12     │      16      │      20      │
L           ├────────────┼───────────┼───────────┼──────────────┼──────────────┤
I           │            │           │  R-009    │  R-003 R-004 │  R-013       │
K 3-Possible│            │           │  R-016    │  R-008 R-010 │  R-015       │
E           │            │           │  R-019    │  R-014 R-018 │              │
L           │     3      │     6     │     9     │      12      │      15      │
I           ├────────────┼───────────┼───────────┼──────────────┼──────────────┤
H           │            │           │           │              │              │
O 2-Unlikely│     2      │     4     │     6     │       8      │      10      │
O           ├────────────┼───────────┼───────────┼──────────────┼──────────────┤
D           │            │           │           │              │              │
  1-Rare    │     1      │     2     │     3     │       4      │       5      │
            └────────────┴───────────┴───────────┴──────────────┴──────────────┘

Legend:  Critical (20-25)   High (13-19)   Medium (6-12)   Low (1-5)
Inherent totals: 2 Critical, 6 High, 12 Medium, 0 Low
```

### Residual Risk Matrix (After Controls)

```text
                                          IMPACT
              1-Negligible  2-Minor   3-Moderate    4-Major      5-Catastrophic
            ┌────────────┬───────────┬───────────┬──────────────┬──────────────┐
5-Almost    │            │           │           │              │              │
Certain     │     5      │    10     │    15     │      20      │      25      │
            ├────────────┼───────────┼───────────┼──────────────┼──────────────┤
4-Likely    │            │           │           │              │              │
            │     4      │     8     │    12     │      16      │      20      │
L           ├────────────┼───────────┼───────────┼──────────────┼──────────────┤
I           │            │  R-002    │  R-005    │              │              │
K 3-Possible│            │           │  R-018    │              │              │
E           │            │           │  R-020    │              │              │
L           │     3      │     6     │     9     │      12      │      15      │
I           ├────────────┼───────────┼───────────┼──────────────┼──────────────┤
H           │            │  R-007    │  R-004    │  R-003 R-010 │  R-001 R-013 │
O 2-Unlikely│            │           │  R-006    │  R-011 R-014 │  R-015 R-017 │
O           │            │           │  R-008    │              │              │
D           │            │           │  R-009    │              │              │
            │            │           │  R-012    │              │              │
            │            │           │  R-019    │              │              │
            │     2      │     4     │     6     │       8      │      10      │
            ├────────────┼───────────┼───────────┼──────────────┼──────────────┤
            │            │           │  R-016    │              │              │
  1-Rare    │     1      │     2     │     3     │       4      │       5      │
            └────────────┴───────────┴───────────┴──────────────┴──────────────┘

Legend:  Critical (20-25)   High (13-19)   Medium (6-12)   Low (1-5)
Residual totals: 0 Critical, 0 High, 18 Medium, 2 Low
```

**Movement summary** — the pattern is consistent: controls reduce *likelihood* but rarely *impact*. A clinical error is just as harmful whether or not a review step existed; the control makes it less likely to reach the patient, not less serious if it does.

| Risk | Inherent | Residual | Movement |
|------|----------|----------|----------|
| R-001 | 🟥 20 (L4×I5) | 🟨 10 (L2×I5) | Critical → Medium; likelihood halved, impact unchanged |
| R-017 | 🟥 20 (L4×I5) | 🟨 10 (L2×I5) | Critical → Medium; likelihood halved, impact unchanged |
| R-005 | 🟧 16 (L4×I4) | 🟨 9 (L3×I3) | High → Medium |
| R-011 | 🟧 16 (L4×I4) | 🟨 8 (L2×I4) | High → Medium; impact unchanged |
| R-012 | 🟧 16 (L4×I4) | 🟨 6 (L2×I3) | High → Medium |
| R-020 | 🟧 16 (L4×I4) | 🟨 9 (L3×I3) | High → Medium |
| R-013 | 🟧 15 (L3×I5) | 🟨 10 (L2×I5) | High → Medium; impact unchanged |
| R-015 | 🟧 15 (L3×I5) | 🟨 10 (L2×I5) | High → Medium; impact unchanged |
| R-016 | 🟨 9 (L3×I3) | 🟩 3 (L1×I3) | Medium → Low — the largest proportional reduction, and the cheapest |

---

## B. Top 10 Risks (Ranked by Residual Score)

| Rank | ID | Title | Category | Inherent | Residual | Owner | Status | Response |
|------|-----|-------|----------|----------|----------|-------|--------|----------|
| 1 | R-017 | Generated clinical error accepted into the record | TECHNOLOGY | 20 | 10 | Clinical Safety Officer | Open | Treat |
| 2 | R-001 | Clinical safety gate overridden by delivery pressure | STRATEGIC | 20 | 10 | Trust Chief Executive | Open | Treat |
| 3 | R-013 | Drift into clinical use triggers unapproved SaMD status | COMPLIANCE | 15 | 10 | Clinical Safety Officer | Open | Terminate |
| 4 | R-015 | AI-attributable harm becomes a national news story | REPUTATIONAL | 15 | 10 | Trust Chief Executive | Open | Treat |
| 5 | R-005 | Assurance and RA capacity unfunded | OPERATIONAL | 16 | 9 | Trust Chief Executive | Open | Treat |
| 6 | R-018 | Drift detection cannot distinguish administrative from clinical use | TECHNOLOGY | 12 | 9 | CCIO | Open | Treat |
| 7 | R-020 | Shadow AI adopted outside the assessed boundary | TECHNOLOGY | 16 | 9 | CISO | Open | Treat |
| 8 | R-003 | Tenancy model decided by default | STRATEGIC | 12 | 8 | CIO / CDIO | Open | Treat |
| 9 | R-010 | Released time booked as a cash saving | FINANCIAL | 12 | 8 | Chief People Officer | Open | Treat |
| 10 | R-011 | Patient identifiable data disclosed via collaboration | COMPLIANCE | 16 | 8 | Caldicott Guardian | Open | Treat |

---

## C. Detailed Risk Register

> Each control carries a maturity marker — **Implemented** (in place and evidenced), **Designed** (specified in requirements, not built), or **Proposed** (identified here only). At v1.0 no control is Implemented; see the Control Maturity Caveat.

### Risk R-001: Clinical safety gate overridden by delivery pressure

**Category:** STRATEGIC
**Status:** Open
**Risk Owner:** Trust Chief Executive (from Stakeholder RACI: Accountable for go/no-go per wave)
**Action Owner:** Delivery Manager
**Supersedes:** STKE R-1, REQ RQ-1

#### Risk Identification

**Risk Description:**
A deployment wave is enabled without an approved clinical safety case, or with a safety case signed under schedule pressure rather than on evidence. The national target of approximately 505,000 staff by October 2026 [NB-C1] creates sustained pressure on a gate that cannot be compressed without being weakened.

**Root Cause:**
The delivery deadline is externally fixed and politically visible; the assurance work is evidence-bound and takes as long as hazard assessment takes. The two are not reconcilable at the margin, and the pressure falls on the party with less institutional power.

**Trigger Events:**

- A wave falls behind schedule and the safety case is the visible critical path
- Clinical Safety Officer capacity is unavailable at the point a wave is ready (see R-005)
- Ambiguity over whether a given deployment is in clinical scope allows the gate to be bypassed by reclassification
- National reporting singles the organisation out as a laggard

**Consequences if Realized:**

- Deployment proceeds with unassessed clinical hazards live in production
- Breach of DCB0160, which requires residual risk to be reduced to as low as reasonably practicable before go-live [NB-C2]
- The Clinical Safety Officer's professional position becomes untenable; likely resignation from the role
- Any subsequent patient harm is materially harder to defend at inquest or CQC inspection
- Precedent set that the gate is negotiable, degrading every subsequent wave

**Affected Stakeholders:**

- **Clinical Safety Officer** (STKE SD-4): personal, professionally registered accountability is bypassed
- **Trust Chief Executive** (SD-16): carries the asymmetric downside of a local failure
- **Frontline clinicians** (SD-10): exposed to unassessed hazards in their own workflow
- **Patients**: ultimate bearers of the consequence

**Related Objectives:**

- **STKE G-1** (Establish clinical safety governance before first deployment): directly negated
- **STKE O-2** (No AI-attributable clinical harm): the principal route to failure
- **REQ BR-001, BR-003**: both depend on the gate holding

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 4 - Likely | Fixed external deadline against non-compressible assurance work, with the assurance party holding less institutional power. Without a technical gate this is the default outcome under pressure, not an aberration. |
| **Impact** | 5 - Catastrophic | Regulatory breach, unassessed hazards live, loss of the CSO role, and materially weakened defensibility of any subsequent harm. |
| **Inherent Risk Score** | **20** (Critical) | 4 × 5 = 20 |

**Risk Zone:** 🟥 Critical (20-25)

#### Current Controls and Mitigations

1. **Technical enforcement of the gate** (REQ FR-018): deployment tooling blocks enablement for any wave lacking recorded CSO approval and SIRO acceptance. Overrides require named executive authorisation and are logged immutably.
   - Owner: Delivery Manager
   - Maturity: **Designed** — specified, not built
   - Effectiveness (once implemented): **Strong** — converts a process step into a control that cannot be quietly skipped

2. **Scope phasing** (STKE Conflict C-1): administrative-only cohorts, whose intended-use boundary excludes clinical workflows, deploy at national pace under a lighter safety case; clinical-adjacent deployment gates separately on evidence.
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Strong** — removes most of the pressure rather than resisting it

3. **Escalation visibility**: any date-over-gate decision escalates to the programme board and is minuted, never absorbed at delivery level.
   - Owner: Trust Chief Executive
   - Maturity: **Proposed**
   - Effectiveness: **Adequate** — does not prevent the decision, but prevents it being taken invisibly

**Overall Control Effectiveness:** Strong once implemented — reduces likelihood from 4 to 2. Impact is unchanged: if the gate is overridden, the consequence is identical.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | A technical block plus phased scope removes both the means and most of the motive. Residual likelihood reflects the deliberate override path, which remains available to a named executive. |
| **Impact** | 5 - Catastrophic | Unchanged. The control makes an override less likely, not less serious. |
| **Residual Risk Score** | **10** (Medium) | 2 × 5 = 10 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 50% reduction from inherent (20 → 10)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:**
The risk cannot be tolerated at inherent level and the underlying activity is the programme itself, so termination is not viable. Treatment through a technical gate and phased scope addresses both means and motive at modest cost.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — a Critical patient-safety risk cannot be accepted, and DCB0160 is statutory guidance rather than an organisational preference
- **Transfer**: Not available — clinical safety accountability cannot be contracted out
- **Terminate**: Rejected — would mean not deploying at all

#### Risk Appetite Assessment

**Provisional appetite for clinical safety / patient harm risks:** Very Low (Score ≤ 4)
**Current Residual Risk Score:** 10 (Medium)
**Assessment:** ❌ **Significantly exceeds appetite** — 2.5× the threshold

**Justification:**
The residual is driven entirely by catastrophic impact, which no control can reduce. Bringing this within a Very Low appetite would require likelihood 1 (Rare), which is achievable only by removing the override path entirely. That is a board decision: whether any executive should be able to override a clinical safety gate.

**Escalation Required:** Yes — Trust Board, with an explicit decision on whether the override path in FR-018 should exist at all.

#### Action Plan

**Additional Mitigations Needed:**

1. **Appoint and fund the Clinical Safety Officer**
   - Description: Substantive appointment with allocated time, not an unfunded addition to a clinical role (dependency D-1)
   - Owner: Trust Chief Executive
   - Due Date: 2026-09-30
   - Expected Impact: Prerequisite for every other control; without it likelihood returns to 4

2. **Board decision on the override path**
   - Description: Determine whether FR-018 should permit executive override at all, or whether the gate is absolute
   - Owner: Trust Chief Executive
   - Due Date: 2026-10-31
   - Expected Impact: If removed, reduces likelihood from 2 to 1, giving residual 5 (Low)

3. **Publish the intended-use boundary before wave 1**
   - Description: Removes the reclassification route that lets a clinical deployment be relabelled as administrative
   - Owner: CCIO
   - Due Date: 2026-10-15
   - Expected Impact: Closes the ambiguity trigger

**Target Residual Risk After Mitigations:**

- Target Likelihood: 1 (Rare) — contingent on the board removing the override path
- Target Impact: 5 (Catastrophic) — irreducible
- Target Score: 5 (Low) ✅ Within a Very Low appetite at the boundary

**Success Criteria:**

- 100% of waves have CSO approval recorded before first enablement
- Zero overrides exercised; any override minuted at board level within 5 working days
- Median CSO engagement-to-go-live lead time of 8 weeks or more

**Monitoring Plan:**

- **Frequency:** Every wave gate, plus monthly at programme board
- **Key Indicators:** waves gated before enablement (%); override count; CSO lead time
- **Escalation Triggers:** any override; any wave where the gate becomes the critical path

---

### Risk R-002: Measured benefit materially below the national pilot figure

**Category:** STRATEGIC
**Status:** Open
**Risk Owner:** National Programme SRO (Stakeholder RACI: Accountable for benefit measurement method)
**Action Owner:** Local programme lead
**Supersedes:** STKE R-2, REQ RQ-2

#### Risk Identification

**Risk Description:**
Locally measured time savings fall well short of the 43 minutes per person per day reported from the national pilot [NB-C1], and no explanation has been prepared. The pilot involved 30,000 staff who volunteered for an AI trial; the deployment population of approximately 505,000 is mandated and cannot be assumed comparable.

**Root Cause:**
A headline figure derived from a self-selecting cohort has become the public benchmark for a mandated rollout, without the selection effect being acknowledged at the point the figure entered circulation.

**Trigger Events:**

- First quarterly benefit report shows a materially lower figure
- A comparable organisation publishes a lower result first
- Baseline capture was skipped for major cohorts (see R-006), leaving the variance unexplainable

**Consequences if Realized:**

- Programme credibility damaged for this deployment and the next
- Value-for-money challenge from Finance, internal audit, or the National Audit Office
- Staff scepticism reinforced where the promised benefit did not materialise in their own experience
- Pressure to overstate results in subsequent reporting

**Affected Stakeholders:**

- **National Programme SRO** (SD-1): accountable for a £120 million commitment against this benchmark
- **Director of Finance** (SD-9): cannot defend recurring licence spend
- **Chief People Officer** (SD-3): loses the workforce narrative
- **Frontline clinicians** (SD-10): experience the gap directly

**Related Objectives:**

- **STKE G-3** (Measure benefit locally): the goal that surfaces this risk
- **STKE O-1, O-6**: both depend on defensible measurement

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 4 - Likely | Volunteer-cohort results routinely exceed mandated-population results. A shortfall is the expected outcome, not a tail risk. |
| **Impact** | 3 - Moderate | Reputational and financial-justification damage requiring significant management effort, but no safety or regulatory consequence. |
| **Inherent Risk Score** | **12** (Medium) | 4 × 3 = 12 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **Local baseline capture before enablement** (REQ FR-015, BR-002): irrecoverable if missed, so enablement is blocked without a recorded baseline or explicit exception.
   - Owner: Local programme lead
   - Maturity: **Designed**
   - Effectiveness: **Strong** — converts an unexplainable shortfall into a measured, attributable variance

2. **Disaggregated reporting by cohort and licence tier** (REQ FR-016): variance is explained by cohort characteristics rather than averaged away.
   - Owner: Local programme lead
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

3. **Expectation setting before measurement**: state publicly that the pilot figure is a ceiling from a volunteer cohort, not a forecast.
   - Owner: National Programme SRO
   - Maturity: **Proposed**
   - Effectiveness: **Strong** — the cheapest and most effective control available, and only available before the first report

**Overall Control Effectiveness:** Adequate — reduces likelihood modestly and impact substantially, because a predicted and explained shortfall is a very different event from a surprising one.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | The shortfall itself remains likely; what falls is the likelihood of it being *unexplained*, which is the actual risk event. |
| **Impact** | 2 - Minor | A variance that was predicted, measured, and explained is a management matter rather than a credibility failure. |
| **Residual Risk Score** | **6** (Medium) | 3 × 2 = 6 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 50% reduction from inherent (12 → 6)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:**
The shortfall cannot be prevented — it is a property of the two populations. What can be treated is the surprise, through baselining and honest expectation setting.

**Alternative Responses Considered:**

- **Tolerate**: Rejected at inherent level; would be defensible once controls are implemented
- **Transfer**: Not applicable
- **Terminate**: Not viable — would mean not measuring benefit

#### Risk Appetite Assessment

**Provisional appetite for STRATEGIC risks:** Medium (Score ≤ 12)
**Current Residual Risk Score:** 6 (Medium)
**Assessment:** ✅ **Within appetite**

**Justification:** Comfortably within threshold once baselining and expectation setting are in place.

**Escalation Required:** No

#### Action Plan

**Additional Mitigations Needed:**

1. **Publish the expectation-setting position before the first benefit report**
   - Description: Written statement that the pilot figure derives from a volunteer cohort and functions as a ceiling
   - Owner: National Programme SRO
   - Due Date: Before first quarterly report
   - Expected Impact: Reduces impact from 3 to 2

2. **Complete baseline capture for 90% or more of cohorts**
   - Description: Time-and-motion sampling plus diary study, before enablement
   - Owner: Local programme lead
   - Due Date: Before each cohort's enablement
   - Expected Impact: Makes variance explainable; without it this control fails entirely

**Target Residual Risk After Mitigations:**

- Target Likelihood: 3 (Possible), Target Impact: 2 (Minor), Target Score: 6 (Medium) ✅

**Success Criteria:**

- Baselines captured for 90% or more of cohorts before enablement
- Every quarterly report states variance against the pilot figure with a cohort-level explanation
- No benefit claim made for a cohort lacking a baseline

**Monitoring Plan:**

- **Frequency:** Quarterly
- **Key Indicators:** baseline coverage (%); measured minutes by cohort and tier; variance from pilot figure
- **Escalation Triggers:** baseline coverage below 75%; variance exceeding 50% with no explanation

---

### Risk R-003: Tenancy model decided by default rather than by evidence

**Category:** STRATEGIC
**Status:** Open
**Risk Owner:** Chief Information Officer / CDIO (Stakeholder RACI: Responsible for tenancy model selection)
**Action Owner:** Enterprise Architect
**Supersedes:** STKE R-7

#### Risk Identification

**Risk Description:**
Architecture work proceeds on an assumed tenancy model that was never formally decided, and the four stated decision factors — cyber maturity, specialised integration need, legacy clinical systems requiring hybrid identity, and capacity to manage clinical safety governance for AI and automation [NB-C3] — are assessed only retrospectively, once reversal has become expensive.

**Root Cause:**
Tenancy is an infrastructure inheritance rather than a decision anyone remembers making. Absent a forcing gate, delivery proceeds on whatever is already in place.

**Trigger Events:**

- Architecture or integration work begins before the decision record exists
- The legacy clinical system inventory is incomplete when the decision is needed
- A shared-tenancy constraint is discovered only when a clinical integration fails

**Consequences if Realized:**

- Expensive rework, or acceptance of a model that cannot support required clinical integrations
- Ambiguity over which controls are inherited and which are locally owned, undermining the DSPT evidence base (R-014)
- Where an independently managed model is adopted without the governance capacity it requires, all local controls become unowned in practice

**Affected Stakeholders:**

- **CIO / CDIO** (SD-8): owns the consequence either way
- **CISO** (SD-7): inherits a materially different control set
- **Clinical Safety Officer** (SD-4): gains or loses local governance capacity

**Related Objectives:**

- **STKE G-4** (Record an evidenced tenancy decision)
- **REQ BR-007**, dependency **D-3**: dependent architecture work is frozen until this is resolved

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Decision-by-default is the common failure mode for inherited infrastructure, though an active programme reduces it somewhat. |
| **Impact** | 4 - Major | Expensive to reverse, and cascades into security control ownership and clinical integration feasibility. |
| **Inherent Risk Score** | **12** (Medium) | 3 × 4 = 12 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **Decision treated as a gating prerequisite** (REQ BR-007, dependency D-3): dependent architecture work is frozen until the board-approved decision record exists.
   - Owner: Enterprise Architect
   - Maturity: **Designed**
   - Effectiveness: **Strong**

2. **All four decision factors assessed and recorded** (STKE Conflict C-4): including a complete legacy clinical system inventory.
   - Owner: CIO / CDIO
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — depends on inventory completeness

3. **Responsibility and resource approved together**: where an independently managed model is chosen, the additional governance capacity is approved in the same board paper.
   - Owner: Trust Chief Executive
   - Maturity: **Proposed**
   - Effectiveness: **Strong** — prevents the specific failure of choosing autonomy without capacity

**Overall Control Effectiveness:** Adequate — reduces likelihood from 3 to 2; impact is unchanged because a wrong decision remains equally expensive.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | A hard freeze on dependent work makes drifting into a default decision difficult. |
| **Impact** | 4 - Major | Unchanged — the decision remains expensive to reverse whether it was deliberate or not. |
| **Residual Risk Score** | **8** (Medium) | 2 × 4 = 8 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 33% reduction from inherent (12 → 8)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:**
The decision must be made either way; treatment ensures it is made deliberately and on evidence rather than by omission.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — the failure mode is silent and discovered late
- **Transfer**: Not applicable
- **Terminate**: Not viable

#### Risk Appetite Assessment

**Provisional appetite for STRATEGIC risks:** Medium (Score ≤ 12)
**Current Residual Risk Score:** 8 (Medium)
**Assessment:** ✅ **Within appetite**

**Escalation Required:** No — though the decision itself requires board approval

#### Action Plan

**Additional Mitigations Needed:**

1. **Complete the legacy clinical system inventory**
   - Description: Full inventory of systems requiring hybrid identity (dependency D-4)
   - Owner: Clinical systems team
   - Due Date: 2026-09-30
   - Expected Impact: Prerequisite for a defensible decision

2. **Produce the tenancy decision record as an ADR**
   - Description: Architecture Decision Record covering all four factors, the inherited-versus-local control split, and the capacity implication
   - Owner: Enterprise Architect
   - Due Date: 2026-10-15
   - Expected Impact: Unblocks dependent architecture work (D-3)

**Target Residual Risk After Mitigations:**

- Target Likelihood: 1 (Rare), Target Impact: 4 (Major), Target Score: 4 (Low) ✅

**Success Criteria:**

- Board-approved decision record covering all four factors with evidence
- 100% legacy clinical system inventory completeness
- Documented split of inherited versus locally owned controls

**Monitoring Plan:**

- **Frequency:** Fortnightly until decided, then on material change
- **Key Indicators:** inventory completeness (%); decision record status
- **Escalation Triggers:** any architecture work commencing before the decision record is approved

---

### Risk R-004: Digital exclusion and inequitable outcomes

**Category:** STRATEGIC
**Status:** Open
**Risk Owner:** Chief People Officer (Stakeholder RACI: Accountable for workforce impact)
**Action Owner:** CCIO

#### Risk Identification

**Risk Description:**
The benefit of AI assistance accrues disproportionately to staff who are already digitally confident, on modern devices, in well-connected settings — widening rather than narrowing existing inequities. Equity risk is a recognised pitfall of this class of transformation [NB-C4].

**Root Cause:**
Tools designed and piloted with confident volunteers optimise for that population. Clinical environment constraints — gloved hands, shared devices, poor lighting, interruption — and variation in digital confidence are systematically under-represented in design.

**Trigger Events:**

- Benefit measurement shows adoption concentrated in particular staff groups or settings
- Accessibility testing is deferred or performed only in office conditions
- Community and general practice settings receive later or lesser capability than acute settings

**Consequences if Realized:**

- Existing workforce inequities widened by a programme intended to relieve them
- Public sector accessibility obligations breached
- Staff groups excluded from a benefit their colleagues receive, damaging the workforce narrative (R-008)
- Where patient-facing consequences follow, inequitable care outcomes

**Affected Stakeholders:**

- **Frontline clinicians** (SD-10) in less well-resourced settings
- **Administrative staff** (SD-12) with lower digital confidence
- **Chief People Officer** (SD-3): accountable for equitable workforce treatment
- **Patients** in settings that fall behind

**Related Objectives:**

- **STKE O-5** (Workforce confidence)
- **REQ NFR-U-002, NFR-U-003, BR-005** · **PRIN 18** (Accessibility and Digital Inclusion)

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Without deliberate counter-measures this is the default distributional outcome, but the programme has explicit equity requirements. |
| **Impact** | 4 - Major | Regulatory exposure under accessibility regulations, plus reputational and workforce damage from a programme that widens inequity. |
| **Inherent Risk Score** | **12** (Medium) | 3 × 4 = 12 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **WCAG 2.2 Level AA conformance with published statement** (REQ NFR-U-002)
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — necessary but insufficient; conformance does not guarantee equitable adoption

2. **Clinical environment usability testing** (REQ NFR-U-003): testing under gloved-hands, shared-device, interrupted conditions rather than in an office.
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Strong**

3. **Equity impact assessed across affected populations** (PRIN 11, PRIN 18)
   - Owner: Chief People Officer
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

4. **Benefit reporting disaggregated by cohort** (REQ FR-016): makes distributional effects visible rather than hidden in an average.
   - Owner: Local programme lead
   - Maturity: **Designed**
   - Effectiveness: **Strong** — detection, not prevention

**Overall Control Effectiveness:** Adequate — reduces both likelihood and impact, principally by making the distribution visible early enough to correct.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Disaggregated measurement plus clinical-environment testing catch most distributional problems before they entrench. |
| **Impact** | 3 - Moderate | Detected early, inequity becomes a correctable delivery issue rather than a systemic outcome. |
| **Residual Risk Score** | **6** (Medium) | 2 × 3 = 6 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 50% reduction from inherent (12 → 6)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:**
Equity outcomes are a design property, controllable through testing conditions, measurement granularity, and deployment sequencing.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — public sector accessibility obligations are not discretionary
- **Transfer**: Not applicable
- **Terminate**: Not viable

#### Risk Appetite Assessment

**Provisional appetite for STRATEGIC risks:** Medium (Score ≤ 12)
**Current Residual Risk Score:** 6 (Medium)
**Assessment:** ✅ **Within appetite**

**Escalation Required:** No

#### Action Plan

**Additional Mitigations Needed:**

1. **Sequence deployment to include under-served settings early**
   - Description: Ensure community and general practice settings appear in early waves rather than last
   - Owner: Delivery Manager
   - Due Date: Wave planning, 2026-09-30
   - Expected Impact: Prevents entrenchment of a two-tier rollout

2. **Accessibility testing with assistive technology users before wave 1**
   - Description: Manual audit with users who have access needs, in clinical conditions
   - Owner: CCIO
   - Due Date: Before wave 1
   - Expected Impact: Reduces likelihood from 2 to 1

**Target Residual Risk After Mitigations:**

- Target Likelihood: 1 (Rare), Target Impact: 3 (Moderate), Target Score: 3 (Low) ✅

**Success Criteria:**

- Accessibility statement published and current
- No staff cohort showing adoption more than 30% below the median without an explanation and remediation plan
- Equity impact assessment completed and recorded before wave 1

**Monitoring Plan:**

- **Frequency:** Quarterly
- **Key Indicators:** adoption spread across cohorts and settings; accessibility conformance; equity assessment status
- **Escalation Triggers:** any cohort more than 30% below median adoption for two consecutive quarters
---

### Risk R-005: Assurance and Registration Authority capacity unfunded

**Category:** OPERATIONAL
**Status:** Open
**Risk Owner:** Trust Chief Executive (Stakeholder RACI: Accountable for resourcing decisions)
**Action Owner:** CIO / CDIO
**Supersedes:** STKE R-4, REQ RQ-4

#### Risk Identification

**Risk Description:**
Clinical Safety Officer, information governance, and Registration Authority capacity is assumed to absorb programme workload on top of existing duties. Both the assurance path and the authenticator migration path stall, and the programme's own gates become its critical path.

**Root Cause:**
Assurance roles are established posts with existing full workloads. Programmes routinely budget for build and deployment while treating assurance as free organisational overhead.

**Trigger Events:**

- Wave 1 approaches with no substantive CSO appointment (dependency D-1)
- Authenticator migration begins without a funded RA uplift (dependency D-5)
- Three separate assurance sign-offs are requested sequentially rather than as one pack

**Consequences if Realized:**

- Deployment waves delayed indefinitely, or the gate is pressured (this is the direct feeder into R-001)
- BR-008 authenticator migration slips independently of deployment, prolonging credential sharing
- Assurance staff burn out or decline the accountability, leaving posts unfilled

**Affected Stakeholders:**

- **Clinical Safety Officer** (SD-4), **Caldicott Guardian** (SD-5), **SIRO** (SD-6): asked to absorb unfunded work
- **Registration Authority Manager** (SD-13): migration workload without capacity
- **National Programme SRO** (SD-1): pace depends on capacity nobody funded

**Related Objectives:**

- **STKE G-1, G-5, G-6, G-7**: all four gated on capacity
- **REQ dependencies D-1, D-5**

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 4 - Likely | No capacity has been funded to date and no CSO is appointed. This is the current state, not a hypothetical. |
| **Impact** | 4 - Major | Blocks four goals simultaneously and directly increases the likelihood of R-001. |
| **Inherent Risk Score** | **16** (High) | 4 × 4 = 16 |

**Risk Zone:** 🟧 High (13-19)

#### Current Controls and Mitigations

1. **Named dependencies with explicit funding requirement** (REQ D-1, D-5): capacity recorded as a programme cost rather than an organisational absorption.
   - Owner: Trust Chief Executive
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — naming the dependency does not fund it

2. **Single integrated assurance pack** (STKE Synergy S-1): CSO, Caldicott Guardian, and SIRO receive one evidence pack covering data flows, intended use, residual risk, and retention, removing sequential sign-off delay.
   - Owner: Enterprise Architect
   - Maturity: **Proposed**
   - Effectiveness: **Strong** — reduces the workload rather than resourcing it

3. **Self-service authenticator management** (REQ FR-010): reduces RA steady-state load [NB-C5].
   - Owner: RA Manager
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — helps steady state, not the migration surge

**Overall Control Effectiveness:** Adequate — reduces demand but does not create supply. Only funding does that.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Demand reduction helps materially, but until posts are funded the shortfall remains realistic. |
| **Impact** | 3 - Moderate | With a single pack and self-service, a capacity shortfall slows the programme rather than blocking it outright. |
| **Residual Risk Score** | **9** (Medium) | 3 × 3 = 9 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 44% reduction from inherent (16 → 9)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:**
Treatable directly through funding and workload reduction. The cost is small relative to the £120 million national envelope and to the consequence of R-001.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — this risk is the upstream cause of the register's highest-scoring risk
- **Transfer**: Partially available — interim CSO capacity could be contracted, though accountability cannot be
- **Terminate**: Not viable

#### Risk Appetite Assessment

**Provisional appetite for OPERATIONAL risks:** Medium (Score ≤ 12)
**Current Residual Risk Score:** 9 (Medium)
**Assessment:** ✅ **Within appetite**

**Justification:** Within threshold, but note that this risk's realisation drives R-001 above appetite. It should be treated with urgency disproportionate to its own score.

**Escalation Required:** No on score; **Yes on dependency** — the CSO appointment is a prerequisite for wave 1

#### Action Plan

1. **Fund and appoint the Clinical Safety Officer** — Owner: Trust Chief Executive · Due: 2026-09-30 · Expected impact: unblocks R-001, R-013, R-017
2. **Fund a fixed-term Registration Authority uplift for the migration period** — Owner: CIO / CDIO · Due: 2026-10-31 · Expected impact: reduces likelihood from 3 to 2
3. **Produce the single integrated assurance pack template** — Owner: Enterprise Architect · Due: 2026-09-30 · Expected impact: removes sequential sign-off delay

**Target Residual Risk After Mitigations:** L2 × I3 = **6** (Medium) ✅

**Success Criteria:**

- CSO appointed with recorded time allocation before wave 1
- RA migration capacity funded before authenticator migration begins
- Assurance sign-off cycle time of 4 weeks or less per wave

**Monitoring Plan:**

- **Frequency:** Monthly at programme board
- **Key Indicators:** CSO appointment status; RA queue length; assurance cycle time
- **Escalation Triggers:** any wave where assurance capacity is the critical path

---

### Risk R-006: Baseline capture skipped, making benefit unprovable

**Category:** OPERATIONAL
**Status:** Open
**Risk Owner:** National Programme SRO (Stakeholder RACI: Accountable for benefit measurement method)
**Action Owner:** Local programme lead
**Supersedes:** REQ RQ-7

#### Risk Identification

**Risk Description:**
Pre-deployment administrative time baselines are not captured for major cohorts before enablement. Because the measurement window closes permanently at enablement, benefit for those cohorts becomes unprovable rather than merely delayed.

**Root Cause:**
Baselining is effort that delivers no visible progress and competes directly with enablement, which does. It is the first activity dropped under schedule pressure, and the only one that cannot be recovered later.

**Trigger Events:**

- A cohort is enabled ahead of schedule for operational reasons
- Time-and-motion sampling is deprioritised as burdensome to already-stretched staff
- The telemetry-use agreement (R-016) is unresolved, blocking measurement design until after enablement

**Consequences if Realized:**

- Benefit for affected cohorts is permanently unprovable; only estimation remains
- Directly disables the principal control for R-002
- Tier-level analysis (O-6) becomes impossible for those cohorts, weakening the licence decision

**Affected Stakeholders:**

- **National Programme SRO** (SD-1), **Director of Finance** (SD-9), **Chief People Officer** (SD-3)

**Related Objectives:**

- **STKE G-3, O-1, O-6** · **REQ BR-002, FR-015**

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 4 - Likely | Baselining is high-effort, low-visibility, and competes with the activity everyone is measured on. |
| **Impact** | 3 - Moderate | Irreversible for affected cohorts, but partial coverage still supports a defensible overall position. |
| **Inherent Risk Score** | **12** (Medium) | 4 × 3 = 12 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **Enablement blocked without a recorded baseline** (REQ FR-015): tooling blocks, or an explicit exception is recorded and disclosed in reporting.
   - Owner: Delivery Manager
   - Maturity: **Designed**
   - Effectiveness: **Strong** — makes the omission a visible decision rather than an oversight

2. **Exceptions disclosed rather than estimated** (REQ FR-016): cohorts without a baseline are excluded from benefit claims and the exclusion is stated.
   - Owner: Local programme lead
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

**Overall Control Effectiveness:** Strong — a hard gate on an irreversible activity is the correct control shape.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | A blocking gate makes silent omission difficult; the exception path remains. |
| **Impact** | 3 - Moderate | Unchanged — irreversibility is a property of the activity, not of the control. |
| **Residual Risk Score** | **6** (Medium) | 2 × 3 = 6 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 50% reduction from inherent (12 → 6)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:** Cheap to control with a blocking gate; expensive and impossible to remediate afterwards.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — irreversibility makes tolerance a permanent decision taken by default
- **Transfer** / **Terminate**: Not applicable

#### Risk Appetite Assessment

**Provisional appetite for OPERATIONAL risks:** Medium (Score ≤ 12)
**Current Residual Risk Score:** 6 (Medium) — ✅ **Within appetite**

**Escalation Required:** No

#### Action Plan

1. **Agree the measurement method with staff-side before wave 1** — Owner: Chief People Officer · Due: 2026-09-30 · Expected impact: removes the dependency that would otherwise delay baselining past enablement
2. **Implement the enablement block in deployment tooling** — Owner: Delivery Manager · Due: Before wave 1 · Expected impact: reduces likelihood from 2 to 1

**Target Residual Risk After Mitigations:** L1 × I3 = **3** (Low) ✅

**Success Criteria:** Baseline coverage of 90% or more of cohorts before enablement; every exception recorded and disclosed

**Monitoring Plan:**

- **Frequency:** Per wave
- **Key Indicators:** baseline coverage (%); exception count
- **Escalation Triggers:** more than one exception per wave

---

### Risk R-007: Service desk overwhelmed by wave enablement surge

**Category:** OPERATIONAL
**Status:** Open
**Risk Owner:** CIO / CDIO (Stakeholder RACI: Accountable for technology operations)
**Action Owner:** IT Service Desk Manager

#### Risk Identification

**Risk Description:**
Each enablement wave produces a concentrated support surge, plus an entirely new class of AI-related query the service desk has no runbook for. Support quality degrades at precisely the moment first impressions are formed.

**Root Cause:**
Wave-based deployment concentrates demand by design. The support model was sized for steady state, and the support uplift was not costed into the programme.

**Trigger Events:**

- A large wave enabled without prior runbook preparation
- Champion network not yet formed, so all queries route to the service desk
- An early defect or confusing behaviour generates correlated tickets

**Consequences if Realized:**

- Slow support at the point of first use, damaging adoption and reinforcing the perception that official tooling is inferior (feeding R-020)
- Steady-state service degraded for unrelated systems
- Service desk staff experience the programme as something done to them

**Affected Stakeholders:**

- **IT Service Desk / Operations** (SD-14): absorbs the surge
- **Frontline clinicians** (SD-10) and **administrative staff** (SD-12): experience poor first-line support

**Related Objectives:**

- **STKE O-5** (Workforce confidence) · **REQ NFR-M-003** (Operational runbooks)

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 4 - Likely | Concentrated demand against a steady-state-sized function, with a novel query class. |
| **Impact** | 2 - Minor | Degraded support is real but recoverable, and affects adoption rather than safety or compliance. |
| **Inherent Risk Score** | **8** (Medium) | 4 × 2 = 8 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **Wave-based rollout with planned cadence** (REQ FR-018): spreads demand rather than concentrating it in a single enablement event.
   - Owner: Delivery Manager
   - Maturity: **Designed**
   - Effectiveness: **Strong**

2. **Runbooks before each wave** (REQ NFR-M-003): covering common failure scenarios and the new AI query class.
   - Owner: IT Service Desk Manager
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

3. **Clinical champion network as first-line deflection** (STKE G-8): at least two champions per 500 users [NB-C6].
   - Owner: L&D lead
   - Maturity: **Designed**
   - Effectiveness: **Strong** — peer support both deflects volume and answers better

**Overall Control Effectiveness:** Strong — reduces likelihood substantially.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Paced waves plus champion deflection plus runbooks address the surge at source. |
| **Impact** | 2 - Minor | Unchanged. |
| **Residual Risk Score** | **4** (Low) | 2 × 2 = 4 |

**Risk Zone:** 🟩 Low (1-5)
**Risk Reduction:** 50% reduction from inherent (8 → 4)

#### Risk Response (4Ts Framework)

**Primary Response:** TOLERATE (Accept)

**Rationale:**
Residual risk is Low and well within appetite. Existing controls are proportionate; further investment in support capacity would cost more than the residual exposure warrants. Accepted subject to monitoring.

**Alternative Responses Considered:**

- **Treat further**: Rejected — additional permanent support capacity is disproportionate to a Low residual
- **Transfer**: Considered — outsourced surge support available if indicators deteriorate
- **Terminate**: Not applicable

#### Risk Appetite Assessment

**Provisional appetite for OPERATIONAL risks:** Medium (Score ≤ 12)
**Current Residual Risk Score:** 4 (Low) — ✅ **Well within appetite**

**Escalation Required:** No

#### Action Plan

1. **Publish runbooks covering the AI query class before wave 1** — Owner: IT Service Desk Manager · Due: Before wave 1
2. **Recruit champions ahead of each wave rather than alongside it** — Owner: L&D lead · Due: 4 weeks before each wave

**Target Residual Risk After Mitigations:** L2 × I2 = **4** (Low) — maintained, not further reduced

**Success Criteria:** First-response time maintained within normal service levels through each wave; champion coverage of at least 2 per 500 users before enablement

**Monitoring Plan:**

- **Frequency:** Per wave, then monthly
- **Key Indicators:** ticket volume per wave; first-response time; champion coverage
- **Escalation Triggers:** first-response time exceeding service level for more than 5 consecutive working days

---

### Risk R-008: Automation anxiety hardens into organised resistance

**Category:** OPERATIONAL
**Status:** Open
**Risk Owner:** Chief People Officer (Stakeholder RACI: Responsible for telemetry use and workforce commitments)
**Action Owner:** Chief People Officer
**Supersedes:** STKE R-6

#### Risk Identification

**Risk Description:**
Time-saving figures are published before the workforce conversation, are read as a redundancy business case, and convert manageable anxiety into formal opposition. A programme whose headline benefit is 43 minutes per person per day [NB-C1] has, from a staff-side perspective, quantified an establishment reduction.

**Root Cause:**
The benefit metric and the redundancy metric are the same number. Nothing in the measurement itself distinguishes "released time reinvested in care" from "posts no longer required" — only an explicit organisational commitment does.

**Trigger Events:**

- Savings published externally before staff-side consultation concludes
- Redeployment and reskilling pathway not defined before rollout
- Automation designed for administrative staff rather than with them
- Any establishment reduction announced in the same period, however unrelated

**Consequences if Realized:**

- Formal dispute, potentially halting enablement
- Adoption resistance among the cohort with the most to gain (administrative staff)
- Loss of the workforce narrative that justifies the programme internally

**Affected Stakeholders:**

- **Administrative and operational staff** (SD-12): most exposed, most anxious
- **Unions and professional bodies** (SD-11): formal counterpart
- **Chief People Officer** (SD-3): owns the commitment

**Related Objectives:**

- **STKE O-5** (Workforce confidence) · **REQ BR-005**

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Anxiety is certain; organised resistance depends on how the programme handles it, which is controllable. |
| **Impact** | 4 - Major | Formal dispute can halt enablement and durably damage the workforce relationship. |
| **Inherent Risk Score** | **12** (Medium) | 3 × 4 = 12 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **Board reinvestment commitment published alongside — never after — the first savings figure** (REQ BR-005)
   - Owner: Trust Chief Executive
   - Maturity: **Proposed**
   - Effectiveness: **Strong** — sequencing is the whole control

2. **Redeployment and reskilling pathway defined before rollout** (REQ BR-005)
   - Owner: Chief People Officer
   - Maturity: **Proposed**
   - Effectiveness: **Strong**

3. **Staff-side representation on the programme board** rather than consultation after decisions (STKE SD-11)
   - Owner: Chief People Officer
   - Maturity: **Proposed**
   - Effectiveness: **Adequate**

4. **Involvement of affected staff in choosing what is automated**
   - Owner: Chief People Officer
   - Maturity: **Proposed**
   - Effectiveness: **Adequate**

**Overall Control Effectiveness:** Strong once implemented — though note all four controls are Proposed, none yet Designed into any artefact beyond BR-005.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Commitments made in advance and in writing address the specific fear rather than dismissing it. |
| **Impact** | 3 - Moderate | Residual disagreement becomes a partnership-forum matter rather than a formal dispute. |
| **Residual Risk Score** | **6** (Medium) | 2 × 3 = 6 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 50% reduction from inherent (12 → 6)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:** Entirely treatable through sequencing and written commitment, at essentially no financial cost — provided it is done before the first savings figure is published.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — the cost of treatment is near zero and the window closes at first publication
- **Transfer** / **Terminate**: Not applicable

#### Risk Appetite Assessment

**Provisional appetite for OPERATIONAL risks:** Medium (Score ≤ 12)
**Current Residual Risk Score:** 6 (Medium) — ✅ **Within appetite**

**Escalation Required:** No

#### Action Plan

1. **Secure a board reinvestment commitment before any savings figure is published** — Owner: Trust Chief Executive · Due: Before first benefit report
2. **Define and publish the redeployment and reskilling pathway** — Owner: Chief People Officer · Due: Before wave 1
3. **Add staff-side representation to the programme board** — Owner: Trust Chief Executive · Due: 2026-09-30

**Target Residual Risk After Mitigations:** L1 × I3 = **3** (Low) ✅

**Success Criteria:** Zero unresolved formal disputes; reinvestment commitment published with the first savings figure; positive staff survey trend on role security

**Monitoring Plan:**

- **Frequency:** Monthly partnership forum
- **Key Indicators:** disputes raised; staff survey score on role security; redeployment pathway status
- **Escalation Triggers:** any formal dispute raised; any savings figure published without the commitment alongside it

---

### Risk R-009: Licence tier committed before per-tier benefit evidence exists

**Category:** FINANCIAL
**Status:** Open
**Risk Owner:** Director of Finance (Stakeholder RACI: Responsible for licence tier assignment)
**Action Owner:** CIO / CDIO

#### Risk Identification

**Risk Description:**
A multi-year tier mix is committed before benefit has been measured per tier. The Standard Service provides web-based applications and a 4 GB mailbox for frontline clinical staff; the Enhanced Service adds larger mailboxes and stronger tooling for heavier users [NB-C7]. If the cheaper tier does not deliver the savings the business case assumes, the commitment cannot be unwound.

**Root Cause:**
Procurement cycles demand a tier decision earlier than evidence cycles can supply one, and the cheaper option always scores better against a scorecard that cannot see the benefit differential.

**Trigger Events:**

- Multi-year agreement signed before the first tier-level benefit report
- Contract omits the right to move users between tiers
- Budget pressure forces a uniform low-tier assignment

**Consequences if Realized:**

- Recurring spend locked to a tier mix that cannot deliver the benefit case
- Frontline clinicians receive capability insufficient for the promised time savings, feeding R-002 and R-020
- Value-for-money position indefensible at review

**Affected Stakeholders:**

- **Director of Finance** (SD-9), **National Programme SRO** (SD-1), **Frontline clinicians** (SD-10)

**Related Objectives:**

- **STKE O-6** (Value for money by tier) · **REQ BR-006**, Conflict C-2

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Procurement timing pressure is real, but the conflict has been identified explicitly and the deferral agreed. |
| **Impact** | 3 - Moderate | Recurring cost consequence over the agreement term, recoverable at renewal. |
| **Inherent Risk Score** | **9** (Medium) | 3 × 3 = 9 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **Tier decision explicitly deferred pending evidence** (STKE Conflict C-2, REQ BR-006)
   - Owner: Director of Finance
   - Maturity: **Designed**
   - Effectiveness: **Strong**

2. **Mixed-tier pilot across comparable cohorts** (REQ FR-016, DR-005 carries `licence_tier`)
   - Owner: Local programme lead
   - Maturity: **Designed**
   - Effectiveness: **Strong** — generates the evidence the decision needs

3. **Contractual right to move users between tiers**
   - Owner: Director of Finance
   - Maturity: **Proposed**
   - Effectiveness: **Strong** — this is the control that transfers the risk

**Overall Control Effectiveness:** Strong — the combination converts an irreversible commitment into a reversible one.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Deferral is agreed and the evidence mechanism exists. |
| **Impact** | 3 - Moderate | With contractual flexibility, a wrong tier assignment is correctable rather than locked. |
| **Residual Risk Score** | **6** (Medium) | 2 × 3 = 6 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 33% reduction from inherent (9 → 6)

#### Risk Response (4Ts Framework)

**Primary Response:** TRANSFER

**Rationale:**
The residual risk is transferred to the supplier agreement through a contractual right to reassign users between tiers. Rather than the organisation bearing the cost of a wrong assignment for the agreement term, the flexibility to correct it is purchased as a contract term. Treatment (the mixed-tier pilot) supports the transfer by generating the evidence needed to exercise it.

**Alternative Responses Considered:**

- **Treat only**: Insufficient alone — evidence without the contractual right to act on it leaves the risk in place
- **Tolerate**: Rejected — recurring spend at national scale is material
- **Terminate**: Not viable

#### Risk Appetite Assessment

**Provisional appetite for FINANCIAL risks:** Medium (Score ≤ 12)
**Current Residual Risk Score:** 6 (Medium) — ✅ **Within appetite**

**Escalation Required:** No

#### Action Plan

1. **Secure the contractual right to move users between tiers** — Owner: Director of Finance · Due: Before agreement signature · Expected impact: the transfer mechanism itself
2. **Run a mixed-tier pilot across comparable cohorts from wave 1** — Owner: Local programme lead · Due: Wave 1
3. **Log any pre-evidence multi-year commitment as a financial risk, not a booked saving** — Owner: Director of Finance · Due: Ongoing

**Target Residual Risk After Mitigations:** L2 × I2 = **4** (Low) ✅

**Success Criteria:** Tier reassignment right present in the agreement; first tier-level benefit report delivered at month 6; no multi-year commitment made before it

**Monitoring Plan:**

- **Frequency:** Quarterly at Finance and Performance Committee
- **Key Indicators:** benefit per user by tier; recurring cost per tier; reassignment right status
- **Escalation Triggers:** any multi-year commitment proposed before tier-level evidence exists

---

### Risk R-010: Released clinical time booked as a cash saving

**Category:** FINANCIAL
**Status:** Open
**Risk Owner:** Chief People Officer (Stakeholder RACI: Accountable for workforce commitments)
**Action Owner:** Director of Finance

#### Risk Identification

**Risk Description:**
Measured time savings are treated as a cash-releasing efficiency and used to justify an establishment reduction, without an explicit board decision to do so. Released clinical time is capacity, not cash, and converting one to the other is a workforce decision rather than an accounting one.

**Root Cause:**
Finance systems represent staff time as cost. Any measured reduction in time spent naturally presents as an available saving unless something explicitly prevents that treatment.

**Trigger Events:**

- Benefit report presented to a finance committee without the capacity/cash distinction stated
- Budget pressure in an unrelated area seeking an offsetting saving
- The reinvestment commitment (R-008) was never made, leaving no barrier

**Consequences if Realized:**

- Direct breach of the reinvestment commitment, triggering R-008 and R-016
- Loss of workforce trust that is very difficult to rebuild
- Clinicians see time savings converted into increased caseload, ending voluntary adoption

**Affected Stakeholders:**

- **Frontline clinicians** (SD-10) and **administrative staff** (SD-12): bear the consequence
- **Unions** (SD-11): would treat this as a breach of agreement
- **Chief People Officer** (SD-3): commitment broken on their behalf

**Related Objectives:**

- **STKE O-1** (time released *and reinvested*) · **REQ BR-005**, and the explicit note in the Budget section that released capacity should not be booked as cash without an establishment decision

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Requires an active misreading, but financial reporting conventions push in this direction by default. |
| **Impact** | 4 - Major | Breaks the central workforce commitment and cascades into two other risks. |
| **Inherent Risk Score** | **12** (Medium) | 3 × 4 = 12 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **Explicit capacity-not-cash framing in benefit reporting** (STKE O-1, REQ Budget section): released capacity is not booked as a cash saving without an explicit establishment decision.
   - Owner: Director of Finance
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — a stated convention, not an enforced control

2. **Board reinvestment commitment** (REQ BR-005)
   - Owner: Trust Chief Executive
   - Maturity: **Proposed**
   - Effectiveness: **Strong** — creates an explicit barrier requiring a visible decision to cross

**Overall Control Effectiveness:** Adequate — reduces likelihood; impact is unchanged because the consequence of a breach is the same however it occurs.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | A published commitment makes the conversion a visible decision rather than an accounting default. |
| **Impact** | 4 - Major | Unchanged — a breach of a published commitment is if anything more damaging than an unstated assumption. |
| **Residual Risk Score** | **8** (Medium) | 2 × 4 = 8 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 33% reduction from inherent (12 → 8)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:** Treatable through explicit commitment and reporting convention at no financial cost.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — the consequence cascades into two further risks
- **Transfer** / **Terminate**: Not applicable

#### Risk Appetite Assessment

**Provisional appetite for FINANCIAL risks:** Medium (Score ≤ 12)
**Current Residual Risk Score:** 8 (Medium) — ✅ **Within appetite**

**Escalation Required:** No

#### Action Plan

1. **State the capacity-not-cash distinction in every benefit report** — Owner: Director of Finance · Due: First report onwards
2. **Obtain and publish the board reinvestment commitment** — Owner: Trust Chief Executive · Due: Before first benefit report
3. **Require any establishment decision arising from released time to go to the partnership forum first** — Owner: Chief People Officer · Due: 2026-10-31 · Expected impact: reduces likelihood from 2 to 1

**Target Residual Risk After Mitigations:** L1 × I4 = **4** (Low) ✅

**Success Criteria:** Reinvestment commitment published; every benefit report carries the capacity/cash distinction; no establishment reduction attributed to programme savings without partnership forum consultation

**Monitoring Plan:**

- **Frequency:** Quarterly
- **Key Indicators:** reinvestment commitment status; establishment changes in affected cohorts
- **Escalation Triggers:** any proposal to convert measured savings into an establishment reduction
---

### Risk R-011: Patient identifiable data disclosed via collaborative channel

**Category:** COMPLIANCE
**Status:** Open
**Risk Owner:** Caldicott Guardian (Stakeholder RACI: Accountable for confidentiality configuration)
**Action Owner:** Information Governance Manager

#### Risk Identification

**Risk Description:**
Patient identifiable information is shared into a channel, workspace, or external recipient outside an approved direct-care purpose. Collaboration platforms make sharing frictionless — which is their value and precisely their risk.

**Root Cause:**
The platform is designed to reduce sharing friction, and clinical work legitimately requires sharing patient information. No policy can reliably distinguish the two at the moment of action; only a technical control operating at that moment can.

**Trigger Events:**

- Data loss prevention controls not configured before clinical use of a workspace
- A workspace's classification is wrong, so the wrong policy applies
- External guest access granted to a workspace containing identifiable data
- Staff route around an over-tight control, moving data somewhere unmonitored

**Consequences if Realized:**

- ICO-reportable personal data breach; potential enforcement action
- Breach of Caldicott principles and DSPT assertions
- Patient confidentiality harmed; individual notification may be required
- CQC interest, and loss of Caldicott Guardian confidence in the platform

**Affected Stakeholders:**

- **Caldicott Guardian** (SD-5): accountable for confidentiality
- **SIRO / DPO** (SD-6): accountable for the breach response
- **ICO** (SD-15): regulator
- **Patients**: the data subjects

**Related Objectives:**

- **STKE G-6, O-3** · **REQ BR-004, FR-011, NFR-C-005** · **PRIN 7** (Confidentiality and the Caldicott Principles)

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 4 - Likely | Across a population of hundreds of thousands of users sharing clinical information daily, inappropriate disclosure without preventive controls is near-inevitable rather than exceptional. |
| **Impact** | 4 - Major | Regulatory exposure, patient harm, and reputational damage; severe but not existential for a single incident. |
| **Inherent Risk Score** | **16** (High) | 4 × 4 = 16 |

**Risk Zone:** 🟧 High (13-19)

#### Current Controls and Mitigations

1. **Preventive identifier-sharing controls** (REQ FR-011): detect and block sharing of patient identifiers outside approved direct-care purposes, without obstructing legitimate sharing [NB-C8].
   - Owner: Information Governance Manager
   - Maturity: **Designed**
   - Effectiveness: **Strong** — blocks at the moment of action rather than after the fact

2. **Workspace classification driving policy selection** (REQ DR-003): `contains_pid` determines which policy applies.
   - Owner: Information Governance Manager
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — depends on classification accuracy

3. **False-positive rate tracked and reviewed** (REQ NFR-C-005): prevents controls being tuned so tightly that staff route around them.
   - Owner: Caldicott Guardian
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — this is what stops the control defeating itself

4. **Data remains within the organisation's own tenancy** [NB-C9]
   - Owner: CIO / CDIO
   - Maturity: **Designed** (contingent on the R-003 tenancy decision)
   - Effectiveness: **Strong** — bounds the blast radius

**Overall Control Effectiveness:** Strong — reduces likelihood from 4 to 2. Impact is unchanged: a disclosure that occurs is equally reportable whether or not controls existed.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Preventive blocking at the point of action addresses the dominant failure mode. Residual reflects misclassified workspaces and novel sharing routes. |
| **Impact** | 4 - Major | Unchanged — regulatory and patient consequences do not depend on whether a control was in place. |
| **Residual Risk Score** | **8** (Medium) | 2 × 4 = 8 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 50% reduction from inherent (16 → 8)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:** Preventive technical control is available, proportionate, and materially more reliable than policy or training alone.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — regulatory obligation, and High at inherent level
- **Transfer**: Not available — data controller accountability cannot be transferred
- **Terminate**: Rejected — would mean not using collaboration tools for clinical work at all

#### Risk Appetite Assessment

**Provisional appetite for COMPLIANCE risks:** Low (Score ≤ 6)
**Current Residual Risk Score:** 8 (Medium)
**Assessment:** ❌ **Exceeds appetite** by 2 points (33% over threshold)

**Justification:**
Driven by irreducible Major impact. Reaching appetite requires likelihood 1 (Rare), achievable only with mature, tuned controls and demonstrated low false-positive rates over time. Realistic within 12 months of implementation, not before.

**Escalation Required:** Yes — SIRO and Caldicott Guardian to record a formal acceptance decision for the interim period, with a target date for reaching appetite.

#### Action Plan

1. **Configure identifier-sharing controls before any clinical use of a workspace** — Owner: Information Governance Manager · Due: Before wave 1 · Expected impact: the primary control
2. **Complete workspace classification for all clinical workspaces** — Owner: Information Governance Manager · Due: Before wave 1 · Expected impact: ensures the right policy applies
3. **Establish false-positive review cycle** — Owner: Caldicott Guardian · Due: Month 2 of operation · Expected impact: prevents staff routing around controls, which would restore likelihood to 4
4. **Restrict external guest access in clinical workspaces by default** — Owner: Information Governance Manager · Due: Before wave 1 · Expected impact: reduces likelihood from 2 to 1

**Target Residual Risk After Mitigations:** L1 × I4 = **4** (Low) ✅ Within appetite

**Success Criteria:**

- Zero ICO-reportable breaches originating from the platform over any rolling 12 months
- 100% of clinical workspaces with classification and policy applied
- False-positive rate trending down quarter on quarter

**Monitoring Plan:**

- **Frequency:** Monthly configuration audit; continuous incident monitoring
- **Key Indicators:** violations blocked; false-positive rate; unclassified workspace count
- **Escalation Triggers:** any reportable breach; any unclassified workspace entering clinical use

---

### Risk R-012: Retention left on product default, breaching record-keeping requirements

**Category:** COMPLIANCE
**Status:** Open
**Risk Owner:** Caldicott Guardian (Stakeholder RACI: Accountable for retention schedule configuration)
**Action Owner:** Information Governance Manager

#### Risk Identification

**Risk Description:**
Collaboration workspaces retain clinical content on the platform's default settings rather than against the applicable clinical schedule. Default retention may conflict with clinical record-keeping requirements, which commonly demand six years for clinical consultations [NB-C10]. Content is therefore either destroyed too early or retained too long — both breaches, in opposite directions.

**Root Cause:**
Product defaults are set for general commercial use and are invisible until they act. Nothing surfaces the mismatch until a record is needed and has already been deleted, or a subject access request reveals content that should have been destroyed.

**Trigger Events:**

- A workspace enters clinical use without explicit retention configuration
- Local administrators create workspaces outside the governed provisioning path
- A platform update changes default retention behaviour
- Records management schedule not agreed before configuration (dependency D-6)

**Consequences if Realized:**

- Clinical records destroyed before the end of their retention period — irreversible, and potentially material to a patient safety investigation or litigation
- Or content retained beyond its lawful period, breaching UK GDPR storage limitation
- DSPT assertion failure; CQC and ICO exposure

**Affected Stakeholders:**

- **Caldicott Guardian** (SD-5), **SIRO / DPO** (SD-6), **Information Governance Manager**
- **Clinical Safety Officer** (SD-4): loses evidence needed for investigation
- **Patients**: records lost or over-retained

**Related Objectives:**

- **STKE G-6, O-3** · **REQ FR-012, DR-003, NFR-C-001** · **PRIN 6** (Data Sovereignty and Residency)

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 4 - Likely | Defaults apply automatically and silently. Without explicit configuration this is the certain outcome for every ungoverned workspace. |
| **Impact** | 4 - Major | Irreversible record loss, or unlawful retention; both carry regulatory and clinical consequence. |
| **Inherent Risk Score** | **16** (High) | 4 × 4 = 16 |

**Risk Zone:** 🟧 High (13-19)

#### Current Controls and Mitigations

1. **Explicit retention against a named schedule for every workspace** (REQ FR-012): no workspace may remain on product default once in clinical use.
   - Owner: Information Governance Manager
   - Maturity: **Designed**
   - Effectiveness: **Strong**

2. **Retention configuration held as code** (REQ NFR-M-002, PRIN 19): deviation becomes visible in review rather than discovered in audit.
   - Owner: CIO / CDIO
   - Maturity: **Designed**
   - Effectiveness: **Strong** — converts a silent failure into a reviewable one

3. **Monthly configuration audit** (REQ NFR-C-003)
   - Owner: Information Governance Manager
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — detection, bounded by audit interval

4. **Retention schedule register agreed with records management** (dependency D-6)
   - Owner: Caldicott Guardian
   - Maturity: **Proposed**
   - Effectiveness: **Strong** — prerequisite for everything above

**Overall Control Effectiveness:** Strong — configuration-as-code plus audit reduces both likelihood and impact, since deviations are caught before retention periods elapse.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Explicit configuration plus drift detection addresses the default-application failure mode. Residual reflects ungoverned workspace creation. |
| **Impact** | 3 - Moderate | Caught within the audit cycle, a misconfiguration is corrected long before a six-year retention period elapses — so the irreversible outcome is largely avoided. |
| **Residual Risk Score** | **6** (Medium) | 2 × 3 = 6 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 63% reduction from inherent (16 → 6) — the largest reduction in the register

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:** A configuration problem with a configuration solution. Cheap to control, expensive and often irreversible to remediate.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — High inherent, regulatory obligation, irreversible consequence
- **Transfer** / **Terminate**: Not applicable

#### Risk Appetite Assessment

**Provisional appetite for COMPLIANCE risks:** Low (Score ≤ 6)
**Current Residual Risk Score:** 6 (Medium)
**Assessment:** ✅ **At appetite threshold** — within, but with no margin

**Justification:** Sits exactly at the boundary. Any degradation in configuration governance pushes it over.

**Escalation Required:** No, but flagged for close monitoring given zero margin

#### Action Plan

1. **Agree the retention schedule register** — Owner: Caldicott Guardian · Due: 2026-09-30 · Expected impact: unblocks all other controls (D-6)
2. **Configure explicit retention for 100% of clinical workspaces** — Owner: Information Governance Manager · Due: Before clinical use
3. **Close the ungoverned workspace creation path** — Owner: CIO / CDIO · Due: Before wave 1 · Expected impact: reduces likelihood from 2 to 1
4. **Automate configuration drift detection** — Owner: CIO / CDIO · Due: Month 3 · Expected impact: shortens detection interval from monthly to continuous

**Target Residual Risk After Mitigations:** L1 × I3 = **3** (Low) ✅

**Success Criteria:** Zero workspaces on product default retention; 100% configured against a named schedule; zero records destroyed before schedule

**Monitoring Plan:**

- **Frequency:** Monthly configuration audit
- **Key Indicators:** workspaces on default retention (target zero); configuration drift events
- **Escalation Triggers:** any workspace found on default retention; any record destroyed before schedule

---

### Risk R-013: Drift into clinical use triggers unapproved medical device status

**Category:** COMPLIANCE
**Status:** Open
**Risk Owner:** Clinical Safety Officer (Stakeholder RACI: Accountable for clinical safety case and SaMD determination)
**Action Owner:** CCIO

#### Risk Identification

**Risk Description:**
The tool is deployed and nationally classified as an administrative productivity tool rather than Software as a Medical Device [NB-C11]. Actual use drifts into clinical decision support, and the deployment thereby meets the definition of a medical device without any of the regulatory approval that status requires.

**Root Cause:**
The SaMD classification is a statement about *intended* use. It remains true only while actual use matches it — and nothing about the technology enforces that boundary. Clinical drift is gradual and, without deliberate measurement, invisible [NB-C12].

**Trigger Events:**

- Staff begin using generative assistance to summarise patient notes or support clinical discussion
- Drift detection is absent or ineffective (R-018)
- A local configuration or prompt extends the tool into clinical workflow without reassessment
- A clinician relies on generated content as a clinical judgement rather than a draft

**Consequences if Realized:**

- Operating an unapproved medical device — a regulatory breach independent of whether harm occurs
- The clinical safety case, written for administrative use, no longer covers actual use
- MHRA interest; potential enforced withdrawal of the capability
- Any harm arising is materially harder to defend (feeds R-015, R-017)

**Affected Stakeholders:**

- **Clinical Safety Officer** (SD-4): the determination is theirs to make and defend
- **CCIO** (SD-2): owns the boundary in practice
- **Trust Chief Executive** (SD-16): carries the regulatory consequence
- **Patients**: exposed to an unassessed clinical tool

**Related Objectives:**

- **STKE G-2, O-2** · **REQ NFR-C-004, FR-004, BR-003** · **PRIN 10, PRIN 11**

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Drift requires a gradual behavioural shift rather than a single act, but the pressure toward it is constant and the tool is genuinely capable of the use. |
| **Impact** | 5 - Catastrophic | Operating an unapproved medical device is an existential regulatory exposure for the deployment and potentially for the national programme. |
| **Inherent Risk Score** | **15** (High) | 3 × 5 = 15 |

**Risk Zone:** 🟧 High (13-19)

#### Current Controls and Mitigations

1. **Clinical-scope AI deployment explicitly out of scope** (REQ Project Scope): the activity that would create the exposure is not undertaken at all in v1.0.
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Strong** — this is the termination decision, not a mitigation

2. **Published intended-use boundary communicated at enablement** (REQ FR-004, STKE G-2)
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

3. **Drift detection within 30 days of occurrence** (REQ FR-004)
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — and itself at risk (see R-018)

4. **SaMD determination recorded per deployment, reassessed on material change** (REQ NFR-C-004)
   - Owner: Clinical Safety Officer
   - Maturity: **Designed**
   - Effectiveness: **Strong**

5. **Training leads with failure modes, not features** (REQ FR-014)
   - Owner: L&D lead
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

**Overall Control Effectiveness:** Strong — but note the dependency: control 3 failing (R-018) would leave drift undetected, restoring likelihood toward 3.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Not undertaking clinical-scope deployment removes the deliberate route; boundary publication and detection address the gradual one. |
| **Impact** | 5 - Catastrophic | Unchanged — regulatory status does not depend on how the drift occurred. |
| **Residual Risk Score** | **10** (Medium) | 2 × 5 = 10 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 33% reduction from inherent (15 → 10)

#### Risk Response (4Ts Framework)

**Primary Response:** TERMINATE (Stop the activity creating the risk)

**Rationale:**
The activity that would create this exposure — clinical-scope AI deployment — is explicitly excluded from scope rather than mitigated. This is a genuine termination: the organisation is choosing not to undertake the activity in this release, and has recorded that choice in the requirements scope statement. The residual risk reflects only *unintended* drift into the terminated activity, which is then treated.

**Alternative Responses Considered:**

- **Treat**: Insufficient alone — mitigating a clinical deployment still leaves an unapproved medical device
- **Tolerate**: Rejected — regulatory exposure is not tolerable at any score
- **Transfer**: Not available — device regulation attaches to the deploying organisation

#### Risk Appetite Assessment

**Provisional appetite for COMPLIANCE risks:** Low (Score ≤ 6); **clinical safety appetite:** Very Low (≤ 4)
**Current Residual Risk Score:** 10 (Medium)
**Assessment:** ❌ **Significantly exceeds appetite** on both scales

**Justification:**
Driven entirely by catastrophic impact. Reaching a Very Low appetite requires likelihood 1, which depends on drift detection actually working — and R-018 records genuine uncertainty about whether it can. This risk cannot be brought within appetite until assumption A-1 is validated.

**Escalation Required:** Yes — Trust Board, coupled with the R-018 validation outcome.

#### Action Plan

1. **Validate assumption A-1 — that telemetry can distinguish administrative from clinical use** — Owner: CCIO · Due: 2026-10-31 · Expected impact: determines whether likelihood 1 is achievable at all
2. **Record the SaMD determination for wave 1 before enablement** — Owner: Clinical Safety Officer · Due: Before wave 1
3. **Define reassessment triggers for material change** — Owner: Clinical Safety Officer · Due: Before wave 1
4. **Establish the sampling-review fallback** for use if A-1 proves false — Owner: CCIO · Due: 2026-11-30

**Target Residual Risk After Mitigations:** L1 × I5 = **5** (Low) — contingent on A-1 validating

**Success Criteria:** SaMD determination recorded per wave; zero confirmed instances of clinical-scope use; drift detection demonstrably able to distinguish use classes

**Monitoring Plan:**

- **Frequency:** Monthly hazard review; continuous drift monitoring
- **Key Indicators:** out-of-boundary detections; boundary comprehension survey results; SaMD determination currency
- **Escalation Triggers:** any confirmed clinical-scope use; A-1 validation failing

---

### Risk R-014: DSPT assurance lapses as change outpaces the assurance cycle

**Category:** COMPLIANCE
**Status:** Open
**Risk Owner:** SIRO (Stakeholder RACI: Accountable for information risk acceptance)
**Action Owner:** CISO / Cyber Security Lead

#### Risk Identification

**Risk Description:**
The estate changes faster than the annual Data Security and Protection Toolkit cycle can absorb, and assurance becomes a point-in-time claim that no longer describes the running system. Compliance is demonstrated primarily through the DSPT, aligned to the NCSC Cyber Assessment Framework [NB-C13].

**Root Cause:**
Annual assurance was designed for estates that changed annually. Wave-based deployment of AI capability changes the assessed surface continuously.

**Trigger Events:**

- AI and collaboration capability not brought into assessed scope before wave 1
- Evidence gathered manually, so it is stale by the time it is submitted
- The tenancy decision (R-003) changes which controls are inherited versus locally owned, invalidating prior evidence
- Local administrators disable controls without review

**Consequences if Realized:**

- DSPT status downgraded, affecting eligibility for national integrations
- SIRO unable to accept risk on current evidence, blocking wave enablement
- CQC and ICO exposure from a demonstrably inaccurate assurance position

**Affected Stakeholders:**

- **SIRO** (SD-6), **CISO** (SD-7), **regulators** (SD-15), **NHS Digital** as shared tenant operator

**Related Objectives:**

- **STKE G-5, O-3** · **REQ BR-004, NFR-C-003** · **PRIN 4** (Security by Design)

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | The organisation maintains DSPT today; the risk arises specifically from the rate of change this programme introduces. |
| **Impact** | 4 - Major | Loss of assurance status blocks national integration eligibility and halts wave enablement. |
| **Inherent Risk Score** | **12** (Medium) | 3 × 4 = 12 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **AI and collaboration capability explicitly in assessed scope** (REQ BR-004, NFR-C-003)
   - Owner: CISO
   - Maturity: **Designed**
   - Effectiveness: **Strong**

2. **60% or more of assertions supported by automated evidence capture** (REQ NFR-C-003): evidence produced continuously rather than assembled at submission.
   - Owner: CISO
   - Maturity: **Designed**
   - Effectiveness: **Strong** — addresses the root cause directly

3. **Security configuration held as code** (REQ NFR-M-002): deviation visible in review.
   - Owner: CIO / CDIO
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

4. **Documented split of inherited versus locally owned controls** (REQ BR-007)
   - Owner: CIO / CDIO
   - Maturity: **Designed** (contingent on R-003)
   - Effectiveness: **Adequate**

**Overall Control Effectiveness:** Adequate — automated evidence is the decisive control, and it is the one furthest from implementation.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Continuous evidence capture keeps assurance current rather than annual. |
| **Impact** | 4 - Major | Unchanged — a lapse has the same consequence however it arose. |
| **Residual Risk Score** | **8** (Medium) | 2 × 4 = 8 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 33% reduction from inherent (12 → 8)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:** Automating evidence capture treats the root cause — the mismatch between change rate and assurance rate — rather than the symptom.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — regulatory and operational consequence
- **Transfer**: Partially — inherited controls transfer to the shared tenant operator, but the assurance obligation does not
- **Terminate**: Not viable

#### Risk Appetite Assessment

**Provisional appetite for COMPLIANCE risks:** Low (Score ≤ 6)
**Current Residual Risk Score:** 8 (Medium)
**Assessment:** ❌ **Exceeds appetite** by 2 points (33% over threshold)

**Justification:** Reaching appetite requires either likelihood 1 (sustained automated evidence at high coverage) or accepting that Major impact is irreducible. Achievable within 12 months as evidence automation matures.

**Escalation Required:** Yes — SIRO to record a formal interim acceptance with a target date.

#### Action Plan

1. **Bring AI and collaboration capability into assessed DSPT scope** — Owner: CISO · Due: Next submission cycle
2. **Reach 60% automated evidence capture** — Owner: CISO · Due: Month 12 · Expected impact: reduces likelihood from 2 to 1
3. **Complete the inherited-versus-local control split** — Owner: CIO / CDIO · Due: With the tenancy decision (R-003)
4. **Remove local administrators' ability to disable governed controls without review** — Owner: CISO · Due: Before wave 1

**Target Residual Risk After Mitigations:** L1 × I4 = **4** (Low) ✅ Within appetite

**Success Criteria:** DSPT "Standards Met" with AI in scope; automated evidence coverage of 60% or more; zero ungoverned control changes

**Monitoring Plan:**

- **Frequency:** Monthly evidence coverage; annual submission
- **Key Indicators:** automated evidence coverage (%); configuration drift events; DSPT assertion status
- **Escalation Triggers:** any assertion moving to "not met"; evidence coverage falling below 40%

---

### Risk R-015: AI-attributable harm becomes a national news story

**Category:** REPUTATIONAL
**Status:** Open
**Risk Owner:** Trust Chief Executive (Stakeholder RACI: Accountable for organisational reputation)
**Action Owner:** Director of Communications

#### Risk Identification

**Risk Description:**
An incident in which generated content contributed to patient harm becomes public — through media, a coroner's inquest, a CQC report, or a parliamentary question. The organisation becomes the named example of NHS AI failure.

**Root Cause:**
The programme is nationally visible and politically salient. Success is a shared, diffuse national story; failure is a specific, local, attributable one. The asymmetry is structural and cannot be removed.

**Trigger Events:**

- R-017 materialises — generated clinical error reaches a patient
- R-013 materialises — unapproved medical device status becomes public
- A near-miss is reported externally before internal disclosure
- A whistleblower raises concerns about drift or gate override

**Consequences if Realized:**

- Sustained national media attention; CQC inspection focus
- National programme momentum damaged for every other NHS organisation
- Clinician confidence collapses; voluntary adoption ends
- Regulatory and political intervention in local decision-making

**Affected Stakeholders:**

- **Trust Chief Executive** (SD-16): asymmetric personal exposure
- **National Programme SRO** (SD-1): national consequence from a local event
- **Frontline clinicians** (SD-10): professional reputation by association
- **Patients and the public**: confidence in NHS AI use

**Related Objectives:**

- **STKE O-2** · **REQ BR-003** · **PRIN 10, PRIN 11**

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Dependent on R-017 or R-013 materialising, both of which are Critical or High at inherent level, combined with high media salience for NHS AI. |
| **Impact** | 5 - Catastrophic | National reputational damage extending beyond the organisation to the whole programme. |
| **Inherent Risk Score** | **15** (High) | 3 × 5 = 15 |

**Risk Zone:** 🟧 High (13-19)

#### Current Controls and Mitigations

1. **All clinical safety controls** (R-001, R-013, R-017 mitigations): this risk is almost entirely derivative — it materialises only if one of those does.
   - Owner: Clinical Safety Officer
   - Maturity: **Designed**
   - Effectiveness: **Strong**

2. **Non-punitive internal reporting route** (REQ FR-005): surfaces problems internally before they surface externally.
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Strong** — the single most effective reputational control is early internal disclosure

3. **Locally owned benefit claims** (STKE Conflict C-5): the organisation is not exposed by national claims made on its behalf.
   - Owner: National Programme SRO
   - Maturity: **Proposed**
   - Effectiveness: **Adequate**

4. **Audit trail sufficient to reconstruct any incident** (REQ FR-003)
   - Owner: Clinical Safety Officer
   - Maturity: **Designed**
   - Effectiveness: **Strong** — determines whether the organisation can demonstrate it acted properly

**Overall Control Effectiveness:** Strong — but wholly dependent on the upstream clinical safety controls actually working.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Follows the reduced likelihood of R-017 and R-013, plus early internal disclosure reducing the chance that a problem first emerges externally. |
| **Impact** | 5 - Catastrophic | Unchanged — media and political consequence does not scale with how well controls were designed. |
| **Residual Risk Score** | **10** (Medium) | 2 × 5 = 10 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 33% reduction from inherent (15 → 10)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:**
Treated indirectly by treating its causes, and directly by ensuring the organisation can demonstrate it acted properly if an incident occurs. A defensible audit trail changes the story from "NHS trust deployed AI recklessly" to "NHS trust detected and disclosed an incident within its own controls".

**Alternative Responses Considered:**

- **Tolerate**: Rejected — catastrophic impact
- **Transfer**: Not available for reputational risk
- **Terminate**: Would mean not deploying at all — disproportionate

#### Risk Appetite Assessment

**Provisional appetite for REPUTATIONAL risks:** Low (Score ≤ 6)
**Current Residual Risk Score:** 10 (Medium)
**Assessment:** ❌ **Exceeds appetite** by 4 points (67% over threshold)

**Justification:**
Irreducible catastrophic impact. Cannot reach appetite while the underlying clinical risks remain above their own appetite. This risk should be reviewed alongside R-017 and R-013 rather than independently.

**Escalation Required:** Yes — Trust Board, jointly with R-013 and R-017.

#### Action Plan

1. **Prepare an incident communications plan before wave 1** — Owner: Director of Communications · Due: Before wave 1 · Expected impact: reduces impact from 5 to 4 by ensuring a prepared, transparent response
2. **Establish the non-punitive reporting route and publicise it** — Owner: CCIO · Due: Before wave 1 · Expected impact: internal disclosure precedes external
3. **Agree with the national programme that benefit claims are locally published** — Owner: Trust Chief Executive · Due: 2026-10-31

**Target Residual Risk After Mitigations:** L2 × I4 = **8** (Medium) — still above appetite; further reduction depends on R-017 and R-013

**Success Criteria:** Zero AI-attributable incidents becoming public before internal disclosure; incident communications plan tested; no national benefit claim published on the organisation's behalf without agreement

**Monitoring Plan:**

- **Frequency:** Monthly, jointly with R-013 and R-017
- **Key Indicators:** internal reports raised (under-reporting is the warning sign, not over-reporting); media monitoring
- **Escalation Triggers:** any external enquiry regarding AI use; any incident with potential media interest

---

### Risk R-016: Telemetry dispute escalates into public disagreement

**Category:** REPUTATIONAL
**Status:** Open
**Risk Owner:** Chief People Officer (Stakeholder RACI: Responsible for telemetry use and access limits)
**Action Owner:** Chief People Officer
**Supersedes:** STKE R-3, REQ RQ-3

#### Risk Identification

**Risk Description:**
Drift monitoring is deployed without a staff-side agreement, is characterised publicly as surveillance of clinicians, and escalates into a formal dispute that halts enablement and attracts external attention.

**Root Cause:**
Safety monitoring and performance surveillance use identical data. Only governance, access control, and trust distinguish them — and none of that is visible to staff unless it is made explicit in advance.

**Trigger Events:**

- Monitoring deployed before the telemetry-use agreement is concluded (dependency D-2)
- Individual-level data found accessible to a line manager
- A disciplinary process appears to rely on usage data
- Monitoring characterised externally before the organisation explains it

**Consequences if Realized:**

- Enablement halted pending resolution
- Public characterisation of the trust as surveilling clinicians
- Drift monitoring withdrawn, which disables the principal control for R-013 and R-017
- Trust damage extending well beyond this programme

**Affected Stakeholders:**

- **Unions and professional bodies** (SD-11), **frontline clinicians** (SD-10)
- **CCIO** (SD-2): loses the drift detection capability
- **Chief People Officer** (SD-3): owns the relationship

**Related Objectives:**

- **STKE O-5, G-2** · **REQ FR-004, FR-006, BR-005**, Conflict C-3

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Highly likely if monitoring is deployed without prior agreement; unlikely if the agreement is concluded first. Entirely dependent on sequencing. |
| **Impact** | 3 - Moderate | Significant disruption and reputational damage, but recoverable and not safety-affecting in itself. |
| **Inherent Risk Score** | **9** (Medium) | 3 × 3 = 9 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **Written telemetry-use agreement concluded before first enablement** (REQ BR-005, dependency D-2): specifies cohort-level operation, names the limited circumstances for individual access, and who authorises it.
   - Owner: Chief People Officer
   - Maturity: **Designed**
   - Effectiveness: **Strong** — decisive when done in the right order

2. **Technical restriction of individual-level data** (REQ FR-006): line managers denied access by control, not policy; access itself logged.
   - Owner: CIO / CDIO
   - Maturity: **Designed**
   - Effectiveness: **Strong** — converts a promise into something staff can verify

3. **Minimum cohort size enforced before reporting** (REQ FR-006)
   - Owner: Local programme lead
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

4. **Staff-side representation on the programme board** (STKE SD-11)
   - Owner: Trust Chief Executive
   - Maturity: **Proposed**
   - Effectiveness: **Adequate**

**Overall Control Effectiveness:** Strong — this risk has the register's most favourable control economics: near-zero cost, decisive effect, provided sequencing holds.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 1 - Rare | With a written agreement concluded in advance and technical enforcement of its terms, the dispute has no substance to form around. |
| **Impact** | 3 - Moderate | Unchanged if it occurs. |
| **Residual Risk Score** | **3** (Low) | 1 × 3 = 3 |

**Risk Zone:** 🟩 Low (1-5)
**Risk Reduction:** 67% reduction from inherent (9 → 3) — the largest proportional reduction in the register

#### Risk Response (4Ts Framework)

**Primary Response:** TOLERATE (Accept, post-treatment)

**Rationale:**
Once the telemetry-use agreement is concluded and technically enforced, residual risk is Low and within appetite. No further investment is warranted; the risk is accepted subject to the agreement remaining in force and monitoring of dispute indicators.

**Alternative Responses Considered:**

- **Treat further**: Unnecessary — residual is already Low
- **Transfer** / **Terminate**: Not applicable

> **Note**: tolerance here is conditional on the agreement existing. Until dependency D-2 is discharged, the effective response is TREAT and the effective score is 9.

#### Risk Appetite Assessment

**Provisional appetite for REPUTATIONAL risks:** Low (Score ≤ 6)
**Current Residual Risk Score:** 3 (Low) — ✅ **Within appetite**

**Escalation Required:** No — provided D-2 is discharged before enablement

#### Action Plan

1. **Conclude the written telemetry-use agreement before any enablement** — Owner: Chief People Officer · Due: 2026-09-30 · Expected impact: the entire control
2. **Implement technical restriction on individual-level access** — Owner: CIO / CDIO · Due: Before wave 1
3. **Add staff-side representation to the programme board** — Owner: Trust Chief Executive · Due: 2026-09-30

**Target Residual Risk After Mitigations:** L1 × I3 = **3** (Low) — maintained

**Success Criteria:** Agreement signed before first enablement; zero line-manager access to individual usage data; zero formal disputes

**Monitoring Plan:**

- **Frequency:** Monthly partnership forum
- **Key Indicators:** agreement status; individual-access requests and authorisations; disputes raised
- **Escalation Triggers:** any enablement proposed before the agreement is signed; any unauthorised individual-level access
---

### Risk R-017: Generated content containing a clinical error is accepted into the record

**Category:** TECHNOLOGY
**Status:** Open
**Risk Owner:** Clinical Safety Officer (Stakeholder RACI: Accountable for clinical safety case)
**Action Owner:** CCIO

#### Risk Identification

**Risk Description:**
A clinician accepts generated content that contains a hallucination, an omission of a critical detail such as an allergy, or an incorrect synthesis of information [NB-C12], and that content enters the clinical record and informs subsequent care. This is the harm the entire clinical safety apparatus exists to prevent.

**Root Cause:**
Generated output is fluent, plausible, and confident regardless of whether it is correct. Review is performed by clinicians under time pressure who are, by design, using the tool because they have insufficient time — the same pressure that makes the tool valuable makes its review step vulnerable.

**Trigger Events:**

- High-volume documentation session with time pressure
- Generated content that is largely correct, making the single error harder to spot than wholesale nonsense
- Review presented as a formality — pre-ticked, defaulted, or bulk-acceptable
- Clinician unfamiliar with the tool's specific failure modes
- Omission rather than commission: the error is what is *absent*, which review is far worse at catching

**Consequences if Realized:**

- Patient harm, potentially severe — an omitted allergy is the canonical example
- Incorrect information persists in the clinical record and propagates to subsequent care
- Serious incident investigation, coroner's inquest, CQC involvement
- Cascades directly into R-013 and R-015
- Clinician professionally exposed for content they did not author

**Affected Stakeholders:**

- **Patients**: bear the harm
- **Frontline clinicians** (SD-10): professionally accountable for accepted content
- **Clinical Safety Officer** (SD-4): the hazard they exist to control
- **Trust Chief Executive** (SD-16): organisational accountability

**Related Objectives:**

- **STKE O-2** (No AI-attributable clinical harm) — the outcome this risk directly negates
- **REQ BR-003, FR-001, FR-002, FR-003, FR-005** · **PRIN 11** (Human Accountability for Automated Output)

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 4 - Likely | Across hundreds of thousands of users generating clinical correspondence daily, with no labelling and no enforced review, acceptance of erroneous content is a near-certainty over any meaningful period. |
| **Impact** | 5 - Catastrophic | Direct patient harm, up to and including death from an omitted contraindication. |
| **Inherent Risk Score** | **20** (Critical) | 4 × 5 = 20 |

**Risk Zone:** 🟥 Critical (20-25)

#### Current Controls and Mitigations

1. **Distinguishable labelling of generated content** (REQ FR-001): persistent visual and structural marker at every point of display and export.
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — necessary but weak alone; labelling changes attention, not accuracy

2. **Enforced human review before clinical record entry** (REQ FR-002): silent or default acceptance is impossible; acceptance recorded per item, not per batch.
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Strong** — the per-item requirement specifically defeats bulk-acceptance behaviour

3. **Generation, review, and acceptance audit trail** (REQ FR-003): attributable and reconstructable during investigation.
   - Owner: Clinical Safety Officer
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — detection and learning, not prevention

4. **Training leading with failure modes** (REQ FR-014, STKE G-8): 85% competence within 60 days, including recognition of omission-type errors.
   - Owner: L&D lead
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

5. **Non-punitive reporting of unreliable output** (REQ FR-005): feeds the hazard log within two actions.
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Strong** — converts near-misses into controls before they become harm

6. **Out of scope for clinical decision support** (REQ Project Scope): bounds the content types where an error could be most consequential.
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Strong**

**Overall Control Effectiveness:** Strong — six layered controls reduce likelihood from 4 to 2. No control reduces impact, and none can: an accepted error harms the patient identically whether or not a review step existed.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Enforced per-item review plus labelling plus failure-mode training addresses the dominant pathway. Residual reflects the irreducible reality that human review under time pressure is imperfect, and is worst at catching omissions. |
| **Impact** | 5 - Catastrophic | Unchanged and irreducible. |
| **Residual Risk Score** | **10** (Medium) | 2 × 5 = 10 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 50% reduction from inherent (20 → 10)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:**
Layered treatment is the only viable response. The activity delivers the programme's entire benefit, so termination would mean abandoning it; the harm cannot be transferred; and Critical inherent risk cannot be tolerated.

**Alternative Responses Considered:**

- **Tolerate**: Rejected absolutely — Critical patient-safety risk
- **Transfer**: Not available — clinical accountability for accepted content rests with the clinician and the organisation, not the supplier
- **Terminate**: Considered and partially applied — clinical decision support *is* terminated (out of scope, see R-013). Terminating administrative use as well would end the programme

#### Risk Appetite Assessment

**Provisional appetite for clinical safety / patient harm risks:** Very Low (Score ≤ 4)
**Current Residual Risk Score:** 10 (Medium)
**Assessment:** ❌ **Significantly exceeds appetite** — 2.5× the threshold

**Justification:**
Catastrophic impact is irreducible, so appetite can only be reached through likelihood 1 (Rare). That would require review to be reliable rather than merely mandatory — plausible only with sustained operational evidence, mature training, and demonstrated near-miss capture. This is the register's central residual exposure and should be understood as the price of the programme, explicitly accepted rather than assumed away.

**Escalation Required:** Yes — Trust Board. This is the risk the board is being asked to accept in order to proceed at all, and it should be presented in exactly those terms.

#### Action Plan

1. **Appoint and fund the Clinical Safety Officer** — Owner: Trust Chief Executive · Due: 2026-09-30 · Expected impact: prerequisite; without an owner this risk is unmanaged
2. **Implement per-item enforced review before wave 1** — Owner: CCIO · Due: Before wave 1 · Expected impact: the single strongest control; without it likelihood returns to 4
3. **Deliver failure-mode training with 85% competence before enablement** — Owner: L&D lead · Due: Within 60 days of each enablement · Expected impact: improves review reliability, targeting likelihood 1
4. **Establish near-miss capture and monthly hazard review** — Owner: Clinical Safety Officer · Due: Before wave 1 · Expected impact: converts near-misses into controls
5. **Design review UX specifically against omission errors** — Owner: CCIO · Due: Before wave 1 · Expected impact: addresses the failure mode review is worst at

**Target Residual Risk After Mitigations:**

- Target Likelihood: 1 (Rare) — requires sustained evidence, realistically 12+ months
- Target Impact: 5 (Catastrophic) — irreducible
- Target Score: 5 (Low) — at the boundary of a Very Low appetite

**Success Criteria:**

- Zero AI-attributable patient safety incidents
- 100% of accepted generated content carrying an attributable review event
- Near-miss reports rising in early operation — a falling rate this early indicates under-reporting, not safety
- 85% or more demonstrating competence within 60 days of enablement

**Monitoring Plan:**

- **Frequency:** Monthly hazard review; continuous incident monitoring
- **Key Indicators:** AI-attributable incidents; near-miss reports; review completion; competence rate
- **Escalation Triggers:** any AI-attributable incident, immediately to Trust Chief Executive; near-miss reporting falling below expected volume

---

### Risk R-018: Drift detection cannot distinguish administrative from clinical use

**Category:** TECHNOLOGY
**Status:** Open
**Risk Owner:** Chief Clinical Information Officer (Stakeholder RACI: Responsible for intended-use boundary definition)
**Action Owner:** CIO / CDIO
**Supersedes:** REQ RQ-5

#### Risk Identification

**Risk Description:**
Assumption A-1 — that telemetry is granular enough to tell administrative use from clinical use — proves false. Drift detection (FR-004) cannot identify out-of-boundary use, and the control credited against R-013 and relied on by R-001 and R-017 does not function.

**Root Cause:**
The distinction between administrative and clinical use is semantic, not structural. Drafting a letter and summarising a consultation may be indistinguishable in telemetry: same tool, same document type, same user, same workflow. The boundary that governs the whole programme may not be observable in the data available.

**Trigger Events:**

- First analysis of drift telemetry shows no usable signal separating use classes
- Cohort-level aggregation (required by FR-006) destroys the granularity detection needs
- Content-based classification is unavailable because content inspection would itself raise confidentiality concerns

**Consequences if Realized:**

- The SaMD boundary (R-013) becomes unenforceable and unverifiable
- Clinical safety assurance rests on an assumption that cannot be evidenced
- The organisation cannot demonstrate to a regulator that the tool stayed within its assessed use
- The C-3 compromise collapses: cohort-level monitoring was accepted *instead of* individual monitoring, and if cohort-level does not work the pressure to expand monitoring returns

**Affected Stakeholders:**

- **CCIO** (SD-2): owns the boundary
- **Clinical Safety Officer** (SD-4): assurance depends on it
- **Staff-side** (SD-11): would face renewed pressure for more granular monitoring

**Related Objectives:**

- **STKE G-2** · **REQ FR-004, assumption A-1** · **PRIN 11**

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Genuinely uncertain. The distinction is semantic and the telemetry has not been examined; this is an untested assumption, not a considered judgement. |
| **Impact** | 4 - Major | Disables a control that three other risks depend on, though it does not itself cause harm. |
| **Inherent Risk Score** | **12** (Medium) | 3 × 4 = 12 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **Assumption explicitly recorded and flagged for validation** (REQ A-1): named as load-bearing rather than buried.
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — visibility, not resolution

2. **Sampling-review fallback** (REQ RQ-5, STKE Conflict C-3): if telemetry proves insufficient, fall back to periodic consented sampling review rather than expanding individual monitoring.
   - Owner: CCIO
   - Maturity: **Proposed**
   - Effectiveness: **Adequate** — slower and less complete, but preserves the C-3 compromise

3. **Boundary comprehension survey** (REQ FR-014, G-2): 80% target for correctly stating the boundary — a behavioural proxy when telemetry cannot measure directly.
   - Owner: L&D lead
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

**Overall Control Effectiveness:** Adequate — the fallback preserves *some* detection capability but does not restore what automated detection would have provided. This is the one risk in the register where controls reduce impact but barely touch likelihood.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Unchanged. No control makes the semantic distinction more observable; the assumption is either true or it is not, and nothing here alters that. |
| **Impact** | 3 - Moderate | The sampling fallback plus comprehension surveys preserve partial detection, so failure degrades assurance rather than eliminating it. |
| **Residual Risk Score** | **9** (Medium) | 3 × 3 = 9 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 25% reduction from inherent (12 → 9) — the lowest reduction in the register, and appropriately so

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:**
The uncertainty is resolvable by testing rather than by control design. The correct treatment is to validate A-1 early, while a fallback still has time to be built, rather than discovering the failure after wave 1.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — three other risks depend on this control functioning
- **Transfer** / **Terminate**: Not applicable

#### Risk Appetite Assessment

**Provisional appetite for TECHNOLOGY risks:** Medium (Score ≤ 9)
**Current Residual Risk Score:** 9 (Medium)
**Assessment:** ✅ **At appetite threshold** — within, with no margin

**Justification:** Sits exactly at threshold. Note that its realisation pushes R-013 further above appetite, so it warrants attention disproportionate to its own score.

**Escalation Required:** No on score; **Yes as a dependency** for R-013's board escalation

#### Action Plan

1. **Validate assumption A-1 against real telemetry before wave 2** — Owner: CIO / CDIO · Due: 2026-10-31 · Expected impact: converts an assumption into a finding either way
2. **Design and cost the sampling-review fallback in parallel** — Owner: CCIO · Due: 2026-11-30 · Expected impact: ensures a control exists if A-1 fails, rather than a gap
3. **Report the A-1 outcome to the board alongside R-013** — Owner: CCIO · Due: Next board cycle after validation

**Target Residual Risk After Mitigations:** L2 × I3 = **6** (Medium) ✅ — likelihood falls only once A-1 is actually tested and, if it fails, the fallback is operating

**Success Criteria:**

- A-1 validated or refuted with evidence before wave 2
- If refuted, the sampling fallback operating before wave 2
- Boundary comprehension at 80% or above regardless of telemetry outcome

**Monitoring Plan:**

- **Frequency:** Monthly until A-1 is resolved
- **Key Indicators:** A-1 validation status; detection rate; comprehension survey results
- **Escalation Triggers:** A-1 refuted with no fallback in place; any wave 2 enablement before validation

---

### Risk R-019: Shared clinical workstations cannot support frictionless authenticators

**Category:** TECHNOLOGY
**Status:** Open
**Risk Owner:** CIO / CDIO (Stakeholder RACI: Accountable for technology operations)
**Action Owner:** Registration Authority Manager

#### Risk Identification

**Risk Description:**
Assumption A-4 proves false: existing shared clinical workstations lack the hardware to support biometrics or high-assurance passkeys. The frictionless authentication that resolves Conflict C-5 requires an unfunded device refresh, and the security-versus-usability trade-off returns as a genuine conflict.

**Root Cause:**
Shared clinical workstations are long-lived, heterogeneous, and replaced on estate cycles rather than programme cycles. Their capability was not surveyed before the authentication approach was chosen.

**Trigger Events:**

- Device capability assessment (dependency D-7) reveals material incapability
- Authenticator migration begins in an area whose devices cannot enrol
- Estate refresh budget unavailable in the programme period

**Consequences if Realized:**

- BR-008 target unachievable in affected areas; credential sharing persists there
- Conflict C-5 reverts to a real trade-off: either accept friction, and with it continued sharing, or fund a refresh
- Attribution — and therefore investigation capability — remains compromised where the estate is weakest, which is likely to correlate with the least well-resourced settings (feeding R-004)

**Affected Stakeholders:**

- **Registration Authority Manager** (SD-13), **CISO** (SD-7), **frontline clinicians** (SD-10) in affected areas

**Related Objectives:**

- **STKE G-7, O-4** · **REQ BR-008, FR-007, NFR-P-001, assumption A-4, dependency D-7** · **PRIN 12**

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Mixed estates commonly contain a substantial minority of older devices; complete capability would be fortunate. |
| **Impact** | 3 - Moderate | Affects a subset of areas rather than the whole programme, and has a known if expensive remedy. |
| **Inherent Risk Score** | **9** (Medium) | 3 × 3 = 9 |

**Risk Zone:** 🟨 Medium (6-12)

#### Current Controls and Mitigations

1. **Device capability assessment as a named dependency** (REQ D-7): surveyed before migration rather than discovered during it.
   - Owner: IT Operations
   - Maturity: **Designed**
   - Effectiveness: **Strong** — early discovery converts a surprise into a plan

2. **Fallback at equivalent assurance** (REQ FR-007): where a frictionless authenticator is unavailable, a fallback at equivalent assurance is offered — explicitly not a shared credential.
   - Owner: RA Manager
   - Maturity: **Designed**
   - Effectiveness: **Adequate** — preserves assurance, not convenience

3. **Area-by-area migration paced to capability** (REQ Data Migration): sequenced by RA capacity and device readiness rather than uniformly.
   - Owner: RA Manager
   - Maturity: **Designed**
   - Effectiveness: **Adequate**

**Overall Control Effectiveness:** Adequate — cannot make incapable devices capable, but ensures the gap is known, planned, and does not silently reintroduce credential sharing.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 2 - Unlikely | Early assessment plus phased migration means capability gaps are identified and planned for rather than encountered mid-rollout. |
| **Impact** | 3 - Moderate | Unchanged — affected areas still need funding or continue with friction. |
| **Residual Risk Score** | **6** (Medium) | 2 × 3 = 6 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 33% reduction from inherent (9 → 6)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:** Early assessment and phased migration are cheap; discovering the gap mid-migration is not.

**Alternative Responses Considered:**

- **Tolerate**: Partially applicable — tolerating friction in a small number of areas may be proportionate, but only as an explicit decision with the credential-sharing consequence acknowledged
- **Transfer**: Not applicable
- **Terminate**: Not viable

#### Risk Appetite Assessment

**Provisional appetite for TECHNOLOGY risks:** Medium (Score ≤ 9)
**Current Residual Risk Score:** 6 (Medium) — ✅ **Within appetite**

**Escalation Required:** No on score; a funding escalation follows if the assessment shows material incapability

#### Action Plan

1. **Complete the shared workstation capability assessment** — Owner: IT Operations · Due: 2026-09-30 · Expected impact: resolves A-4 either way
2. **Cost any required device refresh and escalate as a funding decision** — Owner: CIO / CDIO · Due: 2026-10-31 · Expected impact: makes the trade-off explicit rather than silently accepting friction
3. **Sequence migration to capable areas first** — Owner: RA Manager · Due: Migration planning

**Target Residual Risk After Mitigations:** L1 × I3 = **3** (Low) ✅

**Success Criteria:** 100% device capability assessment coverage before migration; no area migrated without a viable authenticator; no area silently left on shared credentials

**Monitoring Plan:**

- **Frequency:** Monthly during migration
- **Key Indicators:** device capability coverage (%); areas migrated; areas awaiting refresh
- **Escalation Triggers:** more than 20% of shared workstations found incapable; any area continuing with shared credentials beyond its planned migration date

---

### Risk R-020: Shadow AI adopted outside the assessed boundary

**Category:** TECHNOLOGY
**Status:** Open
**Risk Owner:** Chief Information Security Officer (Stakeholder RACI: Accountable for security assurance)
**Action Owner:** CCIO
**Supersedes:** STKE R-5, REQ RQ-6

#### Risk Identification

**Risk Description:**
Staff adopt unapproved AI tools — consumer chatbots, browser extensions, personal accounts — because the approved tooling is slower or less capable, placing patient data outside any assessed control. Where official systems frustrate them, staff adopt unofficial tools [NB-C14]; this is a rational response to friction, not a discipline problem.

**Root Cause:**
Capable consumer AI is freely available, and the gap between what staff need and what approved tooling delivers is filled by whatever is to hand. Prohibition without a usable alternative simply moves the behaviour out of sight.

**Trigger Events:**

- Approved tooling slower than the workaround for a common task (NFR-U-001 not met)
- Capability restricted by licence tier (R-009) below what the role needs
- Capability request process slow enough that staff stop using it
- Deployment wave delayed, leaving a need unmet with an obvious substitute available

**Consequences if Realized:**

- Patient identifiable data processed by an unassessed third party outside UK jurisdiction — an ICO-reportable breach
- No audit trail, no clinical safety assessment, no retention control over that processing
- DSPT assertion failure (R-014)
- The organisation cannot state what tools are in clinical use, undermining every assurance claim

**Affected Stakeholders:**

- **CISO** (SD-7): assurance boundary breached
- **SIRO / DPO** (SD-6): risk accepted on an incomplete picture
- **Caldicott Guardian** (SD-5): confidentiality outside any control
- **Frontline clinicians** (SD-10): exposed to disciplinary risk for a rational workaround

**Related Objectives:**

- **STKE G-5, O-3** · **REQ NFR-U-001, BR-004** · **PRIN 4, PRIN 11**

#### Inherent Risk Assessment (Before Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 4 - Likely | Capable consumer AI is free and immediately available; any capability or speed gap in approved tooling will be filled. Prohibition alone has a poor record here. |
| **Impact** | 4 - Major | Uncontrolled processing of patient data by an unassessed third party, with regulatory and confidentiality consequences. |
| **Inherent Risk Score** | **16** (High) | 4 × 4 = 16 |

**Risk Zone:** 🟧 High (13-19)

#### Current Controls and Mitigations

1. **Usability treated as a security control** (REQ NFR-U-001): approved tooling must be measurably faster than the workaround it replaces, verified by timed task comparison before wave enablement.
   - Owner: CCIO
   - Maturity: **Designed**
   - Effectiveness: **Strong** — addresses the cause rather than the symptom

2. **Fast, non-punitive capability request route** (STKE Synergy S-3)
   - Owner: CCIO
   - Maturity: **Proposed**
   - Effectiveness: **Strong** — gives the need somewhere legitimate to go

3. **Monitoring for unapproved tool use**
   - Owner: CISO
   - Maturity: **Proposed**
   - Effectiveness: **Adequate** — detection only, and detection drives behaviour underground unless paired with control 2

4. **Network and endpoint controls limiting access to unapproved services**
   - Owner: CISO
   - Maturity: **Proposed**
   - Effectiveness: **Weak** — trivially circumvented on personal devices, which is where most shadow use occurs

**Overall Control Effectiveness:** Adequate — the usability control is strong but unproven, and the technical controls are weak against the actual threat model, which is a clinician using a personal phone.

#### Residual Risk Assessment (After Controls)

| Assessment | Rating | Justification |
|------------|--------|---------------|
| **Likelihood** | 3 - Possible | Genuinely reduced where approved tooling is good and the request route works, but personal-device use remains largely uncontrollable by technical means. |
| **Impact** | 3 - Moderate | Detection and a legitimate alternative route mean incidents are more likely to be isolated and caught rather than systemic and hidden. |
| **Residual Risk Score** | **9** (Medium) | 3 × 3 = 9 |

**Risk Zone:** 🟨 Medium (6-12)
**Risk Reduction:** 44% reduction from inherent (16 → 9)

#### Risk Response (4Ts Framework)

**Primary Response:** TREAT (Mitigate/Reduce)

**Rationale:**
Treated primarily by removing the motive rather than blocking the means. Blocking alone fails against personal devices and drives the behaviour out of view, which is worse than visible shadow use.

**Alternative Responses Considered:**

- **Tolerate**: Rejected — High inherent with regulatory consequence
- **Transfer**: Not available
- **Terminate**: Not viable — would mean prohibiting AI entirely, which does not stop personal-device use

#### Risk Appetite Assessment

**Provisional appetite for TECHNOLOGY risks:** Medium (Score ≤ 9)
**Current Residual Risk Score:** 9 (Medium)
**Assessment:** ✅ **At appetite threshold** — within, with no margin

**Justification:** At threshold. Any delay to deployment, or any tier decision that restricts capability below role need, will push it over — the two are directly linked.

**Escalation Required:** No, but flagged: this risk rises whenever the programme slows

#### Action Plan

1. **Establish the capability request route before wave 1** — Owner: CCIO · Due: Before wave 1 · Expected impact: gives unmet need a legitimate destination
2. **Run timed task comparison against current practice before each wave** — Owner: CCIO · Due: Per wave · Expected impact: verifies NFR-U-001 rather than assuming it
3. **Communicate that reporting shadow use is non-punitive** — Owner: CISO · Due: Before wave 1 · Expected impact: surfaces existing use, which almost certainly predates the programme
4. **Baseline current shadow AI use before wave 1** — Owner: CISO · Due: 2026-10-31 · Expected impact: establishes whether the programme reduces or merely relocates the behaviour

**Target Residual Risk After Mitigations:** L2 × I3 = **6** (Medium) ✅ with margin

**Success Criteria:**

- Approved tooling demonstrably faster than the workaround for target tasks
- Capability requests answered within a defined service level
- Measured shadow AI use trending down after enablement
- Zero confirmed instances of patient data in an unapproved service

**Monitoring Plan:**

- **Frequency:** Monthly
- **Key Indicators:** detected unapproved tool use; capability request volume and turnaround; timed task comparison results
- **Escalation Triggers:** any confirmed patient data in an unapproved service; capability request backlog exceeding the service level
---

## D. Risk Category Analysis

### STRATEGIC Risks

**Count:** 4 (R-001, R-002, R-003, R-004) · **Avg inherent:** 14.0 · **Avg residual:** 7.5 · **Control reduction:** 46%

**Key themes:** Every strategic risk here arises from a decision being made by default rather than deliberately — the gate overridden under pressure, the pilot figure adopted as a forecast, the tenancy model inherited rather than chosen, the distributional outcome accepted rather than designed. The common control is the same in each case: force the decision to be explicit, evidenced, and recorded. None of these risks requires new technology.

### OPERATIONAL Risks

**Count:** 4 (R-005, R-006, R-007, R-008) · **Avg inherent:** 12.0 · **Avg residual:** 6.3 · **Control reduction:** 48%

**Key themes:** Capacity and sequencing. R-005 is the most consequential risk in this category not because of its own score but because it is the upstream cause of R-001, the register's joint-highest. R-006 and R-008 share a property that makes them unusually urgent: both have windows that close permanently — baselines cannot be captured after enablement, and a reinvestment commitment cannot be made credibly after a savings figure is published.

### FINANCIAL Risks

**Count:** 2 (R-009, R-010) · **Avg inherent:** 10.5 · **Avg residual:** 7.0 · **Control reduction:** 33%

**Key themes:** The lowest control reduction of any category, for a defensible reason — financial risks here are governed by contract terms and board commitments rather than by technical controls, and neither reduces impact. R-010 is notable as the only risk whose realisation would be a deliberate organisational act rather than a failure.

### COMPLIANCE/REGULATORY Risks

**Count:** 4 (R-011, R-012, R-013, R-014) · **Avg inherent:** 14.8 · **Avg residual:** 8.0 · **Control reduction:** 46%

**Key themes:** The highest average inherent score of any category, and the category containing three of the six appetite exceedances. Two distinct patterns: configuration risks (R-011, R-012) which are cheap to control and expensive to remediate, and regulatory-status risks (R-013, R-014) where impact is irreducible and only likelihood can be moved.

### REPUTATIONAL Risks

**Count:** 2 (R-015, R-016) · **Avg inherent:** 12.0 · **Avg residual:** 6.5 · **Control reduction:** 46%

**Key themes:** These two risks sit at opposite extremes of control economics. R-016 is the cheapest risk in the register to control — a written agreement, concluded before deployment, at essentially no cost, achieving a 67% reduction. R-015 is almost entirely derivative and cannot be reduced below the clinical risks that cause it.

### TECHNOLOGY Risks

**Count:** 4 (R-017, R-018, R-019, R-020) · **Avg inherent:** 14.3 · **Avg residual:** 8.5 · **Control reduction:** 40%

**Key themes:** The highest average residual of any category. R-017 is the risk the programme exists to manage. R-018 is unusual in that controls barely move its likelihood — the uncertainty is resolvable only by testing, not by control design. R-020 is the clearest illustration of the register's recurring lesson: usability is a security control, and prohibition without a usable alternative relocates the behaviour rather than preventing it.

---

## E. Risk Ownership Matrix

| Stakeholder | Owned Risks | Count | Highest Residual | Notes |
|-------------|-------------|-------|------------------|-------|
| Chief People Officer | R-004, R-008, R-010, R-016 | 4 | 8 (R-010) | Heaviest load by count; all workforce-trust risks, all controllable at near-zero cost if sequenced correctly |
| Trust Chief Executive | R-001, R-005, R-015 | 3 | 10 (R-001, R-015) | Owns two of the top five and is escalation point for the rest |
| CIO / CDIO | R-003, R-007, R-019 | 3 | 8 (R-003) | Technology and infrastructure decisions |
| National Programme SRO | R-002, R-006 | 2 | 6 | Both concern benefit measurement integrity |
| Caldicott Guardian | R-011, R-012 | 2 | 8 (R-011) | Both compliance configuration risks; both exceed or sit at appetite |
| Clinical Safety Officer | R-013, R-017 | 2 | 10 (both) | ⚠ **Post not yet filled** — see below |
| Chief Information Security Officer | R-020 | 1 | 9 | At appetite threshold |
| Senior Information Risk Owner | R-014 | 1 | 8 | Exceeds appetite |
| Chief Clinical Information Officer | R-018 | 1 | 9 | At appetite threshold |
| Director of Finance | R-009 | 1 | 6 | The register's only TRANSFER response |

**Concentration findings:**

1. **⚠ The Clinical Safety Officer owns two of the register's three highest-scoring risks, and the post is unfilled.** R-013 and R-017 both carry residual 10 and both significantly exceed appetite. Until dependency D-1 is discharged, these risks have a nominal owner rather than an actual one. This is the most urgent single finding in the register.

2. **The Trust Chief Executive owns or is the escalation point for all five of the top five risks.** Appropriate for accountability, but it creates a single decision bottleneck for the programme's entire critical path. The Audit and Risk Committee should consider whether escalation for R-011 and R-014 could rest with the SIRO alone.

3. **The Chief People Officer's four risks are collectively the cheapest to control in the register** — R-008, R-010, and R-016 are all resolved primarily by making written commitments in the right order, before deployment. Their combined inherent score is 33 and combined residual 23; done early, that could be 15.

---

## F. 4Ts Response Framework Summary

| Response | Count | % | Risks | Rationale pattern |
|----------|-------|---|-------|-------------------|
| **Tolerate** | 2 | 10% | R-007, R-016 | Low residual after treatment; further investment disproportionate. Note R-016's tolerance is conditional on dependency D-2 being discharged first |
| **Treat** | 16 | 80% | R-001, R-002, R-003, R-004, R-005, R-006, R-008, R-010, R-011, R-012, R-014, R-015, R-017, R-018, R-019, R-020 | Mitigable through controls at proportionate cost |
| **Transfer** | 1 | 5% | R-009 | Contractual right to reassign users between licence tiers transfers the cost of a wrong tier decision to the supplier agreement |
| **Terminate** | 1 | 5% | R-013 | Clinical-scope AI deployment is excluded from scope rather than mitigated — the activity creating the exposure is not undertaken |

**Observation on the distribution:** an 80% Treat rate is high, and would normally suggest insufficiently rigorous consideration of alternatives. Here it reflects a genuine constraint — clinical safety and data protection accountability cannot be transferred, and the activities creating most of these risks are the programme itself. The two non-Treat responses that do exist (R-009 Transfer, R-013 Terminate) are both substantive rather than nominal.

---

## G. Risk Appetite Compliance

> **These thresholds are provisional.** No ratified organisational risk appetite statement exists for this programme. They are proposed here for Audit and Risk Committee ratification, calibrated so that appetite for patient-safety risk is materially lower than for delivery or financial risk. Until ratified, "exceeds appetite" is an architect's judgement rather than an organisational position.

| Category | Provisional Threshold | Risks Within | Risks Exceeding | Action Required |
|----------|----------------------|--------------|-----------------|-----------------|
| Clinical safety / patient harm | Very Low (≤ 4) | 0 | R-001, R-013, R-017 | Trust Board acceptance decision |
| COMPLIANCE / Regulatory | Low (≤ 6) | R-012 (at threshold) | R-011, R-013, R-014 | SIRO and Caldicott Guardian formal interim acceptance |
| REPUTATIONAL | Low (≤ 6) | R-016 | R-015 | Trust Board, jointly with R-013 and R-017 |
| TECHNOLOGY | Medium (≤ 9) | R-017*, R-018, R-019, R-020 | — | R-018 and R-020 at threshold with no margin |
| OPERATIONAL | Medium (≤ 12) | R-005, R-006, R-007, R-008 | — | Within appetite |
| FINANCIAL | Medium (≤ 12) | R-009, R-010 | — | Within appetite |
| STRATEGIC | Medium (≤ 12) | R-001*, R-002, R-003, R-004 | — | Within appetite on the strategic scale |

\* R-001 and R-017 are within their *category* appetite but significantly exceed the **clinical safety** appetite, which is the binding constraint for any risk with a patient-harm pathway. Where two scales apply, the lower governs.

**Six unique risks exceed appetite: R-001, R-011, R-013, R-014, R-015, R-017.**

All six are driven by irreducible impact rather than by inadequate controls — in every case the residual sits at likelihood 2 with impact 4 or 5. No additional control will bring them within appetite; only sustained operational evidence reducing likelihood to 1, or a board decision to accept, will resolve them. That is the honest position and it should be presented to the board in those terms rather than as a control gap to be closed.

---

## H. Prioritized Action Plan

### Priority 1: URGENT — prerequisites, and windows that close permanently

| # | Action | Risks Addressed | Owner | Due Date | Status |
|---|--------|-----------------|-------|----------|--------|
| 1 | Appoint and fund the Clinical Safety Officer (dependency D-1) | R-001, R-005, R-013, R-017 | Trust Chief Executive | 2026-09-30 | Not started |
| 2 | Conclude the written telemetry-use agreement (dependency D-2) | R-016, R-018, R-006 | Chief People Officer | 2026-09-30 | Not started |
| 3 | Capture cohort baselines before any enablement | R-002, R-006 | Local programme lead | Before each enablement | Not started |
| 4 | Secure the board reinvestment commitment before any savings figure is published | R-008, R-010 | Trust Chief Executive | Before first benefit report | Not started |
| 5 | Agree the retention schedule register (dependency D-6) | R-012 | Caldicott Guardian | 2026-09-30 | Not started |
| 6 | Ratify the risk appetite thresholds | All appetite exceedances | Audit and Risk Committee | 2026-09-30 | Not started |

> Actions 2, 3 and 4 address windows that close permanently. A baseline cannot be captured after enablement; a telemetry agreement reached after a dispute is a settlement rather than an agreement; a reinvestment commitment made after a savings figure is published is a response rather than a commitment.

### Priority 2: HIGH — controls for risks exceeding appetite

| # | Action | Risks Addressed | Owner | Due Date | Status |
|---|--------|-----------------|-------|----------|--------|
| 7 | Implement per-item enforced human review | R-017 | CCIO | Before wave 1 | Not started |
| 8 | Implement the technical deployment gate (FR-018) | R-001 | Delivery Manager | Before wave 1 | Not started |
| 9 | Configure identifier-sharing controls and workspace classification | R-011 | IG Manager | Before wave 1 | Not started |
| 10 | Validate assumption A-1 — telemetry can distinguish use classes | R-018, R-013 | CIO / CDIO | 2026-10-31 | Not started |
| 11 | Configure explicit retention for all clinical workspaces | R-012 | IG Manager | Before clinical use | Not started |
| 12 | Board decision on whether the FR-018 override path should exist | R-001 | Trust Chief Executive | 2026-10-31 | Not started |
| 13 | Bring AI capability into assessed DSPT scope | R-014 | CISO | Next submission | Not started |
| 14 | Prepare the incident communications plan | R-015 | Director of Communications | Before wave 1 | Not started |

### Priority 3: MEDIUM — treatment for risks within appetite

| # | Action | Risks Addressed | Owner | Due Date | Status |
|---|--------|-----------------|-------|----------|--------|
| 15 | Complete the legacy clinical system inventory (D-4) | R-003 | Clinical systems team | 2026-09-30 | Not started |
| 16 | Produce the tenancy decision record as an ADR | R-003, R-014 | Enterprise Architect | 2026-10-15 | Not started |
| 17 | Complete shared workstation capability assessment (D-7) | R-019 | IT Operations | 2026-09-30 | Not started |
| 18 | Fund the fixed-term Registration Authority uplift (D-5) | R-005 | CIO / CDIO | 2026-10-31 | Not started |
| 19 | Establish the capability request route | R-020 | CCIO | Before wave 1 | Not started |
| 20 | Baseline current shadow AI use | R-020 | CISO | 2026-10-31 | Not started |
| 21 | Publish runbooks covering the AI query class | R-007 | Service Desk Manager | Before wave 1 | Not started |
| 22 | Define and publish the redeployment and reskilling pathway | R-008, R-010 | Chief People Officer | Before wave 1 | Not started |
| 23 | Produce the single integrated assurance pack template | R-005 | Enterprise Architect | 2026-09-30 | Not started |
| 24 | Sequence deployment to include under-served settings early | R-004 | Delivery Manager | Wave planning | Not started |

---

## I. Integration with SOBC

This register feeds the Strategic Outline Business Case as follows. Note that `/arckit:sobc` has not yet been run, and the Budget section of `ARC-001-REQ-v1.0` is deliberately unpopulated pending the tenancy decision (R-003) and tier evidence (R-009) — both of which are risks in this register. The business case cannot be completed honestly until those two are resolved.

### SOBC Strategic Case (Part A)

Strategic risks R-001 to R-004 inform the "why now" and the case for change. R-002 in particular constrains what benefit may be claimed: the Strategic Case must not repeat the national pilot figure as a local forecast.

### SOBC Economic Case (Part B)

Risk-adjusted costs should reflect the funding actions in this register that are not yet in any budget — CSO capacity (action 1), RA migration uplift (action 18), and any device refresh arising from R-019. Optimism bias adjustment should be informed by R-002: a programme whose headline benefit derives from a volunteer cohort warrants an above-standard adjustment.

### SOBC Management Case (Part E — Risk Management)

This register in full, together with the monitoring framework in Section J and the ownership matrix in Section E. The Management Case should state plainly that six risks exceed provisional appetite and that no appetite statement has been ratified.

### SOBC Recommendation

Two risks materially constrain option selection. R-003 (tenancy) is itself an option decision that must precede the business case rather than follow it. R-013's TERMINATE response — excluding clinical-scope AI from scope — is a scoping decision the Economic Case must reflect in its benefit assumptions, since clinical-scope benefits cannot be claimed for an activity that is not being undertaken.

---

## J. Monitoring and Review Framework

### Review Schedule

| Risk Level | Review Frequency | Forum |
|------------|------------------|-------|
| Risks exceeding appetite (R-001, R-011, R-013, R-014, R-015, R-017) | Monthly | Programme board, with quarterly Trust Board reporting |
| At appetite threshold (R-012, R-018, R-020) | Monthly | Programme board |
| Medium residual within appetite | Quarterly | Programme board |
| Low residual (R-007, R-016) | Quarterly | Risk register owner review only |
| All risks | At every wave gate | Clinical Safety Officer and SIRO |

**Additional trigger for re-scoring:** as each control moves from Designed to Implemented, the affected risk is re-scored. Given that zero controls are currently Implemented, the first three monthly reviews should expect substantial movement, and the residual column should be treated as unreliable until control maturity rises.

### Key Risk Indicators (KRIs)

| KRI | Risks Monitored | Threshold | Frequency |
|-----|-----------------|-----------|-----------|
| Controls moved to Implemented (%) | All | Below 50% at wave 1 is a programme-level concern | Monthly |
| AI-attributable patient safety incidents | R-017, R-015, R-013 | Any occurrence | Continuous |
| Near-miss reports per 1,000 users | R-017 | A *falling* rate in early operation signals under-reporting, not safety | Monthly |
| Waves gated before enablement (%) | R-001 | Below 100% | Per wave |
| Gate overrides exercised | R-001 | Any occurrence | Per wave |
| Cohort baseline coverage (%) | R-002, R-006 | Below 90% | Per wave |
| Out-of-boundary use detections | R-013, R-018 | Any confirmed clinical-scope use | Monthly |
| Workspaces on default retention | R-012 | Any | Monthly |
| ICO-reportable breaches from the platform | R-011, R-020 | Any occurrence | Continuous |
| Detected unapproved AI tool use | R-020 | Rising trend after enablement | Monthly |
| Credential-sharing indicators | R-019 | Below 80% reduction at 12 months | Monthly |
| Assurance sign-off cycle time | R-005 | Exceeding 4 weeks per wave | Per wave |
| Formal staff-side disputes | R-008, R-016 | Any occurrence | Monthly |

### Escalation Criteria

Escalate immediately to the Trust Chief Executive, and to the Trust Board at its next sitting, on any of:

- Any AI-attributable patient safety incident
- Any gate override exercised
- Any risk increasing by 5 or more points between reviews
- Any new risk scoring 15 or above at inherent level
- Any confirmed clinical-scope use of the tool (R-013 materialising)
- Any ICO-reportable breach originating from the platform
- Assumption A-1 refuted with no fallback operating (R-018)
- Any enablement proposed before dependencies D-1 or D-2 are discharged

### Reporting Requirements

| Audience | Frequency | Content |
|----------|-----------|---------|
| Clinical Safety Officer and SIRO | Per wave gate | Full register plus hazard log status |
| Programme board | Monthly | Risks exceeding or at appetite; KRI dashboard; action plan progress |
| Trust Board | Quarterly | Appetite exceedances with acceptance decisions; control maturity; incidents |
| Audit and Risk Committee | Quarterly | Appetite compliance; register maintenance quality |
| Partnership forum | Monthly | R-008, R-010, R-016 — the workforce-trust risks |
| National Programme SRO | Quarterly | R-001, R-002, R-006 — pace, benefit, and measurement integrity |

### Risk Register Maintenance

- **Register owner:** Mark Craddock, Enterprise Architect (custodian); accountability for individual risks rests with the named risk owners in Section E
- **Update triggers:** new risk identified; control maturity change; incident or near-miss; wave gate; material change to scope, tenancy, or licensing
- **Version control:** minor increment for re-scoring and status changes; major increment for new or removed risks, or a change to the appetite framework
- **Next review:** 2026-09-18

---

## K. Orange Book Compliance Checklist

### Part I — Risk Management Principles

| Principle | Status | Evidence |
|-----------|--------|----------|
| **A. Governance and Leadership** | ⚠ Partial | Every risk has a named owner drawn from the stakeholder RACI, and reporting lines to board level are defined. **Gap:** the Clinical Safety Officer post owning two of the three highest risks is unfilled, and no risk appetite statement has been ratified. |
| **B. Integration** | ✅ Met | Risks trace to stakeholder goals (STKE G-1 to G-8), outcomes (O-1 to O-6), and requirements. Section I maps the register into the forthcoming SOBC. |
| **C. Collaboration and Best Information** | ⚠ Partial | Risks derive from the stakeholder analysis, the requirements, and the source evidence base. **Gap:** no stakeholder interviews have been conducted (see STKE Appendix A), so likelihood and impact ratings are informed judgement rather than elicited expert consensus. |
| **D. Risk Management Processes** | ✅ Met | Systematic identification across all six categories, inherent and residual assessment, 4Ts response selection with alternatives documented, action plans with named owners and dates, and a monitoring framework. |
| **E. Continual Improvement** | ✅ Met | Monthly review cycle, control-maturity re-scoring trigger, KRIs with thresholds, and defined escalation criteria. |

### Part II — Risk Control Framework

| Pillar | Status | Notes |
|--------|--------|-------|
| **Risk culture** | ⚠ Partial | Non-punitive reporting (FR-005) and the telemetry-use agreement are designed to support an open culture, but neither yet exists. The near-miss KRI deliberately treats under-reporting as the warning signal. |
| **Risk appetite** | ❌ Gap | Provisional thresholds proposed here; none ratified. Six exceedances cannot be formally accepted until they are. |
| **Risk governance** | ⚠ Partial | Ownership, escalation, and reporting defined. Concentration on the Trust Chief Executive and the unfilled CSO post are noted weaknesses. |
| **Risk assurance** | ⚠ Partial | Assurance mechanisms are specified (DSPT, clinical safety case, DPIA) but none are yet operating for this programme. |

**Overall Orange Book position:** the *framework* is compliant; the *operating reality* is not yet, because no control has been implemented and no appetite ratified. This distinction should be stated explicitly to the Audit and Risk Committee rather than allowing a well-formed document to imply a well-managed risk position.

---

## Appendix A: Risk Assessment Scales

### Likelihood Scale (1-5)

| Score | Descriptor | Probability | Interpretation |
|-------|-----------|-------------|----------------|
| 1 | Rare | < 5% | Highly unlikely within the assessment period |
| 2 | Unlikely | 5-25% | Could happen but probably will not |
| 3 | Possible | 25-50% | Reasonable chance |
| 4 | Likely | 50-75% | More likely to happen than not |
| 5 | Almost Certain | > 75% | Expected to occur |

**Assessment period:** 24 months from first enablement, aligned to the deployment and first sustainment year.

### Impact Scale (1-5)

| Score | Descriptor | Clinical | Financial / Delivery | Regulatory / Reputational |
|-------|-----------|----------|---------------------|---------------------------|
| 1 | Negligible | No patient impact | < 5% variance | No external interest |
| 2 | Minor | No harm; inconvenience | 5-10% variance | Internal only |
| 3 | Moderate | Minor harm, fully recoverable | 10-20% variance | Local scrutiny |
| 4 | Major | Significant harm or near-miss with harm potential | 20-40% variance | Regulatory action; regional media |
| 5 | Catastrophic | Severe or fatal harm | > 40% variance | National media; enforcement; existential to the programme |

### Risk Score Matrix (Likelihood × Impact)

| | I=1 | I=2 | I=3 | I=4 | I=5 |
|---|---|---|---|---|---|
| **L=5** | 5 🟩 | 10 🟨 | 15 🟧 | 20 🟥 | 25 🟥 |
| **L=4** | 4 🟩 | 8 🟨 | 12 🟨 | 16 🟧 | 20 🟥 |
| **L=3** | 3 🟩 | 6 🟨 | 9 🟨 | 12 🟨 | 15 🟧 |
| **L=2** | 2 🟩 | 4 🟩 | 6 🟨 | 8 🟨 | 10 🟨 |
| **L=1** | 1 🟩 | 2 🟩 | 3 🟩 | 4 🟩 | 5 🟩 |

🟩 Low (1-5) · 🟨 Medium (6-12) · 🟧 High (13-19) · 🟥 Critical (20-25)

---

## Appendix B: Stakeholder-Risk Linkage

Full traceability from stakeholder driver through risk to action, as required by Orange Book Principle B (Integration).

| Stakeholder | STKE Driver | Concern | Risk(s) | Risk Owner | Primary Action |
|-------------|-------------|---------|---------|------------|----------------|
| National Programme SRO | SD-1 | Evidence return on £120m at national pace | R-001, R-002, R-006 | Trust CEO / SRO | Phase scope; capture baselines before enablement |
| CCIO | SD-2 | Prevent clinical drift | R-013, R-017, R-018 | CSO / CCIO | Validate A-1; enforce per-item review |
| Chief People Officer | SD-3 | Convert released time into retention | R-008, R-010, R-004 | Chief People Officer | Reinvestment commitment before any savings figure |
| Clinical Safety Officer | SD-4 | Discharge DCB0160 accountability | R-001, R-013, R-017 | CSO / Trust CEO | Appoint and fund the post (D-1) |
| Caldicott Guardian | SD-5 | Confidentiality without obstructing care | R-011, R-012 | Caldicott Guardian | Configure DLP and retention before clinical use |
| SIRO / DPO | SD-6 | Accept risk on evidence | R-014, R-011 | SIRO | Automate DSPT evidence capture |
| CISO | SD-7 | Assurance under rapid change | R-014, R-020 | CISO | Usability as a security control; capability request route |
| CIO / CDIO | SD-8 | Right tenancy model | R-003, R-019 | CIO / CDIO | Complete inventory; produce tenancy ADR |
| Director of Finance | SD-9 | Defensible licensing tier | R-009 | Director of Finance | Contractual tier reassignment right |
| Frontline clinicians | SD-10 | Time back without new risk | R-017, R-019, R-020 | CSO / CIO / CISO | Enforced review; frictionless authentication |
| Unions / professional bodies | SD-11 | Protect against second-order effects | R-008, R-016 | Chief People Officer | Telemetry-use agreement before enablement |
| Administrative staff | SD-12 | Benefit without role threat | R-008, R-010 | Chief People Officer | Redeployment and reskilling pathway |
| RA Manager | SD-13 | End credential sharing | R-019 | CIO / CDIO | Device capability assessment |
| L&D lead | SD-14 | Competence not completion | R-017 | CSO | Failure-mode training to 85% competence |
| CQC / ICO | SD-15 | Verifiable compliance | R-011, R-012, R-014 | Caldicott Guardian / SIRO | Continuous evidence capture |
| Trust Chief Executive | SD-16 | Avoid becoming the example | R-001, R-005, R-015 | Trust CEO | Fund assurance capacity; incident communications plan |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Risk Register Owner | Mark Craddock, Enterprise Architect | PENDING | PENDING |
| Clinical Safety Officer | PENDING — post unfilled (D-1) | PENDING | PENDING |
| Senior Information Risk Owner | PENDING | PENDING | PENDING |
| Caldicott Guardian | PENDING | PENDING | PENDING |
| Chief Information Security Officer | PENDING | PENDING | PENDING |
| Chief People Officer | PENDING | PENDING | PENDING |
| Executive Sponsor | PENDING | PENDING | PENDING |

---

## Next Steps

1. **Ratify the risk appetite thresholds** at the Audit and Risk Committee — without this, the six exceedances cannot be formally accepted or closed
2. **Appoint and fund the Clinical Safety Officer** — two of the three highest-scoring risks currently have no actual owner
3. **Validate the register with named risk owners** — likelihood and impact ratings are informed judgement, not elicited consensus (Orange Book Principle C gap)
4. **Escalate the six appetite exceedances to the Trust Board** with the honest framing that they are driven by irreducible impact, not by control gaps
5. **Begin control implementation** in Priority 1 order, and re-score at each monthly review as controls move from Designed to Implemented
6. **Feed this register into `/arckit:sobc`** Management Case Part E — noting that the Economic Case depends on R-003 and R-009 being resolved first
7. **Consider `/arckit:dpia`** — NFR-C-001 makes a DPIA a precondition for every wave, and R-011 and R-014 both depend on it

---

## External References

> This section provides traceability from generated content back to source documents.

### Document Register

| Doc ID | Filename | Type | Source Location | Description |
|--------|----------|------|-----------------|-------------|
| NB | nhs365-book2.pdf | Reference Guide | `000-global/external/` | *NHS 365 — A Best Practices Guide for Transforming UK Healthcare with Microsoft AI* (365apps.pro, 2026-08-11, 23 pages). Cited via the converted Markdown copy held alongside it. |
| STKE | ARC-001-STKE-v1.0.md | ArcKit Artifact | `001-nhs365/` | Stakeholder Drivers & Goals Analysis — source of risk owners (RACI), affected stakeholders, and risks R-1…R-7 consolidated here |
| REQ | ARC-001-REQ-v1.0.md | ArcKit Artifact | `001-nhs365/` | Requirements — source of controls, assumptions A-1…A-6, dependencies D-1…D-7, and risks RQ-1…RQ-7 consolidated here |
| PRIN | ARC-000-PRIN-v1.0.md | ArcKit Artifact | `000-global/` | Architecture Principles — non-compliance with principles 4, 6, 7, 10, 11, 12 and 18 informs several risks |

### Citations

| Citation ID | Doc ID | Page/Section | Category | Quoted Passage |
|-------------|--------|--------------|----------|----------------|
| NB-C1 | NB | Introduction — NHS England's Landmark Copilot Rollout | Risk Factor | "In that pilot, involving over 30,000 staff across 90 NHS organisations, participants saved an average of 43 minutes per person per day on administrative tasks... The rollout, expected to reach over 500,000 clinicians and support staff by October 2026" |
| NB-C2 | NB | Strategic Architecture — Security and Clinical Safety Governance | Compliance Constraint | "clinical risk management standards DCB0129 and DCB0160. The latter requires appointment of a Clinical Safety Officer who identifies hazards, assesses severity and likelihood, and ensures residual risk is reduced to a level that is as low as reasonably practicable before systems go live." |
| NB-C3 | NB | Strategic Architecture — Conclusion | Design Decision | "Critical decision factors include cyber maturity, the need for specialised integrations, the presence of legacy clinical systems that require hybrid identity, and the capacity to manage clinical safety governance for AI and automation." |
| NB-C4 | NB | Introduction — A Practical Guide for the People Driving Change | Risk Factor | "you will find honest discussion of the pitfalls—shadow AI, data quality issues, change fatigue, equity risks, and the critical need for clinical safety and information governance to be designed in from the start." |
| NB-C5 | NB | Care Identity Service — Practical Considerations for Organisations | Risk Factor | "Registration Authorities remain central for identity proofing, role assignment, and smartcard lifecycle management, though self-service options (including Apply for Care ID and smartcard unlock) have expanded." |
| NB-C6 | NB | Teams Rooms — Change Management and Measuring Success | Risk Factor | "Technology alone does not guarantee adoption. Organizations should identify clinical champions among physicians and nurses to lead pilots and advocate for the tools. Training must focus on practical workflows—such as sharing a DICOM image—rather than hardware specifications." |
| NB-C7 | NB | Strategic Architecture — Licensing Approach | Risk Factor | "The Standard Service, based on Microsoft 365 F3, targets frontline clinical staff and provides web-based Office applications, a 4 GB mailbox, and limited OneDrive storage... The Enhanced Service... offers larger mailboxes (50 GB), greater SharePoint allocation, and stronger security and compliance tools." |
| NB-C8 | NB | Workforce Transformation — Information Governance and Security | Compliance Constraint | "Existing tools such as Microsoft Purview can enforce policies that prevent inappropriate sharing of patient identifiers in collaborative channels." |
| NB-C9 | NB | Workforce Transformation — Microsoft 365 as the Digital Backbone | Data Requirement | "Data remains within the organisation's own tenant, simplifying governance and supporting UK data residency requirements." |
| NB-C10 | NB | Teams Rooms — Security, Compliance, and Governance | Data Requirement | "Default Teams retention settings may conflict with clinical record-keeping requirements. Microsoft Purview can enforce appropriate retention—often six years for clinical consultations—while allowing shorter periods for administrative content." |
| NB-C11 | NB | Strategic Architecture — Artificial Intelligence, Automation, and Associated Risks | Compliance Constraint | "Copilot is treated as an administrative productivity tool rather than Software as a Medical Device." |
| NB-C12 | NB | Strategic Architecture — Artificial Intelligence, Automation, and Associated Risks | Risk Factor | "'clinical drift'—the gradual use of generative AI for summarising patient notes or supporting clinical discussion—introduces risks of hallucination, omission of critical details such as allergies, or incorrect synthesis of information." |
| NB-C13 | NB | Care Identity Service — Practical Considerations for Organisations | Compliance Constraint | "Compliance is demonstrated primarily through the Data Security and Protection Toolkit (DSPT), aligned with the National Cyber Security Centre's Cyber Assessment Framework." |
| NB-C14 | NB | Workforce Transformation — Microsoft 365 as the Digital Backbone | Risk Factor | "By offering a coherent, secure experience inside the clinical workflow, trusts can reduce the appeal of 'shadow IT'—unofficial tools staff adopt when official systems frustrate them." |

### Unreferenced Documents

| Filename | Source Location | Reason |
|----------|-----------------|--------|
| README.md | `000-global/policies/` | Directory placeholder; no organisational policy content present. **No risk appetite statement, previous risk assessment, or external threat report has been supplied** — this is why the appetite thresholds in Section G are provisional rather than ratified. |
| README.md | `001-nhs365/external/` | Directory placeholder; no project-specific reference documents supplied yet. |

---

**Generated by**: ArcKit `/arckit:risk` command
**Generated on**: 2026-08-19
**ArcKit Version**: 6.11.0
**Project**: NHS 365 (Project 001)
**Model**: claude-opus-5[1m]

<!-- arckit-provenance:start -->

## Build Provenance

*Stamped automatically by the ArcKit plugin's `provenance-stamp.mjs` PostToolUse hook. Complements (does not replace) the human-authored footer above. Carries only fields the model can't authoritatively self-report: build context from `.arckit/state.json` and effort levels derived from command frontmatter + the silent-downgrade matrix.*

| Field | Value |
|-------|-------|
| Requested Effort | `high` |
| Effective Effort | `high` |
| Stamped at | 2026-08-19T11:37:23.483Z |

<!-- arckit-provenance:end -->
