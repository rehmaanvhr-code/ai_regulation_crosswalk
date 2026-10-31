# Obligations for case: customer_chatbot

Large language model assistant that answers account questions and helps customers file disputes.

Inputs: use case customer_service, data types personal, conversational, decision impact low, regions canada, us, eu, generative True.

## Frameworks in scope

EU AI Act (Regulation 2024/1689) (law). Binding for providers and deployers placing AI systems on the EU market or whose outputs are used in the EU. Most obligations fall on high risk systems listed in Annex III, which includes creditworthiness assessment of natural persons.

Canada AIDA (Bill C-27, Part 3) (proposed law). The Artificial Intelligence and Data Act was introduced in 2022 as part of Bill C-27 and died on the order paper when Parliament was prorogued in January 2025. Included here because it shaped Canadian expectations and because a successor bill is widely expected. Treat all references as the last published draft and companion document.

NIST AI RMF 1.0 (2023) (voluntary framework). Voluntary. Organised into four functions: Govern, Map, Measure, Manage. The Generative AI Profile (NIST AI 600 1, 2024) adds actions for generative systems.

ISO/IEC 42001:2023 (certifiable standard). AI management system standard. Clauses 4 to 10 set the management system, Annex A lists controls, Annex B gives implementation guidance.

OSFI Guideline E-23 Model Risk Management (2025) (regulatory guideline). Applies to federally regulated financial institutions in Canada from May 2027. Expands the 2017 version to cover all models including AI and machine learning, and introduces a model lifecycle with risk based intensity.

Colorado AI Act (SB 24-205) (law). Covers developers and deployers of high risk AI systems that make or are a substantial factor in consequential decisions, including lending and financial services. Effective date was pushed to June 30, 2026 by SB 25B 004.

## Coverage by theme

| Theme | aida | colorado_ai_act | eu_ai_act | iso_42001 | nist_ai_rmf | osfi_e23 |
|---|---|---|---|---|---|---|
| Accountability and governance roles | recommended | required | required | required | recommended | required |
| Bias and fairness testing | required | required | required | recommended | recommended | recommended |
| Data governance and quality | required | recommended | required | required | recommended | required |
| Technical documentation and model cards | required | required | required | required | recommended | required |
| Generative and general purpose model duties | recommended | recommended | required | no | recommended | recommended |
| Incident reporting | required | required | required | recommended | recommended | recommended |
| Post deployment monitoring | required | recommended | required | required | recommended | required |
| Record keeping and logging | required | required | required | required | recommended | required |
| Risk classification and scoping | required | required | required | required | recommended | required |
| Third party and vendor management | no | required | required | required | recommended | required |
| Transparency to affected persons | required | required | required | required | recommended | recommended |

## Obligations

### Risk classification and scoping

EU AI Act (Regulation 2024/1689) (required, Art. 6 and Annex III; Art. 5 prohibited practices): Classify the system against the prohibited list and the Annex III high risk use cases. Creditworthiness and insurance pricing for natural persons are high risk.

Canada AIDA (Bill C-27, Part 3) (required, s. 7 and proposed regulations on high impact systems): Assess whether the system is a high impact system under the regulations. The companion document named decisions about services, employment and credit.

NIST AI RMF 1.0 (2023) (recommended, Map 1.1 to Map 1.5): Establish context, intended purpose and the level of risk the organisation is willing to tolerate.

ISO/IEC 42001:2023 (required, Clause 6.1.2 and A.5 AI system impact assessment): Run an AI risk assessment and an impact assessment proportionate to the system.

OSFI Guideline E-23 Model Risk Management (2025) (required, Section 2 model risk rating): Assign a model risk rating that drives the intensity of validation and monitoring.

Colorado AI Act (SB 24-205) (required, s. 6-1-1701(9) definition of high risk AI system): Determine if the system makes or is a substantial factor in a consequential decision.

### Data governance and quality

EU AI Act (Regulation 2024/1689) (required, Art. 10): Training, validation and testing data must meet quality criteria, be examined for bias and be relevant and representative.

Canada AIDA (Bill C-27, Part 3) (required, s. 6 anonymised data; s. 8 measures to identify and mitigate risk): Establish measures for how anonymised data is used and mitigate risks of harm and biased output.

NIST AI RMF 1.0 (2023) (recommended, Map 2.3, Measure 2.1, Measure 2.2): Document data provenance, representativeness and test set independence.

ISO/IEC 42001:2023 (required, A.7 data for AI systems): Controls on data acquisition, quality, provenance and preparation.

OSFI Guideline E-23 Model Risk Management (2025) (required, Section 3 model lifecycle: data): Data used in models must be fit for purpose, traceable and controlled; expectations scale with model risk.

