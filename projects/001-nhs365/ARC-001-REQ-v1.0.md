# Project Requirements: NHS 365

> **Template Origin**: Official | **ArcKit Version**: 6.11.0 | **Command**: `/arckit:requirements`

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ARC-001-REQ-v1.0 |
| **Document Type** | Business and Technical Requirements |
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
| **Distribution** | Project Team, Architecture Team, Clinical Safety Officer, Caldicott Guardian, SIRO, staff-side representatives |

## Revision History

| Version | Date | Author | Changes | Approved By | Approval Date |
|---------|------|--------|---------|-------------|---------------|
| 1.0 | 2026-08-19 | ArcKit AI | Initial creation from `/arckit:requirements` command | PENDING | PENDING |

## Document Purpose

This document defines the business, functional, non-functional, integration, and data requirements for the NHS 365 programme — the deployment of Microsoft 365, Copilot, and related AI capabilities across NHS organisations. It will be used for vendor RFPs, architecture reviews, clinical safety assessment, and acceptance testing.

Requirements trace to the stakeholder goals in `ARC-001-STKE-v1.0.md` and to the architecture principles in `ARC-000-PRIN-v1.0.md`. Where a requirement exists to satisfy a regulatory obligation rather than a stakeholder preference, that is stated explicitly and the requirement is not negotiable.

**Scope note**: NHS 365 is a deployment and governance programme, not a bespoke software build. Requirements therefore describe the capability an NHS organisation must have in place — configuration, controls, evidence, and process — rather than software to be written from scratch. Requirements remain technology-agnostic where the architecture principles demand it, and name specific national services only where those are mandated.

---

## Executive Summary

### Business Context

NHS England is deploying generative AI assistance to approximately 505,000 staff at a cost of £120 million, following a pilot involving 30,000 users that measured average savings of 43 minutes per person per day on administrative tasks [NB-C1]. The deployment is targeted at October 2026 [NB-C1].

The driver is a workforce crisis: around 1.37 million full-time equivalent staff against approximately 100,020 vacancies — a 6.7% rate — with sickness absence near 5.1%, of which roughly 30% is attributable to anxiety, stress, and depression [NB-C2]. Nearly half of general practice staff report that hardware and software are unfit for purpose, contributing to cognitive overload [NB-C3].

The programme is bounded by obligations that predate it: the Data Security and Protection Toolkit, Caldicott principles, and the clinical risk management standards DCB0129 and DCB0160 [NB-C4]. Nationally the tool is classified as an administrative productivity tool rather than Software as a Medical Device [NB-C5] — a classification that holds only while actual use matches intended use.

### Objectives

1. Deploy AI-assisted productivity capability to eligible staff without clinical harm or confidentiality breach
2. Establish clinical safety governance capable of gating each deployment wave on evidence
3. Measure benefit locally against a local baseline rather than inheriting the national pilot figure
4. Restore attributable access to clinical systems by removing the friction that causes credential sharing
5. Maintain Data Security and Protection Toolkit assurance with AI capability explicitly in scope
6. Demonstrate value for money at licence-tier granularity

### Expected Outcomes

| Outcome | Measure | Source |
|---------|---------|--------|
| Administrative time released and reinvested | Measured minutes per user per day, by cohort and tier | STKE O-1 |
| No AI-attributable clinical harm | Zero attributable safety incidents; 100% hazards with verified controls | STKE O-2 |
| Information governance assurance maintained | DSPT "Standards Met" with AI in scope; zero reportable breaches | STKE O-3 |
| Attributable access | 80% reduction in credential-sharing indicators | STKE O-4 |
| Workforce confidence | Positive survey trend; zero unresolved formal disputes | STKE O-5 |
| Value for money by tier | Benefit reported per licence tier quarterly | STKE O-6 |

### Project Scope

**In scope**:

- Deployment, configuration, and governance of collaboration and AI-assistance capability for NHS staff
- Clinical safety assessment and hazard management under DCB0129/DCB0160
- Identity, authentication, and access lifecycle for clinical systems
- Retention, data loss prevention, and information governance configuration
- Benefit measurement, training, and adoption capability
- Integration with national identity services, directory services, and electronic health records

**Out of scope**:

- Clinical decision support functionality, which would trigger Software as a Medical Device classification [NB-C5] and require a different regulatory pathway
- Patient-facing services and patient-facing AI
- Replacement of the electronic health record
- Network infrastructure procurement
- Any use of patient data for model training

**Explicitly deferred**:

- Clinical-scope AI deployment beyond administrative assistance — deferred pending separate assurance (see Conflict C-1)
- Multi-year licence tier commitment — deferred pending tier-level benefit evidence (see Conflict C-2)

---

## Stakeholders

| Stakeholder | Role | Organization | Involvement Level |
|-------------|------|--------------|-------------------|
| National Programme SRO | Senior Responsible Owner | NHS England | Decision maker — national pace and benefit |
| Trust Chief Executive | Executive Sponsor | Trust executive | Decision maker — accountable for go-live |
| Chief Clinical Information Officer | Clinical design authority | Clinical informatics | Requirements definition — clinical workflow |
| Clinical Safety Officer | Clinical risk management | Clinical governance | Blocking authority — DCB0160 gate |
| Caldicott Guardian | Confidentiality | Information governance | Blocking authority — confidentiality |
| Senior Information Risk Owner | Information risk acceptance | Trust board | Blocking authority — risk acceptance |
| Chief Information Security Officer | Security assurance | Digital / Security | Security review — DSPT and CAF evidence |
| Chief Information Officer / CDIO | Technology strategy | Digital | Technical oversight — tenancy decision |
| Chief People Officer | Workforce | People / HR | Requirements definition — adoption and retention |
| Director of Finance | Financial control | Finance | Decision maker — licence tier |
| Registration Authority Manager | Care Identity lifecycle | Digital / IG | Requirements definition — authentication |
| Frontline clinicians | End users | Clinical services | User acceptance |
| Administrative and operational staff | End users | Operations | User acceptance |
| Staff-side representatives | Staff representation | RCN, BMA, UNISON | Consulted — telemetry and workforce impact |
| Information Governance Manager | IG operations | Information governance | Requirements definition — retention, DLP |
| Learning & Development lead | Training | Education | Requirements definition — competence |

---

## Business Requirements

### BR-001: Deliver assured deployment to eligible staff

**Description**: Deploy AI-assisted productivity capability to all eligible staff in the organisation, in waves, with each wave gated on approved clinical safety and information risk evidence.

**Rationale**: The national programme targets approximately 505,000 staff by October 2026 [NB-C1]. The organisation must contribute to that target without deploying ahead of assurance — the two obligations are reconciled by scope, not by weakening the gate (see Conflict C-1).

**Success Criteria**:

- 100% of deployment waves have Clinical Safety Officer approval recorded before first user enablement
- 100% of deployment waves have SIRO risk acceptance recorded before first user enablement
- Eligible staff enabled in line with the agreed wave schedule, with any date-over-gate decision escalated and minuted

**Priority**: MUST_HAVE

**Stakeholder**: National Programme SRO (STKE SD-1); Trust Chief Executive (SD-16)

**Traces To**: STKE G-1, O-2 · PRIN 10 (Clinical Safety by Design)

---

### BR-002: Evidence benefit against a local baseline

**Description**: Establish a pre-deployment administrative time baseline for each role cohort, and report measured time change quarterly by cohort and by licence tier.

**Rationale**: The 43 minutes per person per day figure was measured on 30,000 pilot participants [NB-C1] who volunteered for an AI trial, and cannot be assumed representative of a mandated population. Baseline capture is irrecoverable once enablement occurs, so this requirement is time-critical in a way most are not.

**Success Criteria**:

- Valid pre-deployment baseline captured for 90% or more of role cohorts
- Benefit reported quarterly, disaggregated by cohort and licence tier
- Variance from the national pilot figure explained rather than averaged away

**Priority**: MUST_HAVE

**Stakeholder**: National Programme SRO (SD-1); Chief People Officer (SD-3); Director of Finance (SD-9)

**Traces To**: STKE G-3, O-1, O-6

---

### BR-003: Cause no AI-attributable clinical harm

**Description**: Maintain zero patient safety incidents attributable to generated content, with every identified hazard carrying a verified control.

**Rationale**: Generative assistance introduces risks of hallucination, omission of critical details such as allergies, and incorrect synthesis [NB-C6]. DCB0160 requires residual clinical risk to be reduced to a level as low as reasonably practicable before go-live [NB-C4]. This is a regulatory obligation, not a target.

**Success Criteria**:

- Zero AI-attributable patient safety incidents
- 100% of identified hazards have a control that has been verified in operation
- Hazard log maintained as a living artefact and reviewed monthly

**Priority**: MUST_HAVE

**Stakeholder**: Clinical Safety Officer (SD-4); CCIO (SD-2); Trust Chief Executive (SD-16)

**Traces To**: STKE G-1, G-2, O-2 · PRIN 10, PRIN 11

---

### BR-004: Maintain information governance assurance through rapid change

**Description**: Achieve and maintain Data Security and Protection Toolkit "Standards Met" with the collaboration and AI capability explicitly in assessed scope, with no ICO-reportable breach originating from the platform.

**Rationale**: Compliance is demonstrated primarily through the DSPT, aligned with the NCSC Cyber Assessment Framework [NB-C7]. Rapid AI-driven change creates new surface faster than annual assurance cycles were designed to absorb.

**Success Criteria**:

- DSPT status "Standards Met" with AI and collaboration capability in scope
- Zero ICO-reportable breaches originating from the platform over any rolling 12 months
- 60% or more of DSPT assertions supported by automated evidence capture

**Priority**: MUST_HAVE

**Stakeholder**: SIRO (SD-6); CISO (SD-7); regulators (SD-15)

**Traces To**: STKE G-5, O-3 · PRIN 4 (Security by Design), PRIN 6, PRIN 7

---

### BR-005: Improve workforce experience without creating role insecurity

**Description**: Deliver measurable reduction in administrative burden while securing, in advance, a written agreement on telemetry use and a board commitment on reinvestment of released time.

**Rationale**: A programme whose headline benefit is time saved has, from a staff-side perspective, quantified a case for reducing establishment. Equity and change-fatigue risks are recognised pitfalls of this kind of transformation [NB-C8]. Resolving this before deployment is cheap; resolving it after the first grievance is not.

**Success Criteria**:

- Written telemetry-use agreement concluded with staff-side representatives before first user enablement
- Board-approved reinvestment commitment published alongside — never after — the first savings figure
- Redeployment and reskilling pathway defined for the roles most affected by automation
- Zero unresolved formal disputes

**Priority**: MUST_HAVE

**Stakeholder**: Chief People Officer (SD-3); staff-side (SD-11); administrative staff (SD-12)

**Traces To**: STKE O-5 · PRIN 11, PRIN 18

---

### BR-006: Demonstrate value for money at licence-tier granularity

**Description**: Report benefit per licence tier against recurring cost per tier, enabling evidence-based tier assignment and reassignment.

**Rationale**: The tiered licensing model ranges from a Standard Service providing web-based applications and a 4 GB mailbox for frontline clinical staff, to an Enhanced Service for managers and heavier administrative users [NB-C9]. The cheapest tier that passes a procurement scorecard may not deliver the savings the benefit case assumes.

**Success Criteria**:

- Licence tier recorded against every measured cohort
- Quarterly benefit-per-tier report produced
- Contractual ability to move users between tiers retained
- No multi-year tier commitment made before tier-level benefit data exists

**Priority**: SHOULD_HAVE

**Stakeholder**: Director of Finance (SD-9); National Programme SRO (SD-1)

**Traces To**: STKE G-3, O-6

---

### BR-007: Record an evidenced tenancy decision

**Description**: Assess and record all four tenancy decision factors — cyber maturity, specialised integration need, legacy clinical systems requiring hybrid identity, and capacity to manage clinical safety governance for AI and automation — and obtain board approval before dependent architecture work proceeds.

**Rationale**: Organisations must weigh the operational simplicity and strong baseline security of a shared environment against the flexibility, and greater responsibility, of an independently managed one; these four factors are the stated critical inputs [NB-C10]. The decision determines which controls are inherited and which are locally owned, and is expensive to reverse.

**Success Criteria**:

- Board-approved tenancy decision record covering all four factors with evidence
- 100% complete inventory of legacy clinical systems requiring hybrid identity
- Documented split of inherited versus locally owned controls
- Where an independently managed model is chosen, the additional governance capacity approved in the same board paper

**Priority**: MUST_HAVE

**Stakeholder**: CIO / CDIO (SD-8); CISO (SD-7); Clinical Safety Officer (SD-4)

**Traces To**: STKE G-4 · PRIN 4, PRIN 6

---

### BR-008: Restore attributable access to clinical systems

