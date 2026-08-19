---
title: "NHS 365 — A Best Practices Guide for Transforming UK Healthcare with Microsoft AI"
publisher: 365apps.pro
source_url: https://365apps.pro/wp-content/uploads/sites/50/2026/08/nhs365-book2.pdf
source_file: nhs365-book2.pdf
source_published: 2026-08-11
retrieved: 2026-08-19
pages: 23
conversion: automated text extraction (pypdf); figures and images are not
 included and callout ordering is reconstructed, not authoritative
---

# NHS 365 — A Best Practices Guide for Transforming UK Healthcare with Microsoft AI

> Reference document for ArcKit governance artifacts, converted from
> `nhs365-book2.pdf` (23 pages) on 2026-08-19. Where exact wording
> matters, quote the PDF rather than this file.

## NHS 365 - A Best Practices Guide for Transforming UK Healthcare with Microsoft AI

The National Health Service stands at a pivotal moment.

For more than seventy-five years it has embodied a simple, powerful promise: care based on need, free at the point of use. That promise remains as vital as ever.

Yet the pressures on the system have never been greater.

Rising demand, workforce shortages, ageing populations, complex multimorbidity, post-pandemic backlogs, and constrained budgets create a daily reality in which clinicians and managers must do more with less while still delivering safe, equitable, and compassionate care.

Technology alone will not solve these challenges. But the right technology, applied thoughtfully and at scale, can amplify the expertise of every nurse, doctor, therapist, administrator, and support worker. It can free time for human connection, surface insights hidden in vast clinical datasets, reduce administrative burden, and help shift care from reactive treatment to proactive prevention.

Among the most powerful enablers of this shift is the combination of Microsoft 365 and Microsoft’s broader AI capabilities—tools already familiar to many NHS organisations and increasingly capable of transforming how care is delivered, coordinated, and improved.

### NHS England’s Landmark Copilot Rollout

This urgency has taken on new significance with NHS England’s landmark decision to roll out Microsoft 365 Copilot to more than half a million healthcare workers.

As announced by Darren Hardman, CEO of Microsoft UK and Ireland, the deployment follows the largest AI trial of its kind in global healthcare. In that pilot, involving over 30,000 staff across 90 NHS organisations, participants saved an average of 43 minutes per person per day on administrative tasks—equivalent to roughly five working weeks per year. Scaled across the service, this represents the potential to reclaim millions of hours annually for direct patient care.

The rollout, expected to reach over 500,000 clinicians and support staff by October 2026, also includes access to Copilot Studio for building custom AI agents, backed by a comprehensive AI skilling programme.

### A Practical Guide for the People Driving Change

This book, *NHS 365 – A Best Practices Guide for Transforming UK Healthcare with Microsoft AI*, is written expressly to support this national rollout and the broader transformation it enables.

It is designed for the people who will make that transformation real: digital leaders, clinical informaticians, IT and cybersecurity teams, operational managers, and the clinicians who will ultimately use these tools at the bedside, in the clinic, and in the community. It is not a marketing brochure or a technical manual.

It is a practical guide grounded in the realities of the NHS—its governance frameworks, data protection requirements, clinical safety standards, funding constraints, and, above all, its unwavering focus on patients and staff. We explore how Microsoft 365, Microsoft Copilot, Azure AI services, Power Platform, and related technologies can be deployed responsibly and effectively across the healthcare landscape.

You will find patterns that have already delivered measurable value in NHS trusts and integrated care systems: reducing documentation time, improving multidisciplinary collaboration, accelerating insight from unstructured data, supporting population health management, and strengthening operational resilience.

Equally important, you will find honest discussion of the pitfalls—shadow AI, data quality issues, change fatigue, equity risks, and the critical need for clinical safety and information governance to be designed in from the start.

### Organised Around Real NHS Priorities

The chapters that follow are organised around real NHS priorities rather than product features.

We examine workforce productivity and wellbeing, clinical documentation and decision support, care coordination across organisational boundaries, operational excellence, research and innovation, and the foundational capabilities of security, identity, compliance, and responsible AI that make everything else possible.

