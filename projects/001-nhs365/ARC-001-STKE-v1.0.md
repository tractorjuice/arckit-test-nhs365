# Stakeholder Drivers & Goals Analysis: NHS 365

> **Template Origin**: Official | **ArcKit Version**: 6.11.0 | **Command**: `/arckit:stakeholders`

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ARC-001-STKE-v1.0 |
| **Document Type** | Stakeholder Drivers & Goals Analysis |
| **Project** | NHS 365 (Project 001) |
| **Classification** | OFFICIAL |
| **Status** | DRAFT |
| **Version** | 1.0 |
| **Created Date** | 2026-08-19 |
| **Last Modified** | 2026-08-19 |
| **Review Cycle** | Quarterly |
| **Next Review Date** | 2026-11-19 |
| **Owner** | Mark Craddock, Enterprise Architect |
| **Reviewed By** | PENDING |
| **Approved By** | PENDING |
| **Distribution** | NHS 365 programme board; Trust executive team; Clinical Safety Officer; Caldicott Guardian; Senior Information Risk Owner; Chief People Officer; staff-side representatives |

## Revision History

| Version | Date | Author | Changes | Approved By | Approval Date |
|---------|------|--------|---------|-------------|---------------|
| 1.0 | 2026-08-19 | ArcKit AI | Initial creation from `/arckit:stakeholders` command | PENDING | PENDING |

---

## Executive Summary

### Purpose

This document identifies key stakeholders in the NHS 365 programme, their underlying drivers (motivations, concerns, pressures), how those drivers manifest into goals, and the measurable outcomes that will satisfy them. It provides traceability from individual stakeholder concerns to programme success metrics.

### Key Findings

The programme's central tension is between **pace and assurance**. A £120 million national deployment to approximately 505,000 staff, targeted at October 2026 [NB-C1], creates political and financial pressure to move quickly, while the Clinical Safety Officer, Caldicott Guardian, and Senior Information Risk Owner each hold a personal, professionally accountable veto that cannot be compressed to fit a delivery date. The second finding is that the benefit case rests on an inherited number: the pilot's 43 minutes saved per person per day [NB-C1] was measured on 30,000 self-selecting volunteers, and no local organisation should treat it as a forecast. The third is that the most dangerous failure mode is not technical but behavioural — "clinical drift" [NB-C2] and credential sharing [NB-C3] are both rational staff responses to friction, and both convert an assured deployment into an unassured one without any change to the technology.

### Critical Success Factors

- Clinical safety governance is established and staffed **before** first deployment, not in parallel with it — DCB0160 requires a named Clinical Safety Officer to reduce residual risk to as low as reasonably practicable before go-live [NB-C4]
- The intended-use boundary is defined, communicated, and monitored, so that administrative-productivity deployment does not migrate into clinical use unassessed [NB-C2]
- Benefit is measured locally against a local baseline rather than asserted from the national pilot figure
- Frontline staff experience the approved tooling as genuinely faster than the workaround, since unusable official tooling is what creates shadow use [NB-C5]
- Staff-side representatives are engaged on the workforce implications of released time before, not after, the savings narrative is published

### Stakeholder Alignment Score

**Overall Alignment**: MEDIUM

Alignment is strong on the *direction* — every stakeholder group accepts that administrative burden is unsustainable against 1.37 million full-time equivalent staff, roughly 100,020 vacancies at a 6.7% rate, and sickness absence near 5.1% [NB-C6]. Alignment is weak on *pace and evidence*. Four material conflicts (C-1 to C-4 below) remain unresolved, and two of them — the assurance gate versus the delivery deadline, and the licensing tier versus the benefit case — must be resolved by the programme board rather than absorbed at delivery level.

---

## Stakeholder Identification

### Internal Stakeholders

| Stakeholder | Role/Department | Influence | Interest | Engagement Strategy |
|-------------|----------------|-----------|----------|---------------------|
| National Programme SRO | NHS England — Senior Responsible Owner | HIGH | HIGH | Manage closely; monthly programme board, benefit reporting |
| Trust Chief Executive | Executive — organisational accountability | HIGH | MEDIUM | Keep satisfied; exception reporting, CQC-relevant risk |
| Chief Clinical Information Officer (CCIO) | Clinical informatics leadership | HIGH | HIGH | Manage closely; clinical design authority, drift monitoring |
| Chief Nursing Information Officer (CNIO) | Nursing informatics leadership | MEDIUM | HIGH | Manage closely; nursing workflow design, champion network |
| Chief Information Officer / CDIO | Technology strategy and tenancy decision | HIGH | HIGH | Manage closely; architecture board, tenancy decision owner |
| Clinical Safety Officer (DCB0160) | Clinical risk management | HIGH | HIGH | Manage closely; hazard log, go-live gate authority |
| Caldicott Guardian | Confidentiality of patient information | HIGH | MEDIUM | Keep satisfied; confidentiality sign-off, DPIA consultation |
| Senior Information Risk Owner (SIRO) | Information risk acceptance | HIGH | MEDIUM | Keep satisfied; formal risk acceptance, DPIA sign-off |
| Chief Information Security Officer / Cyber Lead | DSPT, CAF, security operations | HIGH | MEDIUM | Keep satisfied; security gates, DSPT evidence |
| Chief People Officer | Workforce, retention, wellbeing | HIGH | HIGH | Manage closely; workforce benefit case, staff-side liaison |
| Director of Finance | Licensing spend, benefit realisation | HIGH | MEDIUM | Keep satisfied; quarterly benefit review, tier decisions |
| Frontline clinicians (medical, nursing, AHP) | End users at the point of care | LOW | HIGH | Keep informed; champion network, workflow-based training |
| Administrative and operational staff | End users, largest admin-time cohort | LOW | HIGH | Keep informed; direct engagement on role impact |
| IT Service Desk / Operations | Support and incident handling | MEDIUM | HIGH | Keep informed; rollout wave planning, runbooks |
| Registration Authority Manager | Care Identity lifecycle, smartcards | MEDIUM | HIGH | Keep informed; authenticator migration planning |
| Learning & Development lead | Training, compliance, revalidation | MEDIUM | HIGH | Keep informed; microlearning design, competence measurement |
| Information Governance Manager | Day-to-day IG operations | MEDIUM | HIGH | Keep informed; DLP configuration, retention schedules |

### External Stakeholders

| Stakeholder | Organization | Relationship | Influence | Interest |
|-------------|--------------|--------------|-----------|----------|
| NHS England (national) | NHS England | Mandating authority | HIGH | HIGH |
| NHS Digital and delivery partners | NHS Digital, systems integrators | Shared tenant operator [NB-C7] | HIGH | MEDIUM |
| Care Quality Commission | CQC | Regulator — quality and safety [NB-C8] | HIGH | MEDIUM |
| Information Commissioner's Office | ICO | Regulator — data protection [NB-C8] | HIGH | LOW |
| Platform vendor | Microsoft | Supplier | MEDIUM | HIGH |
| Specialist ISVs | e.g. learning platform providers | Supplier | LOW | HIGH |
| Patients and the public | — | Beneficiary | LOW | HIGH |
| Professional bodies and trade unions | RCN, BMA, UNISON | Staff representation | MEDIUM | HIGH |
| Integrated Care System partners | ICS member organisations | Peer / interdependency | MEDIUM | MEDIUM |

### UK Government Digital Roles (GovS 005)

