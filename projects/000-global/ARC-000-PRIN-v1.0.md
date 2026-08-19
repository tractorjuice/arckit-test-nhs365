# NHS 365 Enterprise Architecture Principles

> **Template Origin**: Official | **ArcKit Version**: 6.11.0 | **Command**: `/arckit:principles`

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ARC-000-PRIN-v1.0 |
| **Document Type** | Architecture Principles |
| **Project** | NHS 365 (Project 000) |
| **Classification** | OFFICIAL |
| **Status** | DRAFT |
| **Version** | 1.0 |
| **Created Date** | 2026-08-19 |
| **Last Modified** | 2026-08-19 |
| **Review Cycle** | Annual |
| **Next Review Date** | 2027-08-19 |
| **Owner** | Mark Craddock, Enterprise Architect |
| **Reviewed By** | PENDING |
| **Approved By** | PENDING |
| **Distribution** | NHS 365 programme team; Architecture Review Board; Clinical Safety Officer; Caldicott Guardian; Senior Information Risk Owner; participating NHS organisations |

## Revision History

| Version | Date | Author | Changes | Approved By | Approval Date |
|---------|------|--------|---------|-------------|---------------|
| 1.0 | 2026-08-19 | ArcKit AI | Initial creation from `/arckit:principles` command | PENDING | PENDING |

---

## Executive Summary

This document establishes the principles governing all technology architecture decisions for NHS 365 — the adoption of cloud productivity, collaboration, and artificial intelligence capabilities across NHS organisations. These principles ensure consistency, clinical safety, security, and alignment with national strategy across all projects and initiatives.

**Scope**: All technology projects, systems, and initiatives within the NHS 365 programme
**Authority**: Enterprise Architecture Review Board
**Compliance**: Mandatory unless exception approved by the CIO, with clinical safety exceptions additionally requiring the Clinical Safety Officer

**Philosophy**: These principles are **technology-agnostic** — they describe WHAT qualities the architecture must have, not HOW to implement them with specific products. Technology selection happens during research and design phases guided by these principles.

**Context**: The programme operates at national scale — a £120 million deployment of generative AI assistance to approximately 505,000 staff, following a 30,000-user pilot [NB-C4]. Scale of that order magnifies both the benefit and the consequence of every architectural decision, which is why information governance and clinical safety must be designed in from the start rather than retrofitted [NB-C12].

**Regulatory baseline**: Every system in scope is subject to the Data Security and Protection Toolkit (DSPT), the Caldicott principles, UK GDPR and the Data Protection Act 2018, and — where a system can affect clinical decision-making — the clinical risk management standards DCB0129 and DCB0160 [NB-C2]. The DSPT is aligned to the National Cyber Security Centre's Cyber Assessment Framework [NB-C13]. Systems serving the public are additionally subject to the Public Sector Bodies (Websites and Mobile Applications) Accessibility Regulations 2018.

---

## I. Strategic Principles

### 1. Scalability and Elasticity

**Principle Statement**:
All systems MUST be designed to scale horizontally to meet demand, with the ability to dynamically adjust capacity based on load.

**Rationale**:
Clinical demand is variable and seasonal, and national rollouts move from pilot to hundreds of thousands of users within months [NB-C4]. Systems must handle both growth and surge without manual intervention or architectural change.

**Implications**:

- Design stateless components that can be replicated
- Avoid hard-coded limits or fixed capacity assumptions
- Plan for distributed deployment across multiple compute locations
- Distribute traffic across instances rather than relying on vertical growth
- Scale capacity automatically against demand metrics
- Size for peak clinical periods, not annual averages

**Validation Gates**:

- [ ] System can scale horizontally (add more instances)
- [ ] No single points of failure that limit scaling
- [ ] Load testing demonstrates capacity growth with added resources
- [ ] Scaling metrics and triggers defined
- [ ] Cost model accounts for variable capacity

---

### 2. Resilience and Fault Tolerance

**Principle Statement**:
All systems MUST gracefully degrade when dependencies fail and recover automatically without data loss or manual intervention. Degraded modes MUST preserve safe clinical operation.

**Rationale**:
Failures are inevitable in distributed systems. In a clinical setting, the manner of failure matters as much as its frequency: a system that fails silently or presents incomplete information is more dangerous than one that fails visibly and hands control back to the clinician.

**Implications**:

- Break circuits on failing external dependencies rather than queueing indefinitely
- Apply timeouts to all network calls
- Retry transient failures with exponential backoff
- Degrade gracefully when non-critical services fail, and make the degradation visible to the user
- Isolate failure domains so one failing component cannot exhaust shared resources
- Define and rehearse the fallback for every clinically significant workflow
- Automate health checking and recovery

**Validation Gates**:

- [ ] Failure modes identified and mitigated
- [ ] Fault injection testing performed
- [ ] Recovery Time Objective (RTO) and Recovery Point Objective (RPO) defined
- [ ] Automated failover tested
- [ ] Degraded mode behaviour documented and clinically reviewed
- [ ] Business continuity fallback documented for each clinical workflow

---

### 3. Interoperability and Integration

**Principle Statement**:
All systems MUST expose functionality through well-defined, versioned interfaces using open, industry-standard protocols. Direct database access across system boundaries is prohibited.

**Rationale**:
Loose coupling through standard interfaces enables independent evolution, supplier diversity, and system composability. It also protects against lock-in: the NHS estate spans multiple organisations, tenancy models, and national services, and interfaces are what allow those to change independently.