**Description**: Eliminate credential sharing on shared clinical workstations by removing the authentication friction that causes it, achieving an 80% reduction in sharing indicators within 12 months per area.

**Rationale**: Credential sharing undermines non-repudiation and patient safety investigations; the stated mitigation is expanding frictionless options such as biometrics and high-assurance passkeys rather than tightening policy [NB-C11]. This is the programme's clearest win-win: it serves security, investigation, and clinician convenience simultaneously.

**Success Criteria**:

- 80% reduction in credential-sharing indicators within 12 months of migration per area
- Median authentication time on shared clinical workstations materially below baseline
- Every sampled clinically significant action attributable to a named individual

**Priority**: MUST_HAVE

**Stakeholder**: Registration Authority Manager (SD-13); CISO (SD-7); frontline clinicians (SD-10)

**Traces To**: STKE G-7, O-4 · PRIN 12 (Identity Assurance and Non-Repudiation)

---

## Functional Requirements

### User Personas

#### Persona 1: Frontline Clinician

**Role**: Doctor, nurse, or allied health professional delivering direct care

**Goals**: Complete documentation faster; spend more time with patients; move between shared workstations without friction

**Frustrations**: Repeated authentication on shared devices; documentation burden; software that is unfit for purpose [NB-C3]

**Constraints**: Interrupted work; gloved hands; shared devices; no protected time for training beyond short units [NB-C12]

**Risk exposure**: Professionally accountable for content they sign, including content they did not author

#### Persona 2: Administrative and Operational Staff

**Role**: Clerical, booking, and operational support

**Goals**: Reduce repetitive workload; be recognised for higher-value work

**Frustrations**: High-volume repetitive tasks; uncertainty about what automation means for the role

**Constraints**: Process-bound work with limited discretion

#### Persona 3: Clinical Safety Officer

**Role**: Named individual accountable under DCB0160

**Goals**: Identify hazards, verify controls, and defend the go-live judgement afterwards

**Frustrations**: Late engagement, when the only options are approve or delay; ambiguity over clinical scope

**Constraints**: Personal professional accountability that does not end when the programme does

#### Persona 4: Registration Authority Operator

**Role**: Issues Care Identities, assigns RBAC positions, controls authenticators [NB-C13]

**Goals**: Maintain attributable access; reduce repetitive unlock and reissue workload

**Frustrations**: Sharing behaviour that cannot be fixed by policy; migration workload without added capacity

#### Persona 5: Information Governance Manager

**Role**: Day-to-day IG operations, retention, and data loss prevention

**Goals**: Configuration that matches clinical schedules; evidence produced continuously

**Frustrations**: Product defaults that conflict with clinical record-keeping [NB-C14]

### Use Cases

#### UC-1: Clinician drafts clinical correspondence with AI assistance

**Actor**: Frontline Clinician

**Preconditions**: User enabled in an approved wave; trained; authenticated at the required assurance level

**Main flow**:

1. Clinician requests assistance drafting correspondence from consultation notes
2. System generates draft content, visually and structurally labelled as generated
3. Clinician reviews, edits, and explicitly accepts or rejects
4. On acceptance, content enters the record attributed to the clinician
5. System records generation, review, and acceptance with attribution

**Alternate flow**: Clinician identifies unreliable output and reports it via a non-punitive route; report is triaged into the hazard log

**Postconditions**: Record updated; audit trail sufficient to reconstruct what was proposed and what a human accepted

#### UC-2: Clinical Safety Officer gates a deployment wave

**Actor**: Clinical Safety Officer

**Preconditions**: Wave scope and intended-use statement defined

**Main flow**:

1. CSO reviews the hazard log for the wave scope
2. CSO verifies each hazard has a control and the control is implemented
3. CSO records approval or refusal against the wave
4. Deployment tooling permits enablement only where approval is recorded

**Alternate flow**: CSO refuses; wave enablement is blocked by the tooling, not by process alone

#### UC-3: Clinician authenticates on a shared clinical workstation

**Actor**: Frontline Clinician

**Main flow**:

1. Clinician presents a frictionless high-assurance authenticator
2. System authenticates against the national care identity service and retrieves national RBAC permissions
3. Session established at the assurance level required for the intended action

**Alternate flow**: Action requires a higher assurance level; system step-ups rather than denying

### Functional Requirements Detail

#### FR-001: Distinguishable labelling of generated content

**Description**: The system MUST present AI-generated content in a form visually and structurally distinguishable from human-authored content, at every point where it is displayed or exported.

**Relates To**: BR-003, UC-1

**Acceptance Criteria**:

- [ ] Given generated content is displayed, when a user views it, then it carries a persistent visual marker distinct from authored content
- [ ] Given generated content is exported or printed, when the output is inspected, then the marker persists
- [ ] Edge case: Given generated content is partially edited by a human, when displayed, then the provenance of the retained generated portion remains identifiable

**Data Requirements**:

- **Inputs**: Generated content, provenance metadata
- **Outputs**: Labelled content
- **Validations**: Provenance metadata present on all generated content

**Priority**: MUST_HAVE

**Complexity**: MEDIUM

**Dependencies**: FR-003

**Traces To**: PRIN 11 · STKE G-2, O-2

---

#### FR-002: Enforced human review before clinical record entry

**Description**: The system MUST require explicit human review and acceptance before any generated content enters the clinical record. Silent or default acceptance MUST NOT be possible.

**Relates To**: BR-003, UC-1

**Acceptance Criteria**:

- [ ] Given generated content, when a user attempts to commit it to the clinical record, then explicit acceptance is required
- [ ] Given a user takes no action, when a session times out, then content is not committed by default
- [ ] Edge case: Given bulk operations, when multiple items are generated, then acceptance is recorded per item, not per batch

**Data Requirements**:

- **Inputs**: Generated content, user acceptance action
- **Outputs**: Committed record content with attribution
- **Validations**: Acceptance event present for every committed generated item

**Priority**: MUST_HAVE

**Complexity**: MEDIUM

**Dependencies**: FR-001, FR-003

**Traces To**: PRIN 11 · STKE G-2, O-2

---

#### FR-003: Generation, review, and acceptance audit trail

**Description**: The system MUST record, for every AI-assisted interaction, what was generated, what was reviewed, what was accepted or rejected, and by which named individual — sufficient to reconstruct the interaction during a safety investigation.

**Relates To**: BR-003, BR-004, UC-1

**Acceptance Criteria**:

- [ ] Given any AI-assisted interaction, when the audit trail is queried, then generation, review, and acceptance events are retrievable with individual attribution
- [ ] Given a safety investigation, when a historic interaction is requested, then it is reconstructable within the applicable retention period
- [ ] Edge case: Given rejected content, when queried, then the rejection is recorded as evidence the control operated

**Data Requirements**:

- **Inputs**: Interaction events, authenticated identity
- **Outputs**: Immutable audit records (see DR-002)
- **Validations**: No interaction without an attributed identity

**Priority**: MUST_HAVE

**Complexity**: HIGH

**Dependencies**: FR-008, NFR-C-002

**Traces To**: PRIN 5, PRIN 11 · STKE O-2

---

#### FR-004: Intended-use boundary definition and drift detection

**Description**: The system MUST support definition of an approved intended-use boundary, and MUST detect and report use outside that boundary within one month of occurrence.

**Relates To**: BR-003, UC-2

**Acceptance Criteria**:

- [ ] Given a published intended-use statement, when usage is analysed, then out-of-boundary use is identified and reported
- [ ] Given an out-of-boundary detection, when reviewed, then median time from occurrence to detection is 30 days or fewer
- [ ] Edge case: Given ambiguous use, when detected, then it is escalated to the CCIO for classification rather than silently permitted

**Data Requirements**:

- **Inputs**: Usage telemetry at cohort level, intended-use definition
- **Outputs**: Drift detection reports
- **Validations**: Reporting operates at cohort level by default (see FR-006)

**Priority**: MUST_HAVE

**Complexity**: HIGH

**Dependencies**: FR-006

**Assumptions**: Telemetry granularity is sufficient to distinguish administrative from clinical use in practice — this assumption is untested and is carried as a risk

**Traces To**: PRIN 11 · STKE G-2, O-2

---

#### FR-005: Non-punitive reporting of unreliable output

**Description**: The system MUST provide a route for any user to report unreliable or unsafe generated output in two actions or fewer from the point of encounter, feeding directly into the hazard log.

**Relates To**: BR-003, UC-1

**Acceptance Criteria**:

- [ ] Given a user encounters unreliable output, when they report it, then the report reaches the hazard log without manager approval
- [ ] Given a report is submitted, when the reporter checks, then they can see it was received and triaged
- [ ] Edge case: Given a report indicates potential patient harm, when triaged, then it escalates to the Clinical Safety Officer immediately

**Data Requirements**:

- **Inputs**: User report, the generated content in question
- **Outputs**: Hazard log entry (see DR-004)
- **Validations**: Reporter identity recorded but not exposed to line management

**Priority**: MUST_HAVE

**Complexity**: LOW

**Dependencies**: FR-017

**Traces To**: PRIN 11 · STKE G-2, O-2

---

#### FR-006: Cohort-level usage reporting with restricted individual access

**Description**: The system MUST report usage at cohort level by default, and MUST technically restrict access to individual-level usage data to named roles under a documented authorisation process. Line managers MUST NOT have access to individual usage data.

**Relates To**: BR-005

**Acceptance Criteria**:

- [ ] Given a line manager account, when individual usage data is requested, then access is denied by technical control, not policy
- [ ] Given a named safety investigation, when individual data is required, then access is granted only under the documented authorisation process and is itself logged
- [ ] Edge case: Given a cohort small enough that individuals are identifiable, when reported, then the cohort is suppressed or aggregated further

**Data Requirements**:

- **Inputs**: Usage telemetry
- **Outputs**: Cohort-level reports
- **Validations**: Minimum cohort size enforced before reporting

**Priority**: MUST_HAVE

**Complexity**: MEDIUM

**Dependencies**: FR-004

**Traces To**: PRIN 5, PRIN 11 · STKE C-3, O-5

---

#### FR-007: Frictionless high-assurance authentication on shared workstations

**Description**: The system MUST support frictionless high-assurance authentication — biometrics and high-assurance passkeys — on shared clinical workstations, meeting the response target in NFR-P-001.

**Relates To**: BR-008, UC-3

**Acceptance Criteria**:

- [ ] Given a shared clinical workstation, when a clinician authenticates using a frictionless authenticator, then session establishment completes within the NFR-P-001 target
- [ ] Given a clinician moves between workstations, when they authenticate at the second, then no credential re-enrolment is required
- [ ] Edge case: Given the frictionless authenticator is unavailable, when the clinician authenticates, then a fallback method at equivalent assurance is offered rather than a shared credential

**Data Requirements**:

- **Inputs**: Authenticator presentation
- **Outputs**: Authenticated session with assurance level asserted
- **Validations**: Assurance level recorded on every session

**Priority**: MUST_HAVE

**Complexity**: HIGH

**Dependencies**: INT-001, NFR-SEC-001

**Traces To**: PRIN 12 · STKE G-7, O-4

---

#### FR-008: Federated authentication to the national care identity service

**Description**: The system MUST authenticate users by federating to the national care identity service rather than maintaining local credentials, and MUST retrieve national RBAC permissions as part of the authentication flow.

**Relates To**: BR-008, UC-3

**Acceptance Criteria**:

- [ ] Given a user signs in, when authentication completes, then identity and national RBAC roles are obtained from the national service
- [ ] Given the national service is unavailable, when a user signs in, then the failure is explicit and no local credential fallback grants clinical access
- [ ] Edge case: Given a user's RBAC position changes centrally, when they next authenticate, then the updated permissions apply

**Data Requirements**:

- **Inputs**: Federated identity assertion
- **Outputs**: Session with identity claims, unique user identifier, and RBAC roles (see DR-001)
- **Validations**: Token handling conforms to NFR-SEC-005

**Priority**: MUST_HAVE

**Complexity**: HIGH

**Dependencies**: INT-001

**Traces To**: PRIN 12 · STKE G-7

---

#### FR-009: Automated joiner-mover-leaver lifecycle

**Description**: The system MUST grant and revoke access automatically as a person joins, changes role, or leaves, with revocation on leaving taking effect immediately.

**Relates To**: BR-008

**Acceptance Criteria**:

- [ ] Given a user is marked as a leaver, when the next access attempt occurs, then access is denied immediately
- [ ] Given a user changes role, when the change is recorded, then entitlements update without manual intervention
- [ ] Edge case: Given a leaver's data must be retained, when access is revoked, then data is retained for the defined period without the account remaining active

**Data Requirements**:

- **Inputs**: Authoritative workforce record changes
- **Outputs**: Entitlement changes, audit record
- **Validations**: No orphaned accounts after the reconciliation cycle

