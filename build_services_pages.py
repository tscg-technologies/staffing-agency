"""
STAFFING AGENCY — 17 Individual Staffing Service Pages Generator
Generates:
1. permanent-staffing.html
2. temporary-staffing.html
3. contract-staffing.html
4. temp-to-hire.html
5. executive-search.html
6. bulk-hiring.html
7. campus-recruitment.html
8. it-staffing.html
9. healthcare-staffing.html
10. industrial-staffing.html
11. blue-collar-staffing.html
12. white-collar-staffing.html
13. skilled-workforce.html
14. unskilled-workforce.html
15. payroll-staffing.html
16. recruitment-process-outsourcing.html
17. project-based-staffing.html
"""

from generate_helpers import render_page, render_placeholder
from build_site_part1 import register_image, write_html

SERVICES_DATA = [
    {
        "slug": "permanent-staffing",
        "title": "Permanent Staffing",
        "badge": "Direct Hire",
        "image": "staffing-permanent-recruitment.jpg",
        "image_desc": "HR executive welcoming a newly appointed permanent employee to a modern corporate office",
        "prompt": "Commercial corporate photograph of an HR manager warmly shaking hands with a newly hired professional in a bright contemporary office foyer with glass architecture. Natural sunlight, confident smiles, business formal attire, subtle branding in background.",
        "lead": "Strategic end-to-end talent sourcing for long-term direct hire organizational roles across professional and technical domains.",
        "overview": "Permanent staffing is engineered for organizations seeking core talent to drive sustained long-term growth. Our methodology encompasses detailed requirement mapping, active market sourcing, comprehensive credential verification, and structured interview facilitation to ensure cultural and technical alignment.",
        "roles": ["Department Managers", "Software Engineers", "Financial Accountants", "HR Business Partners", "Operations Managers", "Sales Directors"],
        "employer_reqs": "Clear job descriptions, defined salary bands, specified technical prerequisites, interview panel availability, and formal employment terms.",
        "candidate_reqs": "Proven industry track record, documented employment history, verified academic credentials, and commitment to long-term career growth.",
        "workflow": [
            ("Role Discovery", "Defining organizational objectives, reporting structures, and core competencies."),
            ("Candidate Sourcing", "Targeted outreach across industry networks and passive talent pools."),
            ("Rigorous Screening", "Competency interviews, credential checks, and reference validations."),
            ("Interview Coordination", "Facilitating multi-stage interviews and panel debriefs."),
            ("Offer & Joining Support", "Assisting in offer discussions and notice period transition management.")
        ],
        "benefits": ["Secures long-term institutional knowledge", "Reduces repetitive recruitment cycles", "Strengthens organizational stability", "Ensures cultural alignment with team values"],
        "related": [("Temporary Staffing", "temporary-staffing.html"), ("Executive Search", "executive-search.html"), ("White-Collar Staffing", "white-collar-staffing.html")],
        "faqs": [
            ("How long does permanent recruitment typically take?", "Timelines vary depending on role seniority and market specialization. Typical search cycles range between two to six weeks from requirement finalization to candidate offer acceptance."),
            ("Who makes the final hiring decision?", "The client employer always retains complete autonomy over final interview evaluations, candidate selection, and employment offers.")
        ]
    },
    {
        "slug": "temporary-staffing",
        "title": "Temporary Staffing",
        "badge": "Contingent Workforce",
        "image": "staffing-temporary-workforce.jpg",
        "image_desc": "Supervisory manager briefing a group of temporary warehouse and logistics workers before a shift",
        "prompt": "Industrial corporate photograph of a logistics supervisor in high-visibility vest holding a digital clipboard and briefing a diverse team of warehouse staff in a modern, clean distribution center. Natural skylights, organized racks, professional posture.",
        "lead": "Agile, scalable workforce deployments designed to accommodate seasonal surges, project peaks, and planned leave coverage.",
        "overview": "Temporary staffing provides businesses with immediate access to qualified personnel on short-term assignments. Whether covering maternity leave, ramping up for seasonal retail demands, or managing manufacturing volume, temporary staff help maintain operational continuity without inflating fixed payroll commitments.",
        "roles": ["Warehouse Associates", "Customer Service Reps", "Assembly Line Staff", "Administrative Assistants", "Inventory Clerks", "Data Entry Operators"],
        "employer_reqs": "Defined assignment duration, clear shift schedules, safety gear specifications (where applicable), and on-site supervisor contacts.",
        "candidate_reqs": "Immediate availability, willingness to work defined shifts, strong punctuality, and flexibility in adapting to client workplaces.",
        "workflow": [
            ("Demand Sizing", "Determining necessary headcount, shift rotas, and assignment dates."),
            ("Rapid Pool Mobilization", "Activating pre-vetted candidate rosters available for immediate placement."),
            ("Orientation Briefing", "Communicating workplace safety, location guidelines, and schedule parameters."),
            ("On-Site Deployment", "Coordinating attendance check-in and initial supervisor introductions."),
            ("Assignment Administration", "Managing timesheet records and replacement coverage if needed.")
        ],
        "benefits": ["Prevents operational bottlenecks during peak seasons", "Mitigates long-term overhead and severance liabilities", "Rapid fulfillment speed for urgent headcount needs", "Workforce elasticity aligned to real-time revenue cycles"],
        "related": [("Temp-to-Hire", "temp-to-hire.html"), ("Contract Staffing", "contract-staffing.html"), ("Bulk Hiring", "bulk-hiring.html")],
        "faqs": [
            ("What is the typical duration of a temporary assignment?", "Assignments can span from a single week to several months, depending on the client's operational schedule and seasonal workload."),
            ("Can temporary staff be converted to permanent roles?", "Yes, employers may explore transition pathways through our structured temp-to-hire conversion model.")
        ]
    },
    {
        "slug": "contract-staffing",
        "title": "Contract Staffing",
        "badge": "Fixed-Term Engagements",
        "image": "staffing-contract-staffing.jpg",
        "image_desc": "Specialized software engineer working on an enterprise cloud infrastructure contract assignment",
        "prompt": "Modern commercial photograph of a technical contractor working on dual high-resolution displays showing cloud infrastructure code in a contemporary co-working environment. Natural window lighting, focused posture, clean minimal aesthetic.",
        "lead": "Targeted fixed-term professional engagements for time-bound initiatives, system upgrades, and technical delivery.",
        "overview": "Contract staffing bridges critical skill gaps by embedding specialized professionals for a predetermined timeframe. Organizations benefit from elite domain expertise without long-term employment commitments, making it ideal for software development sprints, plant retrofits, and financial audits.",
        "roles": ["Cloud Architects", "DevOps Engineers", "ERP Implementation Consultants", "Regulatory Compliance Auditors", "Interim Project Managers", "Cybersecurity Analysts"],
        "employer_reqs": "Documented scope of work, project milestones, duration parameters, system access provisions, and performance deliverables.",
        "candidate_reqs": "Specialized domain mastery, independent execution capability, familiarity with milestone-driven delivery, and contractual flexibility.",
        "workflow": [
            ("Milestone Scoping", "Reviewing technical deliverables, architecture stack, and project lifecycle."),
            ("Specialist Mapping", "Sourcing niche contractors with matching technical proficiencies."),
            ("Technical Evaluation", "Assessing practical project portfolios and problem-solving acumen."),
            ("Contract Alignment", "Establishing fixed engagement terms, SLA milestones, and confidentiality terms."),
            ("Milestone Delivery Tracking", "Ongoing contract coordination and periodic milestone reviews.")
        ],
        "benefits": ["Rapid access to hard-to-find specialized skill sets", "Predictable project budgeting with fixed-term terms", "Eliminates permanent bench costs after project completion", "Accelerates critical digital and infrastructure rollouts"],
        "related": [("Project-Based Staffing", "project-based-staffing.html"), ("IT Staffing", "it-staffing.html"), ("Permanent Staffing", "permanent-staffing.html")],
        "faqs": [
            ("How does contract staffing differ from consulting?", "Contract staffing places dedicated professionals directly under your day-to-day technical direction, whereas consulting often involves third-party project ownership."),
            ("Can contract durations be extended?", "Yes, engagements can be extended upon mutual agreement between the client employer and the contractor prior to expiry.")
        ]
    },
    {
        "slug": "temp-to-hire",
        "title": "Temp-to-Hire Staffing",
        "badge": "Performance Evaluation Model",
        "image": "staffing-candidate-interview.jpg",
        "image_desc": "Hiring manager conducting a mid-assignment performance review with a temp-to-hire candidate",
        "prompt": "Professional corporate photograph of an operations director discussing performance notes with a professional employee across an open office desk. Friendly supportive demeanor, clean modern corporate environment, natural daylight.",
        "lead": "Evaluate on-the-job competency, attendance reliability, and cultural alignment before extending a permanent offer.",
        "overview": "Temp-to-hire provides a risk-mitigated hiring pathway. An employee begins on a temporary basis for an agreed evaluation period (commonly 3 to 6 months). During this time, the employer observes real-world problem solving, team interaction, and productivity, while the candidate evaluates the organizational culture.",
        "roles": ["Inside Sales Representatives", "Quality Assurance Analysts", "Junior Software Developers", "Customer Success Coordinators", "HR Associates", "Executive Assistants"],
        "employer_reqs": "Clear evaluation criteria, scheduled review milestones, transparent conversion benchmarks, and equitable compensation terms upon offer.",
        "candidate_reqs": "Commitment to demonstrating high performance, willingness to undergo the trial period, and desire for eventual permanent integration.",
        "workflow": [
            ("Trial Framework Setup", "Defining probation duration, evaluation criteria, and permanent conversion terms."),
            ("Candidate Selection", "Sourcing candidates interested in long-term employment through an initial trial."),
            ("Trial Period Deployment", "Active work on assignment under temporary staffing terms."),
            ("Performance Review", "Structured 60-day and 90-day progress reviews between manager and candidate."),
            ("Permanent Conversion", "Transitioning the candidate to the client's direct payroll upon mutual consent.")
        ],
        "benefits": ["Significantly reduces permanent hiring mis-hires", "Provides candidates with authentic workplace insights", "Smooth onboarding transition from contingent to core team", "Minimizes organizational disruption"],
        "related": [("Temporary Staffing", "temporary-staffing.html"), ("Permanent Staffing", "permanent-staffing.html"), ("Contract Staffing", "contract-staffing.html")],
        "faqs": [
            ("Is permanent conversion guaranteed in temp-to-hire?", "No. Conversion to permanent employment is strictly subject to performance evaluations, business needs, and mutual agreement between employer and candidate."),
            ("What happens if a candidate is not a cultural fit?", "The employer can conclude the temporary assignment cleanly at any stage within the agreed trial period without permanent severance procedures.")
        ]
    },
    {
        "slug": "executive-search",
        "title": "Executive Search",
        "badge": "Leadership Sourcing",
        "image": "staffing-executive-search.jpg",
        "image_desc": "Executive search consultant meeting privately with a senior C-suite executive candidate",
        "prompt": "Refined executive commercial photograph of two senior business professionals engaged in a discreet discussion in an executive penthouse lounge overlooking a skyline. Elegant navy suits, soft ambient evening twilight, premium architectural interior.",
        "lead": "Discreet, confidential talent mapping and headhunting for senior leadership, board-level, and executive appointments.",
        "overview": "Executive search addresses senior leadership roles where public job postings are inappropriate or ineffective. Our consultants conduct confidential market mapping, approaching established leaders discreetly to evaluate strategic vision, governance acumen, and transformative management capability.",
        "roles": ["Chief Technology Officer (CTO)", "Chief Financial Officer (CFO)", "VP of Global Operations", "Director of Human Resources", "Chief Information Security Officer (CISO)", "Managing Director"],
        "employer_reqs": "Confidentiality briefing, defined executive mandates, compensation benchmarks including equity/incentives, and board panel interview schedules.",
        "candidate_reqs": "Proven multi-year organizational leadership, P&L responsibility, strategic turnaround experience, and verified industry reputation.",
        "workflow": [
            ("Mandate Discovery", "Deep dive into corporate vision, governance priorities, and executive criteria."),
            ("Confidential Market Mapping", "Discreet research identifying passive leaders in relevant industry verticals."),
            ("Preliminary Executive Dialogues", "Confidential exploratory discussions assessing alignment and appetite."),
            ("Comprehensive Vetting", "Leadership assessments, deep reference inquiries, and credential audits."),
            ("Offer Structuring & Close", "Advising on compensation parity, bonus structures, and executive onboarding.")
        ],
        "benefits": ["Guaranteed confidentiality for sensitive organizational transitions", "Access to top 5% of passive leadership talent not on job boards", "Rigorous vetting of leadership track records and governance ethics", "Strategic alignment with long-term enterprise valuation"],
        "related": [("Permanent Staffing", "permanent-staffing.html"), ("Recruitment Consulting", "recruitment-consulting.html"), ("White-Collar Staffing", "white-collar-staffing.html")],
        "faqs": [
            ("Why is executive search conducted confidentially?", "Discretion protects both the hiring organization's strategic initiatives and the current professional standing of participating executives."),
            ("How are executive references verified?", "We conduct comprehensive 360-degree reference inquiries with former board members, direct reports, and professional peers.")
        ]
    },
    {
        "slug": "bulk-hiring",
        "title": "Bulk Hiring",
        "badge": "Mass Recruitment",
        "image": "staffing-bulk-hiring.jpg",
        "image_desc": "A coordinated high-volume recruitment drive room with multiple candidate screening desks",
        "prompt": "Commercial photograph of a large, well-organized corporate recruitment hall with multiple numbered screening booths where candidates are being interviewed concurrently. Bright overhead lighting, professional signage, orderly queues, professional corporate atmosphere.",
        "lead": "Rapid deployment sourcing funnels designed to mobilize large workforce volumes for facility openings and seasonal expansions.",
        "overview": "Bulk hiring requires specialized operational logistics, high-throughput candidate screening frameworks, and multi-channel advertising campaigns. Designed to fill dozens or hundreds of positions simultaneously, our bulk recruitment workflows maintain quality benchmarks while meeting tight ramp-up deadlines.",
        "roles": ["Contact Center Agents", "Warehouse Sorters & Pickers", "Retail Store Associates", "Assembly Handlers", "Bank Branch Clerks", "Field Sales Executives"],
        "employer_reqs": "Aggregate headcount targets, phased mobilization schedules, standardized role specifications, and designated verification teams.",
        "candidate_reqs": "Fundamental domain aptitude, willingness to complete batch assessments, readiness for fast-track onboarding, and valid document compliance.",
        "workflow": [
            ("Campaign Planning", "Multi-channel advertising, community drives, and sourcing outreach setup."),
            ("High-Throughput Funnels", "Automated resume parsing and preliminary phone/digital screening."),
            ("Batch Assessment Days", "Coordinated group evaluation centers, skill testing, and face-to-face interviews."),
            ("Concurrent Documentation Checks", "Rapid identity verification, police checks, and credential validation."),
            ("Cohort Onboarding", "Batch induction coordination, uniform distribution, and facility introduction.")
        ],
        "benefits": ["Fulfills large headcount targets within compressed timelines", "Significantly reduces cost-per-hire via economies of scale", "Standardized testing ensures uniform minimum competency", "Structured cohorts improve early retention and morale"],
        "related": [("Campus Recruitment", "campus-recruitment.html"), ("Blue-Collar Staffing", "blue-collar-staffing.html"), ("Industrial Staffing", "industrial-staffing.html")],
        "faqs": [
            ("How does bulk hiring maintain candidate quality?", "We implement standardized, multi-gate scoring rubrics and document verifications to ensure all placed candidates satisfy agreed threshold competencies."),
            ("What is the lead time needed for a bulk hiring campaign?", "Typically, campaign planning and candidate mobilization require 2 to 4 weeks prior to the target start date.")
        ]
    },
    {
        "slug": "campus-recruitment",
        "title": "Campus Recruitment",
        "badge": "Graduate Programs",
        "image": "staffing-candidate-registration.jpg",
        "image_desc": "University campus hiring event where recent graduates are registering with recruitment coordinators",
        "prompt": "Vibrant corporate photograph of university students in business attire attending an on-campus corporate recruitment booth. Banners with modern geometric motifs, digital tablets for registration, bright auditorium lighting, professional engaging atmosphere.",
        "lead": "Coordinated university engagement campaigns and aptitude assessments to onboard promising entry-level graduate cohorts.",
        "overview": "Campus recruitment bridges academic institutions and enterprise employers, identifying high-potential university graduates for entry-level associate roles and management trainee programs. We coordinate college relations, technical screening drives, and assessment centers.",
        "roles": ["Graduate Trainee Engineers (GTE)", "Junior Business Analysts", "Associate Software Developers", "Management Trainees", "Sales Associates", "Clinical Lab Interns"],
        "employer_reqs": "Academic cutoff criteria (e.g. GPA or degree requirements), program training outlines, salary tiers, and preferred university tiers.",
        "candidate_reqs": "Final-year standing or recent graduation, demonstrated academic performance, foundational theoretical knowledge, and eagerness to learn.",
        "workflow": [
            ("Campus Engagement", "Partnering with university placement cells and scheduling campus drive dates."),
            ("Aptitude & Technical Testing", "Administering proctored cognitive and domain-specific tests."),
            ("Group Discussions & Interviews", "Evaluating communication skills, teamwork, and problem-solving agility."),
            ("Conditional Offer Rollout", "Issuing provisional offers pending final academic semester completion."),
            ("Induction Transition", "Supporting transition from academia into corporate training programs.")
        ],
        "benefits": ["Builds a predictable annual pipeline of energetic fresh talent", "Facilitates customized in-house training for company-specific tools", "High digital literacy and enthusiasm for modern workplace practices", "Cost-effective foundation for organizational succession planning"],
        "related": [("Bulk Hiring", "bulk-hiring.html"), ("IT Staffing", "it-staffing.html"), ("White-Collar Staffing", "white-collar-staffing.html")],
        "faqs": [
            ("Do campus drives cover both undergraduate and postgraduate cohorts?", "Yes, campaigns can be structured for Bachelor's, Master's, or specialized technical diploma programs."),
            ("How are joining dates handled for graduating students?", "Offers are phased to coincide with academic calendar completions and corporate induction cycles.")
        ]
    },
    {
        "slug": "it-staffing",
        "title": "IT Staffing",
        "badge": "Technology & Engineering",
        "image": "staffing-it-professionals.jpg",
        "image_desc": "Software developers and cloud engineers collaborating on code across modern dual-screen workstations",
        "prompt": "Clean modern tech company photograph of two software engineers—one woman, one man—looking at code on multiple vertical and horizontal monitors in an open collaborative office. Soft daylight, clean desk, modern headphones, tech company styling.",
        "lead": "Technical vetting and placement of software developers, cloud architects, DevOps specialists, data engineers, and cybersecurity analysts.",
        "overview": "Information technology staffing demands rigorous technical validation, deep market insight, and rapid turnaround. Our dedicated IT recruiters assess hands-on coding proficiency, system architecture acumen, and modern cloud proficiencies across frontend, backend, data, and infrastructure tracks.",
        "roles": ["Software Developer", "Frontend Developer", "Backend Developer", "Full Stack Developer", "Data Analyst", "Data Engineer", "Cloud Engineer", "DevOps Engineer", "Cybersecurity Analyst", "QA Engineer", "Business Analyst"],
        "employer_reqs": "Technology stack specifications, architectural requirements, experience seniority (junior/mid/senior), remote/hybrid arrangements, and coding test parameters.",
        "candidate_reqs": "Demonstrable software development track record, code repository portfolio (GitHub/GitLab), solid algorithmic understanding, and continuous learning mindset.",
        "workflow": [
            ("Technical Discovery", "Analyzing application architecture, tech stack versions, and delivery methodologies."),
            ("Targeted Tech Sourcing", "Tapping developer networks, open-source communities, and technical repositories."),
            ("Code & Practical Assessment", "Evaluating practical problem-solving through standardized coding evaluations."),
            ("Architecture Interviews", "Coordinating technical panels with client engineering leads and architects."),
            ("Placement & Sprint Onboarding", "Ensuring repo access, credential setup, and sprint integration.")
        ],
        "benefits": ["Access to pre-screened developers capable of immediate codebase contribution", "Accelerates critical feature roadmaps and digital modernization programs", "Reduces engineering lead time spent on preliminary candidate filtering", "Flexible permanent, contract, or squad-based engagement options"],
        "related": [("Contract Staffing", "contract-staffing.html"), ("Project-Based Staffing", "project-based-staffing.html"), ("Permanent Staffing", "permanent-staffing.html")],
        "faqs": [
            ("Do you support both contract and permanent IT placements?", "Yes, we support both direct hire permanent software engineering roles and time-bound contract engagements for agile sprints."),
            ("How do you verify developer technical claims?", "Our vetting combines code review challenges, technical panel evaluations, and verification of past project deliverables.")
        ]
    },
    {
        "slug": "healthcare-staffing",
        "title": "Healthcare Staffing",
        "badge": "Clinical & Support Talent",
        "image": "staffing-healthcare-workers.jpg",
        "image_desc": "Licensed healthcare support professionals in scrubs reviewing patient record logs in a medical clinic corridor",
        "prompt": "Clean, bright commercial healthcare photograph of healthcare professionals wearing hospital scrubs and lab coats in a sterile modern clinic corridor. Natural daylight, compassionate confident expressions, digital tablet in hand, warm professional medical lighting.",
        "lead": "Credentialed clinical assistants, nursing support personnel, medical administration, and allied health staff.",
        "overview": "Healthcare staffing requires unwavering dedication to patient safety, strict regulatory compliance, and rigorous credential verification. We assist hospitals, diagnostic clinics, and residential care facilities in securing qualified medical support staff and healthcare administrative professionals.",
        "roles": ["Nurses", "Healthcare Assistants", "Medical Administrative Staff", "Lab Technicians", "Pharmacy Professionals", "Healthcare Support Staff"],
        "employer_reqs": "Facility accreditation mandates, shift rotas (day/night/weekend), patient-to-staff ratio requirements, and required jurisdiction health department registrations.",
        "candidate_reqs": "Valid medical council / nursing board registration, verified clinical training transcripts, active basic life support certifications, and immunizations.",
        "workflow": [
            ("Clinical Mandate Intake", "Defining patient care scope, departmental specializations, and shift coverage."),
            ("Registry & Credential Verification", "Conducting primary source verification with regional health licensing authorities."),
            ("Clinical Competency Reviews", "Evaluating healthcare protocols, patient privacy compliance, and situational response."),
            ("Facility Credentialing", "Submitting verification dossiers to hospital medical review boards."),
            ("Shift Integration", "Coordinating clinical orientation, EHR system training, and unit introduction.")
        ],
        "benefits": ["Maintains required patient-to-staff ratios during surge periods", "Rigorous primary source credentialing minimizes institutional liability", "Reduces clinical staff burnout through reliable shift coverage", "Supports planned leaves, specialized diagnostic campaigns, and unit expansions"],
        "related": [("Temporary Staffing", "temporary-staffing.html"), ("Permanent Staffing", "permanent-staffing.html"), ("Skilled Workforce", "skilled-workforce.html")],
        "faqs": [
            ("What licensing verifications are performed for healthcare staff?", "Regulated healthcare positions strictly require appropriate qualifications, registration, verification, and jurisdiction-specific authorization before placement."),
            ("Do you supply staff for emergency short-term hospital shifts?", "Yes, we maintain rosters of credentialed healthcare assistants available for scheduled per-diem and temporary assignment coverage.")
        ]
    },
    {
        "slug": "industrial-staffing",
        "title": "Industrial Staffing",
        "badge": "Plant & Production",
        "image": "staffing-industrial-workforce.jpg",
        "image_desc": "Industrial machine operators and quality maintenance technicians in an automated plant facility",
        "prompt": "Industrial documentary photograph of plant operators wearing safety helmets, protective goggles, and work gear operating advanced CNC machinery in a clean automated manufacturing plant. Bright industrial overhead lighting, focused precision, sparks from precision cutting in distant background.",
        "lead": "Reliable machine operators, maintenance technicians, quality inspectors, and industrial plant supervisors.",
        "overview": "Industrial staffing addresses the rigorous talent requirements of automated factories, fabrication units, and processing facilities. We recruit safety-conscious operators and technicians who ensure production lines run efficiently, machinery is maintained, and safety compliance is rigorously preserved.",
        "roles": ["Production Operators", "Machine Operators", "Quality Inspectors", "Maintenance Technicians", "Warehouse Workers", "Industrial Supervisors"],
        "employer_reqs": "Machinery specifications, shift rotation policies, OSHA / industrial safety gear mandates, and production output targets.",
        "candidate_reqs": "Vocational certifications (ITI/diploma), proven machine operation experience, strict adherence to safety protocols, and physical stamina.",
        "workflow": [
            ("Plant Needs Assessment", "Evaluating production machinery, shift schedules, and safety classifications."),
            ("Technical Trade Sourcing", "Mobilizing candidate networks through trade schools and regional technical registries."),
            ("Machine Competency Evaluation", "Verifying practical equipment operation and blueprint/schematic reading."),
            ("Workplace Safety Orientation", "Mandatory briefing on PPE usage, emergency shut-offs, and hazard prevention."),
            ("Plant Floor Deployment", "Coordination with plant managers for shift assignments and time tracking.")
        ],
        "benefits": ["Minimizes expensive line downtime caused by operator shortages", "Trained technicians lower industrial scrap rates and improve yields", "Strict safety vetting protects workforce health and reduces workplace incidents", "Scalable shift additions aligned with raw material deliveries and order batches"],
        "related": [("Blue-Collar Staffing", "blue-collar-staffing.html"), ("Manufacturing Industry", "manufacturing.html"), ("Temporary Staffing", "temporary-staffing.html")],
        "faqs": [
            ("Are operators trained on specific machinery brands?", "We match candidates based on their documented operational history with specific equipment categories (e.g. CNC mills, plastic extruders, packaging lines)."),
            ("How is industrial workplace safety managed?", "Candidates undergo mandatory safety awareness briefings and must comply fully with all host employer plant safety regulations.")
        ]
    },
    {
        "slug": "blue-collar-staffing",
        "title": "Blue-Collar Staffing",
        "badge": "Ground Workforce",
        "image": "staffing-warehouse-workers.jpg",
        "image_desc": "Warehouse ground crew and forklift operators organizing dispatched pallets in a logistics facility",
        "prompt": "Commercial photograph of warehouse workers in high-vis vests and safety boots organizing boxed inventory near a loading dock. Modern logistics hub, forklift parked in background, bright clean facility, teamwork and positive energy.",
        "lead": "Warehouse associates, delivery support staff, drivers, helpers, maintenance technicians, and field workforce personnel.",
        "overview": "Blue-collar staffing keeps the physical economy moving. From distribution centers and freight terminals to field maintenance and assembly lines, we recruit, verify, and mobilize dedicated ground workers who ensure physical products are handled with care and delivered on schedule.",
        "roles": ["Warehouse Associates", "Delivery Support Staff", "Drivers", "Helpers", "Technicians", "Production Workers", "Field Workers"],
        "employer_reqs": "Physical lifting parameters, valid driver licenses (for transport roles), shift rosters, and location accessibility instructions.",
        "candidate_reqs": "Punctuality, physical fitness, valid identity documentation, and readiness for manual or mechanical material handling.",
        "workflow": [
            ("Workforce Sizing", "Determining required ground crews, shift bands, and hub locations."),
            ("Regional Mobilization", "Local outreach and candidate registration drives in surrounding residential zones."),
            ("Identity & Police Verification", "Systematic background cross-checks and physical verification."),
            ("Assignment Briefing", "Orientation on shift timings, transportation routes, and hub conduct rules."),
            ("Shift Coordination", "Daily attendance reconciliation and buffer workforce management.")
        ],
        "benefits": ["Reliable workforce attendance during heavy dispatch cycles", "Reduces localized turnover through proactive candidate relationship support", "Fast replacement dispatch if primary staff are unavailable", "Full regulatory documentation handling for peace of mind"],
        "related": [("Industrial Staffing", "industrial-staffing.html"), ("General Workforce", "unskilled-workforce.html"), ("Logistics Industry", "logistics-transportation.html")],
        "faqs": [
            ("How do you ensure punctual attendance for early morning shifts?", "We deploy localized recruitment models prioritizing workers residing near client distribution hubs, supplemented by attendance monitoring."),
            ("Can you supply seasonal loaders for festive sales spikes?", "Yes, we regularly support high-volume seasonal ramp-ups with temporary warehouse and loading staff.")
        ]
    },
    {
        "slug": "white-collar-staffing",
        "title": "White-Collar Staffing",
        "badge": "Corporate & Administrative",
        "image": "staffing-employer-meeting.jpg",
        "image_desc": "Office executives collaborating in a glass-walled conference room in a corporate headquarters",
        "prompt": "Corporate lifestyle photograph of business executives—accountants, HR specialists, and analysts—reviewing performance charts in a bright, modern corporate office. Clean wood table, coffee cups, laptops, natural morning daylight.",
        "lead": "Administrative executives, HR specialists, accountants, customer support executives, sales executives, and operations managers.",
        "overview": "White-collar staffing provides organizations with skilled knowledge workers who manage essential day-to-day business processes. From managing corporate ledgers to handling customer accounts and coordinating HR initiatives, our candidates possess strong communication, analytical, and software tool proficiencies.",
        "roles": ["Administrative Executives", "HR Executives", "Accountants", "Customer Support Executives", "Sales Executives", "Business Analysts", "Operations Executives"],
        "employer_reqs": "Role responsibilities, software prerequisites (ERP, CRM, Excel, HRIS), reporting hierarchy, and required language proficiencies.",
        "candidate_reqs": "Bachelor's degree or professional business qualification, verified prior administrative experience, and strong interpersonal communication skills.",
        "workflow": [
            ("Functional Role Mapping", "Defining operational workflows, reporting metrics, and departmental duties."),
            ("Professional Network Sourcing", "Reaching verified corporate candidates seeking mid-tier and senior career growth."),
            ("Behavioral & Tool Screening", "Testing business software capabilities (spreadsheets, CRM, accounting tools)."),
            ("Stakeholder Interviews", "Scheduling structured interviews with department heads and team peers."),
            ("Onboarding & Role Integration", "Assisting in documentation submission and workstation briefing.")
        ],
        "benefits": ["Maintains seamless administrative and financial operations", "Skilled corporate executives require minimal procedural ramp-up time", "Fills unexpected corporate vacancies without disruption to ongoing client services", "Available across direct-hire permanent or flexible interim contract models"],
        "related": [("Permanent Staffing", "permanent-staffing.html"), ("Recruitment Consulting", "recruitment-consulting.html"), ("IT Staffing", "it-staffing.html")],
        "faqs": [
            ("Do you screen candidates on specific accounting software?", "Yes, for financial candidates we evaluate hands-on familiarity with popular ERP and accounting software platforms."),
            ("Can corporate administrative roles be filled on contract terms?", "Yes, we provide both permanent and contract white-collar placements to support seasonal accounting audits or leave cover.")
        ]
    },
    {
        "slug": "skilled-workforce",
        "title": "Skilled Workforce Staffing",
        "badge": "Certified Specialists",
        "image": "staffing-manufacturing-workers.jpg",
        "image_desc": "Certified precision welder and electrical maintenance technician inspecting industrial machinery",
        "prompt": "Industrial commercial photograph of a certified technician in safety gear using a digital multimeter to test electrical panels in an industrial manufacturing setting. Crisp detail, clean industrial background, focused concentration, professional workshop lighting.",
        "lead": "Certified technicians, precision machinists, licensed electricians, and vocational trade specialists.",
        "overview": "Skilled workforce staffing connects industrial and commercial enterprises with certified trade professionals possessing formal vocational qualifications. We verify trade licenses, technical apprenticeship records, and hands-on diagnostic abilities to ensure high technical competency.",
        "roles": ["Certified Electricians", "Precision Machinists", "Industrial Welders", "HVAC Technicians", "Instrumentation Specialists", "PLC Programmers"],
        "employer_reqs": "Mandatory trade certification levels, electrical or mechanical schematic standards, safety credentials, and tool ownership requirements.",
        "candidate_reqs": "Recognized vocational trade diploma (ITI, NVQ, City & Guilds or regional equivalent), documented apprenticeship hours, and safety track record.",
        "workflow": [
            ("Trade Requisition Review", "Outlining specific technical schematics, tooling standards, and safety classifications."),
            ("Trade Registry Sourcing", "Activating accredited vocational alumni networks and technical associations."),
            ("Practical Skill Verification", "Confirming trade certificates, license validity, and safety accreditation."),
            ("Technical Interview & Practical Test", "Client technical foreman review and practical shop floor demonstration."),
            ("Deployment & Tool Briefing", "Safety protocol sign-off and project floor deployment.")
        ],
        "benefits": ["Ensures all technical works comply with engineering codes and statutory standards", "Reduces equipment damage risks through certified operational competence", "Provides certified technicians for complex maintenance shutdowns and revamps", "Protects workplace health and safety compliance records"],
        "related": [("Industrial Staffing", "industrial-staffing.html"), ("Construction Industry", "construction.html"), ("General Workforce", "unskilled-workforce.html")],
        "faqs": [
            ("Are trade licenses independently checked?", "Yes, we verify trade licenses and apprenticeship certificates against issuing vocational authorities prior to placement."),
            ("Can skilled technicians be contracted for facility shutdowns?", "Yes, we regularly assemble specialist teams for planned maintenance turnarounds and installation sprints.")
        ]
    },
    {
        "slug": "unskilled-workforce",
        "title": "General Workforce Staffing",
        "badge": "General Support",
        "image": "staffing-warehouse-workers.jpg",
        "image_desc": "General workforce team assisting with physical facility organization and material handling",
        "prompt": "Clean documentary photograph of facility helpers and material handlers wearing clean uniforms and gloves moving cartons in a well-lit logistics environment. Organized warehouse aisle, natural skylight, neat uniform appearance.",
        "lead": "General utility staff, facility helpers, ground workforce assistants, and manual handling personnel.",
        "overview": "General workforce staffing provides dependable, hard-working support personnel for tasks that do not require specialized technical certifications but demand reliability, physical stamina, and strong work ethic. We ensure thorough identity checks, address verifications, and punctuality monitoring.",
        "roles": ["Facility Helpers", "Carton Loaders & Unloaders", "Ground Cleanup Staff", "Material Shifters", "Packing Assistants", "Office Messengers"],
        "employer_reqs": "Specific physical duties, safety equipment provision, shift schedules, and direct supervisor instructions.",
        "candidate_reqs": "Reliability, readiness for physical work, valid national identity documentation, and good conduct record.",
        "workflow": [
            ("Volume & Shift Assessment", "Determining headcounts and work shift parameters."),
            ("Community Mobilization", "Local candidate registration and identity documentation collection."),
            ("Verification & Compliance", "ID verification and address validation."),
            ("Conduct & Safety Briefing", "Orientation on workplace behavior, punctuality, and facility rules."),
            ("On-Site Dispatch", "Coordinated team deployment with supervisor attendance sign-offs.")
        ],
        "benefits": ["Relieves core technical staff from routine physical handling tasks", "Scalable volume staffing on short notice for loading/unloading cycles", "Verified identity documentation ensures site security compliance", "Cost-effective staffing model for high-volume manual tasks"],
        "related": [("Blue-Collar Staffing", "blue-collar-staffing.html"), ("Temporary Staffing", "temporary-staffing.html"), ("Bulk Hiring", "bulk-hiring.html")],
        "faqs": [
            ("How do you ensure site security with general workforce personnel?", "All workers undergo strict national identity verification, residence confirmation, and entry register documentation."),
            ("What is the replacement protocol if a worker fails to report?", "We maintain an active stand-by reserve to dispatch replacement staff promptly to minimize operational disruption.")
        ]
    },
    {
        "slug": "payroll-staffing",
        "title": "Payroll & Staffing Administration",
        "badge": "Administrative Operations",
        "image": "staffing-office-team.jpg",
        "image_desc": "HR administration team consolidating attendance sheets and workforce documentation records",
        "prompt": "Corporate photograph of HR operations staff working on desktop spreadsheets and filing folders in an organized administrative office. Soft ambient lighting, dual monitors, clean corporate setting.",
        "lead": "Employee documentation, attendance administration, timesheet coordination, and payroll data preparation.",
        "overview": "Managing the administrative logistics of a sizable contingent workforce can strain internal HR teams. Our payroll and staffing administration services handle the day-to-day clerical workflows—including employee onboarding files, biometric attendance aggregation, timesheet verification, and structured payroll data formatting.",
        "roles": ["HR Administration Assistants", "Timesheet Coordinators", "Attendance Officers", "Payroll Data Executives", "Compliance Filing Clerks"],
        "employer_reqs": "Agreed pay cycle schedules, attendance recording format (biometric/manual), timesheet approval authorities, and reporting formats.",
        "candidate_reqs": "Accurate bank account details, signed attendance logs, submitted tax declaration forms, and timely timesheet submissions.",
        "workflow": [
            ("Documentation Onboarding", "Collecting candidate identity, bank details, and statutory forms."),
            ("Attendance Aggregation", "Collecting and reconciling daily attendance and shift logs."),
            ("Timesheet Verification", "Securing client supervisor approvals for billable hours and overtime."),
            ("Payroll Data Formulation", "Calculating gross pay figures and generating structured payroll disbursement sheets."),
            ("Record Archival", "Maintaining auditable employee files and compliance documentation records.")
        ],
        "benefits": ["Relieves internal HR and finance departments from repetitive data entry", "Reduces timesheet disputes through structured client manager sign-offs", "Ensures organized, auditable documentation records for contingent workers", "Transparent reporting provides clear workforce expenditure visibility"],
        "related": [("Recruitment Process Outsourcing", "recruitment-process-outsourcing.html"), ("Temporary Staffing", "temporary-staffing.html"), ("Workforce Solutions", "workforce-solutions.html")],
        "faqs": [
            ("Does this service include employer-of-record or statutory tax representation?", "No. This service provides administrative coordination, documentation management, and payroll data preparation only. It does not make legal, statutory compliance, or employer-of-record claims."),
            ("How are timesheets validated?", "Timesheets require explicit written or digital sign-off from authorized client managers before processing.")
        ]
    },
    {
        "slug": "recruitment-process-outsourcing",
        "title": "Recruitment Process Outsourcing (RPO)",
        "badge": "End-to-End Recruitment",
        "image": "staffing-team-collaboration.jpg",
        "image_desc": "An outsourced talent acquisition squad conducting structured hiring pipeline reviews",
        "prompt": "Modern executive commercial photograph of a four-person talent acquisition team gathered around a wall-mounted digital pipeline dashboard displaying candidate progress funnels. Bright corporate studio lighting, confident professional posture.",
        "lead": "Transfer part or all of your internal recruitment workflows under dedicated talent acquisition teams and SLA frameworks.",
        "overview": "Recruitment Process Outsourcing (RPO) embeds dedicated recruitment expertise directly into your talent infrastructure. Acting as an extension of your internal HR team, our RPO consultants manage candidate sourcing, screening, interview coordination, applicant tracking, and hiring metrics under clear service level agreements.",
        "roles": ["Embedded RPO Lead", "Dedicated Sourcing Specialists", "Recruitment Coordinators", "Candidate Screening Interviewers", "Talent Analytics Manager"],
        "employer_reqs": "Target hiring volume projections, access to internal ATS / requisition workflows, defined SLA benchmarks, and designated HR executive sponsors.",
        "candidate_reqs": "Participation in structured multi-stage application assessments and adherence to scheduled evaluation timelines.",
        "workflow": [
            ("Operating Model Design", "Mapping current hiring workflows, defining SLAs, and integrating applicant tracking."),
            ("Team Onboarding & Alignment", "Deploying dedicated recruiters trained on employer brand and job specifications."),
            ("Full-Cycle Sourcing Execution", "Proactive multi-channel sourcing, screening, and interview scheduling."),
            ("Hiring Manager Coordination", "Conducting regular requisition reviews and interview feedback debriefs."),
            ("Analytics & Continuous Tuning", "Monthly SLA reporting on time-to-hire, funnel conversion, and source quality.")
        ],
        "benefits": ["Transforms fixed recruitment overhead into scalable operational expense", "Dramatically improves candidate experience and employer brand resonance", "Standardized screening workflows improve overall quality-of-hire", "Comprehensive talent analytics provide full visibility into recruiting funnels"],
        "related": [("Talent Acquisition", "talent-acquisition.html"), ("Bulk Hiring", "bulk-hiring.html"), ("Recruitment Consulting", "recruitment-consulting.html")],
        "faqs": [
            ("What is the difference between RPO and traditional staffing?", "Traditional staffing fills specific vacancies on a transactional basis. RPO involves managing end-to-end recruitment operations, technology workflows, and employer branding for an entire department or company."),
            ("Can an RPO model be deployed for a specific division only?", "Yes, project-based or modular RPO can be tailored specifically for engineering, sales, or customer service teams.")
        ]
    },
    {
        "slug": "project-based-staffing",
        "title": "Project-Based Staffing",
        "badge": "Dedicated Project Squads",
        "image": "staffing-team-collaboration.jpg",
        "image_desc": "Multidisciplinary project delivery team reviewing milestone Gantt charts in a high-tech conference room",
        "prompt": "Commercial photograph of a dynamic multidisciplinary project squad analyzing software milestone charts on a whiteboard and laptops. Modern tech studio setting, collaborative energy, navy and slate styling, bright natural light.",
        "lead": "Assemble tailored multidisciplinary project squads for defined enterprise deliverables and technology sprints.",
        "overview": "When organizations launch complex technical transformations or strategic initiatives, assembling individual contractors piecemeal creates coordination friction. Project-based staffing provides fully formed, complementary project squads—including technical leads, developers, and QA analysts—aligned to specific milestone deliverables.",
        "roles": ["Project Leads", "Scrum Masters", "Senior Full Stack Engineers", "QA Automation Engineers", "Data Migration Specialists", "Technical Writers"],
        "employer_reqs": "Project charter, milestone release schedules, architectural constraints, security clearance protocols, and acceptance criteria.",
        "candidate_reqs": "Proven track record in agile project environments, cross-functional collaboration skills, and commitment for the project lifecycle.",
        "workflow": [
            ("Sprint & Scope Analysis", "Analyzing project milestones, team composition, and tech stack dependencies."),
            ("Squad Assembly", "Curating balanced squads with complementary technical competencies."),
            ("Coordinated Integration", "Simultaneous onboarding of the squad into client collaboration systems."),
            ("Sprint Execution & Delivery", "Active contribution toward defined sprint deliverables and reviews."),
            ("Knowledge Transfer & Ramp-Down", "Documented knowledge handover before orderly project conclusion.")
        ],
        "benefits": ["Immediate team synergy without the drag of individual onboarding cycles", "Milestone-aligned staffing avoids premature or lagging resource allocation", "Minimizes project risk through balanced, pre-vetted skill combinations", "Clean conclusion upon milestone sign-off without permanent overhead"],
        "related": [("Contract Staffing", "contract-staffing.html"), ("IT Staffing", "it-staffing.html"), ("Workforce Solutions", "workforce-solutions.html")],
        "faqs": [
            ("How quickly can a project squad be deployed?", "Squad assembly typically takes 2 to 4 weeks depending on the technical complexity and team size."),
            ("Does the squad work on-site or remotely?", "Squads can be structured for on-site client facility collaboration, fully remote execution, or hybrid arrangements.")
        ]
    }
]