Throughout, we emphasise best practices that respect NHS values, align with national strategies such as the Long Term Plan and the Data Strategy, and meet the rigorous standards expected by the Care Quality Commission, NHS England, and the Information Commissioner’s Office.

Transformation is not a single project or a one-time deployment. It is a continuous capability—built through clear vision, strong clinical and operational leadership, iterative delivery, measured outcomes, and a culture that treats technology as an enabler of better care rather than an end in itself. Microsoft’s AI tools offer unprecedented opportunity, but opportunity only becomes impact when it is guided by the expertise and judgement of those who understand the NHS from the inside.

This book aims to equip you with the practical knowledge, proven approaches, and critical questions needed to turn that opportunity into lasting improvement—especially as NHS England accelerates the Copilot rollout. The goal is straightforward: to help the NHS harness Microsoft AI so that every interaction with technology leaves more time, more insight, and more capacity for the people the service exists to serve.

The work of transformation is already underway in many places. With the national Copilot deployment now moving forward at pace, let us make it systematic, safe, equitable, and truly transformative.

## Strategic Architecture and Functional Deployment of Microsoft 365 within the NHS

The National Health Service (NHS) in England has undergone a major digital transformation by adopting Microsoft 365 (often referred to as N365) as its primary collaboration and productivity platform. This shift moves the organisation from a fragmented collection of local systems toward a more unified, cloud-based infrastructure serving approximately 1.5 million staff.

The change was driven by clear vulnerabilities exposed in the past and the practical demands of modern healthcare delivery.

### Drivers for Change

Historically, NHS trusts operated largely independent IT environments. Many relied on ageing on-premises servers and unsupported operating systems.

The 2017 WannaCry ransomware attack highlighted the risks of this approach: it disrupted services at 81 of 236 trusts, largely because outdated systems remained in use after a previous national enterprise agreement had expired. Individual organisations, often under financial pressure, struggled to fund timely upgrades.

The COVID-19 pandemic later accelerated the need for secure remote collaboration, video consultations, and reliable shared tools. In response, NHS bodies worked with Microsoft to establish the N365 agreement. This enabled the migration of roughly two million mailboxes and two petabytes of data into Exchange Online and established a standardised national framework for identity, security, and collaboration.

### Licensing Approach

To balance cost with operational needs, the NHS uses a tiered licensing model. The previous Office 365 E3R offering was replaced in early 2024 by two main services. The Standard Service, based on Microsoft 365 F3, targets frontline clinical staff and provides web-based Office applications, a 4 GB mailbox, and limited OneDrive storage.

The Enhanced Service, built on a restricted Microsoft 365 E3 Frontline Worker licence, serves managers, multidisciplinary team coordinators, and heavier administrative users. It offers larger mailboxes (50 GB), greater SharePoint allocation, and stronger security and compliance tools.

Both tiers include advanced identity protection through Entra ID P2. Local administrators retain flexibility: they can enable or disable specific applications such as Power Apps or Bookings through the NHSmail portal and purchase additional licences (for example Power BI or E5 features) where specialised needs exist.

NHS organisations choose between two main tenancy models according to their size, digital maturity, and appetite for local control.

The Shared NHS Tenant is the default for most organisations. Managed centrally by NHS Digital (with support from partners such as Accenture), it delivers economies of scale, consistent Data Loss Prevention policies, and national security baselines. Staff typically use the @nhs.net domain.

Local IT teams do not receive Global Administrator rights; instead they work through role-based access in the NHSmail portal and map policies to their Organisation Data Service codes. This protects the wider estate from misconfiguration but limits deep customisation, independent Graph API permissions, and certain Azure integrations. Any third-party connections must pass central Technical Design Authority review.

The Sovereign (or “own”) Tenant model gives larger trusts or Integrated Care Systems full administrative control. Organisations can run independent email domains (for example @trust.nhs.uk), manage their own Mobile Device Management policies, and integrate complex legacy clinical systems more freely.