**Priority**: MUST_HAVE

**Complexity**: MEDIUM

**Dependencies**: INT-002

**Traces To**: PRIN 12 · STKE G-7 · [NB-C15]

---

#### FR-010: Self-service authenticator management

**Description**: The system SHOULD allow users to self-register and recover modern authenticators, including remote identity proofing and self-service unlock, reducing Registration Authority workload.

**Relates To**: BR-008

**Acceptance Criteria**:

- [ ] Given an enrolled user, when they need to add an authenticator, then they can self-serve without an RA appointment
- [ ] Given a locked credential, when the user requests unlock, then self-service unlock is available where assurance permits
- [ ] Edge case: Given identity proofing is required, when performed remotely, then it meets the applicable identity proofing standard

**Data Requirements**:

- **Inputs**: Identity proofing evidence
- **Outputs**: Enrolled authenticator, RA audit record
- **Validations**: Proofing standard satisfied before enrolment

**Priority**: SHOULD_HAVE

**Complexity**: MEDIUM

**Dependencies**: INT-001

**Traces To**: PRIN 12 · STKE G-7 · [NB-C16]

---

#### FR-011: Prevention of inappropriate identifier sharing

**Description**: The system MUST detect and block sharing of patient identifiers in collaborative channels where the sharing is outside an approved direct-care purpose, without obstructing legitimate direct-care sharing.

**Relates To**: BR-004

**Acceptance Criteria**:

- [ ] Given a user attempts to share patient identifiers into an unapproved channel, when the action is submitted, then it is blocked and the user is told why
- [ ] Given a legitimate direct-care sharing action, when performed, then it succeeds without obstruction
- [ ] Edge case: Given a false positive block, when reported, then the rule is reviewed within a defined period

**Data Requirements**:

- **Inputs**: Message and file content, channel classification
- **Outputs**: Block or allow decision, policy violation record
- **Validations**: False-positive rate tracked and reviewed

**Priority**: MUST_HAVE

**Complexity**: HIGH

**Dependencies**: DR-003

**Traces To**: PRIN 7 · STKE G-6, O-3 · [NB-C17]

---

#### FR-012: Explicit retention configuration per workspace

**Description**: The system MUST apply retention configured against a named retention schedule for every workspace, replacing product defaults. No workspace may remain on default retention once in clinical use.

**Relates To**: BR-004

**Acceptance Criteria**:

- [ ] Given any workspace in clinical use, when configuration is audited, then retention is set against a named schedule
- [ ] Given clinical consultation content, when retention is applied, then the period matches the clinical record schedule, commonly six years
- [ ] Edge case: Given administrative content in a clinical workspace, when retained, then a shorter administrative period may apply where the schedule permits

**Data Requirements**:

- **Inputs**: Retention schedule register, workspace classification
- **Outputs**: Applied retention policy, configuration audit record
- **Validations**: Zero workspaces on product default

**Priority**: MUST_HAVE

**Complexity**: MEDIUM

**Dependencies**: DR-003

**Traces To**: PRIN 6 · STKE G-6, O-3 · [NB-C14]

---

#### FR-013: Role-assigned microlearning inside existing tools

**Description**: The system MUST deliver role-assigned learning in units of 15 minutes or fewer, inside the tools staff already use, without a separate login.

**Relates To**: BR-005

**Acceptance Criteria**:

- [ ] Given a user is enabled, when learning is assigned, then assignment is automatic based on role or specialty
- [ ] Given a user accesses learning, when they do so, then no separate authentication is required
- [ ] Edge case: Given a user changes role, when the change is recorded, then learning assignment updates accordingly

**Data Requirements**:

- **Inputs**: Role and specialty from the workforce record
- **Outputs**: Assigned learning, completion and competence records (see DR-006)
- **Validations**: Records remain within the organisation's security boundary

**Priority**: MUST_HAVE

**Complexity**: MEDIUM

**Dependencies**: INT-004

**Traces To**: STKE G-8, O-5 · [NB-C12]

---

#### FR-014: Competence assessment rather than completion tracking

**Description**: The system MUST assess demonstrated competence — including correct statement of the intended-use boundary and recognition of failure modes — rather than recording module completion alone.

**Relates To**: BR-003, BR-005

**Acceptance Criteria**:

- [ ] Given a user completes learning, when assessed, then competence is evidenced by applied task or assessment, not by completion flag
- [ ] Given the cohort is surveyed, when results are analysed, then 85% or more demonstrate competence within 60 days of enablement
- [ ] Edge case: Given a user fails assessment, when they retry, then targeted remediation is offered rather than module repetition

**Data Requirements**:

- **Inputs**: Assessment responses, applied task observation
- **Outputs**: Competence record (see DR-006)
- **Validations**: Completion alone cannot satisfy the competence flag

**Priority**: SHOULD_HAVE

**Complexity**: MEDIUM

**Dependencies**: FR-013

**Traces To**: STKE G-8, G-2 · PRIN 11

---

#### FR-015: Pre-enablement baseline capture

**Description**: The system and process MUST capture an administrative time baseline for each role cohort before any user in that cohort is enabled.

**Relates To**: BR-002

**Acceptance Criteria**:

- [ ] Given a cohort is scheduled for enablement, when enablement is attempted without a recorded baseline, then enablement is blocked or an explicit exception is recorded
- [ ] Given a baseline is captured, when reviewed, then it uses the agreed method and is comparable across cohorts
- [ ] Edge case: Given a cohort is enabled under exception, when reported, then the missing baseline is disclosed in benefit reporting rather than estimated

**Data Requirements**:

- **Inputs**: Time-and-motion sampling, diary study responses
- **Outputs**: Baseline record (see DR-005)
- **Validations**: Method consistent across cohorts to permit aggregation

**Priority**: MUST_HAVE

**Complexity**: LOW

**Dependencies**: BR-005 (telemetry agreement must precede measurement)

**Traces To**: STKE G-3, O-1

---

#### FR-016: Benefit reporting by cohort and licence tier

**Description**: The system MUST report measured administrative time change quarterly, disaggregated by role cohort and licence tier, with platform telemetry used only as a corroborating signal.

**Relates To**: BR-002, BR-006

**Acceptance Criteria**:

- [ ] Given a reporting period ends, when the report is produced, then results are disaggregated by cohort and tier
- [ ] Given telemetry and survey data disagree, when reported, then both are shown rather than the more favourable one alone
- [ ] Edge case: Given a cohort has no baseline, when reported, then it is excluded from benefit claims and the exclusion is stated

**Data Requirements**:

- **Inputs**: Baseline and follow-up measurements, licence register
- **Outputs**: Quarterly benefit report (see DR-005)
- **Validations**: Cohort suppression applied per FR-006

**Priority**: MUST_HAVE

**Complexity**: MEDIUM

**Dependencies**: FR-015

**Traces To**: STKE G-3, O-1, O-6

---

#### FR-017: Hazard log management

**Description**: The system MUST maintain a hazard log recording each identified hazard, its severity and likelihood assessment, its control, and verification that the control operates — maintained across the lifecycle rather than produced once.

**Relates To**: BR-003, UC-2

**Acceptance Criteria**:

- [ ] Given a hazard is identified, when recorded, then severity, likelihood, control, and verification status are captured
- [ ] Given a material change to the system, when assessed, then affected hazards are flagged for reassessment
- [ ] Edge case: Given a hazard has no verified control, when a wave depends on it, then the wave cannot be approved

**Data Requirements**:

- **Inputs**: Hazard identification from assessment, incidents, and FR-005 reports
- **Outputs**: Hazard log entries (see DR-004)
- **Validations**: Every hazard has an owner and a verification status

**Priority**: MUST_HAVE

**Complexity**: MEDIUM

**Dependencies**: FR-005, INT-005

**Traces To**: PRIN 10 · STKE G-1, O-2 · [NB-C4]

---

#### FR-018: Gate-enforced deployment wave management

**Description**: The deployment tooling MUST prevent user enablement for any wave lacking recorded Clinical Safety Officer approval and SIRO risk acceptance. The gate MUST be a technical control, not a process step.

**Relates To**: BR-001, UC-2

**Acceptance Criteria**:

- [ ] Given a wave without CSO approval, when enablement is attempted, then it is technically blocked
- [ ] Given a wave without SIRO acceptance, when enablement is attempted, then it is technically blocked
- [ ] Edge case: Given an override is exercised, when it occurs, then it requires named executive authorisation and is logged immutably for board reporting

**Data Requirements**:

- **Inputs**: Approval records, wave definition
- **Outputs**: Enablement authorisation, override audit record
- **Validations**: No enablement path bypasses the gate

**Priority**: MUST_HAVE

**Complexity**: MEDIUM

**Dependencies**: FR-017

**Traces To**: PRIN 10, PRIN 21 · STKE G-1, O-2

---

## Non-Functional Requirements (NFRs)

### Performance Requirements

#### NFR-P-001: Response Time

**Requirement**: Interactive operations must complete within targets set against the clinical context of use.

- Authentication on shared clinical workstations: < 5 seconds from authenticator presentation to usable session (95th percentile)
- AI assistance first response: < 5 seconds (95th percentile)
- Clinical record retrieval: < 3 seconds (95th percentile)

**Measurement Method**: Synthetic transaction monitoring plus timed observation on representative shared workstations

**Load Conditions**:

- Peak load: shift-change concurrency, where a large proportion of ward staff authenticate within a short window
- Data volume: audit records scaling with interaction volume (see NFR-S-002)

**Rationale**: Latency in a clinical workflow consumes clinical time and drives staff toward workarounds [NB-C18]. Authentication speed is the specific friction that produces credential sharing (BR-008).

**Priority**: HIGH

**Traces To**: PRIN 15 · STKE G-7

---

#### NFR-P-002: Throughput

**Requirement**: The platform must sustain peak-period interaction volume for the enabled population without degradation, and must scale to three times the initial enabled population without architectural change.

**Measurement Method**: Load testing at projected peak before each wave; production monitoring thereafter

**Rationale**: National rollout moves from pilot to hundreds of thousands of users within months [NB-C1].

**Priority**: HIGH

**Traces To**: PRIN 1, PRIN 15

---

### Availability and Resilience Requirements

#### NFR-A-001: Availability Target

**Requirement**: Availability targets must be derived from clinical criticality and recorded per service, not set uniformly.

- Identity and authentication services: 99.9% or better, reflecting that dependent clinical systems cannot function without them
- Collaboration and AI assistance: 99.5% or better
- Reporting and analytics: 99.0% or better

**Measurement Method**: Service monitoring against agreed measurement windows; supplier SLA reporting

**Rationale**: A service cannot exceed the availability of what it depends on, and criticality must cascade from clinical impact rather than convenience.

**Priority**: CRITICAL

**Traces To**: PRIN 16 · [NB-C19]

---

#### NFR-A-002: Disaster Recovery

**Requirement**: Recovery Time Objective and Recovery Point Objective must be defined per service and validated by test at least annually.

- Identity services: RTO 1 hour, RPO 15 minutes
- Clinical content: RTO 4 hours, RPO 15 minutes
- Audit and hazard records: RPO zero — no acceptable loss

**Measurement Method**: Annual disaster recovery exercise with documented results

**Rationale**: Audit and hazard records are the evidence base for safety investigation; their loss is not recoverable by any other means.

**Priority**: CRITICAL

**Traces To**: PRIN 2, PRIN 16

---

#### NFR-A-003: Fault Tolerance and Clinical Fallback

**Requirement**: Every clinically significant workflow must have a documented and rehearsed fallback for the period the system is unavailable. Degraded modes must be visible to the user, never silent.

**Measurement Method**: Fallback documented per workflow; rehearsal recorded at least annually

**Rationale**: A system that fails silently or presents incomplete information is more dangerous than one that fails visibly and hands control back to the clinician.

**Priority**: CRITICAL

**Traces To**: PRIN 2, PRIN 16

---

### Scalability Requirements

#### NFR-S-001: Horizontal Scaling

**Requirement**: All components must scale horizontally to the full enabled population without architectural change, sized for peak clinical periods rather than annual averages.

**Measurement Method**: Load testing at 3x current enabled population

**Rationale**: The national target is approximately 505,000 staff [NB-C1]; local scaling must not be the constraint on wave cadence.

**Priority**: HIGH

**Traces To**: PRIN 1

---

#### NFR-S-002: Data Volume Scaling

**Requirement**: Audit, hazard, and competence stores must scale to retain records for the full applicable retention period at projected interaction volumes, without degrading query performance for safety investigation.

**Measurement Method**: Volume projection reviewed quarterly; query performance tested at projected Year 3 volume

**Rationale**: Audit retention is bounded by clinical record retention, commonly six years [NB-C14], not by convenience.