**Implications**:

- Use open, documented protocols rather than proprietary interfaces
- Version all interfaces with a published backward-compatibility strategy
- Publish interface specifications as machine-readable contracts
- Prohibit direct database access across system boundaries
- Prefer asynchronous communication for non-real-time interactions
- Account for cross-border divergence within the UK — identifiers and network models differ between the home nations and must be handled explicitly rather than assumed [NB-C10]
- Use recognised health interoperability standards for clinical data exchange

**Validation Gates**:

- [ ] Interface specifications published in a machine-readable format
- [ ] Versioning strategy defined
- [ ] Authentication and authorisation model documented
- [ ] Error handling and retry behaviour specified
- [ ] No direct database coupling across systems
- [ ] Cross-border identifier handling documented where applicable

---

### 4. Security by Design (NON-NEGOTIABLE)

**Principle Statement**:
All architectures MUST implement defence-in-depth security with zero-trust principles. Security is NOT a feature to be added later — it is a foundational requirement.

**Rationale**:
The threat landscape requires assuming breach, eliminating implicit trust, and continuously verifying all access requests. Health and care data is a high-value target, and the sector has already demonstrated the cost of deferred patching and unsupported systems.

**Zero Trust Pillars**:

1. **Identity-Based Access**: No network-based trust; every request authenticated
2. **Least Privilege**: Grant minimum necessary permissions, time-boxed where possible
3. **Encryption Everywhere**: Data encrypted in transit and at rest
4. **Continuous Verification**: Monitor, log, and analyse all access patterns

**Implications**:

- Authenticate every request rather than trusting network location
- Grant least privilege, time-boxed where feasible
- Assume breach: design so that compromise of one component does not permit lateral movement
- Treat security review as a delivery gate, not a parallel activity
- Where a managed environment supplies baseline controls, evidence explicitly which controls are inherited and which remain locally owned

**Mandatory Controls**:

- [ ] Multi-factor authentication for all human access
- [ ] Service-to-service authentication using cryptographically verifiable credentials
- [ ] Automated and non-human accounts authenticated to a recognised secure standard rather than static shared credentials [NB-C10]
- [ ] Secrets held in a managed secret store, never in code or configuration files
- [ ] Network segmentation with minimal trust zones
- [ ] Encryption at rest for all data stores
- [ ] Encrypted transport for all network communication
- [ ] Structured logging of all authentication and authorisation events
- [ ] Regular security testing (penetration testing, vulnerability scanning)
- [ ] Outbound-only connectivity preferred over inbound firewall exceptions where integration patterns allow [NB-C11]

**Compliance Frameworks**:

- Data Security and Protection Toolkit (DSPT), aligned to the NCSC Cyber Assessment Framework [NB-C13]
- ISO 27001 and Cyber Essentials Plus where contractually required
- UK GDPR and the Data Protection Act 2018

**Exceptions**:

- NONE. Security principles are non-negotiable.
- Specific control implementations may vary where compensating controls achieve equivalent assurance.

**Validation Gates**:

- [ ] Threat model completed and reviewed
- [ ] Security controls mapped to requirements
- [ ] Security testing plan defined
- [ ] Incident response runbook created
- [ ] DSPT evidence identified for each applicable assertion

---

### 5. Observability and Operational Excellence

**Principle Statement**:
All systems MUST emit structured telemetry (logs, metrics, traces) enabling real-time monitoring, troubleshooting, capacity planning, and after-the-fact audit of access to personal data.

**Rationale**:
We cannot operate what we cannot observe, and we cannot investigate what we did not record. In health and care, telemetry serves a second purpose beyond operations: it is the evidence base for information governance investigations and patient safety incident review.

**Implications**:

- Instrument at design time, not in response to an incident
- Correlate telemetry across service boundaries using a shared identifier
- Separate operational telemetry from audit records — they carry different retention periods and access rules
- Keep personal and clinical data out of operational logs
- Set alert thresholds against service objectives rather than raw resource metrics

**Telemetry Requirements**:

- **Logging**: Structured logs with correlation IDs
- **Metrics**: Request volume, latency percentiles (p50, p95, p99), error rates
- **Tracing**: Distributed trace context for request flows
- **Alerting**: Service Level Objective (SLO)-based alerting with actionable runbooks
- **Audit**: Attributable record of access to personal and clinical data

**Required Instrumentation**:

- Request volume, latency distribution, error rate
- Resource utilisation (compute, memory, storage, network)
- Service metrics (task completion, adoption, user actions)
- Security events (authentication failures, policy violations, anomalous access)
- AI-assistance events where generative capability is in use, sufficient to reconstruct what was proposed and what a human accepted

**Log Retention**:

- **Security and audit logs**: As required by compliance, and not less than the applicable clinical record retention period
- **Application logs**: Sufficient for troubleshooting (typically 30–90 days)
- **Metrics**: Long-term trends (typically 1–2 years with aggregation)

**Validation Gates**:

- [ ] Logging, metrics, tracing instrumented
- [ ] Dashboards and alerts configured
- [ ] Service Level Objectives (SLOs) and Service Level Indicators (SLIs) defined
- [ ] Runbooks created for common failure scenarios
- [ ] Capacity planning metrics tracked
- [ ] Audit trail sufficient to attribute data access to an individual

---

## II. Data and Information Governance Principles

### 6. Data Sovereignty and Residency