The trade-off is significant: the trust assumes complete responsibility for security operations, compliance accreditation, and ongoing costs. It loses the protective layer of the central Cyber Security Operations Centre. To preserve collaboration, unidirectional cross-tenant synchronisation allows @nhs.net identities to appear in the local tenant without creating duplicate accounts.

The decision therefore balances centralised resilience against local innovation. Shared tenants suit organisations that prioritise standardisation and reduced management overhead; Sovereign tenants suit those whose clinical workflows demand specialised integrations that exceed central constraints.

### Identity, Authentication, and Directory Services

Identity forms the backbone of the N365 environment. TANSync (Tenant Active Directory Network Synchronization), built on Microsoft Identity Manager 2016 and supported by SQL Server, bridges on-premises Active Directory with the cloud. It uses outbound connections only (port 443) to communicate with NHSmail services, avoiding the need to open inbound firewall ports. The system automates the joiner-mover-leaver process so that licences and access are granted or revoked promptly. When a user is marked as a leaver, access is removed immediately and data is retained for a defined period.

Authentication is designed for clinical realities. Integration with the NHS Care Identity Service (CIS2) allows physical smartcards or FIDO2 tokens to satisfy multi-factor authentication requirements. Once a clinician authenticates with a smartcard at a workstation, Conditional Access policies can suppress additional mobile prompts, reducing friction in busy wards and clinics while maintaining security.

### Device Management

Endpoint management relies on the NHSmail Intune service and supports Windows Autopilot for zero-touch provisioning. Organisations follow either a pure cloud track (Azure AD join only) or a hybrid track that maintains domain-joined devices for legacy clinical applications such as PACS or laboratory systems.

The hybrid route requires additional infrastructure, including site-to-site VPNs and forest trusts. All managed devices inherit national security baselines aligned with NCSC guidance, including BitLocker encryption, Microsoft Defender for Endpoint, and application control policies.

### Artificial Intelligence, Automation, and Associated Risks

The NHS has invested substantially in technology modernisation, including a £120 million programme to deploy Microsoft 365 Copilot to around 505,000 staff after a successful pilot involving 30,000 users. Early results suggested average time savings of roughly 43 minutes per person per day. Copilot is treated as an administrative productivity tool rather than Software as a Medical Device.

Nevertheless, “clinical drift”—the gradual use of generative AI for summarising patient notes or supporting clinical discussion—introduces risks of hallucination, omission of critical details such as allergies, or incorrect synthesis of information.

Robotic Process Automation faces similar scrutiny. Unattended bots handling high-volume administrative work are not automatically approved for clinical data processes. Deployments require a Clinical Safety Case Report and formal sign-off by a Senior Information Risk Officer because silent failures could affect patient records.

All identifiable patient data processed by these tools must remain within UK Azure regions.

### Security and Clinical Safety Governance

Central telemetry from the Shared Tenant environment feeds the NHS Cyber Security Operations Centre, which monitors millions of endpoints using Microsoft Sentinel and Defender tools. Rapid response capability has been demonstrated during high-profile vulnerabilities.

Regulatory obligations include the Data Security and Protection Toolkit, the Secure Email Standard (DCB1596—pre-accredited for Shared Tenant users), and clinical risk management standards DCB0129 and DCB0160. The latter requires appointment of a Clinical Safety Officer who identifies hazards, assesses severity and likelihood, and ensures residual risk is reduced to a level that is as low as reasonably practicable before systems go live.

### Conclusion

The move to Microsoft 365 represents more than a technology upgrade; it is a structural change in how the NHS collaborates, protects data, and delivers care.

Organisations must weigh the operational simplicity and strong baseline security of the Shared Tenant against the flexibility—and greater responsibility—of a Sovereign Tenant. Critical decision factors include cyber maturity, the need for specialised integrations, the presence of legacy clinical systems that require hybrid identity, and the capacity to manage clinical safety governance for AI and automation.

Whatever architecture is chosen, the overriding requirement remains the same: digital innovation must support, rather than compromise, patient safety and the integrity of clinical information.

## NHS Workforce Transformation: Leveraging Microsoft 365 and Zensai for Best Practice 'Microlearning'