**Priority**: HIGH

**Traces To**: PRIN 1, PRIN 6

---

### Security Requirements

#### NFR-SEC-001: Authentication

**Requirement**: Authentication assurance must be matched to the sensitivity of the action rather than applied uniformly to the system.

- Highest assurance required for the most sensitive actions, including prescribing and primary clinical record modification
- High assurance sufficient for routine access
- Multi-factor authentication for all human access
- Step-up authentication where an action exceeds the current session's assurance level

**Measurement Method**: Assurance level mapped per action class and reviewed; session assurance recorded and auditable

**Rationale**: Tiered assurance is the stated model [NB-C20]. Uniform high assurance produces friction that drives credential sharing (BR-008); uniform low assurance is unacceptable for prescribing.

**Priority**: CRITICAL

**Traces To**: PRIN 12 · STKE G-7

---

#### NFR-SEC-002: Authorization

**Requirement**: Authorisation must use national role-based access control positions retrieved at authentication, applying least privilege, with local elevation time-boxed and audited.

**Measurement Method**: Entitlement review quarterly; privileged access audit continuous

**Rationale**: National RBAC is the authoritative source for clinical entitlement [NB-C13]; local divergence creates unattributable access.

**Priority**: CRITICAL

**Traces To**: PRIN 4, PRIN 12

---

#### NFR-SEC-003: Data Encryption

**Requirement**: All data must be encrypted at rest and in transit using current recognised standards, with key management separated from data custody.

**Measurement Method**: Configuration audit; annual penetration testing

**Rationale**: Encryption everywhere is a zero-trust pillar and a non-negotiable control.

**Priority**: CRITICAL

**Traces To**: PRIN 4

---

#### NFR-SEC-004: Secrets and Non-Human Authentication

**Requirement**: Secrets must be held in a managed secret store and never in code or configuration. Automated and non-human actors must authenticate to a recognised secure standard rather than with static shared credentials.

**Measurement Method**: Secret scanning in pipelines; inventory of non-human accounts reviewed quarterly

**Rationale**: Automated systems must follow secure robot authentication standards rather than relying on static credentials [NB-C11].

**Priority**: CRITICAL

**Traces To**: PRIN 4, PRIN 12

---

#### NFR-SEC-005: Token Handling and Vulnerability Management

**Requirement**: Federated authentication must use the authorization code flow with proof key for code exchange, with tokens held server-side and never resident in the browser. Vulnerabilities must be remediated within severity-based timeframes.

- Critical vulnerabilities: remediated within 7 days
- High: within 30 days
- Dependency scanning: continuous, not only at build

**Measurement Method**: Architecture review against the pattern; vulnerability management reporting

**Rationale**: The recommended cryptographic pathway is the authorization code flow with PKCE, and architects are strongly advised to implement a backend-for-frontend pattern so tokens never reside in the browser, mitigating cross-site scripting and token theft [NB-C21]. The sector's exposure to unpatched systems is well established [NB-C22].

**Priority**: CRITICAL

**Traces To**: PRIN 4, PRIN 12

---

### Compliance and Regulatory Requirements

#### NFR-C-001: Data Privacy Compliance

**Requirement**: Processing must comply with UK GDPR and the Data Protection Act 2018. A Data Protection Impact Assessment must be completed and SIRO risk acceptance recorded before each wave. Personal and clinical data must remain within the UK.

**Measurement Method**: DPIA completion record; residency position documented and reconfirmed on supplier change

**Rationale**: Keeping data within the organisation's own tenancy simplifies governance and supports UK data residency requirements [NB-C23].

**Priority**: CRITICAL

**Traces To**: PRIN 6, PRIN 7 · STKE G-5

---

#### NFR-C-002: Audit Logging

**Requirement**: All access to personal and clinical data, and all AI generation and acceptance events, must be logged with individual attribution and retained for not less than the applicable clinical record retention period.

**Measurement Method**: Log completeness testing; retention configuration audit

**Rationale**: Telemetry is the evidence base for information governance investigation and patient safety incident review, not only for operations.

**Priority**: CRITICAL

**Traces To**: PRIN 5 · STKE O-2, O-3

---

#### NFR-C-003: Regulatory Reporting and Security Assurance

**Requirement**: The organisation must achieve Data Security and Protection Toolkit "Standards Met" with the collaboration and AI capability in assessed scope, aligned to the NCSC Cyber Assessment Framework, with 60% or more of assertions supported by automated evidence capture.

**Measurement Method**: DSPT submission record; evidence automation coverage reported quarterly

**Rationale**: Compliance is demonstrated primarily through the DSPT, aligned with the Cyber Assessment Framework [NB-C7].

**Priority**: CRITICAL

**Traces To**: PRIN 4 · STKE G-5, O-3

---

#### NFR-C-004: Clinical Risk Management

**Requirement**: Any deployment capable of influencing clinical decision-making, care delivery, or the clinical record must comply with DCB0129 and DCB0160, with a named Clinical Safety Officer, a maintained hazard log, and an approved clinical safety case before go-live. The Software as a Medical Device determination must be recorded for each deployment.

**Measurement Method**: Clinical safety case approval record per wave; SaMD determination recorded

**Rationale**: DCB0160 requires the CSO to reduce residual risk to as low as reasonably practicable before systems go live [NB-C4]. The national classification as an administrative productivity tool rather than Software as a Medical Device [NB-C5] must be re-evaluated locally if intended use differs.

**Priority**: CRITICAL

**Traces To**: PRIN 10 · STKE G-1, O-2

---

#### NFR-C-005: Confidentiality and Caldicott Compliance

**Requirement**: Every use of patient identifiable information must have a documented purpose and lawful basis, use the minimum necessary identifiable data, and be reviewed by the Caldicott Guardian. Controls must not obstruct information sharing required for direct care.

**Measurement Method**: Purpose and lawful basis register; false-positive rate on sharing controls reviewed quarterly

**Rationale**: All solutions must meet the Data Security and Protection Toolkit and Caldicott principles [NB-C17]. The duty to share for direct care carries equal weight with the duty to protect.

**Priority**: CRITICAL

**Traces To**: PRIN 7 · STKE G-6, O-3

---

### Usability Requirements

#### NFR-U-001: User Experience

**Requirement**: Approved tooling must be measurably faster than the workaround it replaces for the target task, measured by timed task comparison before wave enablement.

**Measurement Method**: Timed task comparison against current practice; post-enablement user satisfaction survey

**Rationale**: Where official systems frustrate staff, they adopt unofficial tools [NB-C18]. Usability is therefore a security control, not a preference.

**Priority**: HIGH

**Traces To**: PRIN 15, PRIN 18 · STKE O-5

---

#### NFR-U-002: Accessibility

**Requirement**: All user-facing interfaces must meet WCAG 2.2 Level AA, with an accessibility statement published and maintained, and testing performed with assistive technologies and with users who have access needs.

**Measurement Method**: Automated accessibility testing in the pipeline; periodic manual audit with assistive technology users

**Rationale**: Public sector bodies are legally obliged to meet accessibility requirements under the Public Sector Bodies (Websites and Mobile Applications) Accessibility Regulations 2018.

**Priority**: MUST_HAVE

**Traces To**: PRIN 18

---

#### NFR-U-003: Clinical Environment and Inclusion

**Requirement**: Interfaces must remain usable under clinical environment constraints — gloved hands, shared devices, poor lighting, and frequent interruption — and design must account for variation in digital confidence among staff.

**Measurement Method**: Usability testing in representative clinical environments, not in an office

**Rationale**: Equity risk is a recognised pitfall of digital transformation [NB-C8]; a tool usable only by confident users on modern devices excludes the staff who most need it.

**Priority**: SHOULD_HAVE

**Traces To**: PRIN 18

---

### Maintainability and Supportability Requirements

#### NFR-M-001: Observability

**Requirement**: All components must emit structured logs with correlation identifiers, metrics covering volume, latency percentiles and error rates, and distributed traces. Operational telemetry must be separated from audit records, which carry different retention and access rules. Personal and clinical data must not appear in operational logs.

**Measurement Method**: Instrumentation coverage review; log content scanning for personal data

**Rationale**: We cannot operate what we cannot observe, and we cannot investigate what we did not record.

**Priority**: HIGH

**Traces To**: PRIN 5

---

#### NFR-M-002: Documentation and Configuration as Code

**Requirement**: Architecture documentation must be current, significant decisions recorded as Architecture Decision Records, and all infrastructure, security, and retention configuration held as code so that deviation is visible in review rather than discovered in audit.

**Measurement Method**: Configuration drift detection; ADR coverage of significant decisions

**Rationale**: Manual changes create drift and undocumented state; in a governed environment, configuration as code also produces the change evidence assurance regimes require.

**Priority**: HIGH

**Traces To**: PRIN 17, PRIN 19

---

#### NFR-M-003: Operational Runbooks

**Requirement**: Runbooks must exist for common failure scenarios, for the clinical fallback in NFR-A-003, and for the support surge expected at each wave enablement.

**Measurement Method**: Runbook coverage reviewed before each wave; incident post-mortems reference runbook adequacy

**Rationale**: Wave-based enablement creates a predictable support surge that the service desk has flagged as an unfunded pressure.

**Priority**: SHOULD_HAVE

**Traces To**: PRIN 5, PRIN 17

---

### Portability and Interoperability Requirements

#### NFR-I-001: API Standards

**Requirement**: All interfaces must use open, documented protocols with published machine-readable specifications, versioning, and a backward-compatibility strategy. Direct database access across system boundaries is prohibited.

**Measurement Method**: Interface specification review at architecture gate

**Rationale**: Loose coupling through standard interfaces protects against lock-in across an estate spanning many organisations and tenancy models.

**Priority**: HIGH

**Traces To**: PRIN 3, PRIN 13

---

#### NFR-I-002: Integration Capabilities

**Requirement**: Integration with clinical systems must use recognised health interoperability standards, and must handle cross-border divergence within the UK explicitly rather than assuming a single identifier or network model.

**Measurement Method**: Integration design review; cross-border handling documented where applicable

**Rationale**: Cross-border differences — for example Scotland's CHI identifier and network model versus England's NHS Number and internet-first model — require careful handling for interoperability [NB-C11].

**Priority**: HIGH

**Traces To**: PRIN 3

---

#### NFR-I-003: Data Portability and Exit

**Requirement**: The organisation must be able to export its data — including audit, hazard, and competence records — in a documented, non-proprietary format, and an exit plan must exist before contract signature.

**Measurement Method**: Export tested at least annually; exit plan reviewed at contract renewal

**Rationale**: Data portability is what makes the tenancy and supplier decisions reversible in principle; without it, BR-007 becomes irreversible in practice.

**Priority**: SHOULD_HAVE

**Traces To**: PRIN 3, PRIN 9

---

## Integration Requirements

### External System Integrations

#### INT-001: National Care Identity Service

**Purpose**: Authenticate staff and retrieve national role-based access permissions, avoiding local credential management for clinical access.

**Integration Type**: Real-time API — OpenID Connect identity provider

**Data Exchanged**:

- **From this system to the national service**: Authentication requests, per session
- **From the national service to this system**: Identity token, unique user identifier, profile data, national RBAC roles and permissions, per authentication

**Integration Pattern**: Request/response — authorization code flow with proof key for code exchange

**Authentication**: OpenID Connect, tokens held server-side per NFR-SEC-005

**Error Handling**: Explicit failure with no local credential fallback for clinical access; back-channel logout supported for session management

**SLA**: Aligned to the national service's platinum service level; local design must not add material latency (NFR-P-001)

**Owner**: NHS England Digital

**Priority**: CRITICAL

**Traces To**: FR-007, FR-008, FR-010 · PRIN 12 · [NB-C21]

---

#### INT-002: Directory Synchronisation and Workforce Record

**Purpose**: Automate the joiner-mover-leaver lifecycle so entitlements are granted and revoked promptly.

**Integration Type**: Scheduled synchronisation between on-premises directory and cloud identity

**Data Exchanged**:

- **From workforce record to identity**: Joiner, mover, and leaver events, continuously
- **From identity to workforce record**: Provisioning confirmation and exception reporting

**Integration Pattern**: Outbound-only connection; inbound firewall exceptions must not be required

**Authentication**: Service authentication per NFR-SEC-004

**Error Handling**: Failed synchronisation raises an alert; leaver revocation failures escalate immediately

**SLA**: Leaver revocation effective immediately on the next access attempt

**Owner**: Local IT and HR jointly

**Priority**: CRITICAL

**Traces To**: FR-009 · PRIN 12 · [NB-C15]

---

#### INT-003: Electronic Health Record Systems

**Purpose**: Allow clinical workflows to launch from and return context to the electronic health record without duplicate data entry.