Colorado AI Act (SB 24-205) (recommended, s. 6-1-1702(3) developer documentation on data): Developers must describe the data used to train the system and known limitations.

### Technical documentation and model cards

EU AI Act (Regulation 2024/1689) (required, Art. 11 and Annex IV): Technical documentation covering general description, development process, monitoring, performance metrics and risk management.

Canada AIDA (Bill C-27, Part 3) (required, s. 11 record keeping and s. 12 publication of plain language description): Keep records of mitigation measures and publish a plain language description of a high impact system.

NIST AI RMF 1.0 (2023) (recommended, Govern 1.4, Map 3.4, Measure 2.8): Document the system, its intended uses and evaluation methods; model cards and datasheets are named practices.

ISO/IEC 42001:2023 (required, Clause 7.5 and A.6.2.7 documentation): Maintain documented information on the AI system through its lifecycle.

OSFI Guideline E-23 Model Risk Management (2025) (required, Section 3 model development and documentation): Model documentation must allow an independent party to understand and replicate the model.

Colorado AI Act (SB 24-205) (required, s. 6-1-1702(2) and (3)): Developers must give deployers documentation on intended use, data, performance, limitations and known risks of algorithmic discrimination.

### Transparency to affected persons

EU AI Act (Regulation 2024/1689) (required, Art. 13, Art. 26(11), Art. 50, Art. 86): Instructions for use, notice to natural persons subject to high risk decisions, chatbot disclosure, and a right to explanation of individual decisions.

Canada AIDA (Bill C-27, Part 3) (required, s. 12 plain language description): Publish a plain language description of how the system is used and the decisions it makes.

NIST AI RMF 1.0 (2023) (recommended, Measure 2.8, Measure 2.9): Transparency and explainability are listed trustworthiness characteristics to be measured.

ISO/IEC 42001:2023 (required, A.8 information for interested parties): Provide information on the AI system to users and affected parties.

OSFI Guideline E-23 Model Risk Management (2025) (recommended, Section 3 model use): Explainability expectations rise with model risk, but the guideline speaks to internal users rather than customers.

Colorado AI Act (SB 24-205) (required, s. 6-1-1703(3) and (4), s. 6-1-1704): Deployers must notify consumers before a consequential decision, give reasons for adverse decisions and disclose interaction with AI.

### Bias and fairness testing

EU AI Act (Regulation 2024/1689) (required, Art. 10(2)(f) and (g), Art. 9): Examine data for possible biases that lead to discrimination and take measures to detect and correct them.

Canada AIDA (Bill C-27, Part 3) (required, s. 8 and definition of biased output in s. 5): Establish measures to identify, assess and mitigate risks of biased output.

NIST AI RMF 1.0 (2023) (recommended, Measure 2.11): Fairness and bias are evaluated and results documented.

ISO/IEC 42001:2023 (recommended, A.5.4 and B.5.4 impact assessment on individuals and groups): Assess impacts on individuals and groups including fairness.

OSFI Guideline E-23 Model Risk Management (2025) (recommended, Section 3 validation and Annex on AI/ML): Validation should test for unintended bias where models affect customers; expectations align with conduct obligations.

Colorado AI Act (SB 24-205) (required, s. 6-1-1703(2) impact assessment): Deployers must complete an impact assessment covering known or foreseeable risks of algorithmic discrimination.

### Post deployment monitoring

EU AI Act (Regulation 2024/1689) (required, Art. 72 and Art. 26(5)): Providers must run a post market monitoring system; deployers must monitor operation per instructions.

Canada AIDA (Bill C-27, Part 3) (required, s. 9 monitoring of mitigation measures): Monitor compliance with mitigation measures and their effectiveness.

NIST AI RMF 1.0 (2023) (recommended, Manage 4.1, Measure 3.1): Monitor deployed systems and track risks over time.

ISO/IEC 42001:2023 (required, Clause 9.1 and A.6.2.6 operation and monitoring): Monitor, measure and evaluate AI system performance in operation.

OSFI Guideline E-23 Model Risk Management (2025) (required, Section 3 model monitoring): Ongoing monitoring with thresholds and escalation, frequency set by model risk rating.

Colorado AI Act (SB 24-205) (recommended, s. 6-1-1703(2)(c) annual review of impact assessment): Impact assessments must be reviewed at least annually and after substantial modification.

### Incident reporting

EU AI Act (Regulation 2024/1689) (required, Art. 73): Providers report serious incidents to market surveillance authorities within set deadlines.

Canada AIDA (Bill C-27, Part 3) (required, s. 12 notification of material harm): Notify the Minister as soon as feasible if use of the system results or is likely to result in material harm.