The National Health Service (NHS) faces a profound workforce crisis marked by high vacancies, slowing recruitment, and widespread burnout.

The service employs around 1.37 million full-time equivalent staff, yet vacancies stand at approximately 100,020—a 6.7% rate.

Recruitment growth has decelerated sharply, and sickness absence hovers near 5.1%, with psychiatric issues such as anxiety, stress, and depression accounting for roughly 30% of absences and hundreds of thousands of lost working days each month.

Nearly half of general practice staff report that hardware and software are unfit for purpose, contributing to cognitive overload that undermines both wellbeing and care delivery.

To meet rising demand, the NHS requires sustained productivity gains of 1.5–2% annually. National strategy emphasises “Train, Retain, Reform”: expanding and upskilling the workforce, improving retention, and shifting from reactive, hospital-centric care toward prevention and community-based models.

Digital transformation is central to this agenda. Evidence from digital maturity assessments shows that organisations in the top quartile of digital capability achieve about 8% higher overall productivity, 4% shorter average length of stay, better performance against elective care standards, and stronger oversight scores. Moving from fragmented analogue processes to digital-by-default operations is therefore not optional; it is essential for both operational sustainability and staff experience.

### Microsoft 365 as the Digital Backbone

Microsoft 365 (M365), delivered through the shared N365 tenant, provides a unified operating environment that reduces fragmentation and context-switching.

Core components—Teams, SharePoint, Outlook, Viva Engage, and Entra ID—create a single identity and collaboration layer. Single sign-on via Entra ID cuts password fatigue and administrative burden. By offering a coherent, secure experience inside the clinical workflow, trusts can reduce the appeal of “shadow IT”—unofficial tools staff adopt when official systems frustrate them.

This native ecosystem supports learning, performance management, and knowledge sharing without forcing clinicians to leave the applications they already use for handovers, multidisciplinary team meetings, and documentation. Data remains within the organisation’s own tenant, simplifying governance and supporting UK data residency requirements. The result is lower cognitive load, stronger security posture, and a platform on which specialised workforce tools can sit seamlessly.

### Zensai: Integrating Learning and Performance into Daily Work

Traditional learning management systems often function as passive repositories that staff must deliberately visit.

**Zensai** is built natively for Microsoft 365 and operates inside Teams, SharePoint, and Outlook. No separate logins or fragile integrations are required. Training can be auto-assigned via Entra ID groups according to role or specialty, and all records stay inside the trust’s existing security boundary.

Zensai is structured in tiers. The foundational layer delivers AI-supported course authoring, compliance tracking, and microlearning. A performance management layer adds structured 1:1 conversations, objectives and key results (OKRs), and 360-degree feedback.

The most advanced capability aggregates learning activity, performance data, and sentiment into a Human Success Score—an index that helps surface early signs of disengagement or burnout risk.

Integration with Microsoft Copilot enables practical AI assistance: summarising skills gaps ahead of appraisals, generating complete training modules (including quizzes) from clinical guidelines or standard operating procedures in minutes, and supporting reflective writing through voice-to-text tools.

### Microlearning and Communities of Practice

Clinical staff rarely have time for full-day classroom sessions. Microlearning—focused units typically under 15 minutes—fits better into busy schedules. Educators can prioritise content using a simple framework: material that is fatal if unknown, fundamental to daily practice, frequently used, fixed by policy, or useful for team cohesion. Complementary approaches such as short delivery followed by active teach-back help improve retention.

Virtual Communities of Practice further accelerate knowledge transfer. Hosted in Teams and Viva Engage, these groups enable specialist nurses and other professionals to share tacit expertise across organisational boundaries within Integrated Care Systems.

Evidence from clinical quality improvement work shows that well-supported communities can contribute to measurable reductions in infections and better outcomes in areas such as HIV care. Formal facilitation and clear purpose turn informal networking into a structured mechanism for spreading best practice.

### Streamlining Compliance and Revalidation

Statutory and mandatory training, professional revalidation, and leadership development generate significant administrative load. Initiatives such as standardised core modules that travel with staff between organisations reduce duplication. Within the M365 environment, automated reminders and transparent tracking of protected learning time become straightforward.