**Integration Type**: Real-time API with context launch

**Data Exchanged**:

- **From EHR to this system**: Patient and encounter context, on launch
- **From this system to EHR**: Accepted content committed to the record, with generation provenance and human attribution

**Integration Pattern**: Request/response with context passing

**Authentication**: Federated identity per INT-001; no separate credential

**Error Handling**: Context launch failure must not permit unattributed record writes

**SLA**: Context launch within NFR-P-001 clinical record retrieval target

**Owner**: EHR supplier and local clinical systems team

**Priority**: HIGH

**Traces To**: FR-002, FR-003 · PRIN 3 · [NB-C24]

---

#### INT-004: Learning Platform

**Purpose**: Deliver and record role-assigned microlearning inside the tools staff already use.

**Integration Type**: Embedded application within the collaboration platform

**Data Exchanged**:

- **From workforce record to learning platform**: Role and specialty for auto-assignment
- **From learning platform to reporting**: Completion and competence records

**Integration Pattern**: Native integration, no separate login

**Authentication**: Federated single sign-on

**Error Handling**: Assignment failure raises an exception rather than silently omitting a user

**SLA**: Assignment within 24 hours of role change

**Owner**: Learning & Development, with supplier

**Priority**: MEDIUM

**Traces To**: FR-013, FR-014 · [NB-C12]

---

#### INT-005: Incident Reporting and Hazard Management

**Purpose**: Route reports of unreliable output into clinical risk management, and correlate them with reported patient safety incidents.

**Integration Type**: Event-driven

**Data Exchanged**:

- **From this system to hazard log**: Unreliable-output reports, immediately on submission
- **From incident reporting to hazard log**: Incidents flagged as potentially AI-related, continuously

**Integration Pattern**: Event publication with guaranteed delivery

**Authentication**: Service authentication per NFR-SEC-004

**Error Handling**: Undeliverable reports are queued, never dropped; reporter identity retained but shielded from line management per FR-006

**SLA**: Potential-harm reports reach the Clinical Safety Officer within 1 hour

**Owner**: Clinical governance

**Priority**: HIGH

**Traces To**: FR-005, FR-017 · PRIN 10

---

#### INT-006: National Shared Tenant Services

**Purpose**: Consume centrally managed identity, mail, and security baseline services where the shared tenancy model applies.

**Integration Type**: Consumption of managed platform services

**Data Exchanged**:

- **From national services to this organisation**: Security baselines, data loss prevention policy, mail routing
- **From this organisation to national services**: Configuration exceptions and local policy requests

**Integration Pattern**: Managed service consumption with documented local configuration boundaries

**Authentication**: Federated per INT-001

**Error Handling**: Central policy change affecting local clinical workflow must trigger review, not silent application

**SLA**: Per the national service agreement

**Owner**: NHS Digital and delivery partners

**Priority**: HIGH — becomes CRITICAL if the shared tenancy model is confirmed under BR-007

**Traces To**: BR-007 · [NB-C25]

---

## Data Requirements

### Data Entities

#### DR-001: Care Identity and Access Record

**Description**: The identity, authenticators, and national RBAC entitlements associated with a member of staff.

**Attributes**:

| Attribute | Type | Required | Description | Constraints |
|-----------|------|----------|-------------|-------------|
| user_uuid | UUID | Yes | National unique user identifier | Primary key, sourced from national service |
| profile_data | Object | Yes | Basic identity profile | Sourced from national service, not locally editable |
| rbac_roles | Array | Yes | National role-based access positions | Retrieved at authentication |
| authenticators | Array | Yes | Enrolled authenticators and assurance level | At least one high-assurance method |
| assurance_level | Enum | Yes | Assurance level of current session | ['high', 'very_high'] |
| lifecycle_status | Enum | Yes | Joiner-mover-leaver state | ['active', 'changed', 'leaver'] |
| revoked_at | Timestamp | No | Revocation timestamp | Set immediately on leaver |

**Relationships**: One-to-many with DR-002 (generation records) and DR-006 (competence records) via `user_uuid`

**Data Volume**: Scales with enabled population; national service supports more than 1.3 million workers [NB-C13]

**Access Patterns**: Read at every authentication; written on lifecycle change

**Data Classification**: CONFIDENTIAL

**Data Retention**: Retained per workforce record schedule; access revoked immediately on leaver, data retained for the defined period [NB-C15]

**Rationale**: Attributable identity is the precondition for every other control in this document; without it, audit, investigation, and non-repudiation all fail.

**Priority**: MUST_HAVE

**Traces To**: FR-008, FR-009 · PRIN 12 · STKE G-7, O-4

---

#### DR-002: AI Generation and Acceptance Record

**Description**: The immutable record of what was generated, what a human reviewed, and what was accepted or rejected.

**Attributes**:

| Attribute | Type | Required | Description | Constraints |
|-----------|------|----------|-------------|-------------|
| record_id | UUID | Yes | Unique identifier | Primary key |
| user_uuid | UUID | Yes | Attributed individual | Foreign key to DR-001, never null |
| generated_at | Timestamp | Yes | Generation timestamp | Indexed |
| generated_content_ref | Reference | Yes | Pointer to generated content | Immutable |
| review_outcome | Enum | Yes | Human decision | ['accepted', 'rejected', 'edited'] |
| accepted_at | Timestamp | No | Acceptance timestamp | Required where outcome is accepted or edited |
| intended_use_class | Enum | Yes | Use classification for drift analysis | ['administrative', 'flagged_for_review'] |

**Relationships**: Many-to-one with DR-001 via `user_uuid`; may relate to DR-004 where a hazard arises

**Data Volume**: Highest-volume entity — scales with interaction rate across the enabled population

**Access Patterns**: Write-heavy; read on safety investigation and drift analysis

**Data Classification**: RESTRICTED where content contains patient identifiable data

**Data Retention**: Not less than the applicable clinical record retention period, commonly six years for clinical consultations [NB-C14]

**Rationale**: This record is the evidence that the human-review control actually operated. It is the artefact a safety investigation or coroner would ask for.

**Priority**: MUST_HAVE

**Traces To**: FR-002, FR-003 · PRIN 11 · STKE G-2, O-2

---

#### DR-003: Clinical Collaboration Content

**Description**: Meeting, message, and file content in workspaces used for clinical purposes, including multidisciplinary team and consultation content.

**Attributes**:

| Attribute | Type | Required | Description | Constraints |
|-----------|------|----------|-------------|-------------|
| workspace_id | UUID | Yes | Workspace identifier | Primary key |
| content_class | Enum | Yes | Clinical or administrative | ['clinical_consultation', 'clinical_admin', 'corporate'] |
| retention_schedule | String | Yes | Named schedule applied | Not null; product default prohibited |
| retention_period | Duration | Yes | Applied retention | Six years for clinical consultations [NB-C14] |
| contains_pid | Boolean | Yes | Patient identifiable data present | Drives DLP policy selection |
| dlp_policy_id | Reference | Yes | Applied sharing control | Not null where contains_pid is true |

**Relationships**: One-to-many with policy violation records

**Data Volume**: Grows continuously; retention is the dominant sizing factor

**Access Patterns**: Read by participants; queried for legal hold and investigation

**Data Classification**: RESTRICTED where `contains_pid` is true, otherwise CONFIDENTIAL

**Data Retention**: Per named schedule — six years for clinical consultations, shorter for administrative content where the schedule permits [NB-C14]

**Rationale**: Retention and sharing controls attach to this entity; a workspace left on product default retention is the most common gap between a working platform and a compliant one.

**Priority**: MUST_HAVE

**Traces To**: FR-011, FR-012 · PRIN 6, PRIN 7 · STKE G-6, O-3

---

#### DR-004: Hazard Log Entry

**Description**: An identified clinical hazard, its assessment, control, and verification status.

**Attributes**:

| Attribute | Type | Required | Description | Constraints |
|-----------|------|----------|-------------|-------------|
| hazard_id | String | Yes | Unique hazard reference | Primary key |
| description | Text | Yes | Hazard description | Not null |
| severity | Enum | Yes | Clinical severity assessment | Per DCB0129 severity scale |
| likelihood | Enum | Yes | Likelihood assessment | Per DCB0129 likelihood scale |
| control | Text | Yes | Mitigating control | Not null |
| control_verified | Boolean | Yes | Control verified in operation | Wave approval blocked where false |
| owner | String | Yes | Accountable individual | Not null |
| residual_risk_accepted | Boolean | Yes | ALARP judgement recorded | Set by Clinical Safety Officer only |

**Relationships**: May relate to many DR-002 records; relates to deployment waves

**Data Volume**: Low volume, high criticality

**Access Patterns**: Read at every wave gate; written on identification and reassessment

**Data Classification**: OFFICIAL

**Data Retention**: Life of the system plus the applicable clinical record retention period — RPO zero per NFR-A-002

**Rationale**: The hazard log is the operative artefact of DCB0160 assurance and the record against which each wave gate is decided.

**Priority**: MUST_HAVE

**Traces To**: FR-017, FR-018 · PRIN 10 · STKE G-1, O-2

---

#### DR-005: Benefit Measurement Record

**Description**: Baseline and follow-up administrative time measurements by cohort and licence tier.

**Attributes**:

| Attribute | Type | Required | Description | Constraints |
|-----------|------|----------|-------------|-------------|
| measurement_id | UUID | Yes | Unique identifier | Primary key |
| cohort_id | String | Yes | Role cohort | Not null; minimum size enforced |
| licence_tier | Enum | Yes | Licence tier | ['standard', 'enhanced'] [NB-C9] |
| measurement_type | Enum | Yes | Baseline or follow-up | ['baseline', 'followup_3m', 'followup_6m', 'followup_12m'] |
| method | Enum | Yes | Measurement method | ['time_and_motion', 'diary_study', 'telemetry_corroboration'] |
| admin_minutes_per_day | Decimal | Yes | Measured value | Not null |
| captured_at | Timestamp | Yes | Capture date | Baseline must precede cohort enablement |

**Relationships**: Aggregated for reporting; joined to licence register

**Data Volume**: Low — one record per cohort per measurement point

**Access Patterns**: Written at measurement points; read quarterly for reporting

**Data Classification**: INTERNAL — cohort level only; individual data governed by FR-006

**Data Retention**: Life of the programme plus 3 years for benefit audit

**Rationale**: Without a baseline record captured before enablement, benefit becomes unprovable — and the window to capture it closes permanently at enablement.

**Priority**: MUST_HAVE

**Traces To**: FR-015, FR-016 · STKE G-3, O-1, O-6

---

#### DR-006: Learning and Competence Record

**Description**: Assigned learning, completion, and demonstrated competence per individual.

**Attributes**:

| Attribute | Type | Required | Description | Constraints |
|-----------|------|----------|-------------|-------------|
| record_id | UUID | Yes | Unique identifier | Primary key |
| user_uuid | UUID | Yes | Individual | Foreign key to DR-001 |
| module_id | String | Yes | Learning module | Not null |
| assigned_by_role | String | Yes | Role or specialty driving assignment | Auto-assigned |
| completed_at | Timestamp | No | Completion timestamp | Insufficient alone for competence |
| competence_demonstrated | Boolean | Yes | Applied competence evidenced | Defaults false; completion cannot set it |
| boundary_comprehension | Boolean | No | Correctly stated intended-use boundary | Feeds G-2 measurement |

**Relationships**: Many-to-one with DR-001

**Data Volume**: Scales with enabled population and module count

**Access Patterns**: Written on assessment; read for revalidation and compliance reporting

**Data Classification**: CONFIDENTIAL — staff personal data

**Data Retention**: Per workforce record and professional revalidation requirements

**Rationale**: Competence, not completion, is what evidences that staff understand the intended-use boundary and the failure modes of automated output.

**Priority**: SHOULD_HAVE

**Traces To**: FR-013, FR-014 · PRIN 11 · STKE G-8, O-5

---

### Data Quality Requirements

**Data Accuracy**: Validation enforced at the point of capture rather than downstream. Attribution fields (`user_uuid`) may never be null on DR-002 — an unattributable generation record is a control failure, not a data quality issue.

**Data Completeness**: Baseline records (DR-005) must exist for a cohort before enablement; a missing baseline is disclosed in reporting rather than estimated.

**Data Consistency**: National RBAC (DR-001) is authoritative; local entitlement stores are derived, read-only, and labelled as such.

**Data Timeliness**: Leaver revocation effective immediately; learning assignment within 24 hours of role change; drift detection within 30 days of occurrence.

**Data Lineage**: Provenance recorded for any dataset that grounds automated analysis; transformation logic version-controlled and reviewable.

---

### Data Migration Requirements

**Migration Scope**: Authenticator enrolment migration from existing smartcard-based credentials to frictionless high-assurance methods. No bulk clinical content migration is in scope.