**Principle Statement**:
Data classification, residency, retention, and access controls MUST comply with UK regulatory requirements and NHS information governance policy. Personal and clinical data MUST remain within the controlling organisation's governance boundary.

**Rationale**:
Keeping data within the organisation's own tenancy simplifies governance and supports UK data residency requirements [NB-C7]. Where data leaves that boundary, the organisation retains accountability but loses direct control — so the boundary crossing must be a deliberate, documented decision rather than a side effect of a product choice.

**Implications**:

- Establish the residency and processing position before contract award, not during implementation
- Classify data before deciding where it will be stored
- Configure retention explicitly for every store; never inherit a product default
- Record which organisation is controller and which is processor for each data flow
- Reassess when a supplier changes sub-processors or hosting regions

**Data Classification Tiers**:

1. **Public**: No restrictions (published guidance, public-facing content)
2. **Internal**: Staff-only access (internal documents, non-sensitive operational data)
3. **Confidential**: Need-to-know basis (staff personal data, commercial information)
4. **Restricted**: Highest controls (patient identifiable data, special category data)

**Data Residency**:

- Personal and clinical data must reside in jurisdictions compliant with UK GDPR
- Cross-border transfers require a documented lawful basis and transfer mechanism
- The residency position must be established before procurement, not discovered during implementation

**Data Retention**:

- Retention configured to the applicable clinical or corporate schedule rather than to a product default — default collaboration-tool retention will not match clinical record-keeping requirements and must be overridden explicitly [NB-C5]
- Automatic deletion at end of retention period
- Legal hold process for litigation and investigation
- Backup retention aligned with compliance and recovery requirements

**Validation Gates**:

- [ ] Data classification performed for all data stores
- [ ] Residency requirements mapped to infrastructure
- [ ] Retention policies configured with automated deletion, and explicitly reconciled against clinical record retention
- [ ] Access controls enforce least privilege and need-to-know
- [ ] Lawful basis documented for any cross-border transfer

---

### 7. Confidentiality and the Caldicott Principles

**Principle Statement**:
Every use of patient identifiable information MUST satisfy the Caldicott principles, and technical controls MUST make inappropriate sharing difficult by default rather than relying on user judgement.

**Rationale**:
Collaboration platforms make sharing frictionless, which is their value and their risk. Preventive controls that block inappropriate sharing of patient identifiers are more reliable than policy alone [NB-C6]. The duty to share information for direct care carries equal weight with the duty to protect confidentiality — controls must not obstruct legitimate care.

**Implications**:

- Justify the purpose for every use of patient identifiable information
- Use the minimum necessary identifiable data, and de-identify where the purpose allows
- Apply automated controls that detect and block inappropriate sharing of identifiers in collaborative channels
- Make the lawful basis explicit and recorded for each processing activity
- Ensure the Caldicott Guardian and Senior Information Risk Owner are engaged before, not after, design is fixed
- Do not let confidentiality controls block information sharing that direct care requires

**Validation Gates**:

- [ ] Purpose and lawful basis documented for each use of identifiable data
- [ ] Data minimisation and de-identification assessed
- [ ] Automated controls configured to detect inappropriate sharing of identifiers
- [ ] Caldicott Guardian and SIRO consulted and their position recorded
- [ ] Data Protection Impact Assessment completed where required

---

### 8. Data Quality and Lineage

**Principle Statement**:
Data pipelines MUST maintain data quality standards and provide end-to-end lineage for auditability and troubleshooting.

**Rationale**:
Poor data quality is a recognised pitfall of AI-enabled transformation [NB-C12]. Where automated analysis or generative assistance consumes clinical data, quality defects propagate into outputs that clinicians may reasonably trust. Lineage is what makes such a defect traceable to its source.

**Implications**:

- Validate at the point of capture rather than downstream
- Surface quality defects to data owners, not only to engineers
- Version transformation logic and review it as code
- Assess dataset quality before it grounds automated analysis
- Assign a named owner to each data domain

**Quality Standards**:

- **Completeness**: No unexpected nulls in required fields
- **Consistency**: Cross-system reconciliation
- **Accuracy**: Validation rules and constraints enforced at source
- **Timeliness**: Freshness Service Level Agreements (SLAs) defined and monitored

**Lineage Requirements**:

- Source-to-target mapping documented for all data flows
- Transformation logic version-controlled and reviewable
- Data quality metrics tracked per pipeline
- Impact analysis capability for schema changes
- Provenance recorded for any dataset used to ground or train automated analysis

**Validation Gates**:

- [ ] Data quality rules defined and automated
- [ ] Lineage metadata captured and queryable
- [ ] Data contracts agreed between producers and consumers
- [ ] Schema evolution strategy documented
- [ ] Provenance recorded for AI-consumed datasets

---

### 9. Single Source of Truth

**Principle Statement**:
Every data domain MUST have a single authoritative source. Derived copies MUST be clearly labelled, read-only, and synchronised on a documented schedule.

**Rationale**:
Multiple authoritative sources create inconsistency, reconciliation overhead, and data integrity issues. In a federated estate spanning many organisations, ambiguity about which copy is authoritative is a direct clinical risk.

**Implications**:

- Identify the system of record for each data domain
- Mark derived and cached copies as read-only and label them as derived
- Define a synchronisation strategy for every derived copy
- Avoid bidirectional synchronisation, which creates split-brain scenarios
- Treat national services as authoritative for the data they own rather than replicating and diverging

**Validation Gates**:

- [ ] System of record identified for each data entity
- [ ] Derived copies documented with synchronisation frequency
- [ ] No bidirectional synchronisation without a conflict resolution strategy
- [ ] Reference data management strategy defined for shared data

---

## III. Clinical Safety and Responsible AI Principles

### 10. Clinical Safety by Design (NON-NEGOTIABLE)

**Principle Statement**:
Any system capable of influencing clinical decision-making, care delivery, or the clinical record MUST undergo clinical risk management under DCB0129 and DCB0160, with a named Clinical Safety Officer accountable before go-live.

**Rationale**:
DCB0160 requires appointment of a Clinical Safety Officer who identifies hazards, assesses severity and likelihood, and ensures residual risk is reduced to a level as low as reasonably practicable before systems go live [NB-C2]. This is a regulatory obligation, not a quality aspiration, and it applies to the intended use of the system rather than to the vendor's product category.

**Implications**:

- Appoint and empower a Clinical Safety Officer for each clinically significant system
- Produce a hazard log and clinical safety case, maintained across the product lifecycle rather than produced once at go-live
- Assess intended use explicitly: a tool procured for administrative productivity that is used in a clinical workflow has changed its risk profile and must be re-assessed
- Determine and record whether the system meets the definition of Software as a Medical Device — the classification drives the regulatory pathway [NB-C4]
- Reassess clinical risk on material change, not only at initial deployment
- Ensure clinical safety sign-off gates deployment and cannot be waived by delivery pressure

**Exceptions**:

- NONE for systems in clinical scope. Where a system is assessed as out of clinical scope, that assessment must itself be documented and approved by the Clinical Safety Officer.

**Validation Gates**:

- [ ] Clinical Safety Officer appointed and named
- [ ] Hazard log produced and maintained
- [ ] Clinical safety case approved before go-live
- [ ] Software as a Medical Device determination recorded
- [ ] Residual risk reduced to as low as reasonably practicable and formally accepted
- [ ] Reassessment triggers defined for material change

---

### 11. Human Accountability for Automated Output

**Principle Statement**:
Automated and AI-generated output MUST be presented as advisory, attributable, and reviewable. A human MUST remain accountable for any decision affecting patient care, and the system MUST NOT present generated content in a way that implies clinical authority.

**Rationale**:
Generative assistance introduces risks of hallucination, omission of critical details such as allergies, and incorrect synthesis of information [NB-C3]. "Clinical drift" — the gradual migration of a tool from administrative use into clinical use — is the mechanism by which an approved low-risk deployment becomes an unapproved high-risk one, without any change to the technology itself [NB-C3]. The architecture must make that drift visible and controllable.

**Implications**:

- Label generated content clearly and distinguishably from clinician-authored content
- Require explicit human review and acceptance before generated content enters the clinical record
- Record what was generated, what was accepted, and by whom, sufficient for later review
- Constrain the tool to its assessed intended use, and detect use outside it
- Assess and monitor for inequitable outcomes across patient and staff populations [NB-C12]
- Provide staff with training on the failure modes of automated assistance, not only its features
- Deter unsanctioned AI tools by making approved capability genuinely usable — unusable official tooling creates shadow use [NB-C8]

**Validation Gates**:

- [ ] Generated content visually and structurally distinguishable from authored content
- [ ] Human review step enforced before generated content enters the clinical record
- [ ] Audit trail records generation, review, and acceptance with attribution
- [ ] Intended-use boundary defined, with monitoring for use beyond it
- [ ] Equity impact assessed across affected populations
- [ ] Staff training covers limitations and failure modes

---

### 12. Identity Assurance and Non-Repudiation

**Principle Statement**:
Access to clinical systems MUST be individually attributable. Authentication MUST meet an assurance level proportionate to the sensitivity of the action, and credential sharing MUST be designed out rather than prohibited by policy alone.

**Rationale**:
Credential sharing undermines non-repudiation and compromises patient safety investigations [NB-C10]. Sharing is usually a rational response to authentication friction on shared clinical workstations, so the durable remedy is frictionless strong authentication rather than stricter policy. Assurance should be tiered: the highest level is warranted for prescribing and sensitive record modification, a lower level for routine access [NB-C14].

**Implications**:

- Federate to the national care identity service rather than building bespoke authentication [NB-C9]
- Match authenticator assurance level to the sensitivity of the action, not uniformly to the system
- Prefer frictionless high-assurance methods — biometrics, high-assurance passkeys — on shared clinical devices
- Use the authorization code flow with proof key for code exchange, and keep tokens out of the browser by terminating them server-side [NB-C9]
- Automate the joiner-mover-leaver lifecycle so access is granted and revoked promptly, with immediate revocation on leaving [NB-C11]
- Authenticate automated and non-human actors to a recognised secure standard rather than with static shared credentials [NB-C10]

**Validation Gates**:

- [ ] Federated to the national identity service where the service is applicable
- [ ] Assurance level mapped per action class and justified
- [ ] Token handling pattern reviewed against current secure practice
- [ ] Joiner-mover-leaver automation implemented and tested, including immediate revocation
- [ ] Non-human accounts authenticated without static shared credentials
- [ ] Every clinically significant action attributable to a named individual

---

## IV. Integration Principles

### 13. Loose Coupling

**Principle Statement**:
Systems MUST be loosely coupled through published interfaces, avoiding shared databases, shared file systems, or tight runtime dependencies.

**Rationale**:
Loose coupling enables independent deployment, supplier diversity, team autonomy, and evolution without breaking dependencies. It is also what allows organisations on different tenancy and infrastructure models to integrate with the same national services.