For Nursing and Midwifery Council and General Medical Council revalidation, the shift from episodic bureaucracy to continuous capture is particularly valuable. Practice hours can be logged via integrated systems; continuing professional development is recorded automatically from e-learning and webinars; peer and patient feedback accumulates through structured tools; and reflective accounts can be drafted with AI assistance shortly after shifts.

Leadership programmes, including those offered through the NHS Digital Academy, can link individual development plans directly to organisational objectives, ensuring academic learning translates into operational impact.

### Information Governance and Security

All solutions must meet rigorous NHS standards, including the Data Security and Protection Toolkit and Caldicott principles. Because Zensai operates inside the existing Microsoft tenant, personal data remains under the trust’s control. Existing tools such as Microsoft Purview can enforce policies that prevent inappropriate sharing of patient identifiers in collaborative channels. Certifications held by the platform further support organisational assurance.

### Practical Recommendations

Healthcare leaders can accelerate progress by consolidating onto the native Microsoft 365 ecosystem and retiring overlapping, siloed platforms. Microlearning modules should be prioritised and made available on mobile devices inside Teams.

Virtual Communities of Practice need dedicated clinical facilitation if they are to deliver sustained improvement. Predictive indicators such as engagement and success scores can guide early interventions that protect retention. Finally, revalidation and development activities should be designed to occur organically within daily workflows rather than as separate administrative events.

Taken together, a unified Microsoft 365 foundation combined with a natively integrated human success platform offers a practical route to higher productivity, better retention, and continuous improvement in care quality. By reducing friction, embedding learning in the flow of work, and turning professional development into a continuous rather than episodic activity, the NHS can better support its workforce while advancing the reforms required for future demand.

The technology already exists inside many trusts; the strategic opportunity lies in using it coherently to serve both staff and patients.

## Best Practices for Microsoft Teams Rooms in Healthcare

Deploying Microsoft Teams Rooms (MTR) in healthcare settings marks a major evolution beyond traditional audio-visual systems. It creates a unified communication platform that supports clinical workflows, enables remote collaboration, and integrates with electronic health records (EHRs).

Successful implementation demands careful attention to licensing, network design, security, clinical integration, specialized room configurations, ambient AI tools, and change management. When executed well, MTR becomes a core enabler of efficient, secure, and equitable care delivery.

### Licensing: Choosing Teams Rooms Pro

Licensing forms the foundation of any enterprise healthcare deployment. Microsoft offers a Basic tier at no cost, but it is inadequate for most hospitals. It limits deployments to 25 rooms per tenant and lacks advanced management, security integrations, and AI capabilities.

Teams Rooms Pro, priced at roughly $40 per room per month, removes room limits and includes a management portal with real-time telemetry, AI-based issue detection, Microsoft Intune integration, Defender for Endpoint, Entra ID P1 features, and advanced layouts such as Front Row and Together Mode. It also supports Copilot, IntelliFrame, and speaker recognition.

Standardizing on Pro typically delivers return on investment within 12 to 18 months through reduced helpdesk tickets and automated firmware updates. Compared with alternatives such as Zoom Rooms, it often provides meaningful licensing savings over a multi-year lifecycle for larger deployments while leveraging an organization’s existing Microsoft 365 security stack.

### Operating System Choices: Android vs. Windows

The choice of operating system should match the room’s clinical purpose. Android-based collaboration bars from vendors such as Poly, Logitech, and Yealink suit huddle spaces, small consultation rooms, and administrative areas. These all-in-one devices minimize cabling, simplify deployment, and benefit from the Microsoft Device Ecosystem Platform for improved security and manageability.

