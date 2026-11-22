"""
STAFFING AGENCY — 9 Individual Industry Pages Generator
Generates:
1. it-technology.html
2. healthcare.html
3. manufacturing.html
4. banking-finance.html
5. retail-ecommerce.html
6. construction.html
7. logistics-transportation.html
8. hospitality.html
9. telecommunications.html
"""

from generate_helpers import render_page, render_placeholder
from build_site_part1 import register_image, write_html

INDUSTRIES_DATA = [
    {
        "slug": "it-technology",
        "title": "IT & Technology",
        "badge": "Digital & Software",
        "image": "staffing-it-professionals.jpg",
        "image_desc": "Software engineering leads conducting an architecture review in a modern technology campus",
        "prompt": "Commercial photograph of technology team reviewing cloud architecture diagrams on a transparent glass board in a high-tech modern office. Confident expressions, natural daylight, navy and grey business casual attire.",
        "intro": "The technology sector operates at high velocity, requiring agile hiring models to support cloud transformations, data engineering, software development, and cybersecurity defense. We partner with technology enterprises and digital startups to deploy vetted technical professionals.",
        "workforce_reqs": "Rapid ramp-ups for sprint teams, full-stack engineers experienced in modern microservices, cloud certified architects, and automated testing specialists.",
        "challenges": "Fierce talent competition, rapid technological obsolescence, high salary variance, and high rates of passive candidates not actively seeking roles.",
        "services": [("IT Staffing", "it-staffing.html"), ("Contract Staffing", "contract-staffing.html"), ("Project-Based Staffing", "project-based-staffing.html"), ("Executive Search", "executive-search.html")],
        "roles": ["Full Stack Developers", "Cloud Architects", "DevOps Engineers", "Cybersecurity Analysts", "Data Engineers", "QA Automation Specialists", "Scrum Masters", "Solutions Architects"],
        "considerations": "Practical code evaluation, architecture defense panels, remote collaboration capability, and cultural alignment with agile sprint cadences.",
        "workflow": [
            ("Technical Requisition Intake", "Mapping tech stacks, frameworks, cloud platforms, and architecture requirements."),
            ("Passive Talent Outreach", "Targeted outreach across developer forums, open source repositories, and technical networks."),
            ("Practical Coding Assessment", "Evaluating real-world problem-solving and clean code standards."),
            ("Technical Interview Coordination", "Facilitating panels with client engineering leads and principal architects."),
            ("Sprint Onboarding", "Assisting in repository access, security approvals, and sprint team integration.")
        ]
    },
    {
        "slug": "healthcare",
        "title": "Healthcare",
        "badge": "Clinical & Allied Health",
        "image": "staffing-healthcare-workers.jpg",
        "image_desc": "Qualified healthcare professionals and clinical assistants in a hospital medical center",
        "prompt": "Bright, uplifting commercial healthcare photograph of nursing staff and medical assistants collaborating near a clinical nursing station in a modern hospital facility. Clean aesthetic, compassionate smiles, clinical scrubs.",
        "intro": "Healthcare organizations require dedicated clinical support, allied health specialists, and administrative personnel to maintain superior patient care standards. We support hospitals, diagnostic clinics, outpatient centers, and long-term care facilities with thoroughly credentialed healthcare talent.",
        "workforce_reqs": "Maintaining strict patient-to-staff ratios, round-the-clock shift coverage, verified clinical credentials, and rapid surge staffing during seasonal health emergencies.",
        "challenges": "Rigorous regulatory licensing verifications, clinical burnout and turnover, specialized accreditation requirements, and strict regional compliance.",
        "services": [("Healthcare Staffing", "healthcare-staffing.html"), ("Temporary Staffing", "temporary-staffing.html"), ("Permanent Staffing", "permanent-staffing.html"), ("Bulk Hiring", "bulk-hiring.html")],
        "roles": ["Nurses", "Healthcare Assistants", "Medical Laboratory Technicians", "Pharmacy Assistants", "Medical Records Administrators", "Patient Care Coordinators", "Clinical Support Staff"],
        "considerations": "Regulated healthcare positions strictly require appropriate qualifications, registration, verification, and jurisdiction-specific authorization before placement.",
        "workflow": [
            ("Clinical Mandate Intake", "Evaluating departmental patient care scope and shift coverage needs."),
            ("Primary Source Verification", "Confirming medical council registrations, nursing licenses, and clinical degrees."),
            ("Safety & Privacy Vetting", "Verifying healthcare compliance awareness and infection control training."),
            ("Facility Credentialing Review", "Submitting verification dossiers to hospital medical review committees."),
            ("Unit Induction", "Coordinating clinical orientation and electronic medical record system training.")
        ]
    },
    {
        "slug": "manufacturing",
        "title": "Manufacturing",
        "badge": "Industrial & Plant Operations",
        "image": "staffing-manufacturing-workers.jpg",
        "image_desc": "Manufacturing line operators and assembly specialists in an automated clean factory",
        "prompt": "Documentary industrial photograph of manufacturing operators in safety gear monitoring automated robotic assembly arms in a pristine modern automotive manufacturing facility. Clean floors, bright overhead lighting.",
        "lead": "Plant operators, CNC machinists, quality inspectors, assembly technicians, and manufacturing plant supervisors.",
        "intro": "Modern manufacturing balances advanced automation with skilled human craftsmanship. We support automotive, consumer electronics, chemical, and industrial fabrication plants with safety-trained plant operators and technical maintenance teams.",
        "workforce_reqs": "Reliable three-shift workforce scheduling, mechanical aptitude, adherence to 5S and workplace safety standards, and seasonal ramp-up capacity.",
        "challenges": "Skilled trade shortages, aging workforce transitions, geographic isolation of production plants, and high absenteeism during holiday cycles.",
        "services": [("Industrial Staffing", "industrial-staffing.html"), ("Skilled Workforce", "skilled-workforce.html"), ("Temporary Staffing", "temporary-staffing.html"), ("Bulk Hiring", "bulk-hiring.html")],
        "roles": ["CNC Machine Operators", "Assembly Line Workers", "Quality Control Inspectors", "Maintenance Technicians", "Tool & Die Specialists", "Plant Supervisors", "Safety Officers"],
        "considerations": "Practical machine operating tests, spatial reasoning evaluations, verified trade diplomas, and physical fitness assessments.",
        "workflow": [
            ("Plant Shift Analysis", "Determining machinery lines, shift timings, and daily output quotas."),
            ("Vocational Trade Sourcing", "Mobilizing candidates from accredited technical training institutes."),
            ("Technical & Safety Testing", "Verifying machine operation safety protocols and PPE compliance."),
            ("Plant Floor Interview", "On-site assessment with shift foremen and plant managers."),
            ("Shift Deployment & Tooling", "Induction briefing and shift allocation.")
        ]
    },
    {
        "slug": "banking-finance",
        "title": "Banking & Finance",
        "badge": "Financial Services",
        "image": "staffing-employer-meeting.jpg",
        "image_desc": "Financial analysts and auditors reviewing investment statements in a corporate financial office",
        "prompt": "Commercial corporate photograph of financial executives in sharp business attire reviewing balance sheets and financial models on laptops in an upscale glass-walled finance boardroom. City skyline, elegant ambiance.",
        "intro": "The financial services sector demands absolute numerical precision, strict regulatory compliance, and unwavering integrity. We support retail banks, investment institutions, fintech firms, and accounting practices with vetted financial professionals.",
        "workforce_reqs": "Accountants proficient in statutory reporting, risk analysts, internal audit specialists, financial modelers, and customer banking officers.",
        "challenges": "Intense competition for certified chartered accountants, deep background and credit vetting requirements, and seasonal audit crunches.",
        "services": [("Permanent Staffing", "permanent-staffing.html"), ("White-Collar Staffing", "white-collar-staffing.html"), ("Contract Staffing", "contract-staffing.html"), ("Executive Search", "executive-search.html")],
        "roles": ["Senior Accountants", "Financial Analysts", "Compliance Officers", "Internal Auditors", "Risk Analysts", "Accounts Payable Specialists", "Branch Operations Managers"],
        "considerations": "Rigorous background checks, verification of accounting credentials (CA/CPA/ACCA), financial software proficiency tests, and ethical history review.",
        "workflow": [
            ("Financial Role Discovery", "Analyzing reporting standards (GAAP/IFRS), ledger volume, and audit deadlines."),
            ("Credentialed Talent Sourcing", "Reaching qualified accounting alumni and corporate finance networks."),
            ("Technical Accounting Screening", "Testing financial statement preparation, taxation principles, and ERP skills."),
            ("Executive Interview Coordination", "Facilitating multi-stage interviews with financial controllers and CFOs."),
            ("Compliance Check & Onboarding", "Comprehensive financial background verification and onboarding.")
        ]
    },
    {
        "slug": "retail-ecommerce",
        "title": "Retail & E-commerce",
        "badge": "Consumer Commerce",
        "image": "staffing-bulk-hiring.jpg",
        "image_desc": "Retail store associates and visual merchandising coordinators preparing an apparel showroom",
        "prompt": "Vibrant commercial photograph of retail team members in modern branded uniforms arranging merchandise and greeting customers in a sleek, brightly lit flagship store. Cheerful expressions, clean aisles, modern retail design.",
        "intro": "Retail and e-commerce require exceptional workforce agility to handle weekend traffic spikes, promotional sales events, holiday surges, and rapid warehouse fulfillment. We provide omnichannel staffing from in-store sales associates to e-commerce catalog coordinators.",
        "workforce_reqs": "Customer-facing sales personnel, inventory stocking staff, cashiers, order pickers, and e-commerce return processors.",
        "challenges": "High seasonal turnover, sudden demand surges during festive shopping seasons, and the requirement for flexible weekend/evening shift coverage.",
        "services": [("Temporary Staffing", "temporary-staffing.html"), ("Bulk Hiring", "bulk-hiring.html"), ("Blue-Collar Staffing", "blue-collar-staffing.html"), ("Temp-to-Hire", "temp-to-hire.html")],
        "roles": ["Store Associates", "Cashiers", "Visual Merchandisers", "Order Fulfillment Pickers", "Customer Support Agents", "E-commerce Catalog Specialists", "Store Supervisors"],
        "considerations": "Customer service orientation, active listening skills, POS software familiarity, and punctuality during extended operational hours.",
        "workflow": [
            ("Seasonal Volume Planning", "Forecasting headcount needs for store launches or festive sales peaks."),
            ("Batch Walk-In Drives", "Organizing localized recruitment drives in retail trade catchments."),
            ("Customer Service Simulation", "Evaluating customer interaction, cash handling, and teamwork."),
            ("Rapid Background Verification", "Fast-track identity and residential documentation checks."),
            ("Store Deployment", "Immediate placement with store managers for on-floor training.")
        ]
    },
    {
        "slug": "construction",
        "title": "Construction",
        "badge": "Infrastructure & Civil Works",
        "image": "staffing-industrial-workforce.jpg",
        "image_desc": "Civil site engineers and heavy equipment operators reviewing blueprints on an active infrastructure site",
        "prompt": "Commercial construction photograph of site safety engineers wearing white hard hats and high-vis vests reviewing architectural blueprints on an active commercial building project. Blue sky, steel structure in background, focused teamwork.",
        "intro": "The construction and infrastructure sector demands certified safety consciousness, technical trade competence, and robust physical capability. We support commercial builders, civil engineering contractors, and infrastructure developers with verified site personnel.",
        "workforce_reqs": "Certified heavy machinery operators, site safety supervisors, skilled civil tradesmen, and general site utility helpers.",
        "challenges": "Weather-related project delays affecting staffing schedules, strict adherence to site safety mandates, and shortages of certified equipment operators.",
        "services": [("Skilled Workforce", "skilled-workforce.html"), ("General Workforce", "unskilled-workforce.html"), ("Contract Staffing", "contract-staffing.html"), ("Industrial Staffing", "industrial-staffing.html")],
        "roles": ["Site Safety Supervisors", "Civil Foremen", "Excavator & Crane Operators", "Certified Welders", "Carpenters & Masons", "Surveyors", "Site Helpers"],
        "considerations": "Valid heavy equipment operator licenses, mandatory OSHA / site safety training certifications, and zero-tolerance safety compliance.",
        "workflow": [
            ("Project Phase Review", "Mapping construction stages from earthmoving to structural and finishing."),
            ("Heavy Equipment Verification", "Validating operator licenses, safety training cards, and field experience."),
            ("Safety Induction Vetting", "Mandatory testing on PPE usage, fall protection, and site hazards."),
            ("Site Superintendent Interview", "On-site practical equipment handling verification."),
            ("Site Gate Badge Onboarding", "Entry authorization and shift assignment.")
        ]
    },
    {
        "slug": "logistics-transportation",
        "title": "Logistics & Transportation",
        "badge": "Supply Chain & Distribution",
        "image": "staffing-warehouse-workers.jpg",
        "image_desc": "Supply chain coordinators and freight handlers organizing inventory near loading bays in a distribution hub",
        "prompt": "Dynamic commercial photograph of supply chain handlers in high-visibility vests scanning barcodes on pallets near open warehouse loading bays. Forklifts moving in background, clean organized logistics center, natural sunlight.",
        "intro": "Supply chain resilience depends entirely on dependable talent. From regional fulfillment centers to last-mile delivery fleets, we provide reliable freight coordinators, warehouse material handlers, forklift operators, and dispatchers.",
        "workforce_reqs": "Reliable attendance during tight dispatch schedules, familiarity with warehouse management systems (WMS), and stamina for fast-paced fulfillment.",
        "challenges": "Volume fluctuations driven by consumer buying peaks, driver shortages, and the need for 24/7 round-the-clock shift staffing.",
        "services": [("Blue-Collar Staffing", "blue-collar-staffing.html"), ("Temporary Staffing", "temporary-staffing.html"), ("Bulk Hiring", "bulk-hiring.html"), ("General Workforce", "unskilled-workforce.html")],
        "roles": ["Warehouse Sorters & Pickers", "Forklift Operators", "Fleet Dispatchers", "Inventory Controllers", "Freight Handlers", "Logistics Coordinators", "Hub Supervisors"],
        "considerations": "WMS barcode scanner familiarity, forklift operating licenses, physical fitness, and punctuality during unsociable shift hours.",
        "workflow": [
            ("Hub Shift Capacity Sizing", "Forecasting parcel throughput and determining shift workforce counts."),
            ("Localized Sourcing Drives", "Mobilizing candidate pools living within accessible commuting distance."),
            ("Material Handling & Safety Vetting", "Verifying equipment operation credentials and ergonomics guidelines."),
            ("Hub Manager Review", "Shift scheduling and introduction to loading dock safety rules."),
            ("Live Shift Deployment", "Daily attendance tracking and stand-by replacement coverage.")
        ]
    },
    {
        "slug": "hospitality",
        "title": "Hospitality",
        "badge": "Hotels, Dining & Events",
        "image": "staffing-office-team.jpg",
        "image_desc": "Hospitality front office team and event coordinators reviewing banquet service schedules",
        "prompt": "Elegant commercial hospitality photograph of hotel guest relations associates in immaculate tailored suits greeting guests in a luxury hotel lobby with marble floors and warm chandeliers. Gracious confident smiles, pristine aesthetic.",
        "intro": "Hospitality is defined by guest experience, poise, and operational excellence. We provide luxury hotels, resort destinations, event banqueting venues, and premium restaurants with polished front-of-house staff, culinary assistants, and housekeeping teams.",
        "workforce_reqs": "Impeccable personal presentation, cordial communication, food safety hygiene certifications, and stamina for high-volume weekend and banqueting events.",
        "challenges": "High industry attrition, seasonal resort peak demands, and the requirement for multilingual communication capabilities.",
        "services": [("Temporary Staffing", "temporary-staffing.html"), ("Permanent Staffing", "permanent-staffing.html"), ("Bulk Hiring", "bulk-hiring.html"), ("White-Collar Staffing", "white-collar-staffing.html")],
        "roles": ["Front Desk Executives", "Guest Relations Associates", "Event & Banquet Captains", "Housekeeping Supervisors", "Line Cooks & Kitchen Assistants", "Food & Beverage Stewards", "Concierge Staff"],
        "considerations": "Interpersonal etiquette, grooming standards, language fluency, food handler hygiene certifications, and calm situational problem solving.",
        "workflow": [
            ("Event & Season Briefing", "Reviewing guest occupancy projections, banqueting schedules, and service standards."),
            ("Hospitality Pool Activation", "Sourcing from hotel management institutes and experienced hospitality rosters."),
            ("Grooming & Etiquette Vetting", "Verifying service posture, communication poise, and guest problem resolution."),
            ("General Manager Interview", "Client walkthrough and departmental role assignment."),
            ("Service Shift Deployment", "Uniform allocation and station briefing before guest arrival.")
        ]
    },
    {
        "slug": "telecommunications",
        "title": "Telecommunications",
        "badge": "Networks & Connectivity",
        "image": "staffing-contract-staffing.jpg",
        "image_desc": "Telecommunications fiber optic engineers and network specialists testing connectivity hardware",
        "prompt": "Commercial technology photograph of telecommunications engineers in hard hats and reflective vests inspecting fiber optic distribution racks in a network operations center. Fiber cables, digital diagnostic tools, focused teamwork.",
        "intro": "As optical fiber networks expand and wireless infrastructure evolves, telecommunications companies require specialized network technicians, field installation crews, NOC analysts, and enterprise B2B sales professionals.",
        "workforce_reqs": "Certified optical fiber splicers, tower climbing safety certified technicians, network operations center (NOC) engineers, and commercial broadband sales reps.",
        "challenges": "Geographically dispersed installation sites, safety risks associated with tower climbing and field work, and rapid technology standard shifts.",
        "services": [("Technical Staffing", "it-staffing.html"), ("Contract Staffing", "contract-staffing.html"), ("Field Workforce", "blue-collar-staffing.html"), ("White-Collar Staffing", "white-collar-staffing.html")],
        "roles": ["Fiber Optic Technicians", "NOC Operations Engineers", "Tower Rigging Specialists", "Field Installation Techs", "RF Planning Engineers", "Enterprise Broadband Sales Reps", "Telecom Project Coordinators"],
        "considerations": "Working at heights safety certifications, fiber optical OTDR testing proficiency, driving licenses, and technical schematic interpretation.",
        "workflow": [
            ("Network Rollout Scoping", "Defining coverage zones, tower sites, and technician skill bands."),
            ("Field Technician Sourcing", "Mobilizing candidate pools with electronics and telecom trade diplomas."),
            ("Height & Electrical Safety Checks", "Confirming mandatory tower climbing and electrical safety certificates."),
            ("Field Supervisor Review", "Technical tool handling assessment and client team briefing."),
            ("Field Vehicle & Route Deployment", "Tool kit issuance and assignment to territory installation squads.")
        ]
    }
]