**Migration Strategy**: Phased by clinical area, sequenced to match Registration Authority capacity rather than deployment wave cadence.

**Data Transformation**: None — enrolment is additive; existing credentials remain valid during transition.

**Data Validation**: Enrolment verified per user; sharing indicators measured before and after per area to evidence the BR-008 target.

**Rollback Plan**: Existing credentials remain functional throughout transition, so rollback is withdrawal of the new authenticator rather than restoration of data.

**Migration Timeline**: Per-area, gated on RA capacity; 12-month measurement window per area begins at area completion.

---

## Constraints and Assumptions

### Technical Constraints

- All new integrations with national clinical systems must use the current national care identity service; legacy authentication is not permitted [NB-C21]
- Shared tenancy imposes central configuration boundaries that local administrators cannot override, including data loss prevention policy and national security baselines [NB-C25]
- Legacy clinical systems requiring hybrid identity constrain the tenancy decision and must be inventoried before BR-007 can be answered
- Outbound-only connectivity is preferred; inbound firewall exceptions require explicit security approval [NB-C15]
- Cross-border differences in identifier and network model must be handled explicitly where services span the home nations [NB-C11]

### Business Constraints

- National target of approximately 505,000 staff by October 2026 [NB-C1]
- Programme funding envelope of £120 million nationally [NB-C1]
- Licence tiers are fixed by the national agreement; the organisation chooses assignment, not tier design [NB-C9]
- Clinical Safety Officer and SIRO hold blocking authority that programme escalation cannot override
- Registration Authority capacity constrains authenticator migration pace independently of deployment pace

### Assumptions

| ID | Assumption | Risk if false |
|----|-----------|---------------|
| A-1 | Telemetry granularity can distinguish administrative from clinical use | FR-004 cannot detect drift; BR-003 assurance weakens materially |
| A-2 | The pilot population's 43 minutes per day is an upper bound, not a forecast | Benefit reporting under-delivers against public expectation (see R-2 in STKE) |
| A-3 | Clinical Safety Officer capacity can be funded and recruited | BR-001 gate becomes the rate limiter on deployment |
| A-4 | Devices on shared clinical workstations support frictionless authenticators | BR-008 requires hardware refresh not currently funded |
| A-5 | Staff-side agreement on telemetry can be reached before first enablement | FR-004 and FR-006 blocked; deployment delayed (see Conflict C-3) |
| A-6 | The national service maintains its stated availability | NFR-A-001 for dependent services cannot be met |

---

## Success Criteria and KPIs

### Business Success Metrics

| KPI | Baseline | Target | Frequency | Traces To |
|-----|----------|--------|-----------|-----------|
| Administrative minutes saved per user per day | To be captured per cohort | Locally evidenced, honestly reported | Quarterly | BR-002, O-1 |
| AI-attributable patient safety incidents | Not applicable | Zero | Continuous | BR-003, O-2 |
| DSPT status with AI in scope | Maintained, AI out of scope | Standards Met, AI in scope | Annual | BR-004, O-3 |
| ICO-reportable breaches from the platform | Not applicable | Zero | Continuous | BR-004, O-3 |
| Credential-sharing indicators | To be measured | 80% reduction per area within 12 months | Monthly | BR-008, O-4 |
| Benefit reported per licence tier | Not measured | Quarterly report produced | Quarterly | BR-006, O-6 |

### Technical Success Metrics

| KPI | Target | Traces To |
|-----|--------|-----------|
| Waves gated on approved safety case before enablement | 100% | FR-018, NFR-C-004 |
| Workspaces with explicit retention configuration | 100% | FR-012, NFR-C-001 |
| Hazards with verified controls | 100% | FR-017 |
| DSPT assertions with automated evidence | 60% or more | NFR-C-003 |
| Median authentication time, shared workstations | < 5 seconds (95th percentile) | NFR-P-001 |
| Out-of-boundary use detection latency | 30 days or fewer | FR-004 |

### User Adoption Metrics

| KPI | Target | Traces To |
|-----|--------|-----------|
| Competence demonstrated within 60 days of enablement | 85% or more | FR-014 |
| Users able to state the intended-use boundary correctly | 80% or more | FR-014, G-2 |
| Cohorts with a valid pre-enablement baseline | 90% or more | FR-015 |
| Clinical champions recruited per 500 users | At least 2 | STKE G-8 |
| Voluntary adoption exceeding mandated enablement | Positive trend | O-5 |

---

## Dependencies and Risks

### Dependencies

| ID | Dependency | Owner | Impact if late |
|----|-----------|-------|----------------|
| D-1 | Clinical Safety Officer appointed and funded | Trust executive | BR-001 and BR-003 cannot proceed; all waves blocked |
| D-2 | Staff-side telemetry agreement concluded | Chief People Officer | FR-004, FR-006 blocked; deployment delayed |
| D-3 | Tenancy decision approved | CIO / CDIO | Dependent architecture work frozen (BR-007) |
| D-4 | Legacy clinical system inventory complete | Clinical systems team | BR-007 cannot be answered |
| D-5 | Registration Authority migration capacity funded | Trust executive | BR-008 timeline slips independently of deployment |
| D-6 | Retention schedule register agreed | Caldicott Guardian, records management | FR-012 cannot be configured |
| D-7 | Shared workstation device capability confirmed | IT Operations | FR-007 may require unfunded hardware refresh (A-4) |

### Risks

| ID | Risk | Probability | Impact | Mitigation | STKE Ref |
|----|------|-------------|--------|------------|----------|
| RQ-1 | Safety gate overridden by delivery pressure | MEDIUM | HIGH | Administrative-first scoping; technical gate in FR-018; override requires named executive authorisation | R-1 |
| RQ-2 | Local benefit materially below the pilot figure | HIGH | MEDIUM | Set expectation before measurement; report by cohort and tier so variance is explainable | R-2 |
| RQ-3 | Telemetry dispute halts deployment | MEDIUM | HIGH | Conclude agreement before enablement (D-2); technical restriction in FR-006 | R-3 |
| RQ-4 | Assurance and RA roles unfunded, becoming the bottleneck | HIGH | HIGH | Fund capacity explicitly (D-1, D-5); single integrated evidence pack | R-4 |
| RQ-5 | Drift detection cannot distinguish administrative from clinical use | MEDIUM | HIGH | Validate A-1 before relying on FR-004; fall back to sampling review if telemetry is insufficient | — |
| RQ-6 | Shadow AI adopted outside the assessed boundary | MEDIUM | HIGH | Treat usability as a security control (NFR-U-001); fast non-punitive capability request route | R-5 |
| RQ-7 | Baseline capture skipped under rollout pressure | HIGH | MEDIUM | Enablement blocked without baseline or recorded exception (FR-015) | R-2 |

---

## Requirement Conflicts & Resolutions

> Conflicts below originate from the stakeholder conflict analysis in `ARC-001-STKE-v1.0.md` and are restated here as requirement-level trade-offs.

### Conflict C-1: Delivery pace versus clinical assurance

**Conflicting Requirements**:

- **Requirement A**: BR-001 — deliver deployment in line with the October 2026 national target
- **Requirement B**: NFR-C-004 and FR-018 — every wave gated on an approved clinical safety case, technically enforced

**Stakeholders Involved**:

- **National Programme SRO** (STKE SD-1): Wants BR-001 because accountability for a £120 million national commitment attracts NAO and parliamentary scrutiny
- **Clinical Safety Officer** (SD-4): Wants NFR-C-004 because DCB0160 places personal, professionally registered accountability on the signature

**Nature of Conflict**: The date is fixed and the assurance work is not compressible without weakening it. Hazard assessment takes the time it takes; a safety case signed to meet a date is not a safety case.

**Trade-off Analysis**:

| Option | Pros | Cons | Impact |
|--------|------|------|--------|
| **Option 1**: Prioritise pace — enable on schedule, complete safety cases in parallel | ✅ Meets national target<br>✅ Benefit starts sooner | ❌ Deploys ahead of assurance<br>❌ CSO cannot sign; regulatory breach | SRO satisfied<br>CSO cannot participate |
| **Option 2**: Prioritise assurance — gate every wave, accept slippage | ✅ Full regulatory compliance<br>✅ CSO accountability intact | ❌ National target missed<br>❌ Organisation flagged as laggard | CSO satisfied<br>SRO exposed |
| **Option 3**: Phase by scope — administrative-only first at pace, clinical-adjacent gated separately | ✅ Both largely satisfied<br>✅ Lighter safety case moves fast | ❌ Requires a defensible boundary<br>❌ Two assurance tracks to run | Both largely satisfied |
| **Option 4**: Innovate — fund CSO capacity so assurance scales with rollout | ✅ Removes the bottleneck<br>✅ No standard weakened | ❌ Recruitment lead time<br>❌ Unbudgeted cost | Both satisfied if funded in time |

**Resolution Strategy**: PHASE, with elements of INNOVATE

**Decision**: Option 3 combined with Option 4. Deploy first to cohorts whose intended-use boundary excludes clinical workflows, which requires a lighter safety case and can move at national pace. Gate clinical-adjacent deployment separately on assurance rather than date. Fund Clinical Safety Officer capacity as a programme cost (D-1) so assurance scales rather than throttles.

**Rationale**: The conflict is between pace and *scope of assurance*, not between pace and safety as such. Splitting the scope preserves both the national contribution and the regulatory standard. The standard itself is not adjustable — DCB0160 is statutory guidance, not a programme preference.

**Decision Authority**: Trust Chief Executive, per the STKE RACI for go/no-go. Escalation to NHS England Programme SRO where local resolution fails. Note that escalation can change the schedule; it cannot change the CSO's answer.

**Impact on Requirements**:

- **Modified**: BR-001 success criteria now measure gate compliance, not enablement count alone
- **Added**: FR-018 makes the gate a technical control rather than a process step
- **Added**: FR-004 makes the administrative/clinical boundary observable, which Option 3 depends on
- **Deferred**: Clinical-scope AI deployment moved out of v1.0 scope entirely

**Stakeholder Management**:

- **National Programme SRO (lost some pace)**: Administrative-first still contributes materially to the national count. Any date-over-gate decision is escalated and minuted rather than absorbed silently.
- **Clinical Safety Officer (lost nothing on standard, gained workload)**: Capacity funded; engaged at design stage while options still exist.

**Future Consideration**: Clinical-scope deployment reassessed once the administrative deployment has 6 months of drift-detection data (FR-004) to evidence whether the boundary holds in practice.

---

### Conflict C-2: Licence cost control versus benefit capability

**Conflicting Requirements**:

- **Requirement A**: BR-006 — control recurring licence cost, favouring the Standard Service tier for frontline clinical staff
- **Requirement B**: BR-002 and NFR-U-001 — deliver and evidence time savings that may depend on capability present only in the Enhanced tier

**Stakeholders Involved**:

- **Director of Finance** (SD-9): Wants BR-006 because recurring per-user cost at scale is the dominant financial variable
- **Frontline clinicians** (SD-10) and **National Programme SRO** (SD-1): Want BR-002 because the benefit case — and the clinicians' experience — depends on capability actually delivering

**Nature of Conflict**: The Standard Service provides web-based applications, a 4 GB mailbox, and limited storage; the Enhanced Service adds larger mailboxes and stronger tooling [NB-C9]. Choosing the cheaper tier before benefit is measured risks a business case that cannot be realised at the tier purchased.

**Trade-off Analysis**:

| Option | Pros | Cons | Impact |
|--------|------|------|--------|
| **Option 1**: Standard tier for all frontline | ✅ Lowest recurring cost | ❌ Benefit may not materialise<br>❌ Business case unrealisable | Finance satisfied<br>SRO and clinicians exposed |
| **Option 2**: Enhanced tier for all | ✅ Maximum capability | ❌ Highest recurring cost<br>❌ Unjustifiable without evidence | Clinicians satisfied<br>Finance objects |
| **Option 3**: Mixed pilot, decide on evidence | ✅ Evidence-led<br>✅ No premature commitment | ❌ Delays the tier decision<br>❌ Two configurations to support | Both deferred but satisfied |
| **Option 4**: Standard now, upgrade on evidence | ✅ Low initial cost | ❌ Upgrade may be contractually hard<br>❌ Poor first impression damages adoption | Finance satisfied initially |

**Resolution Strategy**: COMPROMISE, deciding on evidence rather than on assumption

**Decision**: Option 3. Deploy a deliberately mixed-tier pilot across comparable cohorts, measure benefit per tier from wave 1 (FR-016), and defer any multi-year tier commitment until tier-level data exists. Retain the contractual ability to move users between tiers.

**Rationale**: Neither stakeholder has the evidence to win this argument today. The cost of a short deferral is far lower than the cost of a multi-year commitment to the wrong tier mix. Refusing to decide prematurely is the decision.