Windows-based systems are essential for complex environments such as multidisciplinary team (MDT) rooms, tumor boards, and training centers. They support modular peripherals, multiple cameras, advanced digital signal processors, and sophisticated ceiling microphone arrays. Hardware options include Lenovo ThinkSmart computes paired with Logitech Tap or Crestron Flex systems. Matching the OS to the space ensures both performance and long-term maintainability. Network Optimization and Quality of Service Clinical communication cannot tolerate jitter or dropped frames, especially when competing with large DICOM imaging files or EHR traffic. Quality of Service (QoS) with proper Differentiated Services Code Point (DSCP) markings is therefore mandatory. Recommended markings include DSCP 46 (Expedited Forwarding) for audio on UDP ports 50000–50019, DSCP 34 (Assured Forwarding AF41) for video on 50020–50039, DSCP 18 (AF21) for screen sharing on 50040–50059, and DSCP 40 (CS5) for signaling on 50070–50089.

Proxy configurations present another common pitfall. Teams Rooms does not support authenticated proxies. Administrators should set the ProxySettingsPerUser registry key to 0 for machine-wide proxy settings, create explicit exemptions for Microsoft 365 and Teams URLs, and deploy the full internal certificate chain if SSL inspection is in use. These steps prevent join failures and management agent issues after Windows updates.

### Security, Compliance, and Governance

MTR devices must be treated as critical endpoints subject to HIPAA, GDPR, and similar regulations. Zero-touch provisioning via Windows Autopilot and continuous monitoring with Microsoft Defender for Endpoint are standard. Secure boot should be enforced, USB mass storage disabled, and modifications to the local Skype user account avoided to prevent application breakage. Just-in-time access for maintenance further reduces risk.

Data lifecycle policies require careful configuration. Default Teams retention settings may conflict with clinical record-keeping requirements. Microsoft Purview can enforce appropriate retention—often six years for clinical consultations—while allowing shorter periods for administrative content. Data loss prevention policies help block accidental sharing of patient lists or financial information. Remote clinicians must follow strict protocols: private workspaces, no paper handling of sensitive material, and avoidance of public Wi-Fi. Clinical Integration and Telehealth Workflows The Microsoft Teams EHR connector transforms meeting rooms into virtual care hubs. Clinicians can launch visits directly from Epic Hyperspace/Haiku or Cerner PowerChart. Patients join via secure browser links without downloading an app, entering a branded virtual waiting room. Azure Communication Services helps bridge clinical data into the Teams session.

Virtual nursing models leverage the same infrastructure. One remote nurse can monitor multiple patients, contributing to reported reductions in falls with injury of around 39 percent. Mobile workstations and medical carts equipped with Teams Rooms hardware enable bedside specialist consultations. These carts need robust batteries (such as LiFePO4) for long shifts and IP54-rated protection to withstand rigorous cleaning with bleach solutions or hospital-grade wipes.

### Specialized Environments: MDT and Tumor Board Rooms

Multidisciplinary team rooms demand higher standards than typical conference spaces. Displays must support DICOM Part 14 GSDF calibration so grayscale accuracy for MRI, CT, and PET images matches diagnostic workstations. Ceiling beamforming microphone arrays, such as the Shure MXA920 or Sennheiser TCC2, provide zero-touch infection control and AI-driven tracking of presenters as they move and gesture toward images.

Environmental design also matters. Lighting should achieve a high Color Rendering Index (CRI of 90 or better in many cases) for accurate tissue and slide representation. Acoustic performance targets, such as NC-30 or appropriate Sound Transmission Class ratings, protect patient privacy and prevent sound leakage. Ambient Clinical Intelligence with DAX Copilot Microsoft’s Dragon Ambient eXperience (DAX) Copilot, stemming from the Nuance acquisition, addresses documentation burden—a major contributor to clinician burnout. The system passively captures conversations and generates structured SOAP notes within seconds, often saving several minutes per encounter and contributing to substantial reported reductions in burnout.

Pricing typically ranges from roughly $369 to $600 per provider per month. Lower-cost alternatives exist but may lack deep EHR write-back. Governance is non-negotiable. Large language models carry hallucination rates of 1–3 percent, so every note requires human review, editing, and signature before it becomes part of the legal medical record. Patients must be informed and given an opt-out option, and Business Associate Agreements must ensure audio data is not used to train public models.

### Change Management and Measuring Success