**Implications**:

- Communicate through published interfaces or asynchronous events
- Prohibit direct database access across system boundaries
- Let each system manage its own data lifecycle
- Keep shared libraries minimal, favouring duplication over coupling
- Avoid distributed transactions across systems

**Validation Gates**:

- [ ] Systems communicate via interfaces or events, not shared data stores
- [ ] No shared mutable state
- [ ] Each system has an independent data store
- [ ] Deployment of one system does not require deployment of another
- [ ] Interface changes versioned with backward compatibility

---

### 14. Asynchronous Communication

**Principle Statement**:
Systems SHOULD use asynchronous communication for non-real-time interactions to improve resilience and decoupling.

**Rationale**:
Asynchronous patterns reduce temporal coupling, improve fault tolerance, and enable better scalability — particularly when integrating with legacy clinical systems whose availability cannot be guaranteed.

**Implications**:

- Decide synchronous versus asynchronous per interaction, not per system
- Design consumers to be idempotent, since at-least-once delivery implies duplicates
- Publish and version event schemas as first-class contracts
- Make eventual consistency visible to users where it could affect a clinical decision
- Provide a defined path for messages that cannot be processed

**When to Use Asynchronous**:

- Non-real-time business processes (referrals, batch reporting, notifications)
- Event notification and publish/subscribe patterns
- Long-running operations that do not require an immediate response
- Integration with slow or unreliable external systems

**When Synchronous is Acceptable**:

- Real-time clinical interactions requiring immediate feedback
- Query operations that are read-only and idempotent
- Transactions requiring immediate consistency

**Validation Gates**:

- [ ] Asynchronous patterns used for non-real-time flows
- [ ] Message durability and delivery guarantees defined
- [ ] Event schemas versioned and published
- [ ] Dead letter handling and error paths configured

---

## V. Quality Attributes

### 15. Performance and Efficiency

**Principle Statement**:
All systems MUST meet defined performance targets under expected load with efficient use of computational resources.

**Rationale**:
Latency in a clinical workflow is not merely an inconvenience: it consumes clinical time and drives staff toward unsanctioned workarounds [NB-C8]. Performance targets must be set against the clinical context of use, not against a generic benchmark.

**Performance Targets** (define for each system):

- **Response Time**: p50, p95, p99 latency targets
- **Throughput**: Requests per second, transactions per minute
- **Concurrency**: Simultaneous user and request capacity
- **Resource Efficiency**: Compute and memory utilisation targets

**Implications**:

- Define performance requirements before implementation, expressed in clinical terms where relevant
- Perform load testing before production deployment
- Monitor performance continuously rather than at a point in time
- Optimise hot paths identified through profiling
- Apply caching strategies for expensive operations, respecting data freshness requirements

**Validation Gates**:

- [ ] Performance requirements defined with measurable targets
- [ ] Load testing performed at expected capacity
- [ ] Performance metrics monitored in production
- [ ] Capacity planning model defined

---

### 16. Availability and Reliability

**Principle Statement**:
All systems MUST meet defined availability targets with automated recovery and minimal data loss, with targets set according to clinical criticality.

**Rationale**:
National identity and clinical services operate to high availability targets because dependent clinical systems cannot function without them. Availability requirements must cascade from clinical criticality rather than being set uniformly.

**Implications**:

- Derive availability targets from clinical criticality and record the derivation
- Identify and remove single points of failure, including shared dependencies
- Test failover and restore on a schedule rather than assuming they work
- Account for dependency availability — a service cannot exceed the availability of what it depends on
- Agree availability commitments with suppliers contractually

**Availability Targets** (define for each system):

- **Uptime SLA**: e.g. 99.9% (43.8 minutes downtime per month), 99.95%, 99.99%
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime
- **Recovery Point Objective (RPO)**: Maximum acceptable data loss

**High Availability Patterns**:

- Redundancy across independent failure domains
- Automated health checks and failover
- Active-active or active-passive configurations
- Regular disaster recovery testing
- Documented clinical fallback for the period a system is unavailable

**Validation Gates**:

- [ ] Availability SLA defined and traced to clinical criticality
- [ ] RTO and RPO requirements documented
- [ ] Redundancy strategy implemented
- [ ] Failover tested regularly
- [ ] Backup and restore procedures validated
- [ ] Clinical fallback procedure documented and rehearsed

---

### 17. Maintainability and Evolvability

**Principle Statement**:
All systems MUST be designed for change, with clear separation of concerns, modular architecture, and comprehensive documentation.

**Rationale**:
Software spends most of its lifetime in maintenance. The sector has already demonstrated the cost of systems that became unmaintainable and unsupported. Design decisions should optimise for understandability and modifiability over initial delivery speed.

**Implications**:

- Structure systems modularly with clear boundaries
- Separate concerns (business logic, data access, presentation)
- Write self-documenting code with meaningful names
- Record significant choices in Architecture Decision Records
- Maintain automated testing sufficient to enable confident refactoring
- Plan for supported-lifetime management of every dependency

**Validation Gates**:

- [ ] Architecture documentation exists and is current
- [ ] Module boundaries clear with defined responsibilities
- [ ] Automated test coverage enables safe refactoring
- [ ] Architecture Decision Records document key choices
- [ ] Dependency support lifecycle tracked with an upgrade plan

---

### 18. Accessibility and Digital Inclusion