> The [Government Functional Standard for Digital (GovS 005)](https://www.gov.uk/government/publications/government-functional-standard-govs-005-digital) defines mandatory digital governance roles. NHS bodies are not central government departments and apply these indirectly, through NHS England and DHSC assurance rather than directly to CDDO. The mapping below records how each role is discharged in this programme.

| Role | Responsibility | Typical Power/Interest | Engagement Strategy |
|------|---------------|----------------------|---------------------|
| Senior Responsible Owner (SRO) | Accountable for digital outcomes and spend controls | HIGH / HIGH | Manage Closely — programme board, decision escalation |
| Service Owner | Owns the end-to-end service and user outcomes | HIGH / HIGH | Manage Closely — service reviews; held by CCIO/CIO jointly here |
| Product Manager | Prioritises capability against user needs and policy | MEDIUM / HIGH | Keep Informed — roadmap input, adoption backlog |
| Delivery Manager | Manages delivery cadence, risks, and dependencies | MEDIUM / HIGH | Keep Informed — wave planning, risk log |
| CDDO (Central Digital & Data Office) | Cross-government standards and spend control | HIGH / MEDIUM | Keep Satisfied — engaged via NHS England, not directly |
| CDIO (Chief Digital Information Officer) | Departmental digital strategy and technology oversight | HIGH / MEDIUM | Keep Satisfied — quarterly strategy alignment |
| DDaT Profession Lead | Digital, Data & Technology capability framework | LOW / MEDIUM | Monitor — capability assessment, recruitment |

### UK Government Security Roles (GovS 007)

> The [Government Functional Standard for Security (GovS 007)](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security) defines mandatory protective security roles. In NHS bodies the equivalent assurance is demonstrated through the Data Security and Protection Toolkit, aligned to the NCSC Cyber Assessment Framework [NB-C9].

| Role | Responsibility | Typical Power/Interest | Engagement Strategy |
|------|---------------|----------------------|---------------------|
| Senior Security Risk Owner (SSRO) | Owns protective security risk at board level | HIGH / MEDIUM | Keep Satisfied — board risk reporting |
| Departmental Security Officer (DSO) | Security coordination and policy implementation | HIGH / MEDIUM | Keep Satisfied — compliance gates, incident reporting |
| Senior Information Risk Owner (SIRO) | Owns information risk, signs off risk acceptance | HIGH / MEDIUM | Keep Satisfied — information risk decisions, DPIA sign-off |
| Cyber Security Lead | Operational cyber security, CAF and DSPT evidence | MEDIUM / HIGH | Keep Informed — security architecture review, testing |

### NHS Statutory and Clinical Roles

> These roles have no GovS equivalent and are specific to health and care. Each carries personal professional accountability, which is why none of them can be overridden by programme delivery pressure.

| Role | Statutory or Standards Basis | Power/Interest | Engagement Strategy |
|------|------------------------------|----------------|---------------------|
| Clinical Safety Officer | DCB0160 — clinical risk management [NB-C4] | HIGH / HIGH | Manage Closely — holds the go-live gate |
| Caldicott Guardian | Caldicott principles — confidentiality [NB-C10] | HIGH / MEDIUM | Keep Satisfied — confidentiality sign-off |
| Registration Authority Manager | Care Identity issuance and RBAC assignment [NB-C11] | MEDIUM / HIGH | Keep Informed — authenticator lifecycle |
| Data Protection Officer | UK GDPR Article 37 | HIGH / MEDIUM | Keep Satisfied — DPIA, lawful basis |

### Stakeholder Power-Interest Grid

```text
                          INTEREST
              Low                         High
        ┌─────────────────────┬─────────────────────┐
        │                     │                     │
        │   KEEP SATISFIED    │   MANAGE CLOSELY    │
   High │                     │                     │
        │ • ICO               │ • National SRO      │
        │ • Trust CEO         │ • CCIO              │
        │ • Caldicott Guardian│ • CIO / CDIO        │
 P      │ • SIRO / DPO        │ • Clinical Safety   │
 O      │ • CISO              │   Officer           │
 W      │ • Director of       │ • Chief People      │
 E      │   Finance           │   Officer           │
 R      │ • CQC               │ • NHS England       │
        │ • NHS Digital       │                     │
        ├─────────────────────┼─────────────────────┤
        │                     │                     │
        │      MONITOR        │    KEEP INFORMED    │
        │                     │                     │
   Low  │ • Specialist ISVs   │ • Frontline         │
        │ • Industry bodies   │   clinicians        │
        │                     │ • Admin & ops staff │
        │                     │ • IT Service Desk   │
        │                     │ • RA Manager        │
        │                     │ • L&D lead          │
        │                     │ • Patients & public │
        │                     │ • Unions / RCN, BMA │
        └─────────────────────┴─────────────────────┘
```

| Stakeholder | Power | Interest | Quadrant | Engagement Strategy |
|-------------|-------|----------|----------|---------------------|
| National Programme SRO | HIGH | HIGH | Manage Closely | Monthly programme board |
| CCIO | HIGH | HIGH | Manage Closely | Clinical design authority, fortnightly |
| CIO / CDIO | HIGH | HIGH | Manage Closely | Architecture board, fortnightly |
| Clinical Safety Officer | HIGH | HIGH | Manage Closely | Hazard log review, go-live gate |
| Chief People Officer | HIGH | HIGH | Manage Closely | Monthly workforce benefit review |
| NHS England (national) | HIGH | HIGH | Manage Closely | National reporting cadence |
| CNIO | MEDIUM | HIGH | Manage Closely | Nursing workflow design |
| Trust Chief Executive | HIGH | MEDIUM | Keep Satisfied | Board exception reporting |
| Caldicott Guardian | HIGH | MEDIUM | Keep Satisfied | Confidentiality gates |
| SIRO / DPO | HIGH | MEDIUM | Keep Satisfied | Risk acceptance, DPIA sign-off |
| CISO / Cyber Lead | HIGH | MEDIUM | Keep Satisfied | DSPT evidence checkpoints |
| Director of Finance | HIGH | MEDIUM | Keep Satisfied | Quarterly benefit review |
| CQC | HIGH | MEDIUM | Keep Satisfied | Inspection readiness evidence |
| NHS Digital / delivery partners | HIGH | MEDIUM | Keep Satisfied | Shared tenant service reviews |
| ICO | HIGH | LOW | Keep Satisfied | Breach reporting only, if required |
| Frontline clinicians | LOW | HIGH | Keep Informed | Champion network, workflow training |
| Administrative and operational staff | LOW | HIGH | Keep Informed | Role-impact briefings |
| IT Service Desk / Operations | MEDIUM | HIGH | Keep Informed | Wave planning, runbooks |
| Registration Authority Manager | MEDIUM | HIGH | Keep Informed | Authenticator migration plan |
| Learning & Development lead | MEDIUM | HIGH | Keep Informed | Microlearning design |
| Unions and professional bodies | MEDIUM | HIGH | Keep Informed | Partnership forum, quarterly |
| Patients and the public | LOW | HIGH | Keep Informed | Transparency publication |
| Specialist ISVs | LOW | HIGH | Monitor | Supplier reviews |

**Quadrant Interpretation:**

- **Manage Closely** (High Power, High Interest): Key decision-makers requiring active engagement
- **Keep Satisfied** (High Power, Low Interest): Influential stakeholders needing periodic updates
- **Keep Informed** (Low Power, High Interest): Engaged stakeholders needing regular communication
- **Monitor** (Low Power, Low Interest): Minimal engagement required

---

## Stakeholder Drivers Analysis

### SD-1: National Programme SRO — Demonstrate return on a £120 million national commitment

**Stakeholder**: NHS England Senior Responsible Owner for the national deployment

**Driver Category**: STRATEGIC

**Driver Statement**: Deliver visible, defensible benefit from a £120 million programme deploying AI assistance to approximately 505,000 staff by October 2026, and be able to evidence it when asked.

**Context & Background**: The deployment follows the largest AI trial of its kind in global healthcare, in which 30,000 participants saved an average of 43 minutes per person per day on administrative tasks [NB-C1]. That figure is now the public benchmark for the programme. A national commitment of this size attracts scrutiny from the Department, the National Audit Office, and the press; a programme that cannot evidence benefit becomes a case study in wasted public money.

**Driver Intensity**: CRITICAL

**Enablers** (What would help):

- Consistent, comparable benefit measurement across participating organisations
- Early adopter sites willing to publish honest results, including disappointing ones
- Clear separation of administrative benefit (claimable now) from clinical benefit (requires assurance)

**Blockers** (What would hinder):

- Local organisations measuring differently, or not at all, producing unaggregatable data
- A high-profile safety or confidentiality incident early in rollout
- Benefit realisation that materially undershoots the pilot figure, with no explanation prepared

**Related Stakeholders**:

- Director of Finance (SD-9) shares the benefit-evidence need but from a cost-control angle
- Clinical Safety Officer (SD-4) is the principal constraint on the pace this driver demands

---

### SD-2: Chief Clinical Information Officer — Prevent clinical drift

**Stakeholder**: CCIO, supported by CNIO

**Driver Category**: RISK

**Driver Statement**: Ensure that a tool approved for administrative productivity is not quietly used for clinical purposes it was never assessed for, and that clinicians understand where its judgement cannot be trusted.

**Context & Background**: "Clinical drift" — the gradual use of generative AI for summarising patient notes or supporting clinical discussion — introduces risks of hallucination, omission of critical details such as allergies, or incorrect synthesis of information [NB-C2]. Nationally, the tool is treated as an administrative productivity tool rather than Software as a Medical Device [NB-C12]. That classification holds only while actual use matches intended use. The CCIO carries clinical credibility with colleagues and will be the person asked, at a coroner's inquest or a serious incident review, why the boundary was not enforced.

**Driver Intensity**: CRITICAL

**Enablers** (What would help):

- Technical monitoring that detects use outside the assessed boundary rather than relying on policy
- Training that leads with failure modes, not features
- A visible, credible route for clinicians to report unreliable output without blame

**Blockers** (What would hinder):

- Marketing language that implies clinical capability
- Time pressure that makes unassessed shortcuts attractive
- Absence of any measurement of what the tool is actually being used for

**Related Stakeholders**:

- Clinical Safety Officer (SD-4) holds the formal gate; the CCIO holds the clinical relationship
- Frontline clinicians (SD-10) are the population in which drift occurs

---

### SD-3: Chief People Officer — Convert released time into retention

**Stakeholder**: Chief People Officer / Director of Workforce

**Driver Category**: OPERATIONAL

**Driver Statement**: Reduce the administrative burden that is driving burnout and attrition, and be able to show the workforce that technology investment improved their working lives.

**Context & Background**: The service faces a profound workforce crisis marked by high vacancies, slowing recruitment, and widespread burnout, employing around 1.37 million full-time equivalent staff against approximately 100,020 vacancies — a 6.7% rate. Sickness absence hovers near 5.1%, with anxiety, stress, and depression accounting for roughly 30% of absences [NB-C6]. Nearly half of general practice staff report that hardware and software are unfit for purpose, contributing to cognitive overload that undermines both wellbeing and care delivery [NB-C13]. The Chief People Officer is measured on vacancy and turnover rates that technology alone cannot move, but that poor technology demonstrably worsens.

**Driver Intensity**: HIGH

**Enablers** (What would help):

- Genuine time savings that staff themselves perceive, not only savings visible in dashboards
- Explicit organisational commitment that released time is reinvested in care and rest, not extracted as headcount
- Role-relevant training delivered inside the working day

**Blockers** (What would hinder):

- A savings narrative published before staff-side consultation, read as a redundancy signal
- Training that adds burden rather than relieving it
- Deployment to a licence tier that does not deliver the capability the benefit case assumed

**Related Stakeholders**:

- Unions and professional bodies (SD-11) will test the reinvestment commitment
- Frontline clinicians (SD-10) and administrative staff (SD-12) are the affected population

---

### SD-4: Clinical Safety Officer — Discharge a personal DCB0160 accountability

**Stakeholder**: Clinical Safety Officer

**Driver Category**: COMPLIANCE

**Driver Statement**: Satisfy the DCB0160 obligation to identify hazards, assess severity and likelihood, and reduce residual clinical risk to a level that is as low as reasonably practicable before systems go live — and be personally able to defend that judgement.

**Context & Background**: Regulatory obligations include the Data Security and Protection Toolkit, the Secure Email Standard, and clinical risk management standards DCB0129 and DCB0160; the latter requires appointment of a Clinical Safety Officer who performs exactly this function before go-live [NB-C4]. This is a named individual with professional registration at stake. Unlike most programme roles, the accountability does not dissolve when the programme closes.

**Driver Intensity**: CRITICAL

**Enablers** (What would help):

- Early involvement, while design is still changeable
- A clear intended-use statement to assess against
- Adequate time and analyst support to build the hazard log properly

**Blockers** (What would hinder):

- Being engaged after design freeze, when the only options are approve or delay
- Pressure to sign off against a deadline rather than against evidence
- Ambiguity over whether a given deployment is in clinical scope

**Related Stakeholders**:

- National Programme SRO (SD-1) exerts the pace pressure this driver resists
- CCIO (SD-2) shares the clinical risk concern from a behavioural angle

---

### SD-5: Caldicott Guardian — Protect confidentiality without obstructing care

**Stakeholder**: Caldicott Guardian

**Driver Category**: COMPLIANCE

**Driver Statement**: Ensure every use of patient identifiable information is justified, minimal, and lawful — while honouring the equal duty to share information for direct care.

**Context & Background**: All solutions must meet rigorous NHS standards including the Data Security and Protection Toolkit and Caldicott principles [NB-C10]. Collaboration platforms make sharing frictionless, which is their value and their risk: preventive controls that block inappropriate sharing of patient identifiers in collaborative channels are more reliable than policy alone [NB-C10]. The Caldicott Guardian is frequently cast as an obstacle, and is motivated to avoid that reputation while still discharging the duty.

**Driver Intensity**: HIGH

**Enablers** (What would help):

- Technical controls that make the wrong action difficult rather than merely forbidden
- Data flow mapping produced before, not after, configuration decisions
- Evidence that controls have not obstructed legitimate direct-care sharing

**Blockers** (What would hinder):

- Default platform configuration adopted without review
- Being consulted only at the point of sign-off
- Controls so restrictive that clinicians route around them

**Related Stakeholders**:

- SIRO and DPO (SD-6) require the same evidence pack
- Information Governance Manager operationalises these decisions daily

---

### SD-6: Senior Information Risk Owner — Accept risk on the record, with evidence

**Stakeholder**: SIRO, supported by the Data Protection Officer

**Driver Category**: RISK

**Driver Statement**: Formally accept residual information risk in a way that is defensible to the board, the ICO, and any subsequent investigation.

**Context & Background**: The SIRO's signature converts a technical position into a personal, board-level accountability. Compliance is demonstrated primarily through the DSPT, aligned with the NCSC Cyber Assessment Framework [NB-C9]. Where data remains within the organisation's own tenant, governance is simplified and UK data residency requirements are supported [NB-C14] — a materially easier risk position to accept than one involving external processing.

**Driver Intensity**: HIGH

**Enablers** (What would help):

- Completed DPIA with a clear residual risk statement
- Explicit articulation of which controls are inherited from the managed environment and which are locally owned
- Documented data residency and sub-processor position

**Blockers** (What would hinder):

- Being asked to accept risk that has not been quantified
- Supplier changes to hosting or sub-processors discovered after sign-off
- Unclear controller/processor boundaries between the organisation and national services

**Related Stakeholders**:

- CISO (SD-7) supplies much of the technical evidence
- Caldicott Guardian (SD-5) covers the confidentiality dimension of the same decision

---

### SD-7: CISO / Cyber Security Lead — Maintain DSPT assurance under rapid change

**Stakeholder**: Chief Information Security Officer / Cyber Security Lead

**Driver Category**: COMPLIANCE

**Driver Statement**: Maintain demonstrable security assurance while the estate changes faster than the assurance cycle, and avoid becoming the department that missed the next systemic exposure.

**Context & Background**: The sector carries the memory of the 2017 WannaCry attack, which disrupted services at 81 of 236 trusts, largely because outdated systems remained in use after a previous national enterprise agreement had expired [NB-C15]. Compliance is demonstrated primarily through the DSPT, aligned with the NCSC Cyber Assessment Framework [NB-C9]. Rapid AI-driven change creates new surface faster than assurance processes were designed to absorb.

**Driver Intensity**: HIGH

**Enablers** (What would help):

- Security and retention configuration held as code, so deviation is visible in review rather than in audit
- Clear inheritance model for baseline controls in a centrally managed environment
- Automated evidence collection for DSPT assertions

**Blockers** (What would hinder):

- Shadow AI adopted outside any assurance process [NB-C16]
- Local administrator flexibility used to disable controls without review
- Assurance treated as a one-off gate rather than a continuous position

**Related Stakeholders**:

- SIRO (SD-6) consumes this evidence to accept risk
- Frontline staff (SD-10) create shadow use when approved tooling frustrates them

---

### SD-8: CIO / CDIO — Choose the right tenancy model and own the consequence

**Stakeholder**: Chief Information Officer / Chief Digital Information Officer

**Driver Category**: STRATEGIC

**Driver Statement**: Select between a centrally managed shared environment and an independently managed one, balancing operational simplicity against the flexibility that local clinical integration demands — and be able to justify the choice later.

**Context & Background**: Organisations must weigh the operational simplicity and strong baseline security of the Shared Tenant against the flexibility — and greater responsibility — of a Sovereign Tenant. Critical decision factors include cyber maturity, the need for specialised integrations, the presence of legacy clinical systems that require hybrid identity, and the capacity to manage clinical safety governance for AI and automation [NB-C17]. The shared model is managed centrally by NHS Digital with delivery partners, giving economies of scale, consistent data loss prevention, and national security baselines [NB-C7]. The decision is expensive to reverse.

**Driver Intensity**: HIGH

**Enablers** (What would help):

- Honest self-assessment of local cyber maturity and clinical safety governance capacity
- Full inventory of legacy clinical systems requiring hybrid identity
- Willingness to accept central constraint where local differentiation adds no clinical value

**Blockers** (What would hinder):

- Sovereignty chosen for autonomy's sake without the capability to discharge the responsibility
- Shared tenancy chosen for cost without checking that clinical integrations are feasible within central constraints
- The decision made implicitly, by default, rather than explicitly and recorded

**Related Stakeholders**:

- CISO (SD-7) inherits a materially different control set depending on the choice
- Clinical Safety Officer (SD-4) gains or loses local governance capacity

---

### SD-9: Director of Finance — Make the licensing tier defensible

**Stakeholder**: Director of Finance

**Driver Category**: FINANCIAL

**Driver Statement**: Control recurring licence cost while ensuring the tier purchased is actually capable of delivering the benefit the business case assumed.

**Context & Background**: The NHS uses a tiered licensing model. The Standard Service targets frontline clinical staff with web-based applications, a 4 GB mailbox, and limited storage; the Enhanced Service, built on a restricted Frontline Worker licence, serves managers and heavier administrative users with larger mailboxes and stronger security and compliance tools [NB-C18]. Recurring per-user cost at national scale is the dominant financial variable, and the cheapest tier that satisfies a procurement scorecard may not be the tier that produces the time savings the benefit case rests on.

**Driver Intensity**: HIGH

**Enablers** (What would help):

- Benefit measured per licence tier, not averaged across the estate
- Clear mapping of role to tier based on observed work patterns
- Ability to move users between tiers as evidence accumulates

**Blockers** (What would hinder):

- Benefit claimed in aggregate, hiding tier-level underperformance
- Tier assignment driven by budget rather than by role need
- Sunk-cost commitment to a multi-year tier mix before evidence exists

**Related Stakeholders**:

- National Programme SRO (SD-1) needs the benefit case to hold
- Frontline clinicians (SD-10) experience the capability limits of the cheaper tier

---

### SD-10: Frontline clinicians — Get time back without inheriting new risk

**Stakeholder**: Doctors, nurses, allied health professionals

**Driver Category**: PERSONAL

**Driver Statement**: Spend less time on documentation and administration and more on patients — without being made accountable for output they cannot verify, or monitored in ways that feel punitive.

**Context & Background**: This group experiences the administrative burden directly and stands to gain most from its reduction. They are also the group most exposed if generated content is wrong: an omitted allergy is their professional problem, not the vendor's [NB-C2]. Clinical staff rarely have time for full-day classroom sessions, which is why microlearning in focused units typically under 15 minutes fits better into their schedules [NB-C19]. Where official systems frustrate them, staff adopt unofficial tools [NB-C16] — a rational response, not a discipline problem.

**Driver Intensity**: HIGH

**Enablers** (What would help):

- Tooling that is demonstrably faster than the current workaround
- Frictionless authentication on shared clinical workstations
- Explicit assurance that usage telemetry serves safety, not performance management
- Training built around real workflows rather than product features [NB-C20]

**Blockers** (What would hinder):

- Authentication friction on shared devices
- Output that is confidently wrong, encountered early in adoption
- Any suggestion that time saved converts to increased caseload

**Related Stakeholders**:

- CCIO (SD-2) advocates for this group's safety interest
- Chief People Officer (SD-3) depends on this group perceiving genuine benefit

---

### SD-11: Unions and professional bodies — Protect staff from the second-order effects

**Stakeholder**: RCN, BMA, UNISON and equivalent staff-side representatives

**Driver Category**: RISK

**Driver Statement**: Ensure that productivity gains are not converted into establishment cuts, that AI-derived telemetry is not used in performance management, and that professional judgement is not eroded by automation.

**Context & Background**: A programme whose headline benefit is "43 minutes per person per day" [NB-C1] is, from a staff-side perspective, a programme that has quantified a case for reducing establishment. Equity risk is also a recognised pitfall of this kind of transformation [NB-C21]. Staff-side bodies are typically supportive of tools that reduce burden and hostile to the surveillance capability those tools create as a by-product.

**Driver Intensity**: MEDIUM

**Enablers** (What would help):

- Written agreement on the permitted uses of usage telemetry, made before deployment
- Board-level commitment on reinvestment of released time
- Representation on the programme board rather than consultation after decisions

**Blockers** (What would hinder):

- Savings published as a financial efficiency before workforce discussion
- Individual-level usage data accessible to line managers
- Deskilling concerns dismissed rather than addressed

**Related Stakeholders**:

- Chief People Officer (SD-3) is the primary counterpart
- Frontline clinicians (SD-10) and administrative staff (SD-12) are represented

---

### SD-12: Administrative and operational staff — Benefit most, fear most

**Stakeholder**: Administrative, clerical, and operational support staff

**Driver Category**: PERSONAL

**Driver Statement**: Reduce repetitive workload and be recognised for higher-value work, without the automation of routine tasks being read as the automation of the role.

**Context & Background**: This group performs the largest share of the administrative tasks the programme targets, so it stands to see the largest measured time saving — and is therefore the group most reasonably anxious about what that measurement implies. Their concern is not technological but existential, and it will not be addressed by feature training.

**Driver Intensity**: MEDIUM

**Enablers** (What would help):

- Explicit redeployment and reskilling pathway defined before rollout
- Involvement in designing which tasks are automated
- Recognition of the higher-value work that replaces automated tasks

**Blockers** (What would hinder):

- Silence on job security while savings are publicised
- Automation designed for them rather than with them

**Related Stakeholders**:

- Unions (SD-11) represent this concern formally
- Chief People Officer (SD-3) owns the redeployment commitment

---

### SD-13: Registration Authority Manager — End credential sharing

**Stakeholder**: Registration Authority Manager

**Driver Category**: OPERATIONAL

**Driver Statement**: Maintain attributable access to clinical systems, and remove the credential-sharing behaviour that makes attribution unreliable.

**Context & Background**: Access is managed locally by Registration Authorities, which issue Care Identities, assign role-based access control positions, and control authenticators [NB-C11]. A persistent human risk is smartcard sharing, which undermines non-repudiation and patient safety investigations; the mitigation is expanding frictionless options such as biometrics and high-assurance passkeys [NB-C3]. Registration Authorities carry the operational load of every authenticator change, so a migration that is good for security may be a significant workload for this team.

**Driver Intensity**: HIGH

**Enablers** (What would help):

- Expanded self-service, including remote identity proofing and self-service unlock [NB-C22]
- Frictionless authenticators that remove the incentive to share
- Realistic resourcing for the migration period

**Blockers** (What would hinder):

- Authenticator migration scheduled without additional RA capacity
- Shared clinical workstations where re-authentication remains slow
- Sharing treated as a disciplinary matter rather than a design failure

**Related Stakeholders**:

- CISO (SD-7) and SIRO (SD-6) depend on attribution for investigation
- Frontline clinicians (SD-10) are the population whose behaviour must change

---

### SD-14: Learning & Development lead — Prove competence, not completion

**Stakeholder**: Learning & Development / Education lead

**Driver Category**: OPERATIONAL

**Driver Statement**: Deliver training that changes practice and supports revalidation, rather than training that generates completion statistics.

**Context & Background**: Clinical staff rarely have time for full-day classroom sessions; microlearning in units typically under 15 minutes fits better into busy schedules, and content can be prioritised by whether it is fatal if unknown, fundamental to daily practice, frequently used, fixed by policy, or useful for team cohesion [NB-C19]. Training must focus on practical workflows rather than hardware specifications, and clinical champions among physicians and nurses should lead pilots and advocate for the tools [NB-C20].

**Driver Intensity**: MEDIUM

**Enablers** (What would help):

- Learning delivered inside the tools staff already use, without separate logins
- Auto-assignment by role or specialty
- Measurement of applied competence rather than module completion

**Blockers** (What would hinder):

- Training treated as a compliance tick-box
- Content built around product features rather than clinical workflows
- No protected time to complete it

**Related Stakeholders**:

- CCIO (SD-2) depends on training to communicate failure modes
- Frontline clinicians (SD-10) are the audience

---

### SD-15: Regulators (CQC and ICO) — Verifiable compliance, not assertion

**Stakeholder**: Care Quality Commission; Information Commissioner's Office

**Driver Category**: COMPLIANCE

**Driver Statement**: Confirm that services meet quality, safety, and data protection standards through evidence that can be inspected, and that failures are reported promptly.

**Context & Background**: Best practice must meet the rigorous standards expected by the Care Quality Commission, NHS England, and the Information Commissioner's Office [NB-C8]. Neither regulator has day-to-day interest in the programme, but both have decisive influence when something goes wrong. Their driver is satisfied by evidence produced as a by-product of good operation, not by evidence assembled in response to an inspection.

**Driver Intensity**: MEDIUM

**Enablers** (What would help):

- Continuous evidence capture rather than pre-inspection assembly
- Clear audit trail of who accessed what, and what generated content a human accepted
- Transparent publication of how automated tools are used

**Blockers** (What would hinder):

- Evidence held only in individuals' knowledge
- Retention configured to product defaults rather than clinical schedules [NB-C23]
- Inability to reconstruct an incident from available logs

**Related Stakeholders**:

- Trust Chief Executive (SD-16) carries the consequence of an adverse finding
- SIRO, DPO, and Caldicott Guardian produce the evidence

---

### SD-16: Trust Chief Executive — Avoid becoming the cautionary example

**Stakeholder**: Trust Chief Executive

**Driver Category**: RISK

**Driver Statement**: Capture the workforce and productivity benefit without the organisation becoming the first named example of an NHS AI failure.

**Context & Background**: A chief executive's exposure here is asymmetric. Successful adoption is a modest, shared, national story; a confidentiality breach or an AI-attributable patient harm is a specific, local, personally attributable one, with CQC and press consequences. This drives a preference for being an early follower rather than a first mover, which is in tension with national pace expectations.

**Driver Intensity**: HIGH

**Enablers** (What would help):

- Evidence from comparable organisations that have deployed safely
- Clear internal accountability so that assurance is visibly discharged
- Realistic, locally owned benefit claims that will not later be contradicted

**Blockers** (What would hinder):

- Pressure to be an early adopter without additional assurance support
- Benefit claims made nationally on the organisation's behalf
- Ambiguity about who holds the go-live decision

**Related Stakeholders**:

- National Programme SRO (SD-1) applies the pace pressure
- Clinical Safety Officer (SD-4) provides the assurance that makes acceptance possible

---

## Driver-to-Goal Mapping

### Goal G-1: Establish clinical safety governance before first deployment

**Derived From Drivers**: SD-2, SD-4, SD-16

**Goal Owner**: Clinical Safety Officer

**Goal Statement**: Appoint a Clinical Safety Officer, publish a clinical risk management plan and hazard log, and record an approved intended-use statement for every deployment wave, with all of this complete before the first user in that wave is enabled.

**Why This Matters**: DCB0160 requires the CSO to reduce residual clinical risk to as low as reasonably practicable before go-live [NB-C4]. Doing this after deployment is not a delayed control; it is a failed one. It also gives the CCIO the boundary against which drift can be detected (SD-2) and gives the Chief Executive the visible discharge of accountability they need (SD-16).

**Success Metrics**:

- **Primary Metric**: Percentage of deployment waves with CSO-approved safety case before first enablement — target 100%
- **Secondary Metrics**:
  - Median lead time between CSO engagement and go-live (target: 8 weeks or more)
  - Number of hazards identified per wave, and proportion with controls verified

**Baseline**: No CSO appointed to this programme; no hazard log exists

**Target**: 100% of waves gated, sustained across the rollout

**Measurement Method**: Programme assurance register, cross-checked against the deployment tooling's enablement log

**Dependencies**:

- CSO appointed with sufficient allocated time, not as an unfunded addition to a clinical role
- Intended-use statement agreed by CCIO and programme board

**Risks to Achievement**:

- CSO capacity becomes the rate limiter on national pace, creating pressure to weaken the gate
- Ambiguity over which deployments are in clinical scope leads to inconsistent gating

---

### Goal G-2: Define, communicate, and monitor the intended-use boundary

**Derived From Drivers**: SD-2, SD-4, SD-10, SD-15

**Goal Owner**: Chief Clinical Information Officer

**Goal Statement**: Publish an intended-use statement distinguishing approved administrative use from prohibited clinical use, communicate it to 100% of enabled users at enablement, and implement monitoring that detects out-of-boundary use within one month of occurrence.

**Why This Matters**: The national position treats the tool as an administrative productivity tool rather than Software as a Medical Device [NB-C12]. That classification is a statement about intended use, and it stops being true the moment actual use diverges. Clinical drift is gradual and invisible without deliberate measurement [NB-C2].

**Success Metrics**:

- **Primary Metric**: Detected out-of-boundary use incidents per 1,000 active users per month — target: detected and remediated, not zero-reported
- **Secondary Metrics**:
  - Percentage of users who can correctly state the boundary when surveyed (target: 80% or more)
  - Median time from detection to remediation (target: 30 days or fewer)

**Baseline**: No boundary defined; no monitoring capability

**Target**: Boundary published, monitoring live before wave 2

**Measurement Method**: Usage telemetry reviewed against the intended-use statement; quarterly user survey

**Dependencies**:

- Telemetry available at sufficient granularity, with staff-side agreement on its permitted use (SD-11)
- Non-punitive reporting route established

**Risks to Achievement**:

- Monitoring perceived as surveillance, triggering staff-side objection (see C-3)
- Detection capability insufficient to distinguish administrative from clinical use in practice

---

### Goal G-3: Measure benefit locally against a local baseline

**Derived From Drivers**: SD-1, SD-3, SD-9

**Goal Owner**: National Programme SRO, delegated to local programme leads

**Goal Statement**: Establish a pre-deployment administrative time baseline for each role cohort, and report measured time change per cohort and per licence tier quarterly, using a method consistent enough to aggregate nationally.

**Why This Matters**: The 43 minutes per person per day figure came from 30,000 pilot participants [NB-C1] who volunteered for an AI trial — a population that cannot be assumed representative of 505,000 mandated users. The SRO needs defensible numbers (SD-1); Finance needs them broken down by tier to know whether the cheaper tier delivers (SD-9); the Chief People Officer needs them credible to staff (SD-3). One measurement approach serves all three.

**Success Metrics**:

- **Primary Metric**: Measured administrative minutes saved per user per day, by role cohort and licence tier
- **Secondary Metrics**:
  - Percentage of cohorts with a valid pre-deployment baseline (target: 90% or more)
  - Variance between local measured saving and the national pilot figure, with explanation

**Baseline**: No local baseline captured; national pilot figure of 43 minutes per person per day is the only reference

**Target**: Baselines captured for 90% of cohorts before enablement; quarterly reporting from wave 1

**Measurement Method**: Time-and-motion sampling plus self-reported diary study at baseline and at 3, 6, and 12 months; platform telemetry as a corroborating signal only

**Dependencies**:

- Baseline capture completed before enablement — irrecoverable if missed
- Agreement with staff-side on measurement method (SD-11)

**Risks to Achievement**:

- Baseline capture skipped under rollout pressure, making benefit unprovable
- Measured saving materially below the pilot figure, with no prepared narrative

---

### Goal G-4: Record an evidenced tenancy decision

**Derived From Drivers**: SD-8, SD-7, SD-4

**Goal Owner**: Chief Information Officer / CDIO

**Goal Statement**: Assess and record all four tenancy decision factors — cyber maturity, specialised integration need, legacy clinical systems requiring hybrid identity, and capacity to manage clinical safety governance for AI and automation — and obtain board approval of the tenancy model before any architecture work depends on it.

**Why This Matters**: The choice balances centralised resilience against local innovation, and the four factors above are the stated critical inputs [NB-C17]. The decision determines which controls are inherited and which are locally owned, so the CISO's control set (SD-7) and the CSO's local governance capacity (SD-4) both follow from it. It is expensive to reverse.

**Success Metrics**:

- **Primary Metric**: Board-approved tenancy decision record, with all four factors assessed and evidenced — binary
- **Secondary Metrics**:
  - Inventory completeness for legacy clinical systems requiring hybrid identity (target: 100%)
  - Documented split of inherited versus locally owned controls

**Baseline**: No formal decision record; model currently applied by default

**Target**: Decision recorded and approved within 8 weeks

**Measurement Method**: Board minute and decision record, reviewed against the four factors

**Dependencies**:

- Honest cyber maturity self-assessment
- Complete legacy clinical system inventory

**Risks to Achievement**:

- Sovereignty selected for autonomy without capacity to discharge the added responsibility
- Decision deferred until architecture has already assumed one model

---

### Goal G-5: Achieve DSPT assurance with AI and collaboration controls in scope

**Derived From Drivers**: SD-6, SD-7, SD-15

**Goal Owner**: Chief Information Security Officer

**Goal Statement**: Achieve and evidence DSPT "Standards Met" with the collaboration and AI capability explicitly in scope, with DPIA completed and SIRO risk acceptance recorded before each wave.

**Why This Matters**: Compliance is demonstrated primarily through the DSPT, aligned with the NCSC Cyber Assessment Framework [NB-C9]. The SIRO cannot accept risk that has not been evidenced (SD-6), and regulators expect evidence produced continuously rather than assembled at inspection (SD-15).

**Success Metrics**:

- **Primary Metric**: DSPT status "Standards Met" with AI and collaboration capability in scope
- **Secondary Metrics**:
  - Percentage of DSPT assertions with automated evidence capture (target: 60% or more)
  - DPIA and SIRO acceptance complete before wave enablement (target: 100%)

**Baseline**: DSPT status maintained, but AI capability not yet in assessed scope

**Target**: In-scope assurance achieved before wave 2

**Measurement Method**: DSPT submission record; programme assurance register

**Dependencies**:

- Tenancy decision (G-4) determines the inherited control baseline
- Retention and DLP configuration (G-6) forms part of the evidence

**Risks to Achievement**:

- Rate of change outpaces the assurance cycle
- Shadow AI adoption outside the assessed boundary [NB-C16]

---

### Goal G-6: Configure retention and data loss prevention to clinical schedules

**Derived From Drivers**: SD-5, SD-6, SD-15

**Goal Owner**: Information Governance Manager

**Goal Statement**: Replace default platform retention with configuration matching the applicable clinical and corporate retention schedules — including six years for clinical consultations — and enable controls that block inappropriate sharing of patient identifiers, before clinical use of any collaboration workspace.

**Why This Matters**: Default collaboration retention settings may conflict with clinical record-keeping requirements; retention must be enforced deliberately, often six years for clinical consultations, with shorter periods for administrative content [NB-C23]. Preventive sharing controls are more reliable than policy alone [NB-C10]. This is the single most common configuration gap between a working platform and a compliant one.

**Success Metrics**:

- **Primary Metric**: Percentage of workspaces with retention explicitly configured against a named schedule — target 100%
- **Secondary Metrics**:
  - Identifier-sharing policy violations detected and blocked per month (expected to fall after training)
  - Zero workspaces remaining on product default retention

**Baseline**: Platform defaults in force; no reconciliation to clinical schedules performed

**Target**: 100% explicit configuration before clinical use

**Measurement Method**: Configuration audit against the retention schedule register, held as code and reviewed

**Dependencies**:

- Retention schedule register agreed with the Caldicott Guardian and records management
- Configuration expressed as code so deviation is visible in review

**Risks to Achievement**:

- Controls tuned so tightly that clinicians route around them, defeating the purpose
- Retention decisions made per-workspace by local administrators without governance

---

### Goal G-7: Eliminate credential sharing through frictionless strong authentication

**Derived From Drivers**: SD-13, SD-7, SD-10

**Goal Owner**: Registration Authority Manager

**Goal Statement**: Migrate shared clinical workstations to frictionless high-assurance authentication — biometrics and high-assurance passkeys — and reduce measured credential-sharing indicators by 80% within 12 months of migration in each area.

**Why This Matters**: Credential sharing undermines non-repudiation and patient safety investigations, and the stated mitigation is expanding frictionless options rather than tightening policy [NB-C3]. This goal serves the RA Manager's attribution need (SD-13), the CISO's investigative capability (SD-7), and — crucially — the clinicians' own desire for less friction (SD-10). It is the clearest win-win in the programme.

**Success Metrics**:

- **Primary Metric**: Reduction in credential-sharing indicators (concurrent-session anomalies, sign-in pattern outliers) — target 80% reduction
- **Secondary Metrics**:
  - Median authentication time on shared clinical workstations (target: materially below current)
  - Percentage of users enrolled on a frictionless high-assurance authenticator
  - Self-service adoption rate, reducing RA workload [NB-C22]

**Baseline**: Sharing prevalence unmeasured; authentication friction on shared devices unquantified

**Target**: Baseline established within 8 weeks; 80% reduction within 12 months per area

**Measurement Method**: Authentication telemetry analysis; RA workload reporting; timed observation on representative shared workstations

**Dependencies**:

- RA team capacity funded for the migration period
- Devices capable of supporting the chosen authenticators

**Risks to Achievement**:

- RA capacity insufficient, making migration the bottleneck
- Sharing addressed as a disciplinary matter, driving it underground rather than eliminating it

---

### Goal G-8: Deliver role-based microlearning that demonstrates competence

**Derived From Drivers**: SD-14, SD-10, SD-2

**Goal Owner**: Learning & Development lead

**Goal Statement**: Deliver role-assigned microlearning in units of 15 minutes or fewer, inside the tools staff already use, covering approved use and failure modes, with 85% of enabled users demonstrating competence — not merely completion — within 60 days of enablement.

**Why This Matters**: Clinical staff rarely have time for full-day sessions; microlearning fits busy schedules, and content should be prioritised by whether it is fatal if unknown, fundamental to daily practice, frequently used, fixed by policy, or useful for team cohesion [NB-C19]. Training must focus on practical workflows rather than specifications, with clinical champions leading pilots [NB-C20]. This is also the CCIO's principal channel for communicating failure modes (SD-2).

**Success Metrics**:

- **Primary Metric**: Percentage of enabled users demonstrating competence within 60 days — target 85%
- **Secondary Metrics**:
  - Percentage of modules 15 minutes or shorter (target: 90% or more)
  - Clinical champions recruited per 500 users (target: at least 2)
  - Percentage able to state the intended-use boundary correctly (shared with G-2)

**Baseline**: No AI-specific training exists; general platform training is feature-led

**Target**: 85% competence within 60 days of enablement, from wave 1

**Measurement Method**: In-tool assessment and applied-task observation, not module completion records

**Dependencies**:

- Protected time for completion agreed with operational managers
- Clinical champion network established (SD-10)

**Risks to Achievement**:

- Competence measurement diluted to completion measurement under time pressure
- No protected time, making training an added burden and reinforcing resistance (SD-3)

---

## Goal-to-Outcome Mapping

### Outcome O-1: Clinical and administrative time released and visibly reinvested

**Supported Goals**: G-3, G-8, G-7

**Outcome Statement**: Measured administrative time per user per day falls against a local baseline, and the released capacity is demonstrably reinvested in direct care or staff rest rather than absorbed as increased caseload.

**Measurement Details**:

- **KPI**: Administrative minutes per user per day, by role cohort and licence tier
- **Current Value**: Unmeasured locally; national pilot reference is 43 minutes saved per person per day [NB-C1]
- **Target Value**: Locally evidenced saving, reported honestly against baseline, with reinvestment tracked
- **Measurement Frequency**: Quarterly
- **Data Source**: Time-and-motion sampling and diary study; platform telemetry as corroboration only
- **Report Owner**: Local programme lead, aggregated by National Programme SRO

**Business Value**:

- **Financial Impact**: Capacity released rather than cash released — the value is care delivered, and should not be booked as a cash saving without an explicit establishment decision
- **Strategic Impact**: Evidence base for continued national investment
- **Operational Impact**: Reduced documentation burden and cognitive overload [NB-C13]
- **Customer Impact**: More clinician time available for direct patient contact

**Timeline**:

- **Phase 1 (Months 1-3)**: Baselines captured; no benefit claimed
- **Phase 2 (Months 4-6)**: First measured cohort results; variance from pilot figure explained
- **Phase 3 (Months 7-12)**: Benefit sustained across cohorts; tier-level differences understood
- **Sustainment (Year 2+)**: Measurement folded into routine workforce reporting

**Stakeholder Benefits**:

- **National Programme SRO**: Defensible national benefit evidence (SD-1)
- **Chief People Officer**: Credible workforce narrative (SD-3)
- **Frontline clinicians**: Experienced, not merely reported, relief (SD-10)
- **Director of Finance**: Tier-level value for money (SD-9)

**Leading Indicators** (early signals of success):

- Baseline capture completion rate above 90%
- Self-reported task friction falling in pulse surveys
- Voluntary adoption rate exceeding mandated enablement

**Lagging Indicators** (final proof of success):

- Sustained reduction in measured administrative minutes at 12 months
- Reinvestment evidenced in job-plan or rota data

---

### Outcome O-2: No AI-attributable clinical harm, with hazards demonstrably controlled

**Supported Goals**: G-1, G-2, G-8

**Outcome Statement**: Zero patient safety incidents attributable to generated content, with every identified hazard carrying a verified control and every deployment wave gated by an approved safety case.

**Measurement Details**:

- **KPI**: AI-attributable patient safety incidents; percentage of hazards with verified controls
- **Current Value**: Not applicable — no deployment yet; no hazard log exists
- **Target Value**: Zero AI-attributable harm; 100% of hazards with verified controls
- **Measurement Frequency**: Monthly hazard review; incident reporting continuous
- **Data Source**: Hazard log; local incident reporting system
- **Report Owner**: Clinical Safety Officer

**Business Value**:

- **Financial Impact**: Avoided litigation, remediation, and regulatory cost
- **Strategic Impact**: Preserves organisational and national licence to continue
- **Operational Impact**: Clinician trust, without which adoption stalls
- **Customer Impact**: Patient safety maintained through the change

**Timeline**:

- **Phase 1 (Months 1-3)**: Hazard log established; wave 1 safety case approved
- **Phase 2 (Months 4-6)**: Drift monitoring operational; first quarterly hazard review
- **Phase 3 (Months 7-12)**: Controls verified in live operation; safety case updated on change
- **Sustainment (Year 2+)**: Hazard log maintained as a living artefact

**Stakeholder Benefits**:

- **Clinical Safety Officer**: Accountability discharged with evidence (SD-4)
- **CCIO**: Drift detected rather than discovered (SD-2)
- **Trust Chief Executive**: Assurance visibly discharged (SD-16)
- **CQC**: Inspectable evidence (SD-15)

**Leading Indicators** (early signals of success):

- Hazards identified per wave (a rising count early is healthy, not alarming)
- Out-of-boundary use detected and remediated
- Clinician-reported unreliable-output volume — under-reporting is the risk signal

**Lagging Indicators** (final proof of success):

- Zero AI-attributable harm sustained across 12 months
- Independent review confirms residual risk is as low as reasonably practicable

---

### Outcome O-3: Information governance assurance maintained through rapid change

**Supported Goals**: G-5, G-6, G-4

**Outcome Statement**: DSPT "Standards Met" maintained with AI and collaboration capability in scope, with no ICO-reportable breach originating from the collaboration platform and retention configured to clinical schedules throughout.

**Measurement Details**:

- **KPI**: DSPT status; ICO-reportable breaches from the platform; percentage of workspaces on explicit retention
- **Current Value**: DSPT maintained but AI capability out of scope; retention on defaults
- **Target Value**: In-scope "Standards Met"; zero reportable breaches; 100% explicit retention
- **Measurement Frequency**: Monthly configuration audit; annual DSPT submission
- **Data Source**: DSPT submission; configuration audit; IG incident log
- **Report Owner**: SIRO, supported by the Information Governance Manager

**Business Value**:

- **Financial Impact**: Avoided regulatory penalty and remediation cost
- **Strategic Impact**: Continued eligibility to operate national integrations
- **Operational Impact**: Confidentiality controls that do not obstruct direct care
- **Customer Impact**: Patient confidentiality preserved

**Timeline**:

- **Phase 1 (Months 1-3)**: DPIA complete; retention register agreed
- **Phase 2 (Months 4-6)**: Retention and DLP configured; SIRO acceptance recorded
- **Phase 3 (Months 7-12)**: In-scope DSPT achieved; automated evidence capture established
- **Sustainment (Year 2+)**: Continuous evidence, no pre-inspection assembly

**Stakeholder Benefits**:

- **SIRO and DPO**: Risk accepted on evidence (SD-6)
- **Caldicott Guardian**: Confidentiality protected without obstruction (SD-5)
- **CISO**: Assurance keeps pace with change (SD-7)
- **ICO and CQC**: Inspectable, continuous evidence (SD-15)

**Leading Indicators** (early signals of success):

- Percentage of assertions with automated evidence capture
- Identifier-sharing violations blocked before disclosure
- Shadow AI detections falling as approved tooling improves

**Lagging Indicators** (final proof of success):

- In-scope DSPT "Standards Met" achieved
- Zero ICO-reportable breaches from the platform over 12 months

---

### Outcome O-4: Attributable access to clinical systems

**Supported Goals**: G-7

**Outcome Statement**: Every clinically significant action is attributable to a named individual, with credential sharing reduced by 80% and authentication friction on shared clinical workstations materially lower than baseline.

**Measurement Details**:

- **KPI**: Credential-sharing indicators; median authentication time on shared workstations
- **Current Value**: Sharing prevalence unmeasured; friction unquantified
- **Target Value**: 80% reduction in sharing indicators; measurable friction reduction
- **Measurement Frequency**: Monthly
- **Data Source**: Authentication telemetry; timed observation; RA workload reporting
- **Report Owner**: Registration Authority Manager

**Business Value**:

- **Financial Impact**: Reduced investigation cost; avoided regulatory exposure
- **Strategic Impact**: Foundation for wider digital identity modernisation
- **Operational Impact**: Faster access at the point of care, and reliable audit
- **Customer Impact**: Patient safety investigations can establish who did what

**Timeline**:

- **Phase 1 (Months 1-3)**: Sharing and friction baselines established
- **Phase 2 (Months 4-6)**: Frictionless authenticators deployed in pilot areas
- **Phase 3 (Months 7-12)**: Rollout to remaining shared workstations
- **Sustainment (Year 2+)**: 80% reduction sustained; self-service adoption maintained

**Stakeholder Benefits**:

- **RA Manager**: Attribution restored, workload reduced through self-service (SD-13)
- **CISO and SIRO**: Reliable investigative capability (SD-7, SD-6)
- **Frontline clinicians**: Less friction, which is why this one succeeds (SD-10)

**Leading Indicators** (early signals of success):

- Authenticator enrolment rate
- Falling median authentication time in pilot areas
- Rising self-service transaction share

**Lagging Indicators** (final proof of success):

- 80% reduction in sharing indicators sustained
- Every sampled clinically significant action attributable to an individual

---

### Outcome O-5: Workforce confidence in the change

**Supported Goals**: G-3, G-8, G-2

**Outcome Statement**: Staff report that the technology reduced their burden, trust that usage telemetry is not used punitively, and see no unmanaged threat to their role — evidenced by survey and by the absence of formal staff-side dispute.

**Measurement Details**:

- **KPI**: Staff survey score on burden reduction and telemetry trust; formal disputes raised
- **Current Value**: Nearly half of general practice staff report hardware and software unfit for purpose [NB-C13]
- **Target Value**: Majority positive on burden reduction; zero unresolved formal disputes
- **Measurement Frequency**: Quarterly pulse survey; continuous dispute tracking
- **Data Source**: Staff pulse survey; partnership forum records
- **Report Owner**: Chief People Officer

**Business Value**:

- **Financial Impact**: Reduced turnover and agency cost
- **Strategic Impact**: Organisational capacity to absorb further change
- **Operational Impact**: Adoption depth rather than nominal enablement
- **Customer Impact**: Staff wellbeing correlates with care quality

**Timeline**:

- **Phase 1 (Months 1-3)**: Telemetry-use agreement concluded with staff-side before enablement
- **Phase 2 (Months 4-6)**: First pulse survey after wave 1
- **Phase 3 (Months 7-12)**: Trend established across waves
- **Sustainment (Year 2+)**: Folded into the annual staff survey

**Stakeholder Benefits**:

- **Chief People Officer**: Retention narrative grounded in evidence (SD-3)
- **Unions and professional bodies**: Commitments visible and tracked (SD-11)
- **Administrative staff**: Role concerns addressed explicitly (SD-12)

**Leading Indicators** (early signals of success):

- Telemetry-use agreement signed before first enablement
- Voluntary adoption exceeding mandated enablement
- Champion network recruitment ahead of target

**Lagging Indicators** (final proof of success):

- Sustained positive survey trend on burden and trust
- No formal dispute escalated beyond the partnership forum

---

### Outcome O-6: Defensible value for money by licence tier

**Supported Goals**: G-3, G-4

**Outcome Statement**: Benefit per licence tier is measured and reported, enabling evidence-based tier assignment and a defensible answer to any value-for-money challenge.

**Measurement Details**:

- **KPI**: Measured benefit per user per licence tier against recurring cost per tier
- **Current Value**: Not measured; tier assignment currently role-assumption based
- **Target Value**: Benefit reported per tier quarterly, with tier reassignment where evidence warrants
- **Measurement Frequency**: Quarterly
- **Data Source**: G-3 measurement broken down by tier; licence register
- **Report Owner**: Director of Finance

**Business Value**:

- **Financial Impact**: Avoided over-licensing and under-licensing; defensible recurring spend
- **Strategic Impact**: Evidence for national tier policy
- **Operational Impact**: Capability matched to role need
- **Customer Impact**: Resource directed where it produces care capacity

**Timeline**:

- **Phase 1 (Months 1-3)**: Tier-level measurement design agreed
- **Phase 2 (Months 4-6)**: First tier-level benefit report
- **Phase 3 (Months 7-12)**: Tier reassignment where evidence warrants
- **Sustainment (Year 2+)**: Annual tier review

**Stakeholder Benefits**:

- **Director of Finance**: Defensible recurring spend (SD-9)
- **National Programme SRO**: National tier evidence (SD-1)
- **Frontline clinicians**: Capability matched to actual need (SD-10)

**Leading Indicators** (early signals of success):

- Tier recorded against every measured cohort
- Early divergence in benefit between tiers identified

**Lagging Indicators** (final proof of success):

- Tier mix adjusted on evidence rather than assumption
- Value-for-money position withstands external review

---

## Complete Traceability Matrix

### Stakeholder → Driver → Goal → Outcome

| Stakeholder | Driver ID | Driver Summary | Goal ID | Goal Summary | Outcome ID | Outcome Summary |
|-------------|-----------|----------------|---------|--------------|------------|-----------------|
| National Programme SRO | SD-1 | Evidence return on £120m | G-3 | Measure benefit locally | O-1 | Time released and reinvested |
| National Programme SRO | SD-1 | Evidence return on £120m | G-3 | Measure benefit locally | O-6 | Value for money by tier |
| CCIO | SD-2 | Prevent clinical drift | G-2 | Define and monitor boundary | O-2 | No AI-attributable harm |
| CCIO | SD-2 | Prevent clinical drift | G-8 | Competence-based training | O-2 | No AI-attributable harm |
| Chief People Officer | SD-3 | Convert time into retention | G-3 | Measure benefit locally | O-1 | Time released and reinvested |
| Chief People Officer | SD-3 | Convert time into retention | G-8 | Competence-based training | O-5 | Workforce confidence |
| Clinical Safety Officer | SD-4 | Discharge DCB0160 duty | G-1 | Safety governance before deployment | O-2 | No AI-attributable harm |
| Clinical Safety Officer | SD-4 | Discharge DCB0160 duty | G-4 | Evidenced tenancy decision | O-3 | IG assurance maintained |
| Caldicott Guardian | SD-5 | Confidentiality without obstruction | G-6 | Retention and DLP to clinical schedules | O-3 | IG assurance maintained |
| SIRO / DPO | SD-6 | Accept risk on evidence | G-5 | DSPT with AI in scope | O-3 | IG assurance maintained |
| SIRO / DPO | SD-6 | Accept risk on evidence | G-6 | Retention and DLP configured | O-3 | IG assurance maintained |
| CISO / Cyber Lead | SD-7 | Assurance under rapid change | G-5 | DSPT with AI in scope | O-3 | IG assurance maintained |
| CISO / Cyber Lead | SD-7 | Assurance under rapid change | G-7 | Frictionless strong authentication | O-4 | Attributable access |
| CIO / CDIO | SD-8 | Right tenancy model | G-4 | Evidenced tenancy decision | O-3 | IG assurance maintained |
| CIO / CDIO | SD-8 | Right tenancy model | G-4 | Evidenced tenancy decision | O-6 | Value for money by tier |
| Director of Finance | SD-9 | Defensible licensing tier | G-3 | Measure benefit locally | O-6 | Value for money by tier |
| Frontline clinicians | SD-10 | Time back without new risk | G-7 | Frictionless strong authentication | O-4 | Attributable access |
| Frontline clinicians | SD-10 | Time back without new risk | G-8 | Competence-based training | O-1 | Time released and reinvested |
| Frontline clinicians | SD-10 | Time back without new risk | G-2 | Define and monitor boundary | O-2 | No AI-attributable harm |
| Unions / professional bodies | SD-11 | Protect against second-order effects | G-2 | Boundary and telemetry agreement | O-5 | Workforce confidence |
| Unions / professional bodies | SD-11 | Protect against second-order effects | G-3 | Measure benefit locally | O-5 | Workforce confidence |
| Administrative staff | SD-12 | Benefit without role threat | G-3 | Measure benefit locally | O-5 | Workforce confidence |
| RA Manager | SD-13 | End credential sharing | G-7 | Frictionless strong authentication | O-4 | Attributable access |
| L&D lead | SD-14 | Competence not completion | G-8 | Competence-based training | O-5 | Workforce confidence |
| CQC / ICO | SD-15 | Verifiable compliance | G-5 | DSPT with AI in scope | O-3 | IG assurance maintained |
| CQC / ICO | SD-15 | Verifiable compliance | G-6 | Retention to clinical schedules | O-3 | IG assurance maintained |
| Trust Chief Executive | SD-16 | Avoid being the example | G-1 | Safety governance before deployment | O-2 | No AI-attributable harm |
| Trust Chief Executive | SD-16 | Avoid being the example | G-5 | DSPT with AI in scope | O-3 | IG assurance maintained |

### Conflict Analysis

**Competing Drivers**:

- **C-1: Delivery pace versus clinical assurance.** The National Programme SRO (SD-1) is accountable for enabling approximately 505,000 staff by October 2026 [NB-C1], while the Clinical Safety Officer (SD-4) cannot sign a safety case faster than hazards can be properly assessed [NB-C4]. These are incompatible at the margin: the deadline is fixed and the assurance work is not compressible without weakening it.
  - **Resolution Strategy**: Split the scope rather than the standard. Deploy first to purely administrative cohorts where the intended-use boundary excludes clinical workflows, which requires a lighter safety case and can move at national pace. Gate clinical-adjacent deployment separately, on assurance rather than on date. Fund CSO capacity as a programme cost so that assurance scales with rollout instead of throttling it. Escalate to the programme board any wave where the date would otherwise override the gate — this decision must be taken visibly, not absorbed silently at delivery level.

- **C-2: Licence cost control versus the benefit case.** The Director of Finance (SD-9) is incentivised toward the cheaper Standard Service tier for frontline clinical staff, which provides web-based applications and a 4 GB mailbox [NB-C18], while the benefit case rests on time savings that may depend on capability present only in the higher tier — and frontline clinicians (SD-10) experience that gap directly.
  - **Resolution Strategy**: Refuse to settle the tier mix before evidence exists. Measure benefit per tier from wave 1 (G-3, O-6), deploy a deliberately mixed pilot across both tiers in comparable cohorts, and commit contractually to the ability to move users between tiers. Treat any multi-year tier commitment made before tier-level benefit data as a financial risk to be logged, not a saving to be booked.

- **C-3: Drift monitoring versus staff trust.** Detecting clinical drift (SD-2) requires observing what staff actually do with the tool, while unions and professional bodies (SD-11) and clinicians themselves (SD-10) will reasonably object to usage telemetry that could support performance management.
  - **Resolution Strategy**: Conclude a written telemetry-use agreement with staff-side representatives **before** first enablement, specifying that monitoring operates at cohort level for safety purposes, that individual-level data is not available to line managers, and naming the limited circumstances (a specific safety investigation) in which individual data may be accessed and who authorises it. Give staff-side representation on the programme board rather than consultation after decisions. This conflict is cheap to resolve early and extremely expensive to resolve after the first grievance.

- **C-4: Central standardisation versus local clinical integration.** The shared environment delivers economies of scale, consistent data loss prevention, and national security baselines [NB-C7], while organisations with legacy clinical systems requiring hybrid identity or specialised integration need flexibility that exceeds central constraints [NB-C17]. The CIO (SD-8) must choose; the CISO (SD-7) and Clinical Safety Officer (SD-4) inherit different responsibilities depending on the answer.
  - **Resolution Strategy**: Force the decision to be explicit and evidenced (G-4) rather than arrived at by default. Assess all four stated factors, complete the legacy clinical system inventory first, and record which controls are inherited versus locally owned. Where sovereignty is chosen, fund the additional local governance capacity in the same board paper that approves the model — the responsibility and the resource must be approved together or not at all.

- **C-5: Early-adopter pressure versus reputational caution.** The National Programme SRO (SD-1) needs visible early adopters; the Trust Chief Executive (SD-16) faces asymmetric downside, since success is a shared national story and failure is a specific local one.
  - **Resolution Strategy**: Offer enhanced central assurance support — CSO capacity, DPIA templates, evaluation design — as the explicit consideration for early adoption, and agree that benefit claims for early sites are published by the organisation itself rather than nationally on its behalf.

**Synergies**:

- **S-1: One evidence pack, three signatures.** The Clinical Safety Officer (SD-4), Caldicott Guardian (SD-5), and SIRO (SD-6) each need overlapping evidence — data flows, intended use, residual risk, retention position. Producing a single integrated assurance pack (G-1, G-5, G-6) satisfies all three and removes the sequential sign-off delay that would otherwise compound C-1.
- **S-2: Friction reduction serves security and clinicians alike.** Eliminating credential sharing (SD-13) and reducing authentication friction (SD-10) are the same intervention [NB-C3]. G-7 is the programme's clearest win-win and should be sequenced early to build clinician goodwill for the harder changes.
- **S-3: Usable tooling is a security control.** Reducing shadow IT and shadow AI (SD-7) is achieved by making approved tooling genuinely better, not by prohibition [NB-C16] — aligning the CISO's assurance interest with the clinicians' usability interest.
- **S-4: Honest measurement serves everyone except a premature narrative.** The SRO (SD-1), Finance (SD-9), Chief People Officer (SD-3), and staff-side (SD-11) all benefit from the same rigorous local measurement (G-3). The only interest served by asserting the national pilot figure locally is short-term optics, and it is the fastest route to losing all four.

---

## Communication & Engagement Plan

### Stakeholder-Specific Messaging

#### National Programme SRO

**Primary Message**: Locally evidenced benefit will be defensible under scrutiny in a way that the inherited pilot figure will not.

**Key Talking Points**:

- Baseline capture is irrecoverable if skipped — the window closes at enablement
- Administrative-first scoping lets pace and assurance proceed in parallel rather than in conflict
- Tier-level evidence protects the programme against a value-for-money challenge

**Communication Frequency**: Monthly

**Preferred Channel**: Programme board with a one-page benefit dashboard

**Success Story**: A published local result, honestly reported, that a select committee could examine without embarrassment.

---

#### Clinical Safety Officer, Caldicott Guardian, and SIRO

**Primary Message**: You will be engaged while design is still changeable, and you will receive one integrated evidence pack rather than three partial ones.

**Key Talking Points**:

- Engagement at design stage, not at sign-off, when options still exist
- A single assurance pack covering data flows, intended use, residual risk, and retention (S-1)
- CSO capacity funded as a programme cost, so the gate is resourced rather than merely asserted

**Communication Frequency**: Fortnightly during design, monthly thereafter

**Preferred Channel**: Assurance working group

**Success Story**: A wave gated on evidence, on schedule, because the evidence was ready — not because the standard was relaxed.

---

#### Frontline clinicians and administrative staff

**Primary Message**: This should make your day shorter, and we will tell you honestly where it cannot be trusted.

**Key Talking Points**:

- What the tool is approved for, and specifically what it must not be used for
- Faster sign-in on shared workstations — the change most likely to be felt immediately
- Telemetry is for safety at cohort level, and your line manager cannot see your individual usage
- Training is 15 minutes at a time, inside the tools you already use, built around your actual workflow

**Communication Frequency**: At enablement, then monthly via champions

**Preferred Channel**: Clinical champions, team meetings, in-tool prompts

**Success Story**: "I got home on time because the letters were already drafted" — and a colleague who caught a wrong summary, reported it, and was thanked rather than blamed.

---

#### Unions and professional bodies

**Primary Message**: The telemetry-use agreement and the reinvestment commitment are settled in writing before the first user is enabled.

**Key Talking Points**:

- Written limits on telemetry use, agreed before deployment, not after a grievance
- Board commitment that released time is reinvested in care and rest
- Representation on the programme board, not consultation after decisions
- Redeployment and reskilling pathway defined for roles most affected by automation

**Communication Frequency**: Monthly partnership forum, plus board attendance

**Preferred Channel**: Formal partnership forum with written agreements

**Success Story**: Savings published jointly, with the reinvestment commitment quoted alongside the number.

---

#### Trust Chief Executive and Board

**Primary Message**: The assurance is visibly discharged, and the exposure is understood and managed.

**Key Talking Points**:

- Named accountability for each gate, with escalation defined
- Administrative-first scoping materially limits early clinical exposure
- Benefit claims are locally owned, so the organisation is not exposed by a national number

**Communication Frequency**: Monthly exception report; quarterly full review

**Preferred Channel**: Board paper with a risk-and-assurance annex

**Success Story**: A CQC conversation in which the evidence is already assembled.

---

#### Director of Finance

**Primary Message**: Tier decisions will be made on measured benefit rather than on list price.

**Key Talking Points**:

- Benefit measured and reported per tier from wave 1
- Mixed-tier pilot avoids a premature multi-year commitment
- Released capacity is care capacity, and should not be booked as cash without an explicit establishment decision

**Communication Frequency**: Quarterly

**Preferred Channel**: Finance and performance committee

**Success Story**: A tier mix adjusted on evidence, with the saving explained rather than assumed.

---

## Change Impact Assessment

### Impact on Stakeholders

| Stakeholder | Current State | Future State | Change Magnitude | Resistance Risk | Mitigation Strategy |
|-------------|---------------|--------------|------------------|-----------------|---------------------|
| Frontline clinicians | Manual documentation; shared credentials on ward workstations | AI-assisted drafting with mandatory review; individual frictionless authentication | HIGH | MEDIUM | Champion-led workflow training; sequence authentication improvement first to build goodwill |
| Administrative staff | High-volume repetitive administrative tasks | Automated drafting; shift toward exception handling and higher-value work | HIGH | HIGH | Redeployment and reskilling pathway published before rollout; involvement in choosing what is automated |
| Clinical Safety Officer | Role may be unfilled or unfunded for this programme | Named, resourced, gate-holding accountability | HIGH | LOW | Fund capacity as a programme cost; provide analyst support |
| Registration Authority team | Smartcard issuance and unlock workload | Authenticator migration surge, then reduced steady-state through self-service | HIGH | MEDIUM | Fund migration-period capacity; sequence by area; expand self-service early [NB-C22] |
| IT Service Desk | Steady-state platform support | Enablement-wave support surge; new AI-related query class | MEDIUM | LOW | Wave-based rollout; runbooks and champion deflection before each wave |
| Information Governance Manager | Periodic IG casework | Continuous configuration governance and DLP tuning | MEDIUM | LOW | Configuration held as code; automated evidence capture |
| Line managers | Manage by presence and output | Same, but with new telemetry they must not misuse | MEDIUM | MEDIUM | Explicit training on telemetry limits; access technically restricted, not merely discouraged |
| Director of Finance | Annual licence renewal | Quarterly tier-level benefit review | LOW | LOW | Provide the tier-level reporting they currently lack |

### Change Readiness

**Champions** (Enthusiastic supporters):

- **Chief People Officer** — the programme offers a credible answer to burnout and attrition pressures they cannot otherwise move (SD-3)
- **Frontline clinicians in high-documentation specialties** — the burden is felt daily and the benefit is immediate
- **Registration Authority Manager** — frictionless authentication solves a problem they have owned without a remedy for years (SD-13)
- **CCIO and CNIO** — provided the intended-use boundary is real and enforced

**Fence-sitters** (Neutral, need convincing):

- **Trust Chief Executive** — will move once assurance is visibly discharged and early-adopter exposure is bounded (SD-16)
- **Director of Finance** — needs tier-level evidence before committing recurring spend (SD-9)
- **Line managers** — supportive of productivity, uncertain about their own role in a monitored workflow
- **IT Service Desk** — willing, but conscious of an unfunded support surge

**Resisters** (Opposed or sceptical):

- **Unions and professional bodies** — resist the second-order effects, not the technology. Address with a written telemetry-use agreement and a board reinvestment commitment, both concluded before first enablement (SD-11, C-3)
- **Administrative staff in highly automatable roles** — resistance is rational and existential. Address with a published redeployment and reskilling pathway and genuine involvement in automation design (SD-12)
- **Clinicians who have encountered unreliable AI output** — the most credible sceptics in the organisation. Address by taking their examples seriously, feeding them into the hazard log, and recruiting the most vocal among them as reviewers rather than treating them as obstacles

---

## Risk Register (Stakeholder-Related)

### Risk R-1: Clinical safety gate is overridden by delivery pressure

**Related Stakeholders**: Clinical Safety Officer, National Programme SRO, Trust Chief Executive

**Risk Description**: The October 2026 target [NB-C1] causes a wave to be enabled without an approved safety case, or with a safety case signed under pressure rather than on evidence.

**Impact on Goals**: G-1 fails outright; G-2 and O-2 compromised

**Probability**: MEDIUM

**Impact**: HIGH

**Mitigation Strategy**: Administrative-first scoping (C-1) so pace and assurance are not in direct competition; CSO capacity funded as a programme cost; any date-over-gate decision escalated to the programme board and minuted, never taken at delivery level

**Contingency Plan**: Halt the affected wave, complete the safety case retrospectively, and review all activity in the exposure window for harm

---

### Risk R-2: Local benefit falls materially short of the national pilot figure

**Related Stakeholders**: National Programme SRO, Director of Finance, Chief People Officer

**Risk Description**: Measured local saving is well below 43 minutes per person per day [NB-C1] because the pilot population self-selected, and no explanation was prepared — damaging credibility for this programme and the next.

**Impact on Goals**: G-3 delivers an unwelcome answer; O-1 and O-6 undermined

**Probability**: HIGH

**Impact**: MEDIUM

**Mitigation Strategy**: Set expectations before measurement, not after — state publicly that the pilot figure is a ceiling from a volunteer cohort, not a forecast; capture baselines properly; report by cohort and tier so variance is explainable rather than merely disappointing

**Contingency Plan**: Publish the variance with analysis, and reframe the case around the cohorts where benefit is real rather than defending an average

---

### Risk R-3: Telemetry dispute stalls deployment

**Related Stakeholders**: Unions, frontline clinicians, CCIO, Chief People Officer

**Risk Description**: Drift monitoring is deployed without a staff-side agreement, is characterised as surveillance, and triggers a formal dispute that halts enablement.

**Impact on Goals**: G-2 blocked; O-2 and O-5 compromised

**Probability**: MEDIUM

**Impact**: HIGH

**Mitigation Strategy**: Conclude the written telemetry-use agreement before first enablement (C-3); restrict individual-level data technically rather than by policy; give staff-side programme board representation

**Contingency Plan**: Suspend individual-level collection, retain cohort-level safety monitoring only, and renegotiate

---

### Risk R-4: Assurance roles are unfunded and become the bottleneck

**Related Stakeholders**: Clinical Safety Officer, Caldicott Guardian, SIRO, RA Manager

**Risk Description**: CSO, IG, and Registration Authority capacity is assumed to absorb programme workload on top of existing duties, and the assurance and authenticator migration paths both stall.

**Impact on Goals**: G-1, G-5, G-6, G-7 all delayed

**Probability**: HIGH

**Impact**: HIGH

**Mitigation Strategy**: Fund assurance and RA capacity explicitly in the programme budget; produce one integrated evidence pack rather than three (S-1); expand self-service to reduce RA steady-state load [NB-C22]

**Contingency Plan**: Slow the wave cadence to match assurance capacity rather than deploying unassured

---

### Risk R-5: Shadow AI adoption outside the assessed boundary

**Related Stakeholders**: CISO, CCIO, frontline clinicians

**Risk Description**: Staff adopt unapproved AI tools because approved tooling is slower or less capable, placing patient data outside any assessed control [NB-C16].

**Impact on Goals**: G-5 and G-2 undermined; O-3 at risk

**Probability**: MEDIUM

**Impact**: HIGH

**Mitigation Strategy**: Treat usability as a security control (S-3) — prioritise making approved tooling faster than the workaround; monitor for unapproved tool use; provide a fast, non-punitive route to request capability

**Contingency Plan**: Assess exposure, notify SIRO and DPO, and prioritise the capability gap that drove the behaviour rather than only blocking the tool

---

### Risk R-6: Automation anxiety hardens into organised resistance

**Related Stakeholders**: Administrative staff, unions, Chief People Officer

**Risk Description**: Time-saving figures are published before the workforce conversation, are read as a redundancy business case, and convert manageable anxiety into formal opposition.

**Impact on Goals**: G-3 and G-8 impaired; O-5 fails

**Probability**: MEDIUM

**Impact**: MEDIUM

**Mitigation Strategy**: Publish the reinvestment commitment alongside — never after — the first savings figure; define the redeployment and reskilling pathway before rollout; involve affected staff in choosing what is automated

**Contingency Plan**: Pause external benefit communication, convene the partnership forum, and republish with the workforce position agreed

---

### Risk R-7: Tenancy decision made by default

**Related Stakeholders**: CIO / CDIO, CISO, Clinical Safety Officer

**Risk Description**: Architecture work proceeds assuming a tenancy model that was never formally decided, and the four stated decision factors [NB-C17] are assessed only retrospectively, after reversal has become expensive.

**Impact on Goals**: G-4 fails; G-5 evidence base unstable

**Probability**: MEDIUM

**Impact**: HIGH

**Mitigation Strategy**: Treat the tenancy decision as a gating prerequisite for architecture work; complete the legacy clinical system inventory first; approve responsibility and resource in the same board paper

**Contingency Plan**: Freeze dependent architecture work until the decision record is approved

---

## Governance & Decision Rights

### Decision Authority Matrix (RACI)

| Decision Type | Responsible | Accountable | Consulted | Informed |
|---------------|-------------|-------------|-----------|----------|
| Tenancy model selection | CIO / CDIO | Trust Chief Executive | CISO, Clinical Safety Officer, SIRO, NHS Digital | Programme board, ICS partners |
| Clinical safety case approval and go-live gate | Clinical Safety Officer | Clinical Safety Officer | CCIO, CNIO, clinical leads | Programme board, Trust Chief Executive |
| Intended-use boundary definition | CCIO | Clinical Safety Officer | CNIO, frontline clinicians, unions | All enabled users |
| Information risk acceptance | SIRO | SIRO | DPO, Caldicott Guardian, CISO | Trust board |
| Confidentiality and data-sharing configuration | Information Governance Manager | Caldicott Guardian | DPO, CISO, clinical leads | Frontline staff |
| Retention schedule configuration | Information Governance Manager | Caldicott Guardian | Records management, Clinical Safety Officer | IT Operations |
| Licence tier assignment | Director of Finance | Trust Chief Executive | CIO, CCIO, Chief People Officer | Programme board |
| Telemetry use and access limits | Chief People Officer | Trust Chief Executive | Unions, DPO, CCIO, line managers | All staff |
| Deployment wave scheduling | Delivery Manager | Programme SRO | Clinical Safety Officer, IT Service Desk, RA Manager | All stakeholders |
| Authenticator migration approach | RA Manager | CISO | Clinical leads, IT Operations, frontline representatives | All users |
| Benefit measurement method | Local programme lead | Programme SRO | Finance, Chief People Officer, unions | Programme board |
| Training design and competence standard | L&D lead | CCIO | Clinical champions, CNIO, frontline staff | Line managers |
| Redeployment and reskilling pathway | Chief People Officer | Trust Chief Executive | Unions, affected staff, line managers | All staff |
| Go/no-go for each deployment wave | Delivery Manager | Trust Chief Executive | Clinical Safety Officer (veto), SIRO (veto), CISO | All stakeholders |

> **Note on vetoes**: The Clinical Safety Officer and SIRO hold blocking authority on their respective domains. This is not a delegation from the programme and cannot be overridden by the programme board — it derives from DCB0160 [NB-C4] and from the SIRO's personal accountability for information risk. Escalation can change the schedule; it cannot change the answer.

### Escalation Path

1. **Level 1 — Delivery Manager / Local programme lead**: Day-to-day scheduling, resourcing, and dependency decisions
2. **Level 2 — Programme Board**: Scope, wave sequencing, budget variance, conflicts C-2 and C-5, tier decisions
3. **Level 3 — Trust Executive / Chief Executive**: Tenancy model, telemetry policy, workforce commitments, conflicts C-3 and C-4
4. **Level 4 — NHS England Programme SRO**: National pace expectations, cross-organisation dependencies, conflict C-1 where local resolution fails
5. **Parallel — Clinical Safety Officer and SIRO**: Clinical safety and information risk escalate directly to the Trust Chief Executive and Board, bypassing the programme hierarchy. Any attempt to route these through Level 1 or 2 is itself a governance failure and should be reported as such.

---

## Validation & Sign-off

### Stakeholder Review

| Stakeholder | Review Date | Comments | Status |
|-------------|-------------|----------|--------|
| Clinical Safety Officer | PENDING | Not yet appointed — appointment is a prerequisite for G-1 | PENDING |
| Caldicott Guardian | PENDING | Awaiting first assurance working group | PENDING |
| Senior Information Risk Owner | PENDING | Awaiting DPIA scope | PENDING |
| Chief People Officer | PENDING | Awaiting staff-side engagement plan | PENDING |
| Staff-side representatives | PENDING | Telemetry-use agreement not yet opened | PENDING |
| CIO / CDIO | PENDING | Awaiting tenancy decision paper | PENDING |

### Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor | PENDING | PENDING | PENDING |
| Business Owner | PENDING | PENDING | PENDING |
| Enterprise Architect | Mark Craddock | PENDING | PENDING |

---

## Appendices

### Appendix A: Stakeholder Interview Summaries

No stakeholder interviews have been conducted. This analysis is derived from the NHS 365 source book and from documented NHS governance structures, and it should be validated by interview before it is relied on for decisions.

**Priority interviews before v2.0**:

- Clinical Safety Officer (once appointed) — hazard identification approach, capacity, gate expectations
- Staff-side representatives — telemetry limits, reinvestment commitment, redeployment concerns
- Frontline clinicians in two contrasting specialties — actual documentation burden and current workarounds
- Registration Authority Manager — current sharing prevalence, migration capacity
- Director of Finance — tier assignment logic and appetite for a mixed-tier pilot

**Validation risk**: Driver intensities and resistance assessments in this document are inferred, not observed. Sections most likely to change after interview are SD-11 and SD-12 (staff-side and administrative staff drivers) and the resistance ratings in the Change Impact Assessment.

---

### Appendix B: Survey Results

No stakeholder surveys have been conducted. The quarterly pulse survey supporting O-5, and the boundary-comprehension survey supporting G-2, are both proposed here and not yet designed.

---

### Appendix C: References

- `ARC-000-PRIN-v1.0.md` — NHS 365 Enterprise Architecture Principles, particularly Principle 10 (Clinical Safety by Design), Principle 11 (Human Accountability for Automated Output), and Principle 12 (Identity Assurance and Non-Repudiation), which correspond directly to drivers SD-4, SD-2, and SD-13
- *NHS 365 — A Best Practices Guide for Transforming UK Healthcare with Microsoft AI* — `projects/000-global/external/nhs365-book2.pdf`
- Government Functional Standard GovS 005 (Digital) and GovS 007 (Security)
- DCB0129 and DCB0160 clinical risk management standards
- Data Security and Protection Toolkit; NCSC Cyber Assessment Framework

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-19 | ArcKit AI | Initial draft from `/arckit:stakeholders` |

## External References

> This section provides traceability from generated content back to source documents.
> Follow citation instructions in the project's citation reference guide.

### Document Register

| Doc ID | Filename | Type | Source Location | Description |
|--------|----------|------|-----------------|-------------|
| NB | nhs365-book2.pdf | Reference Guide | `000-global/external/` | *NHS 365 — A Best Practices Guide for Transforming UK Healthcare with Microsoft AI* (365apps.pro, 2026-08-11, 23 pages). Cited via the converted Markdown copy `nhs365-book2.md` held alongside it. |
| PRIN | ARC-000-PRIN-v1.0.md | ArcKit Artifact | `000-global/` | NHS 365 Enterprise Architecture Principles v1.0 — 21 principles providing the governance context for stakeholder goals |

### Citations

| Citation ID | Doc ID | Page/Section | Category | Quoted Passage |
|-------------|--------|--------------|----------|----------------|
| NB-C1 | NB | Introduction — NHS England's Landmark Copilot Rollout | Stakeholder Need | "the deployment follows the largest AI trial of its kind in global healthcare. In that pilot, involving over 30,000 staff across 90 NHS organisations, participants saved an average of 43 minutes per person per day on administrative tasks... The rollout, expected to reach over 500,000 clinicians and support staff by October 2026" |
| NB-C2 | NB | Strategic Architecture — Artificial Intelligence, Automation, and Associated Risks | Risk Factor | "'clinical drift'—the gradual use of generative AI for summarising patient notes or supporting clinical discussion—introduces risks of hallucination, omission of critical details such as allergies, or incorrect synthesis of information." |
| NB-C3 | NB | Care Identity Service — Governance, Identity Lifecycle, and Risks | Risk Factor | "A persistent human risk is smartcard sharing, which undermines non-repudiation and patient safety investigations. CIS2 mitigates this by expanding frictionless options such as biometrics and high-assurance passkeys." |
| NB-C4 | NB | Strategic Architecture — Security and Clinical Safety Governance | Compliance Constraint | "clinical risk management standards DCB0129 and DCB0160. The latter requires appointment of a Clinical Safety Officer who identifies hazards, assesses severity and likelihood, and ensures residual risk is reduced to a level that is as low as reasonably practicable before systems go live." |
| NB-C5 | NB | Workforce Transformation — Microsoft 365 as the Digital Backbone | Stakeholder Need | "By offering a coherent, secure experience inside the clinical workflow, trusts can reduce the appeal of 'shadow IT'—unofficial tools staff adopt when official systems frustrate them." |
| NB-C6 | NB | Workforce Transformation — opening | Business Requirement | "The National Health Service (NHS) faces a profound workforce crisis marked by high vacancies, slowing recruitment, and widespread burnout. The service employs around 1.37 million full-time equivalent staff, yet vacancies stand at approximately 100,020—a 6.7% rate... sickness absence hovers near 5.1%, with psychiatric issues such as anxiety, stress, and depression accounting for roughly 30% of absences" |
| NB-C7 | NB | Strategic Architecture — Licensing Approach | Design Decision | "The Shared NHS Tenant is the default for most organisations. Managed centrally by NHS Digital (with support from partners such as Accenture), it delivers economies of scale, consistent Data Loss Prevention policies, and national security baselines." |
| NB-C8 | NB | Introduction — Organised Around Real NHS Priorities | Compliance Constraint | "best practices that respect NHS values, align with national strategies such as the Long Term Plan and the Data Strategy, and meet the rigorous standards expected by the Care Quality Commission, NHS England, and the Information Commissioner's Office." |
| NB-C9 | NB | Care Identity Service — Practical Considerations for Organisations | Compliance Constraint | "Compliance is demonstrated primarily through the Data Security and Protection Toolkit (DSPT), aligned with the National Cyber Security Centre's Cyber Assessment Framework." |
| NB-C10 | NB | Workforce Transformation — Information Governance and Security | Compliance Constraint | "All solutions must meet rigorous NHS standards, including the Data Security and Protection Toolkit and Caldicott principles... Existing tools such as Microsoft Purview can enforce policies that prevent inappropriate sharing of patient identifiers in collaborative channels." |
| NB-C11 | NB | Care Identity Service — From CIS1 to CIS2 | Stakeholder Need | "Supporting more than 1.3 million workers and handling tens of millions of authentications each month, access is managed locally by Registration Authorities (RAs). These bodies issue Care Identities, assign role-based access control (RBAC) positions, and control authenticators." |
| NB-C12 | NB | Strategic Architecture — Artificial Intelligence, Automation, and Associated Risks | Compliance Constraint | "Copilot is treated as an administrative productivity tool rather than Software as a Medical Device." |
| NB-C13 | NB | Workforce Transformation — opening | Risk Factor | "Nearly half of general practice staff report that hardware and software are unfit for purpose, contributing to cognitive overload that undermines both wellbeing and care delivery." |
| NB-C14 | NB | Workforce Transformation — Microsoft 365 as the Digital Backbone | Data Requirement | "Data remains within the organisation's own tenant, simplifying governance and supporting UK data residency requirements." |
| NB-C15 | NB | Strategic Architecture — Drivers for Change | Risk Factor | "The 2017 WannaCry ransomware attack highlighted the risks of this approach: it disrupted services at 81 of 236 trusts, largely because outdated systems remained in use after a previous national enterprise agreement had expired." |
| NB-C16 | NB | Introduction — A Practical Guide for the People Driving Change | Risk Factor | "you will find honest discussion of the pitfalls—shadow AI, data quality issues, change fatigue, equity risks, and the critical need for clinical safety and information governance to be designed in from the start." |
| NB-C17 | NB | Strategic Architecture — Conclusion | Design Decision | "Organisations must weigh the operational simplicity and strong baseline security of the Shared Tenant against the flexibility—and greater responsibility—of a Sovereign Tenant. Critical decision factors include cyber maturity, the need for specialised integrations, the presence of legacy clinical systems that require hybrid identity, and the capacity to manage clinical safety governance for AI and automation." |
| NB-C18 | NB | Strategic Architecture — Licensing Approach | Procurement Constraint | "The Standard Service, based on Microsoft 365 F3, targets frontline clinical staff and provides web-based Office applications, a 4 GB mailbox, and limited OneDrive storage... The Enhanced Service, built on a restricted Microsoft 365 E3 Frontline Worker licence, serves managers, multidisciplinary team coordinators, and heavier administrative users." |
| NB-C19 | NB | Workforce Transformation — Microlearning and Communities of Practice | Stakeholder Need | "Clinical staff rarely have time for full-day classroom sessions. Microlearning—focused units typically under 15 minutes—fits better into busy schedules. Educators can prioritise content using a simple framework: material that is fatal if unknown, fundamental to daily practice, frequently used, fixed by policy, or useful for team cohesion." |
| NB-C20 | NB | Teams Rooms — Change Management and Measuring Success | Stakeholder Need | "Technology alone does not guarantee adoption. Organizations should identify clinical champions among physicians and nurses to lead pilots and advocate for the tools. Training must focus on practical workflows—such as sharing a DICOM image—rather than hardware specifications." |
| NB-C21 | NB | Introduction — A Practical Guide for the People Driving Change | Risk Factor | "equity risks, and the critical need for clinical safety and information governance to be designed in from the start." |
| NB-C22 | NB | Care Identity Service — Practical Considerations for Organisations | Stakeholder Need | "Registration Authorities remain central for identity proofing, role assignment, and smartcard lifecycle management, though self-service options (including Apply for Care ID and smartcard unlock) have expanded." |
| NB-C23 | NB | Teams Rooms — Security, Compliance, and Governance | Data Requirement | "Default Teams retention settings may conflict with clinical record-keeping requirements. Microsoft Purview can enforce appropriate retention—often six years for clinical consultations—while allowing shorter periods for administrative content." |

### Unreferenced Documents

| Filename | Source Location | Reason |
|----------|-----------------|--------|
| README.md | `000-global/policies/` | Directory placeholder; no organisational policy content present. No org charts, governance structures, or existing stakeholder maps have been supplied — see Appendix A for the validation risk this creates. |
| README.md | `001-nhs365/external/` | Directory placeholder created by this command; no project-specific reference documents supplied yet. |

---

**Generated by**: ArcKit `/arckit:stakeholders` command
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
| Stamped at | 2026-08-19T10:50:48.331Z |

<!-- arckit-provenance:end -->