Technology alone does not guarantee adoption. Organizations should identify clinical champions among physicians and nurses to lead pilots and advocate for the tools. Training must focus on practical workflows—such as sharing a DICOM image—rather than hardware specifications.

Key performance indicators include room utilization data from the Pro Management Portal, reductions in documentation time, nursing staff retention linked to virtual support models, and clinician satisfaction scores. Monitoring these metrics helps refine the deployment and demonstrate value.

### Conclusion

Microsoft Teams Rooms in healthcare has evolved from a simple conferencing upgrade into a sophisticated clinical platform.

By standardizing on Teams Rooms Pro licensing, selecting the right operating system for each space, enforcing network prioritization and strong security controls, integrating with EHRs, designing specialized diagnostic rooms to clinical standards, carefully governing ambient AI, and investing in change management, healthcare organizations can improve collaboration, reduce administrative burden, enhance patient safety, and support better outcomes. Success rests on meticulous planning that aligns technology with the realities of clinical care and regulatory requirements.

## Evolution of the NHS Care Identity Service Architecture

The **NHS Care Identity Service (CIS)**, and specifically its modern authentication component **CIS2 Authentication**, is the national identity and access management platform for health and social care professionals in England.

It enables secure, auditable sign-in to national clinical systems, Spine services, and many third-party applications that handle patient data.

The NHS Care Identity Service (CIS), and particularly its modern authentication component CIS2 Authentication, serves as the national identity and access management platform for health and social care professionals in England.

It enables secure, auditable sign-in to national clinical systems, Spine services, and many third-party applications handling patient data. Supporting more than 1.3 million workers and handling tens of millions of authentications each month, access is managed locally by Registration Authorities (RAs). These bodies issue Care Identities, assign role-based access control (RBAC) positions, and control authenticators.

### From CIS1 to CIS2

CIS1, the legacy system, relied almost exclusively on physical NHS smartcards and required a connection to the Health and Social Care Network (HSCN). It used the older Spine Security Broker / Identity Agent approach, along with proprietary elements such as Java applets and Internet Explorer 11 support. This closed-loop model created significant technical debt and limited flexibility for a mobile workforce.

CIS2 is the strategic, internet-facing replacement. Built on OpenID Connect (OIDC) standards, it supports a much wider range of authenticators and operates over the public internet rather than depending solely on HSCN. CIS1 is deprecated and scheduled for full retirement by the end of February 2027.

All new integrations must use CIS2. The service runs at a platinum level with 24/7 support and high availability (targeting 99.9% uptime). Historical data has shown hundreds of millions of authentications in multi-month periods, with growing volumes from mobile and non-smartcard methods.

### Supported Authenticators and Assurance Levels

Authenticators are classified by NIST Authenticator Assurance Levels:

**AAL3 (very high confidence)** — required for the most sensitive applications: physical NHS smartcards (via CIS2 Smartcard Connect software, usable over the internet or HSCN), FIDO2 security keys (such as YubiKeys), Windows Hello (in supported configurations), and certain high-assurance passkeys.

**AAL2 (high confidence)** — suitable for many applications: Microsoft Authenticator app, NHS.net Connect (formerly NHSmail) credentials combined with Microsoft Authenticator, standard passkeys, and iPad app authentication.

Users can often self-register modern authenticators against their Care Identity profile. Smartcards remain common on shared clinical workstations and kiosks. The shift reduces hardware-tethered constraints while preserving strong security for primary clinical record modifications, prescribing, and highly sensitive data access.

### How Integration Works for Developers

CIS2 Authentication acts as an OIDC identity provider. A typical flow is:

1. The user launches a healthcare application.
2. The application redirects the browser to the CIS2 authentication endpoint.
3. The user authenticates with their chosen method.
4. CIS2 returns an ID token (and optionally an access token) containing identity claims, a unique user ID (UUID), basic profile data, and national RBAC roles/permissions.
5. The application uses this information for session creation and authorisation, and may call the userinfo endpoint for additional attributes.

Key capabilities include strong multi-factor authentication without building it in-house, retrieval of national RBAC permissions, support for back-channel logout and session management, and an optional “Care Identity” branded login button.