**Principle Statement**:
All services MUST meet recognised accessibility standards, and design MUST account for variation in digital confidence, device availability, and connectivity among both staff and patients.

**Rationale**:
Public sector services are legally obliged to meet accessibility requirements, and equity risk is a recognised pitfall of digital transformation [NB-C12]. A service that works only for confident users on modern devices excludes precisely the populations with the greatest health needs.

**Implications**:

- Meet the applicable WCAG conformance level for all user-facing interfaces
- Publish and maintain an accessibility statement
- Test with assistive technologies and with users who have access needs
- Provide non-digital or assisted routes where a service is essential
- Consider clinical environment constraints — gloved hands, shared devices, poor lighting, interruption
- Assess whether design choices disadvantage any patient or staff group

**Validation Gates**:

- [ ] Accessibility conformance level defined and tested against
- [ ] Accessibility statement published and current
- [ ] Testing performed with assistive technologies
- [ ] Assisted digital or non-digital route defined where the service is essential
- [ ] Equity impact assessed and recorded

---

## VI. Development Practices

### 19. Infrastructure as Code

**Principle Statement**:
All infrastructure and platform configuration MUST be defined as code, version-controlled, and deployed through automated pipelines.

**Rationale**:
Manual changes create drift, inconsistency, and undocumented state. Defining infrastructure as code enables repeatability, auditability, and disaster recovery. In a governed environment it also produces the change evidence that assurance regimes require.

**Implications**:

- Define all infrastructure declaratively in code
- Subject infrastructure changes to code review
- Make environments reproducible from code
- Prohibit manual changes to production infrastructure
- Version infrastructure alongside application code
- Treat security and retention policy configuration as code, so that a deviation from the required setting is visible in review rather than discovered in audit

**Validation Gates**:

- [ ] Infrastructure defined as code
- [ ] Infrastructure code version-controlled
- [ ] Automated deployment pipeline for infrastructure
- [ ] No manual infrastructure changes in production
- [ ] Governance-relevant configuration held as code

---

### 20. Automated Testing

**Principle Statement**:
All code changes MUST be validated through automated testing before deployment to production.

**Rationale**:
Manual regression testing does not scale to the change rate of a national platform, and untested change in a clinical system transfers risk directly to patients. Automated tests are what make continuous improvement safe rather than reckless.

**Implications**:

- Write tests alongside code, not afterwards
- Gate merge on passing tests
- Prioritise coverage of clinically significant paths over uniform coverage targets
- Maintain test data that is representative but contains no real patient data
- Treat a flaky test as a defect, not as noise to be retried

**Test Pyramid**:

- **Unit Tests**: Fast, isolated, high coverage (70–80% of tests)
- **Integration Tests**: Component interactions (15–20% of tests)
- **End-to-End Tests**: Critical user journeys (5–10% of tests)

**Required Test Types**:

- Functional tests (does it work?)
- Performance tests (is it fast enough?)
- Security tests (is it secure?)
- Resilience tests (does it handle failures?)
- Accessibility tests (can everyone use it?)

**Validation Gates**:

- [ ] Automated tests exist and pass before merge
- [ ] Test coverage meets defined thresholds
- [ ] Critical clinical paths have end-to-end tests
- [ ] Performance tests run regularly
- [ ] Accessibility checks automated where automatable

---

### 21. Continuous Integration and Deployment

**Principle Statement**:
All code changes MUST go through automated build, test, and deployment pipelines with quality gates at each stage.

**Rationale**:
Manual deployment is slow, inconsistent, and leaves no reliable audit trail. Automated pipelines make every change reproducible and evidenced — which is what assurance regimes require, and what allows rapid patching when a vulnerability emerges.

**Implications**:

- Deploy through the pipeline only; no manual production changes
- Keep the pipeline fast enough that teams do not route around it
- Scan dependencies continuously, not only at build time
- Make rollback a tested path rather than a theoretical one
- Record approval and, where applicable, clinical safety evidence for each production release

**Pipeline Stages**:

1. **Source Control**: All changes committed to version control
2. **Build**: Automated compilation and packaging
3. **Test**: Automated test execution
4. **Security Scan**: Dependency and code vulnerability scanning
5. **Deployment**: Automated deployment to environments

**Quality Gates**:

- All tests must pass
- No critical security vulnerabilities
- Code review approval required
- Clinical safety sign-off required for changes in clinical scope
- Deployment requires a production readiness checklist

**Validation Gates**:

- [ ] Automated CI/CD pipeline exists
- [ ] Pipeline includes security scanning
- [ ] Deployment is automated and repeatable
- [ ] Rollback capability tested
- [ ] Clinical safety gate enforced for clinically significant changes

---

## VII. Exception Process

### Requesting Architecture Exceptions

Principles are mandatory unless a documented exception is approved by the Enterprise Architecture Review Board.

**Valid Exception Reasons**:

- Technical constraints that prevent compliance
- Regulatory or legal requirements
- Transitional state during migration
- Pilot or proof-of-concept with a defined end date

**Exception Request Requirements**:

- [ ] Justification with business and technical rationale
- [ ] Alternative approach and compensating controls
- [ ] Risk assessment and mitigation plan
- [ ] Expiration date (exceptions are time-bound)
- [ ] Remediation plan to achieve compliance

**Approval Process**:

1. Submit exception request to the Enterprise Architecture team
2. Review by the Architecture Review Board
3. CIO approval for exceptions to critical principles
4. Clinical Safety Officer approval additionally required where the exception touches Principle 10, 11, or 12
5. Document the exception in project architecture documentation
6. Review open exceptions quarterly