def make_all_industry_pages():
    for ind in INDUSTRIES_DATA:
        # Register image
        register_image(
            ind["image"], f"{ind['slug']}.html", "Industry Overview",
            ind["image_desc"], "16:9", "1200x800", "Landscape",
            ind["prompt"], "Wide landscape commercial shot of industry professionals engaged in domain workflow",
            "Eye-level medium-wide shot", "Natural corporate/industrial balanced lighting",
            "Modern sector-specific workplace facility", "High-end commercial documentary photography",
            "Navy, corporate blue, industry ambient accents", "Subjects centered in midground"
        )

        # Build workflow steps HTML
        steps_html = ""
        for i, (title, desc) in enumerate(ind["workflow"], 1):
            teal_class = "teal" if i % 2 == 0 else ""
            steps_html += f"""
            <div class="process-step">
              <div class="step-number {teal_class}">{i}</div>
              <h4 class="step-title" style="font-size: 1.05rem;">{title}</h4>
              <p class="step-text">{desc}</p>
            </div>
            """

        # Build roles HTML
        roles_html = "".join([f'<span class="tag-badge" style="font-size: 0.85rem; padding: 0.35rem 0.85rem;">{r}</span>' for r in ind["roles"]])

        # Build services HTML
        services_html = "".join([f'<div class="card" style="padding: 1.5rem;"><h4 style="margin-bottom: 0.5rem;"><a href="{url}">{name}</a></h4><p class="text-muted" style="font-size: 0.85rem; margin-bottom: 0.75rem;">Tailored staffing solution for this sector.</p><a href="{url}" class="card-link" style="font-size: 0.85rem;">Explore Service &rarr;</a></div>' for name, url in ind["services"]])

        content = f"""
        <!-- Industry Hero -->
        <section class="page-hero">
          <div class="container">
            <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">{ind["badge"]}</span>
            <h1>{ind["title"]} Staffing Solutions</h1>
            <p class="lead">
              Tailored workforce acquisition, flexible staffing models, and specialized candidate vetting aligned with the unique requirements of the {ind["title"]} industry.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
              <a href="request-staff.html" class="btn btn-teal">Request {ind["title"]} Staff</a>
              <a href="jobs.html" class="btn btn-outline-white">Explore {ind["title"]} Jobs</a>
            </div>
          </div>
        </section>

        <!-- Industry Introduction & Visual -->
        <section class="section">
          <div class="container">
            <div class="grid-2" style="align-items: center; gap: 3.5rem;">
              <div>
                <span class="section-subtitle">Sector Introduction</span>
                <h2>Talent Dynamics in {ind["title"]}</h2>
                <p>{ind["intro"]}</p>
                <div class="demo-callout-box">
                  <strong>Notice:</strong> This industry page outlines typical recruitment practices and workforce models for the {ind["title"]} sector. All client engagements are tailored to individual enterprise specifications.
                </div>
              </div>
              <div>
                {render_placeholder(ind["image"], "ratio-16-9", ind["image"], 1200, 800, ind["image_desc"])}
              </div>
            </div>
          </div>
        </section>

        <!-- Typical Workforce Reqs & Common Hiring Challenges -->
        <section class="section section-bg-light">
          <div class="container">
            <div class="grid-2" style="gap: 2.5rem;">
              <div class="card" style="border-top: 4px solid var(--color-corporate-blue);">
                <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
                <h3 class="card-title">Typical Workforce Requirements</h3>
                <p style="font-size: 0.95rem; line-height: 1.6;">{ind["workforce_reqs"]}</p>
              </div>

              <div class="card" style="border-top: 4px solid var(--color-teal-accent);">
                <div class="card-icon teal"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div>
                <h3 class="card-title">Common Hiring Challenges</h3>
                <p style="font-size: 0.95rem; line-height: 1.6;">{ind["challenges"]}</p>
              </div>
            </div>
          </div>
        </section>

        <!-- Example Job Categories in Sector -->
        <section class="section">
          <div class="container">
            <div class="section-header text-center">
              <span class="section-subtitle teal">Role Spectrum</span>
              <h2>Common Job Roles in {ind["title"]}</h2>
              <p class="lead">Typical job profiles we source and evaluate across this sector.</p>
            </div>

            <div class="job-tags" style="justify-content: center; max-width: 900px; margin: 0 auto 2.5rem;">
              {roles_html}
            </div>

            <div class="card" style="max-width: 860px; margin: 0 auto; padding: 2rem;">
              <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">Recruitment Considerations</h3>
              <p style="color: var(--color-body-text); font-size: 0.95rem; line-height: 1.6;">{ind["considerations"]}</p>
            </div>
          </div>
        </section>

        <!-- Illustrative Sourcing Workflow -->
        <section class="section section-bg-light">
          <div class="container">
            <div class="section-header text-center">
              <span class="section-subtitle">Recruitment Lifecycle</span>
              <h2>Sourcing Workflow for {ind["title"]}</h2>
              <p class="lead">Structured stages engineered for quality talent alignment.</p>
            </div>

            <div class="process-timeline">
              {steps_html}
            </div>
          </div>
        </section>

        <!-- Relevant Staffing Services for Sector -->
        <section class="section">
          <div class="container">
            <div class="section-header text-center">
              <span class="section-subtitle teal">Service Alignment</span>
              <h2>Relevant Staffing Services for {ind["title"]}</h2>
              <p class="lead">Staffing models most frequently deployed for this industry.</p>
            </div>

            <div class="grid-4">
              {services_html}
            </div>
          </div>
        </section>

        <!-- Dual CTA Section -->
        <section class="section section-bg-navy">
          <div class="container text-center">
            <h2 style="color: #FFF;">Build Your {ind["title"]} Team</h2>
            <p style="color: #C0CDDF; max-width: 600px; margin: 0 auto 2rem;">Submit your staffing requisition or explore open demo job vacancies in the {ind["title"]} sector.</p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
              <a href="request-staff.html" class="btn btn-teal btn-lg">Request {ind["title"]} Staff</a>
              <a href="jobs.html" class="btn btn-outline-white btn-lg">Explore {ind["title"]} Jobs</a>
            </div>
          </div>
        </section>
        """

        filename = f"{ind['slug']}.html"
        write_html(filename, render_page(
            f"{ind['title']} Staffing Solutions — Industry Recruitment",
            f"Tailored {ind['title']} staffing solutions: workforce requirements, hiring challenges, common roles, and sourcing workflows.",
            "industries", content,
            breadcrumbs=[("Home", "index.html"), ("Industries", "industries.html"), (ind["title"], None)]
        ))

print("make_all_industry_pages defined.")