The recommended cryptographic pathway is the Authorization Code Flow with Proof Key for Code Exchange (PKCE). This protects against authorization code interception. Architects are strongly advised to implement the Backend-for- Frontend (BFF) pattern so that tokens never reside in the browser, mitigating XSS and token theft risks. Tokens are managed server-side, with the browser communicating via secure HTTP-only cookies.

Onboarding typically takes 6 weeks to 3 months: engage with NHS England Digital, design and build the OIDC integration, test in Path-to-Live environments, complete technical and clinical safety assurance, sign a Connection Agreement, and go live. CIS2 is required for NHS England staff-facing applications and third-party apps accessing national “user-restricted” APIs; it is strongly recommended for other health and social care software needing MFA.

### Integration with Microsoft 365 / NHSmail / Entra ID

In the NHS Microsoft 365 (N365 / NHSmail) environment, CIS2 reduces authentication friction. Authenticating with an NHS smartcard or other strong CIS2 authenticator (such as a FIDO2 key) can satisfy multi-factor requirements in Microsoft Entra ID Conditional Access policies.

Users are often not prompted again for a separate Microsoft Authenticator challenge when accessing Teams, Outlook, SharePoint, and related services. This is especially valuable in high-pressure clinical settings. NHSmail credentials can themselves serve as a CIS2 authenticator for AAL2 applications once linked to a Care Identity. Local administrators manage policies via security groups, named locations, and other Conditional Access features.

### Practical Considerations for Organisations

Registration Authorities remain central for identity proofing, role assignment, and smartcard lifecycle management, though self-service options (including Apply for Care ID and smartcard unlock) have expanded. Device setup for smartcards now uses CIS2 Smartcard Connect plus Credential Management, supporting Windows 10/11, modern browsers, and standard internet connections.

It replaces the older Identity Agent; legacy Identity Agent versions are scheduled for structural blocking by February 2027. Clinical safety and governance standards (including DCB0160 where applicable) continue to apply. Organisations must plan migration of any remaining CIS1-dependent applications ahead of the 2027 deadline. Hardware is moving toward Series 10 smartcards with SHA-2 hashing.

Importantly, session behaviour has changed: removing a smartcard no longer automatically logs the user out of all applications (as in CIS1). Sessions must be terminated manually or via application inactivity timers.

CIS combines Role-Based Access Control (RBAC) and Position-Based Access Control (PBAC). National R-codes define job roles (examples include Clinical Practitioner R8000, Health Professional R8003, Receptionist R8009). Granular B-codes grant specific activities, such as viewing or updating Summary Care Records. PBAC further restricts access by Organisation Data Service (ODS) codes.

Clinicians who work across multiple organisations select the appropriate profile at login; the selected_roleid and ODS code appear in the JWT for precise audit trails supporting clinical governance and financial processes.

### Governance, Identity Lifecycle, and Risks

Compliance is demonstrated primarily through the Data Security and Protection Toolkit (DSPT), aligned with the National Cyber Security Centre’s Cyber Assessment Framework. Identity proofing has been modernised via the GPG45-compliant “Apply for Care ID” platform, which supports remote biometric checks (photo ID upload and facial video) alongside database uniqueness validation.

A persistent human risk is smartcard sharing, which undermines non-repudiation and patient safety investigations. CIS2 mitigates this by expanding frictionless options such as biometrics and high-assurance passkeys. Cross-border differences (for example, Scotland’s CHI identifier and SWAN network versus England’s NHS Number and internet-first model) require careful handling for interoperability. Automated systems must follow Secure Robot Authentication standards rather than relying on static credentials.

### Benefits and Strategic Direction

CIS2 modernises authentication for a mobile and hybrid workforce while maintaining the high assurance levels required for clinical systems.

It reduces dependence on the restricted HSCN network, supports a broader range of devices, and enables improved single sign-on experiences across national and local systems—including closer alignment with the Microsoft 365 estate used by most NHS staff. Looking ahead to 2027 and beyond, the roadmap emphasises full CIS1 retirement, API modernisation, expanded self-service for authenticators, and continued emphasis on open standards.