**Non-Waivable Principles**:

Principle 4 (Security by Design) and Principle 10 (Clinical Safety by Design) admit no exception. Implementation may vary where compensating controls achieve equivalent assurance, but the obligation itself cannot be waived.

---

## VIII. Governance and Compliance

### Architecture Review Gates

All projects must pass architecture reviews at key milestones:

**Discovery**:

- [ ] Architecture principles understood
- [ ] High-level approach aligns with principles
- [ ] Clinical scope determination made
- [ ] No obvious principle violations

**Design**:

- [ ] Detailed architecture documented
- [ ] Compliance with each principle validated
- [ ] Exceptions requested and approved
- [ ] Security and data principles validated
- [ ] Data Protection Impact Assessment completed where required
- [ ] Clinical hazard log opened where in clinical scope

**Pre-Production**:

- [ ] Implementation matches approved architecture
- [ ] All validation gates passed
- [ ] Operational readiness verified
- [ ] Clinical safety case approved where in clinical scope
- [ ] DSPT evidence captured

### Enforcement

- Architecture reviews are **mandatory** for all projects
- Principle violations must be remediated before production deployment
- Approved exceptions are time-bound and reviewed quarterly
- Retrospective reviews for compliance on live systems
- Clinical safety and security gates cannot be bypassed by delivery escalation

### Tenancy and Delegated Responsibility

Where organisations operate under different tenancy models, accountability for these principles varies but is never removed. A shared, centrally managed environment delivers consistent baseline controls and reduced management overhead; an independently managed environment offers greater flexibility and carries correspondingly greater local responsibility [NB-C1]. Each organisation MUST record which model it operates under and which principles it discharges locally rather than inheriting. The decision factors — cyber maturity, need for specialised integration, presence of legacy clinical systems requiring hybrid identity, and capacity to manage clinical safety governance for AI and automation — MUST be assessed and recorded rather than assumed [NB-C1].

---

## IX. Appendix

### Principle Summary Checklist

| Principle | Category | Criticality | Validation |
|-----------|----------|-------------|------------|
| 1. Scalability and Elasticity | Strategic | HIGH | Load testing, scaling metrics |
| 2. Resilience and Fault Tolerance | Strategic | CRITICAL | Fault injection, RTO/RPO |
| 3. Interoperability and Integration | Strategic | HIGH | Interface specs, versioning |
| 4. Security by Design | Strategic | CRITICAL | Threat model, penetration testing |
| 5. Observability and Operational Excellence | Strategic | HIGH | Metrics, logs, traces, audit trail |
| 6. Data Sovereignty and Residency | Data | CRITICAL | Residency mapping, retention audit |
| 7. Confidentiality and Caldicott | Data | CRITICAL | Caldicott/SIRO sign-off, DPIA |
| 8. Data Quality and Lineage | Data | MEDIUM | Quality metrics, lineage capture |
| 9. Single Source of Truth | Data | HIGH | System of record register |
| 10. Clinical Safety by Design | Clinical | CRITICAL | Hazard log, clinical safety case |
| 11. Human Accountability for Automated Output | Clinical | CRITICAL | Review gate, generation audit trail |
| 12. Identity Assurance and Non-Repudiation | Clinical | CRITICAL | Assurance level mapping, attribution |
| 13. Loose Coupling | Integration | HIGH | Deployment independence |
| 14. Asynchronous Communication | Integration | MEDIUM | Async patterns used |
| 15. Performance and Efficiency | Quality | HIGH | Load testing |
| 16. Availability and Reliability | Quality | CRITICAL | SLA monitoring, DR test |
| 17. Maintainability and Evolvability | Quality | MEDIUM | Documentation, ADRs, tests |
| 18. Accessibility and Digital Inclusion | Quality | HIGH | WCAG conformance, equity assessment |
| 19. Infrastructure as Code | DevOps | HIGH | IaC coverage |
| 20. Automated Testing | DevOps | HIGH | Test coverage |
| 21. Continuous Integration and Deployment | DevOps | HIGH | Pipeline exists, safety gate |

### Category Index

| Category | Principles | Focus |
|----------|-----------|-------|
| Strategic | 1–5 | Business and enterprise-wide qualities |
| Data | 6–9 | Information governance and data management |
| Clinical | 10–12 | Patient safety, responsible AI, attribution |
| Integration | 13–14 | Application interaction patterns |
| Quality | 15–18 | Runtime and experience qualities |
| DevOps | 19–21 | Technology delivery practice |

---

**Document Version History**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-19 | ArcKit AI | Initial draft |

## External References

> This section provides traceability from generated content back to source documents.
> Follow citation instructions in the project's citation reference guide.

### Document Register

| Doc ID | Filename | Type | Source Location | Description |
|--------|----------|------|-----------------|-------------|
| NB | nhs365-book2.pdf | Reference Guide | `000-global/external/` | *NHS 365 — A Best Practices Guide for Transforming UK Healthcare with Microsoft AI* (365apps.pro, 2026-08-11, 23 pages). Cited via the converted Markdown copy `nhs365-book2.md` held alongside it. |

### Citations