NIST AI RMF 1.0 (2023) (recommended, Manage 4.3, Govern 4.3): Processes for incident response and sharing incident information.

ISO/IEC 42001:2023 (recommended, Clause 10.2 and A.6.2.8 event logging): Treat AI incidents as nonconformities and keep event logs.

OSFI Guideline E-23 Model Risk Management (2025) (recommended, Section 4 governance and escalation): Escalate model failures internally; regulatory reporting flows through existing OSFI incident expectations.

Colorado AI Act (SB 24-205) (required, s. 6-1-1702(5) and s. 6-1-1703(7)): Developers and deployers must notify the Attorney General within 90 days of discovering algorithmic discrimination.

### Third party and vendor management

EU AI Act (Regulation 2024/1689) (required, Art. 25 and Art. 53 for general purpose model providers): Responsibilities along the value chain; deployers that substantially modify become providers.

Canada AIDA (Bill C-27, Part 3): not addressed. The draft placed obligations on whoever makes the system available or manages its operation, without a separate vendor regime.

NIST AI RMF 1.0 (2023) (recommended, Govern 6.1, Govern 6.2, Map 4.1): Policies for third party software, data and models, including contingency when they fail.

ISO/IEC 42001:2023 (required, A.10 third party and customer relationships): Allocate responsibilities with suppliers and ensure supplier processes meet the organisation's requirements.

OSFI Guideline E-23 Model Risk Management (2025) (required, Section 3 and link to Guideline B-10): Vendor and open source models are in scope; institutions remain accountable for validation and monitoring.

Colorado AI Act (SB 24-205) (required, s. 6-1-1702 developer duties to deployers): Developers must furnish deployers with the information needed for impact assessments.

### Record keeping and logging

EU AI Act (Regulation 2024/1689) (required, Art. 12, Art. 19, Art. 26(6)): Automatic logging over the lifetime; providers and deployers keep logs at least six months.

Canada AIDA (Bill C-27, Part 3) (required, s. 10 and s. 11): Keep records of the assessment, mitigation measures and monitoring.

NIST AI RMF 1.0 (2023) (recommended, Govern 1.5, Measure 2.1): Keep records of risk management decisions and evaluation results.

ISO/IEC 42001:2023 (required, Clause 7.5.3 and A.6.2.8): Control documented information and log events through operation.

OSFI Guideline E-23 Model Risk Management (2025) (required, Section 4 model inventory): Maintain an enterprise model inventory with status, rating and ownership.

Colorado AI Act (SB 24-205) (required, s. 6-1-1703(2)(e) retention): Retain impact assessments and records for at least three years after final deployment.

### Accountability and governance roles

EU AI Act (Regulation 2024/1689) (required, Art. 9, Art. 17, Art. 26): Risk management system and quality management system for providers; deployer duties.

Canada AIDA (Bill C-27, Part 3) (recommended, Companion document on accountability framework): An accountability framework with roles, training and policies was expected to be set by regulation.

NIST AI RMF 1.0 (2023) (recommended, Govern 1.1 to Govern 2.2): Policies, roles and senior accountability for AI risk.

ISO/IEC 42001:2023 (required, Clause 5 leadership, A.3 internal organisation): Top management commitment, policy and defined roles.

OSFI Guideline E-23 Model Risk Management (2025) (required, Section 4 governance framework): Senior management owns the model risk framework; independent review function; clear model owner, developer, validator roles.

Colorado AI Act (SB 24-205) (required, s. 6-1-1703(1) risk management policy): Deployers must adopt a risk management policy and program; NIST AI RMF or ISO 42001 are named as reference frameworks.

### Generative and general purpose model duties

EU AI Act (Regulation 2024/1689) (required, Art. 50(2), Art. 53 to Art. 55): Mark synthetic content; general purpose model providers keep technical documentation, copyright policy and training summary; systemic risk models face evaluation and incident duties.

Canada AIDA (Bill C-27, Part 3) (recommended, Minister's November 2023 proposed amendments): Proposed amendments would have added obligations for general purpose systems and machine learning models.

NIST AI RMF 1.0 (2023) (recommended, NIST AI 600 1 Generative AI Profile): Actions for confabulation, information integrity, harmful content and data privacy specific to generative systems.

ISO/IEC 42001:2023: not addressed. No generative specific controls; general controls apply.

OSFI Guideline E-23 Model Risk Management (2025) (recommended, Annex on AI and machine learning models): Generative models are models; explainability and monitoring expectations are heightened where outputs are not deterministic.

Colorado AI Act (SB 24-205) (recommended, s. 6-1-1704 disclosure of AI interaction): Consumers must be told when they are interacting with an AI system.
