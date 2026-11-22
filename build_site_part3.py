"""
STAFFING AGENCY — Core Pages Part 3
Includes services.html, industries.html, process.html, workforce-solutions.html,
talent-acquisition.html, recruitment-consulting.html, team.html, leadership.html,
case-studies.html, case-study-details.html, insights.html, article-details.html, faq.html, contact.html.
"""

from generate_helpers import render_page, render_placeholder, LOGO_SVG
from build_site_part1 import register_image, write_html

# ==============================================================================
# 3. SERVICES DIRECTORY — services.html
# ==============================================================================
def make_services():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Workforce Capabilities</span>
        <h1>Comprehensive Staffing Services</h1>
        <p class="lead">
          Organized into five core recruitment categories: Permanent Recruitment, Flexible Staffing, High-Volume Sourcing, Specialized Staffing, and Recruitment Operations.
        </p>
      </div>
    </section>

    <!-- Category A: Permanent Recruitment -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Category A</span>
          <h2>Permanent Recruitment</h2>
          <p class="text-muted">Direct hire and long-term placement models built for strategic organizational growth.</p>
        </div>

        <div class="grid-3">
          <div class="service-card">
            <h3 class="card-title">Permanent Staffing</h3>
            <p class="card-body">Comprehensive sourcing, screening, and placement for full-time corporate and technical personnel.</p>
            <a href="permanent-staffing.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">Executive Search</h3>
            <p class="card-body">Targeted, confidential leadership recruitment for C-suite, VP, and Director-level appointments.</p>
            <a href="executive-search.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">White-Collar Staffing</h3>
            <p class="card-body">Mid-level professionals across finance, administration, HR, marketing, and corporate operations.</p>
            <a href="white-collar-staffing.html" class="card-link">Service Details &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Category B: Flexible Staffing -->
    <section class="section section-bg-light">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle teal">Category B</span>
          <h2>Flexible Staffing</h2>
          <p class="text-muted">Agile workforce engagements that adapt to operational cycles and project milestones.</p>
        </div>

        <div class="grid-4">
          <div class="service-card">
            <h3 class="card-title">Temporary Staffing</h3>
            <p class="card-body">Short-term workforce additions to handle peak seasonal workloads and temporary vacancies.</p>
            <a href="temporary-staffing.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">Contract Staffing</h3>
            <p class="card-body">Fixed-term specialized engagements for dedicated deliverables and technical assignments.</p>
            <a href="contract-staffing.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">Temp-to-Hire</h3>
            <p class="card-body">Evaluate real-world job performance and cultural fit before committing to a permanent offer.</p>
            <a href="temp-to-hire.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">Project-Based Staffing</h3>
            <p class="card-body">Assemble tailored multidisciplinary project squads for defined enterprise deliverables.</p>
            <a href="project-based-staffing.html" class="card-link">Service Details &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Category C: High-Volume Recruitment -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Category C</span>
          <h2>High-Volume Recruitment</h2>
          <p class="text-muted">Engineered sourcing engines for rapid staff mobilization and campus hiring.</p>
        </div>

        <div class="grid-2">
          <div class="service-card">
            <h3 class="card-title">Bulk Hiring</h3>
            <p class="card-body">Multi-channel recruitment campaigns and screening funnels designed to hire dozens or hundreds of candidates concurrently.</p>
            <a href="bulk-hiring.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">Campus Recruitment</h3>
            <p class="card-body">Coordinated university engagement drives, aptitude filtering, and cohort onboarding for fresh graduate talent.</p>
            <a href="campus-recruitment.html" class="card-link">Service Details &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Category D: Specialized Staffing -->
    <section class="section section-bg-light">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle teal">Category D</span>
          <h2>Specialized Staffing</h2>
          <p class="text-muted">Vertical-specific talent networks matching sector technical criteria.</p>
        </div>

        <div class="grid-3">
          <div class="service-card">
            <h3 class="card-title">IT Staffing</h3>
            <p class="card-body">Software developers, cloud engineers, data analysts, QA testers, and cybersecurity specialists.</p>
            <a href="it-staffing.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">Healthcare Staffing</h3>
            <p class="card-body">Qualified medical assistants, clinical technicians, and healthcare administrative support.</p>
            <a href="healthcare-staffing.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">Industrial Staffing</h3>
            <p class="card-body">Machine operators, assembly technicians, and manufacturing maintenance experts.</p>
            <a href="industrial-staffing.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">Blue-Collar Staffing</h3>
            <p class="card-body">Warehouse crew, inventory handlers, packing operators, and delivery logistics teams.</p>
            <a href="blue-collar-staffing.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">Skilled Workforce Staffing</h3>
            <p class="card-body">Certified trade specialists, electrical technicians, and specialized mechanical operators.</p>
            <a href="skilled-workforce.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">General Workforce Staffing</h3>
            <p class="card-body">General utility personnel, facility helpers, and ground workforce assistants.</p>
            <a href="unskilled-workforce.html" class="card-link">Service Details &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Category E: Recruitment Operations -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Category E</span>
          <h2>Recruitment Operations</h2>
          <p class="text-muted">Process outsourcing and administrative workforce management solutions.</p>
        </div>

        <div class="grid-2">
          <div class="service-card">
            <h3 class="card-title">Recruitment Process Outsourcing (RPO)</h3>
            <p class="card-body">End-to-end management of recruitment workflows, candidate pipelines, applicant tracking, and hiring metrics under service level agreements.</p>
            <a href="recruitment-process-outsourcing.html" class="card-link">Service Details &rarr;</a>
          </div>
          <div class="service-card">
            <h3 class="card-title">Payroll &amp; Staffing Administration</h3>
            <p class="card-body">Attendance record keeping, timesheet consolidation, payroll data preparation, and candidate employment documentation administration.</p>
            <a href="payroll-staffing.html" class="card-link">Service Details &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="section section-bg-navy">
      <div class="container text-center">
        <h2 style="color: #FFF;">Have Specific Staffing Requirements?</h2>
        <p style="color: #C0CDDF; max-width: 600px; margin: 0 auto 2rem;">Our talent specialists can review your organizational workforce needs and propose an appropriate model.</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="request-staff.html" class="btn btn-teal btn-lg">Request Staff</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Us</a>
        </div>
      </div>
    </section>
    """
    write_html("services.html", render_page(
        "Staffing Services — Comprehensive Recruitment Solutions",
        "Explore our 17 staffing services categorized across permanent recruitment, flexible staffing, high-volume sourcing, specialized staffing, and recruitment operations.",
        "services", content,
        breadcrumbs=[("Home", "index.html"), ("Staffing Services", None)]
    ))

# ==============================================================================
# 4. INDUSTRIES DIRECTORY — industries.html
# ==============================================================================
def make_industries():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Sector Alignment</span>
        <h1>Industries We Serve</h1>
        <p class="lead">
          Understanding the distinct hiring rhythms, regulatory qualifications, and skill sets across 9 major commercial and industrial sectors.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid-3">
          <div class="industry-card">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg></div>
            <h3 class="card-title">IT &amp; Technology</h3>
            <p class="card-body">Software engineering, cloud infrastructure, cybersecurity, QA, and data analytics talent.</p>
            <a href="it-technology.html" class="card-link">Explore Sector &rarr;</a>
          </div>

          <div class="industry-card">
            <div class="card-icon teal"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
            <h3 class="card-title">Healthcare</h3>
            <p class="card-body">Clinical technicians, medical administrative staff, nursing support, and laboratory assistants.</p>
            <a href="healthcare.html" class="card-link">Explore Sector &rarr;</a>
          </div>

          <div class="industry-card">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg></div>
            <h3 class="card-title">Manufacturing</h3>
            <p class="card-body">Machinists, production line operators, quality auditors, and facility maintenance crew.</p>
            <a href="manufacturing.html" class="card-link">Explore Sector &rarr;</a>
          </div>

          <div class="industry-card">
            <div class="card-icon teal"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
            <h3 class="card-title">Banking &amp; Finance</h3>
            <p class="card-body">Accountants, ledger clerks, financial analysts, risk managers, and auditing personnel.</p>
            <a href="banking-finance.html" class="card-link">Explore Sector &rarr;</a>
          </div>

          <div class="industry-card">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg></div>
            <h3 class="card-title">Retail &amp; E-commerce</h3>
            <p class="card-body">Store executives, merchandising specialists, customer care, and order fulfillment workers.</p>
            <a href="retail-ecommerce.html" class="card-link">Explore Sector &rarr;</a>
          </div>

          <div class="industry-card">
            <div class="card-icon teal"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18M3 7l9-4 9 4M4 10v11M20 10v11M8 14v7M12 14v7M16 14v7"/></svg></div>
            <h3 class="card-title">Construction</h3>
            <p class="card-body">Site safety supervisors, heavy machinery operators, civil technicians, and site tradesmen.</p>
            <a href="construction.html" class="card-link">Explore Sector &rarr;</a>
          </div>

          <div class="industry-card">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg></div>
            <h3 class="card-title">Logistics &amp; Transportation</h3>
            <p class="card-body">Fleet dispatchers, warehouse material handlers, freight coordinators, and sorters.</p>
            <a href="logistics-transportation.html" class="card-link">Explore Sector &rarr;</a>
          </div>

          <div class="industry-card">
            <div class="card-icon teal"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg></div>
            <h3 class="card-title">Hospitality</h3>
            <p class="card-body">Front office staff, guest relations, culinary assistants, banqueting, and housekeeping staff.</p>
            <a href="hospitality.html" class="card-link">Explore Sector &rarr;</a>
          </div>

          <div class="industry-card">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/></svg></div>
            <h3 class="card-title">Telecommunications</h3>
            <p class="card-body">Tower maintenance crew, optical cable technicians, network operation engineers, and sales reps.</p>
            <a href="telecommunications.html" class="card-link">Explore Sector &rarr;</a>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("industries.html", render_page(
        "Industries We Serve — Sector-Specific Staffing Solutions",
        "Discover our workforce solutions across 9 key industries including IT, healthcare, manufacturing, banking, retail, construction, logistics, and telecom.",
        "industries", content,
        breadcrumbs=[("Home", "index.html"), ("Industries", None)]
    ))

# ==============================================================================
# 5. PROCESS — process.html (6 steps timeline)
# ==============================================================================
def make_process():
    register_image(
        "staffing-recruitment-process.jpg", "process.html", "Process Overview",
        "Talent acquisition specialist reviewing shortlisted candidate resumes against client job specifications",
        "16:9", "1200x800", "Landscape",
        "Crisp corporate photograph of a recruitment manager in professional attire reviewing printed resumes and dual monitor candidate evaluation dashboards in a tidy office environment. Soft warm lamp light, glass desk, subtle graph overlays, focused analytical posture.",
        "Centered recruiter with monitor screens flanking on left and right", "Eye-level medium shot", "Warm interior balanced studio lighting",
        "Contemporary open-plan recruitment agency workspace", "Editorial corporate workplace photography",
        "Navy, white, subtle amber lighting accents", "Subject centered behind desk with resume documents"
    )

    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Methodology</span>
        <h1>Our Recruitment Process</h1>
        <p class="lead">
          A disciplined 6-stage recruitment roadmap engineered to connect hiring organizations with thoroughly evaluated talent.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="demo-callout-box">
          <strong>Process Disclaimer:</strong> The recruitment stages described represent an illustrative procedural framework. Final hiring decisions, employment offers, and terms of employment are solely made by the client hiring organization. No outcome or timeline is guaranteed.
        </div>

        <div style="margin: 2.5rem 0;">
          {render_placeholder("staffing-recruitment-process.jpg", "ratio-21-9", "staffing-recruitment-process.jpg", 1200, 520, "Talent acquisition specialist reviewing candidate profiles and job criteria")}
        </div>

        <!-- 6 Step Timeline -->
        <div style="display: flex; flex-direction: column; gap: 2rem;">
          <div class="card" style="border-left: 5px solid var(--color-corporate-blue); padding: 2rem;">
            <div style="display: flex; gap: 1.5rem; align-items: flex-start;">
              <div class="step-number" style="margin-bottom: 0;">1</div>
              <div>
                <h3 style="font-size: 1.3rem; margin-bottom: 0.5rem;">Step 1 — Requirement Understanding</h3>
                <p>
                  We initiate every engagement with a structured discovery session to understand the employer's organizational objectives, mandatory qualifications, day-to-day responsibilities, reporting hierarchies, and team culture. This ensures all subsequent sourcing adheres strictly to accurate role criteria.
                </p>
              </div>
            </div>
          </div>

          <div class="card" style="border-left: 5px solid var(--color-teal-accent); padding: 2rem;">
            <div style="display: flex; gap: 1.5rem; align-items: flex-start;">
              <div class="step-number teal" style="margin-bottom: 0;">2</div>
              <div>
                <h3 style="font-size: 1.3rem; margin-bottom: 0.5rem;">Step 2 — Candidate Sourcing</h3>
                <p>
                  Using targeted industry databases, professional talent networks, passive candidate mapping, and referral channels, our recruitment team identifies a broad pool of prospective candidates possessing the requisite background.
                </p>
              </div>
            </div>
          </div>

          <div class="card" style="border-left: 5px solid var(--color-corporate-blue); padding: 2rem;">
            <div style="display: flex; gap: 1.5rem; align-items: flex-start;">
              <div class="step-number" style="margin-bottom: 0;">3</div>
              <div>
                <h3 style="font-size: 1.3rem; margin-bottom: 0.5rem;">Step 3 — Initial Screening</h3>
                <p>
                  Our consultants perform structured preliminary evaluations to confirm academic credentials, practical experience, career motivations, notice period availability, and alignment with client expectations.
                </p>
              </div>
            </div>
          </div>

          <div class="card" style="border-left: 5px solid var(--color-teal-accent); padding: 2rem;">
            <div style="display: flex; gap: 1.5rem; align-items: flex-start;">
              <div class="step-number teal" style="margin-bottom: 0;">4</div>
              <div>
                <h3 style="font-size: 1.3rem; margin-bottom: 0.5rem;">Step 4 — Interview Coordination</h3>
                <p>
                  We manage end-to-end interview scheduling between shortlisted candidates and corporate hiring panels, including sending brief packages, calendar management, and post-interview candidate feedback gathering.
                </p>
              </div>
            </div>
          </div>

          <div class="card" style="border-left: 5px solid var(--color-corporate-blue); padding: 2rem;">
            <div style="display: flex; gap: 1.5rem; align-items: flex-start;">
              <div class="step-number" style="margin-bottom: 0;">5</div>
              <div>
                <h3 style="font-size: 1.3rem; margin-bottom: 0.5rem;">Step 5 — Selection Support</h3>
                <p>
                  Once client managers identify their preferred candidate, we assist in facilitating offer expectations, clarifying remuneration structures, and answering candidate questions to ensure aligned commitments.
                </p>
              </div>
            </div>
          </div>

          <div class="card" style="border-left: 5px solid var(--color-teal-accent); padding: 2rem;">
            <div style="display: flex; gap: 1.5rem; align-items: flex-start;">
              <div class="step-number teal" style="margin-bottom: 0;">6</div>
              <div>
                <h3 style="font-size: 1.3rem; margin-bottom: 0.5rem;">Step 6 — Joining Coordination</h3>
                <p>
                  We maintain regular contact with selected candidates throughout their notice periods, assisting with joining documentation checks, induction scheduling, and initial placement integration.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("process.html", render_page(
        "Our Recruitment Process — 6-Stage Sourcing Workflow",
        "Detailed 6-stage recruitment roadmap from requirement analysis to candidate sourcing, screening, interviews, selection, and onboarding support.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("Recruitment Process", None)]
    ))

# ==============================================================================
# 6. WORKFORCE SOLUTIONS — workforce-solutions.html
# ==============================================================================
def make_workforce_solutions():
    register_image(
        "staffing-workforce-planning.jpg", "workforce-solutions.html", "Models Overview",
        "Workforce strategists analyzing capacity planning diagrams and organizational charts",
        "16:9", "1200x800", "Landscape",
        "Corporate photograph of two workforce management analysts standing before a large digital whiteboard displaying capacity planning flowcharts and team shift structures. Modern office setting, natural lighting, professional posture, navy and white corporate apparel.",
        "Medium wide shot, whiteboard elements visible with subjects engaged", "Eye-level medium angle", "Natural cool daylight supplemented with ambient office lighting",
        "Modern corporate operations strategy room", "Clean corporate editorial style",
        "Navy blue, slate, teal highlights", "Subjects standing midground with planning diagrams"
    )

    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Enterprise Strategy</span>
        <h1>Workforce Solutions</h1>
        <p class="lead">
          Scalable workforce structures designed to assist organizations in balancing permanent core teams with flexible contingent labor.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3rem;">
          <div>
            <span class="section-subtitle">Adaptive Capacity</span>
            <h2>Flexible Workforce Planning</h2>
            <p>
              In dynamic economic landscapes, rigid staffing models introduce operational risk. Enterprise workforce planning blends permanent core leadership with adaptable contingent staffing pools, enabling companies to manage workload variations without overextending internal HR capabilities.
            </p>
            <p>
              Our workforce frameworks help corporate managers evaluate workload volatility, skill availability, and project durations to select the most appropriate staffing model.
            </p>
            <div class="demo-callout-box">
              <strong>Notice:</strong> This page presents illustrative organizational models. All statutory employment obligations, contracts, and policies are subject to regional jurisdiction laws and employer terms.
            </div>
          </div>
          <div>
            {render_placeholder("staffing-workforce-planning.jpg", "ratio-16-9", "staffing-workforce-planning.jpg", 1200, 800, "Workforce strategists analyzing organizational models")}
          </div>
        </div>
      </div>
    </section>

    <!-- Interactive UI Mockup: Workforce Overview Dashboard -->
    <section class="section section-bg-light">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle teal">Illustrative Dashboard</span>
          <h2>Workforce Allocation Model</h2>
          <p class="lead">Simulated dashboard displaying balanced talent distribution across staffing models.</p>
        </div>

        <div class="mockup-window">
          <div class="mockup-header">
            <div class="mockup-controls">
              <span class="mockup-dot red"></span>
              <span class="mockup-dot yellow"></span>
              <span class="mockup-dot green"></span>
            </div>
            <span class="mockup-title">WORKFORCE_ALLOCATION_VIEWER // v2.4 (DEMO)</span>
            <span class="demo-disclaimer-pill" style="margin-bottom: 0;">ILLUSTRATIVE DEMO DATA</span>
          </div>
          <div class="mockup-body">
            <div class="grid-4" style="margin-bottom: 1.5rem;">
              <div class="card" style="padding: 1.25rem;">
                <span class="text-muted" style="font-size: 0.8rem;">Permanent Core</span>
                <h3 style="font-size: 1.6rem; color: var(--color-corporate-blue); margin: 0.25rem 0;">65%</h3>
                <span style="font-size: 0.75rem; color: var(--color-muted-text);">Institutional Knowledge &amp; Strategy</span>
              </div>
              <div class="card" style="padding: 1.25rem;">
                <span class="text-muted" style="font-size: 0.8rem;">Contingent / Temporary</span>
                <h3 style="font-size: 1.6rem; color: var(--color-teal-accent); margin: 0.25rem 0;">20%</h3>
                <span style="font-size: 0.75rem; color: var(--color-muted-text);">Seasonal &amp; Volume Scalability</span>
              </div>
              <div class="card" style="padding: 1.25rem;">
                <span class="text-muted" style="font-size: 0.8rem;">Contract / Project</span>
                <h3 style="font-size: 1.6rem; color: var(--color-secondary-navy); margin: 0.25rem 0;">10%</h3>
                <span style="font-size: 0.75rem; color: var(--color-muted-text);">Specialized Technology Delivery</span>
              </div>
              <div class="card" style="padding: 1.25rem;">
                <span class="text-muted" style="font-size: 0.8rem;">Temp-to-Hire</span>
                <h3 style="font-size: 1.6rem; color: #D97706; margin: 0.25rem 0;">5%</h3>
                <span style="font-size: 0.75rem; color: var(--color-muted-text);">Performance Evaluation Pipeline</span>
              </div>
            </div>
            <div style="background: var(--color-white); border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.25rem; font-size: 0.85rem; color: var(--color-muted-text); text-align: center;">
              ILLUSTRATIVE DEMO DATA — NOT CONNECTED TO A LIVE RECRUITMENT SYSTEM
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("workforce-solutions.html", render_page(
        "Workforce Solutions — Enterprise Staffing Architecture",
        "Explore flexible workforce planning, blended staffing models, and scalable workforce architectures for modern enterprises.",
        "employers", content,
        breadcrumbs=[("Home", "index.html"), ("Workforce Solutions", None)]
    ))

print("make_services, make_industries, make_process, make_workforce_solutions defined.")