def make_all_service_pages():
    for s in SERVICES_DATA:
        # Register image
        register_image(
            s["image"], f"{s['slug']}.html", "Service Hero & Overview",
            s["image_desc"], "16:9", "1200x800", "Landscape",
            s["prompt"], "Wide landscape shot with subjects engaged in professional workflow",
            "Eye-level medium shot", "Natural balanced corporate lighting",
            "Modern professional office or facility environment", "High-end commercial corporate photography",
            "Navy blue, corporate slate, bright blue, teal accent", "Subjects centered in midground"
        )

        # Build workflow steps HTML
        steps_html = ""
        for i, (title, desc) in enumerate(s["workflow"], 1):
            teal_class = "teal" if i % 2 == 0 else ""
            steps_html += f"""
            <div class="process-step">
              <div class="step-number {teal_class}">{i}</div>
              <h4 class="step-title" style="font-size: 1.05rem;">{title}</h4>
              <p class="step-text">{desc}</p>
            </div>
            """

        # Build roles HTML
        roles_html = "".join([f'<span class="tag-badge" style="font-size: 0.85rem; padding: 0.35rem 0.85rem;">{r}</span>' for r in s["roles"]])

        # Build benefits HTML
        benefits_html = "".join([f'<li style="margin-bottom: 0.75rem; display: flex; gap: 0.5rem; align-items: flex-start;"><svg style="width: 18px; height: 18px; color: var(--color-teal-accent); flex-shrink: 0; margin-top: 0.2rem;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg><span>{b}</span></li>' for b in s["benefits"]])

        # Build related services HTML
        related_html = "".join([f'<div class="card" style="padding: 1.5rem;"><h4 style="margin-bottom: 0.5rem;"><a href="{url}">{name}</a></h4><p class="text-muted" style="font-size: 0.85rem; margin-bottom: 0.75rem;">Explore related workforce capabilities.</p><a href="{url}" class="card-link" style="font-size: 0.85rem;">View Service &rarr;</a></div>' for name, url in s["related"]])

        # Build FAQs HTML
        faqs_html = ""
        for i, (q, a) in enumerate(s["faqs"]):
            active_cls = "active" if i == 0 else ""
            exp = "true" if i == 0 else "false"
            faqs_html += f"""
            <div class="accordion-item {active_cls}">
              <button class="accordion-header" type="button" aria-expanded="{exp}">
                <span>{q}</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">{a}</div>
            </div>
            """

        content = f"""
        <!-- Service Hero -->
        <section class="page-hero">
          <div class="container">
            <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">{s["badge"]}</span>
            <h1>{s["title"]}</h1>
            <p class="lead">{s["lead"]}</p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="request-staff.html" class="btn btn-teal">Request Staff for This Service</a>
              <a href="jobs.html" class="btn btn-outline-white">Browse Related Jobs</a>
            </div>
          </div>
        </section>

        <!-- Service Overview & Visual -->
        <section class="section">
          <div class="container">
            <div class="grid-2" style="align-items: center; gap: 3.5rem;">
              <div>
                <span class="section-subtitle">Service Overview</span>
                <h2>Specialized Sourcing &amp; Execution</h2>
                <p>{s["overview"]}</p>
                
                <h3 style="font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: 0.75rem;">Common Roles Associated With This Service</h3>
                <div class="job-tags" style="margin-bottom: 1.5rem;">
                  {roles_html}
                </div>
              </div>
              <div>
                {render_placeholder(s["image"], "ratio-16-9", s["image"], 1200, 800, s["image_desc"])}
              </div>
            </div>
          </div>
        </section>

        <!-- Employer Requirements & Candidate Profile Considerations -->
        <section class="section section-bg-light">
          <div class="container">
            <div class="grid-2" style="gap: 2.5rem;">
              <div class="card" style="border-top: 4px solid var(--color-corporate-blue);">
                <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
                <h3 class="card-title">Employer Requirements</h3>
                <p class="text-muted" style="margin-bottom: 1rem;">Key criteria client organizations typically define for this engagement model:</p>
                <p style="font-size: 0.95rem; line-height: 1.6;">{s["employer_reqs"]}</p>
                <div style="margin-top: 1.5rem;">
                  <a href="request-staff.html" class="btn btn-outline btn-sm">Submit Staffing Inquiry &rarr;</a>
                </div>
              </div>

              <div class="card" style="border-top: 4px solid var(--color-teal-accent);">
                <div class="card-icon teal"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="7" r="4"/><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/></svg></div>
                <h3 class="card-title">Candidate Profile Considerations</h3>
                <p class="text-muted" style="margin-bottom: 1rem;">What recruiters look for in prospective candidates seeking these opportunities:</p>
                <p style="font-size: 0.95rem; line-height: 1.6;">{s["candidate_reqs"]}</p>
                <div style="margin-top: 1.5rem;">
                  <a href="register-candidate.html" class="btn btn-outline btn-sm">Register as Candidate &rarr;</a>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Recruitment Workflow -->
        <section class="section">
          <div class="container">
            <div class="section-header text-center">
              <span class="section-subtitle teal">Recruitment Lifecycle</span>
              <h2>Recruitment Workflow for {s["title"]}</h2>
              <p class="lead">Structured stages designed to maintain evaluation quality and timely fulfillment.</p>
            </div>

            <div class="process-timeline">
              {steps_html}
            </div>
          </div>
        </section>

        <!-- Potential Business Benefits -->
        <section class="section section-bg-light">
          <div class="container">
            <div class="grid-2" style="align-items: center; gap: 3rem;">
              <div>
                <span class="section-subtitle">Organizational Value</span>
                <h2>Potential Business Benefits</h2>
                <p class="lead" style="font-size: 1.05rem;">How engaging this specialized service helps companies optimize operational efficiency.</p>
                <ul style="margin-top: 1.5rem;">
                  {benefits_html}
                </ul>
                <div class="demo-callout-box" style="margin-top: 1.5rem;">
                  <strong>Notice:</strong> Sourcing timelines, candidate availability, and business outcomes vary based on industry conditions and client-specific criteria. No guaranteed hiring or cost-savings are implied.
                </div>
              </div>
              <div>
                <div class="card" style="padding: 2rem;">
                  <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">Related Staffing Services</h3>
                  <div style="display: flex; flex-direction: column; gap: 1rem;">
                    {related_html}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Frequently Asked Questions -->
        <section class="section">
          <div class="container" style="max-width: 860px;">
            <div class="section-header text-center">
              <span class="section-subtitle">Common Questions</span>
              <h2>{s["title"]} FAQs</h2>
              <p class="text-muted">Direct answers to common inquiries regarding this staffing service.</p>
            </div>

            <div class="accordion-group">
              {faqs_html}
            </div>
          </div>
        </section>

        <!-- Dual CTA Section -->
        <section class="section section-bg-navy">
          <div class="container text-center">
            <h2 style="color: #FFF;">Get Started With {s["title"]}</h2>
            <p style="color: #C0CDDF; max-width: 600px; margin: 0 auto 2rem;">Connect with our recruitment advisors to discuss your hiring requirements or explore open demo job vacancies.</p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
              <a href="request-staff.html" class="btn btn-teal btn-lg">Request Staff</a>
              <a href="jobs.html" class="btn btn-outline-white btn-lg">Search Job Vacancies</a>
            </div>
          </div>
        </section>
        """

        filename = f"{s['slug']}.html"
        write_html(filename, render_page(
            f"{s['title']} — Staffing & Recruitment Services",
            f"Comprehensive {s['title']} solutions: candidate sourcing, screening workflows, associated roles, and business benefits.",
            "services", content,
            breadcrumbs=[("Home", "index.html"), ("Staffing Services", "services.html"), (s["title"], None)]
        ))

print("make_all_service_pages defined.")