**Decision Authority**: Trust Chief Executive on recommendation from Director of Finance, per the STKE RACI for licence tier assignment.

**Impact on Requirements**:

- **Modified**: BR-006 priority set to SHOULD_HAVE for the reporting capability, but the underlying tier decision is explicitly deferred
- **Added**: FR-016 requires disaggregation by tier, which the original benefit reporting did not
- **Added**: DR-005 carries `licence_tier` as a required attribute so the analysis is possible at all

**Stakeholder Management**:

- **Director of Finance (deferred, not denied)**: Receives quarterly tier-level reporting they do not have today, which strengthens rather than weakens cost control.
- **Frontline clinicians (uncertainty retained)**: Mixed pilot means some cohorts get lower capability initially; this is communicated as a time-boxed evaluation, not a permanent decision.

**Future Consideration**: Tier mix reviewed at 6 and 12 months against DR-005 data. Any multi-year commitment made before that point is logged as a financial risk, not booked as a saving.

---

### Conflict C-3: Drift detection versus staff trust

**Conflicting Requirements**:

- **Requirement A**: FR-004 — detect use outside the intended-use boundary, which requires observing what staff actually do
- **Requirement B**: FR-006 and BR-005 — restrict individual-level usage data and secure staff-side agreement that telemetry is not punitive

**Stakeholders Involved**:

- **CCIO** (SD-2) and **Clinical Safety Officer** (SD-4): Want FR-004 because clinical drift is invisible without deliberate measurement
- **Staff-side representatives** (SD-11) and **frontline clinicians** (SD-10): Want FR-006 because usage telemetry is trivially repurposed for performance management

**Nature of Conflict**: Safety monitoring and surveillance use the same data. The distinction is entirely a matter of governance, access control, and trust — not of technology.

**Trade-off Analysis**:

| Option | Pros | Cons | Impact |
|--------|------|------|--------|
| **Option 1**: Full individual telemetry | ✅ Maximum drift visibility | ❌ Near-certain formal dispute<br>❌ Drives concealment, reducing real visibility | CCIO satisfied<br>Staff-side objects |
| **Option 2**: No usage telemetry | ✅ No trust concern | ❌ Drift undetectable<br>❌ BR-003 assurance fails | Staff-side satisfied<br>CSO cannot assure |
| **Option 3**: Cohort-level default, individual by authorised exception | ✅ Drift visible at population level<br>✅ Trust preserved | ❌ Slower to detect individual-level drift | Both largely satisfied |
| **Option 4**: Cohort-level plus voluntary self-reporting | ✅ Adds qualitative signal | ❌ Depends on reporting culture existing first | Both satisfied if culture holds |

**Resolution Strategy**: COMPROMISE, settled in writing before deployment

**Decision**: Option 3 with Option 4 as a supporting mechanism. Telemetry operates at cohort level by default with minimum cohort sizes enforced; individual-level access is technically restricted to named roles under a documented authorisation process, is itself logged, and is available only for a specific named safety investigation. Line managers have no access. FR-005 provides the voluntary reporting channel.

**Rationale**: This conflict is cheap to resolve before deployment and extremely expensive after the first grievance. Making the restriction technical rather than policy-based is what converts a promise into a control staff can verify.

**Decision Authority**: Trust Chief Executive, with staff-side agreement required, per the STKE RACI for telemetry use and access limits.

**Impact on Requirements**:

- **Modified**: FR-004 detection latency target relaxed to 30 days, reflecting cohort-level rather than real-time individual detection
- **Added**: FR-006 minimum cohort size and technical access restriction
- **Added**: D-2 made a hard dependency — no enablement before the agreement is concluded

**Stakeholder Management**:

- **CCIO (lost detection speed)**: Cohort-level detection is slower but sustainable; concealment driven by surveillance would produce worse visibility than the delay does.
- **Staff-side (gained enforceable limits)**: Restriction is technical and auditable, plus programme board representation.

**Future Consideration**: If A-1 proves false and cohort-level telemetry cannot distinguish administrative from clinical use (RQ-5), the fallback is periodic consented sampling review rather than expanding individual monitoring.

---

### Conflict C-4: Central standardisation versus local clinical integration

**Conflicting Requirements**:

- **Requirement A**: INT-006 and BR-007 — consume centrally managed baselines, gaining economies of scale and consistent security
- **Requirement B**: INT-003 and NFR-I-002 — integrate with legacy clinical systems that may require hybrid identity and exceed central constraints

**Stakeholders Involved**:

- **CIO / CDIO** (SD-8): Must choose, and owns the consequence either way
- **CISO** (SD-7) and **Clinical Safety Officer** (SD-4): Inherit materially different responsibilities depending on the answer

**Nature of Conflict**: The shared model delivers consistent data loss prevention and national security baselines [NB-C25]; the independent model offers flexibility with greater responsibility [NB-C10]. An organisation cannot have central simplicity and local freedom simultaneously.

**Trade-off Analysis**:

| Option | Pros | Cons | Impact |
|--------|------|------|--------|
| **Option 1**: Shared tenancy | ✅ Inherited baselines<br>✅ Lower management overhead | ❌ Legacy clinical integration may be infeasible | CISO satisfied<br>Clinical systems constrained |
| **Option 2**: Independent tenancy | ✅ Full integration freedom | ❌ All controls locally owned<br>❌ Requires governance capacity | Clinical systems satisfied<br>CISO and CSO exposed |
| **Option 3**: Shared with documented exceptions | ✅ Balance | ❌ Exception process becomes the bottleneck | Partial satisfaction |
| **Option 4**: Decide on evidence against the four stated factors | ✅ Defensible either way | ❌ Requires inventory work first | Correct by construction |

**Resolution Strategy**: PRIORITIZE evidence over preference

**Decision**: Option 4. Assess all four stated decision factors [NB-C10], complete the legacy clinical system inventory first (D-4), and approve the model and the governance capacity it demands in the same board paper. The decision itself is deferred; the *method* is not.

**Rationale**: Neither model is right in the abstract. The failure mode is not choosing wrongly — it is choosing by default, discovering the constraint later, and finding reversal expensive. Requiring responsibility and resource to be approved together prevents the specific failure of choosing autonomy without the capacity to discharge it.

**Decision Authority**: Trust Chief Executive on recommendation from CIO / CDIO, per the STKE RACI for tenancy model selection.

**Impact on Requirements**:

- **Modified**: INT-006 priority is conditional — HIGH, rising to CRITICAL if shared tenancy is confirmed
- **Added**: BR-007 success criteria require documented split of inherited versus locally owned controls
- **Blocked**: Dependent architecture work frozen until the decision record is approved (D-3)

**Stakeholder Management**:

- **CIO / CDIO**: Gains a defensible decision record rather than an inherited default.
- **CISO and Clinical Safety Officer**: Both see the control and governance implications before the decision, not after.

**Future Consideration**: Reassess if the national shared-tenant service materially changes its constraint model, or on acquisition or merger.

---

### Conflict C-5: Authentication assurance versus authentication speed

**Conflicting Requirements**:

- **Requirement A**: NFR-SEC-001 — assurance matched to action sensitivity, with the highest level for prescribing and record modification
- **Requirement B**: NFR-P-001 and FR-007 — authentication on shared clinical workstations within 5 seconds

**Stakeholders Involved**:

- **CISO** (SD-7) and **RA Manager** (SD-13): Want assurance because attribution underpins investigation
- **Frontline clinicians** (SD-10): Want speed because friction is what makes credential sharing rational

**Nature of Conflict**: Historically, higher assurance meant more friction, and more friction produced the sharing behaviour that destroyed attribution — the control defeating itself.

**Trade-off Analysis**:

| Option | Pros | Cons | Impact |
|--------|------|------|--------|
| **Option 1**: Uniform highest assurance | ✅ Maximum assurance on paper | ❌ Friction drives sharing<br>❌ Real attribution falls | Nobody satisfied in practice |
| **Option 2**: Uniform lower assurance | ✅ Fast | ❌ Unacceptable for prescribing | Clinicians satisfied<br>CISO objects |
| **Option 3**: Tiered assurance with step-up on sensitive action | ✅ Fast for routine<br>✅ High where it matters | ❌ Requires per-action classification | Both satisfied |
| **Option 4**: Frictionless high-assurance methods throughout | ✅ Removes the trade-off entirely | ❌ Device capability dependency (A-4) | Both satisfied if devices support it |

**Resolution Strategy**: INNOVATE — the trade-off is largely dissolvable

**Decision**: Option 3 combined with Option 4. Match assurance level to action sensitivity with step-up rather than uniform enforcement, and deploy frictionless high-assurance methods — biometrics and high-assurance passkeys — so that high assurance is not synonymous with high friction.

**Rationale**: This is the one conflict in the programme that is not a genuine trade-off. The source is explicit that the mitigation for sharing is expanding frictionless options rather than tightening policy [NB-C11]. Security and usability point the same direction here, which is why BR-008 should be sequenced early to build clinician goodwill for the harder changes.

**Decision Authority**: CISO with RA Manager, per the STKE RACI for authenticator migration approach.

**Impact on Requirements**:

- **Added**: NFR-SEC-001 step-up authentication requirement
- **Added**: FR-007 explicit fallback at equivalent assurance, preventing shared-credential fallback
- **Dependency**: D-7 device capability confirmation, since A-4 is the assumption this resolution rests on

**Stakeholder Management**:

- Both parties gain. The residual risk is A-4 — if shared workstation devices cannot support frictionless authenticators, this reverts to a real conflict requiring unfunded hardware refresh.

**Future Consideration**: If D-7 shows material device incapability, escalate as a funding decision rather than silently accepting friction and the sharing it causes.

---

## Timeline and Milestones

### High-Level Milestones

| Milestone | Target | Dependencies | Gate |
|-----------|--------|--------------|------|
| M1 — Clinical Safety Officer appointed and funded | Month 1 | D-1 | Prerequisite for all waves |
| M2 — Staff-side telemetry agreement concluded | Month 2 | D-2 | Prerequisite for first enablement |
| M3 — Tenancy decision approved | Month 2 | D-3, D-4 | Unblocks dependent architecture |
| M4 — Retention and DLP configured | Month 3 | D-6 | Prerequisite for clinical workspace use |
| M5 — Cohort baselines captured | Month 3 | FR-015 | Irrecoverable if missed |
| M6 — Wave 1 safety case approved, first enablement | Month 4 | M1, M2, M4, M5 | CSO and SIRO gate |
| M7 — Drift monitoring operational | Month 5 | M2, FR-004 | Prerequisite for wave 2 |
| M8 — Authenticator migration, first areas | Months 4–9 | D-5, D-7 | Paced by RA capacity |
| M9 — First tier-level benefit report | Month 6 | M5, FR-016 | Informs tier decision |
| M10 — DSPT submission with AI in scope | Per DSPT cycle | M4, NFR-C-003 | Annual assurance |
| M11 — National target contribution | October 2026 | All above | Subject to C-1 resolution |

---

## Budget

### Cost Estimate

Costs are not yet established for this organisation. The national programme envelope is £120 million for approximately 505,000 staff [NB-C1], but local cost depends on the tenancy decision (BR-007), the tier mix (BR-006), and the assurance capacity that Conflict C-1 requires to be funded.

| Cost Category | Status | Note |
|---------------|--------|------|
| Recurring licence cost | TO BE ESTABLISHED | Depends on tier mix; deliberately deferred pending FR-016 evidence |
| Clinical Safety Officer capacity | TO BE ESTABLISHED | Programme cost per Conflict C-1 resolution; D-1 |
| Registration Authority migration capacity | TO BE ESTABLISHED | Fixed-term uplift; D-5 |
| Shared workstation device capability | TO BE ESTABLISHED | Contingent on A-4 / D-7 assessment |
| Training and champion network | TO BE ESTABLISHED | Protected time is the dominant cost, not content |
| Benefit measurement | TO BE ESTABLISHED | Time-and-motion sampling has real staff cost |

> **Gap**: This section is the largest outstanding item in v1.0. It requires the tenancy decision (M3) and the tier evidence (M9) before it can be completed with integrity. Producing a figure now would be a guess presented as an estimate.

### Ongoing Operational Costs

To be established alongside the above. Note that released clinical time is capacity, not cash, and should not be booked as a recurring saving without an explicit establishment decision — see STKE O-1 and BR-005.

---

## Approval

### Requirements Review

| Reviewer | Role | Review Date | Status |
|----------|------|-------------|--------|
| Clinical Safety Officer | Clinical risk management | PENDING | PENDING — post appointment (D-1) |
| Caldicott Guardian | Confidentiality | PENDING | PENDING |
| Senior Information Risk Owner | Information risk | PENDING | PENDING |
| Chief Clinical Information Officer | Clinical design authority | PENDING | PENDING |
| Chief Information Security Officer | Security | PENDING | PENDING |
| Staff-side representatives | Staff representation | PENDING | PENDING — required before FR-004 and FR-006 |
| Director of Finance | Financial control | PENDING | PENDING |

### Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Executive Sponsor | PENDING | PENDING | PENDING |
| Clinical Safety Officer | PENDING | PENDING | PENDING |
| Senior Information Risk Owner | PENDING | PENDING | PENDING |
| Enterprise Architect | Mark Craddock | PENDING | PENDING |

---

## Appendices

### Appendix A: Glossary

| Term | Definition |
|------|------------|
| AAL | Authenticator Assurance Level — tiered authentication strength [NB-C20] |
| ALARP | As Low As Reasonably Practicable — the residual risk standard in DCB0160 |
| CAF | Cyber Assessment Framework — NCSC framework to which the DSPT is aligned [NB-C7] |
| Caldicott principles | Principles governing use of patient identifiable information |
| Clinical drift | Gradual migration of a tool from administrative into clinical use without reassessment [NB-C6] |
| CSO | Clinical Safety Officer — named accountable individual under DCB0160 [NB-C4] |
| DCB0129 / DCB0160 | Clinical risk management standards for health IT manufacturers and organisations |
| DLP | Data Loss Prevention — controls preventing inappropriate data sharing |
| DSPT | Data Security and Protection Toolkit — NHS information governance assurance [NB-C7] |
| Intended use | The approved scope of use against which clinical risk was assessed |
| PKCE | Proof Key for Code Exchange — protects the authorization code flow [NB-C21] |
| RA | Registration Authority — issues Care Identities and assigns RBAC positions [NB-C13] |
| RBAC | Role-Based Access Control — national permission model |
| SaMD | Software as a Medical Device — regulatory classification [NB-C5] |
| SIRO | Senior Information Risk Owner — accepts information risk at board level |

### Appendix B: Reference Documents

- `ARC-000-PRIN-v1.0.md` — NHS 365 Enterprise Architecture Principles (21 principles)
- `ARC-001-STKE-v1.0.md` — Stakeholder Drivers & Goals Analysis (16 drivers, 8 goals, 6 outcomes, 5 conflicts)
- *NHS 365 — A Best Practices Guide for Transforming UK Healthcare with Microsoft AI* — `projects/000-global/external/nhs365-book2.pdf`

### Appendix C: Wireframes and Mockups

None. Interface design is out of scope for this document; NFR-U-001 requires timed task comparison against current practice before wave enablement, which will drive interface decisions.

### Appendix D: Data Models

Entity definitions are in the Data Requirements section (DR-001 to DR-006). A full data model with relationships, cardinality, and GDPR mapping should be produced by `/arckit:data-model`.

---

## External References

> This section provides traceability from generated content back to source documents.

### Document Register

| Doc ID | Filename | Type | Source Location | Description |
|--------|----------|------|-----------------|-------------|
| NB | nhs365-book2.pdf | Reference Guide | `000-global/external/` | *NHS 365 — A Best Practices Guide for Transforming UK Healthcare with Microsoft AI* (365apps.pro, 2026-08-11, 23 pages). Cited via the converted Markdown copy held alongside it. |
| STKE | ARC-001-STKE-v1.0.md | ArcKit Artifact | `001-nhs365/` | Stakeholder Drivers & Goals Analysis — source of all goal, outcome, driver, and conflict traceability |
| PRIN | ARC-000-PRIN-v1.0.md | ArcKit Artifact | `000-global/` | Enterprise Architecture Principles — source of NFR alignment and non-negotiable constraints |

### Citations

| Citation ID | Doc ID | Page/Section | Category | Quoted Passage |
|-------------|--------|--------------|----------|----------------|
| NB-C1 | NB | Introduction — NHS England's Landmark Copilot Rollout | Business Requirement | "In that pilot, involving over 30,000 staff across 90 NHS organisations, participants saved an average of 43 minutes per person per day on administrative tasks... The rollout, expected to reach over 500,000 clinicians and support staff by October 2026" |
| NB-C2 | NB | Workforce Transformation — opening | Business Requirement | "The service employs around 1.37 million full-time equivalent staff, yet vacancies stand at approximately 100,020—a 6.7% rate... sickness absence hovers near 5.1%, with psychiatric issues such as anxiety, stress, and depression accounting for roughly 30% of absences" |
| NB-C3 | NB | Workforce Transformation — opening | Business Requirement | "Nearly half of general practice staff report that hardware and software are unfit for purpose, contributing to cognitive overload that undermines both wellbeing and care delivery." |
| NB-C4 | NB | Strategic Architecture — Security and Clinical Safety Governance | Compliance Constraint | "clinical risk management standards DCB0129 and DCB0160. The latter requires appointment of a Clinical Safety Officer who identifies hazards, assesses severity and likelihood, and ensures residual risk is reduced to a level that is as low as reasonably practicable before systems go live." |
| NB-C5 | NB | Strategic Architecture — Artificial Intelligence, Automation, and Associated Risks | Compliance Constraint | "Copilot is treated as an administrative productivity tool rather than Software as a Medical Device." |
| NB-C6 | NB | Strategic Architecture — Artificial Intelligence, Automation, and Associated Risks | Risk Factor | "'clinical drift'—the gradual use of generative AI for summarising patient notes or supporting clinical discussion—introduces risks of hallucination, omission of critical details such as allergies, or incorrect synthesis of information." |
| NB-C7 | NB | Care Identity Service — Practical Considerations for Organisations | Compliance Constraint | "Compliance is demonstrated primarily through the Data Security and Protection Toolkit (DSPT), aligned with the National Cyber Security Centre's Cyber Assessment Framework." |
| NB-C8 | NB | Introduction — A Practical Guide for the People Driving Change | Risk Factor | "you will find honest discussion of the pitfalls—shadow AI, data quality issues, change fatigue, equity risks, and the critical need for clinical safety and information governance to be designed in from the start." |
| NB-C9 | NB | Strategic Architecture — Licensing Approach | Procurement Constraint | "The Standard Service, based on Microsoft 365 F3, targets frontline clinical staff and provides web-based Office applications, a 4 GB mailbox, and limited OneDrive storage... The Enhanced Service, built on a restricted Microsoft 365 E3 Frontline Worker licence, serves managers, multidisciplinary team coordinators, and heavier administrative users. It offers larger mailboxes (50 GB), greater SharePoint allocation, and stronger security and compliance tools." |
| NB-C10 | NB | Strategic Architecture — Conclusion | Design Decision | "Organisations must weigh the operational simplicity and strong baseline security of the Shared Tenant against the flexibility—and greater responsibility—of a Sovereign Tenant. Critical decision factors include cyber maturity, the need for specialised integrations, the presence of legacy clinical systems that require hybrid identity, and the capacity to manage clinical safety governance for AI and automation." |
| NB-C11 | NB | Care Identity Service — Governance, Identity Lifecycle, and Risks | Security Requirement | "A persistent human risk is smartcard sharing, which undermines non-repudiation and patient safety investigations. CIS2 mitigates this by expanding frictionless options such as biometrics and high-assurance passkeys. Cross-border differences (for example, Scotland's CHI identifier and SWAN network versus England's NHS Number and internet-first model) require careful handling for interoperability. Automated systems must follow Secure Robot Authentication standards rather than relying on static credentials." |
| NB-C12 | NB | Workforce Transformation — Microlearning and Communities of Practice | Functional Requirement | "Clinical staff rarely have time for full-day classroom sessions. Microlearning—focused units typically under 15 minutes—fits better into busy schedules." |
| NB-C13 | NB | Care Identity Service — From CIS1 to CIS2 | Integration Requirement | "Supporting more than 1.3 million workers and handling tens of millions of authentications each month, access is managed locally by Registration Authorities (RAs). These bodies issue Care Identities, assign role-based access control (RBAC) positions, and control authenticators." |
| NB-C14 | NB | Teams Rooms — Security, Compliance, and Governance | Data Requirement | "Default Teams retention settings may conflict with clinical record-keeping requirements. Microsoft Purview can enforce appropriate retention—often six years for clinical consultations—while allowing shorter periods for administrative content." |
| NB-C15 | NB | Strategic Architecture — Identity, Authentication, and Directory Services | Integration Requirement | "It uses outbound connections only (port 443) to communicate with NHSmail services, avoiding the need to open inbound firewall ports. The system automates the joiner-mover-leaver process so that licences and access are granted or revoked promptly. When a user is marked as a leaver, access is removed immediately and data is retained for a defined period." |
| NB-C16 | NB | Care Identity Service — Practical Considerations for Organisations | Functional Requirement | "Registration Authorities remain central for identity proofing, role assignment, and smartcard lifecycle management, though self-service options (including Apply for Care ID and smartcard unlock) have expanded." |
| NB-C17 | NB | Workforce Transformation — Information Governance and Security | Compliance Constraint | "All solutions must meet rigorous NHS standards, including the Data Security and Protection Toolkit and Caldicott principles... Existing tools such as Microsoft Purview can enforce policies that prevent inappropriate sharing of patient identifiers in collaborative channels." |
| NB-C18 | NB | Workforce Transformation — Microsoft 365 as the Digital Backbone | Non-Functional Requirement | "By offering a coherent, secure experience inside the clinical workflow, trusts can reduce the appeal of 'shadow IT'—unofficial tools staff adopt when official systems frustrate them." |
| NB-C19 | NB | Care Identity Service — From CIS1 to CIS2 | Non-Functional Requirement | "The service runs at a platinum level with 24/7 support and high availability (targeting 99.9% uptime)." |
| NB-C20 | NB | Care Identity Service — Supported Authenticators and Assurance Levels | Security Requirement | "AAL3 (very high confidence) — required for the most sensitive applications: physical NHS smartcards... AAL2 (high confidence) — suitable for many applications: Microsoft Authenticator app, NHS.net Connect credentials..." |
| NB-C21 | NB | Care Identity Service — How Integration Works for Developers | Security Requirement | "All new integrations must use CIS2... The recommended cryptographic pathway is the Authorization Code Flow with Proof Key for Code Exchange (PKCE)... Architects are strongly advised to implement the Backend-for-Frontend (BFF) pattern so that tokens never reside in the browser." |
| NB-C22 | NB | Strategic Architecture — Drivers for Change | Risk Factor | "The 2017 WannaCry ransomware attack highlighted the risks of this approach: it disrupted services at 81 of 236 trusts, largely because outdated systems remained in use after a previous national enterprise agreement had expired." |
| NB-C23 | NB | Workforce Transformation — Microsoft 365 as the Digital Backbone | Data Requirement | "Data remains within the organisation's own tenant, simplifying governance and supporting UK data residency requirements." |
| NB-C24 | NB | Teams Rooms — Security, Compliance, and Governance | Integration Requirement | "The Microsoft Teams EHR connector transforms meeting rooms into virtual care hubs. Clinicians can launch visits directly from Epic Hyperspace/Haiku or Cerner PowerChart." |
| NB-C25 | NB | Strategic Architecture — Licensing Approach | Design Decision | "The Shared NHS Tenant is the default for most organisations. Managed centrally by NHS Digital (with support from partners such as Accenture), it delivers economies of scale, consistent Data Loss Prevention policies, and national security baselines." |

### Unreferenced Documents

| Filename | Source Location | Reason |
|----------|-----------------|--------|
| README.md | `000-global/policies/` | Directory placeholder; no organisational policy content present. No RFP/ITT documents, legacy system specifications, or user research reports have been supplied — Budget and several assumptions remain open as a direct result. |
| README.md | `001-nhs365/external/` | Directory placeholder; no project-specific reference documents supplied yet. |

---

**Generated by**: ArcKit `/arckit:requirements` command
**Generated on**: 2026-08-19
**ArcKit Version**: 6.11.0
**Project**: NHS 365 (Project 001)
**Model**: claude-opus-5[1m]
**Generation Context**: Derived from ARC-001-STKE-v1.0 (goals, drivers, conflicts, RACI), ARC-000-PRIN-v1.0 (21 architecture principles), and the NHS 365 source book. No RFP, legacy system specification, or user research was available.

<!-- arckit-provenance:start -->

## Build Provenance

*Stamped automatically by the ArcKit plugin's `provenance-stamp.mjs` PostToolUse hook. Complements (does not replace) the human-authored footer above. Carries only fields the model can't authoritatively self-report: build context from `.arckit/state.json` and effort levels derived from command frontmatter + the silent-downgrade matrix.*

| Field | Value |
|-------|-------|
| Requested Effort | `max` |
| Effective Effort | `max` |
| Stamped at | 2026-08-19T11:05:24.187Z |

<!-- arckit-provenance:end -->