| Citation ID | Doc ID | Page/Section | Category | Quoted Passage |
|-------------|--------|--------------|----------|----------------|
| NB-C1 | NB | Strategic Architecture — Conclusion | Design Decision | "Organisations must weigh the operational simplicity and strong baseline security of the Shared Tenant against the flexibility—and greater responsibility—of a Sovereign Tenant. Critical decision factors include cyber maturity, the need for specialised integrations, the presence of legacy clinical systems that require hybrid identity, and the capacity to manage clinical safety governance for AI and automation." |
| NB-C2 | NB | Strategic Architecture — Security and Clinical Safety Governance | Compliance Constraint | "Regulatory obligations include the Data Security and Protection Toolkit, the Secure Email Standard (DCB1596—pre-accredited for Shared Tenant users), and clinical risk management standards DCB0129 and DCB0160. The latter requires appointment of a Clinical Safety Officer who identifies hazards, assesses severity and likelihood, and ensures residual risk is reduced to a level that is as low as reasonably practicable before systems go live." |
| NB-C3 | NB | Strategic Architecture — Artificial Intelligence, Automation, and Associated Risks | Risk Factor | "Nevertheless, 'clinical drift'—the gradual use of generative AI for summarising patient notes or supporting clinical discussion—introduces risks of hallucination, omission of critical details such as allergies, or incorrect synthesis of information." |
| NB-C4 | NB | Strategic Architecture — Artificial Intelligence, Automation, and Associated Risks | Compliance Constraint | "The NHS has invested substantially in technology modernisation, including a £120 million programme to deploy Microsoft 365 Copilot to around 505,000 staff after a successful pilot involving 30,000 users... Copilot is treated as an administrative productivity tool rather than Software as a Medical Device." |
| NB-C5 | NB | Teams Rooms — Security, Compliance, and Governance | Data Requirement | "Default Teams retention settings may conflict with clinical record-keeping requirements. Microsoft Purview can enforce appropriate retention—often six years for clinical consultations—while allowing shorter periods for administrative content." |
| NB-C6 | NB | Workforce Transformation — Information Governance and Security | Compliance Constraint | "All solutions must meet rigorous NHS standards, including the Data Security and Protection Toolkit and Caldicott principles... Existing tools such as Microsoft Purview can enforce policies that prevent inappropriate sharing of patient identifiers in collaborative channels." |
| NB-C7 | NB | Workforce Transformation — Microsoft 365 as the Digital Backbone | Data Requirement | "Data remains within the organisation's own tenant, simplifying governance and supporting UK data residency requirements." |
| NB-C8 | NB | Workforce Transformation — Microsoft 365 as the Digital Backbone | Risk Factor | "By offering a coherent, secure experience inside the clinical workflow, trusts can reduce the appeal of 'shadow IT'—unofficial tools staff adopt when official systems frustrate them." |
| NB-C9 | NB | Care Identity Service — How Integration Works for Developers | Security Requirement | "The recommended cryptographic pathway is the Authorization Code Flow with Proof Key for Code Exchange (PKCE)... Architects are strongly advised to implement the Backend-for-Frontend (BFF) pattern so that tokens never reside in the browser, mitigating XSS and token theft risks." |
| NB-C10 | NB | Care Identity Service — Governance, Identity Lifecycle, and Risks | Risk Factor | "A persistent human risk is smartcard sharing, which undermines non-repudiation and patient safety investigations... Cross-border differences (for example, Scotland's CHI identifier and SWAN network versus England's NHS Number and internet-first model) require careful handling for interoperability. Automated systems must follow Secure Robot Authentication standards rather than relying on static credentials." |
| NB-C11 | NB | Strategic Architecture — Identity, Authentication, and Directory Services | Security Requirement | "It uses outbound connections only (port 443)... avoiding the need to open inbound firewall ports. The system automates the joiner-mover-leaver process so that licences and access are granted or revoked promptly. When a user is marked as a leaver, access is removed immediately." |
| NB-C12 | NB | Introduction — A Practical Guide for the People Driving Change | Risk Factor | "Equally important, you will find honest discussion of the pitfalls—shadow AI, data quality issues, change fatigue, equity risks, and the critical need for clinical safety and information governance to be designed in from the start." |
| NB-C13 | NB | Care Identity Service — Practical Considerations for Organisations | Compliance Constraint | "Compliance is demonstrated primarily through the Data Security and Protection Toolkit (DSPT), aligned with the National Cyber Security Centre's Cyber Assessment Framework." |
| NB-C14 | NB | Care Identity Service — Supported Authenticators and Assurance Levels | Security Requirement | "AAL3 (very high confidence) — required for the most sensitive applications... AAL2 (high confidence) — suitable for many applications." |

### Unreferenced Documents

| Filename | Source Location | Reason |
|----------|-----------------|--------|
| README.md | `000-global/policies/` | Directory placeholder; no organisational policy content present. No policies have yet been supplied to constrain these principles. |

---

**Generated by**: ArcKit `/arckit:principles` command
**Generated on**: 2026-08-19
**ArcKit Version**: 6.11.0
**Project**: NHS 365 (Project 000)
**Model**: claude-opus-5[1m]

<!-- arckit-provenance:start -->

## Build Provenance

*Stamped automatically by the ArcKit plugin's `provenance-stamp.mjs` PostToolUse hook. Complements (does not replace) the human-authored footer above. Carries only fields the model can't authoritatively self-report: build context from `.arckit/state.json` and effort levels derived from command frontmatter + the silent-downgrade matrix.*

| Field | Value |
|-------|-------|
| Requested Effort | `high` |
| Effective Effort | `high` |
| Stamped at | 2026-08-19T10:38:57.520Z |

<!-- arckit-provenance:end -->
