"""
STAFFING AGENCY — Master Site Builder
Constructs all 52 HTML pages, sitemap.xml, robots.txt, and IMAGE-GENERATION-GUIDE.md.
"""

import os
from generate_helpers import render_page, render_placeholder, LOGO_SVG

# Global inventory for IMAGE-GENERATION-GUIDE.md
IMAGE_INVENTORY = []

def register_image(filename, page, section, desc, ratio, resolution, orientation, prompt, composition, angle, lighting, bg, style, palette, subject_pos):
    IMAGE_INVENTORY.append({
        "filename": filename,
        "page": page,
        "section": section,
        "desc": desc,
        "ratio": ratio,
        "resolution": resolution,
        "orientation": orientation,
        "prompt": prompt,
        "composition": composition,
        "angle": angle,
        "lighting": lighting,
        "bg": bg,
        "style": style,
        "palette": palette,
        "subject_pos": subject_pos
    })
    return filename

def write_html(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename}")

# ==============================================================================
# 1. HOMEPAGE — index.html
# ==============================================================================
def make_index():
    register_image(
        "staffing-hero-team.jpg", "index.html", "Hero Section",
        "Diverse recruitment and corporate team collaborating in a modern architectural office",
        "16:9", "1920x1080", "Landscape",
        "Cinematic photograph of a diverse, professional corporate staffing and HR team collaborating around a sleek conference table in a modern glass-walled office. Natural daylight streaming through floor-to-ceiling windows, subtle navy and slate corporate attire, friendly confident expressions, soft depth of field, high-end commercial corporate photography style.",
        "Rule of thirds, team centered with subtle breathing room on left", "Eye-level cinematic medium shot", "Soft natural architectural daylight with subtle fill",
        "Modern high-rise office interior with glass partitions and cityscape blur", "Corporate documentary editorial photography",
        "Navy blue, crisp white, slate grey, warm wood accents", "Midground conference seating with natural engagement"
    )

    content = f"""
    <!-- Hero Section -->
    <section class="page-hero" style="padding: 5.5rem 0 4.5rem;">
      <div class="container">
        <div style="max-width: 860px;">
          <div class="demo-disclaimer-pill" style="background: rgba(255, 255, 255, 0.15); color: #FFFFFF; border-color: rgba(255, 255, 255, 0.3);">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            Generic Staffing &amp; Talent Solutions Platform
          </div>
          <h1>Connecting Businesses With the Right Talent</h1>
          <p class="lead">
            Flexible staffing and workforce solutions designed to help businesses find the people they need while connecting job seekers with meaningful career opportunities.
          </p>
          <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 2rem;">
            <a href="request-staff.html" class="btn btn-teal btn-lg">Hire Staff</a>
            <a href="jobs.html" class="btn btn-outline-white btn-lg">Find Jobs</a>
          </div>
        </div>

        <!-- Hero Image Placeholder -->
        <div style="margin-top: 3.5rem;">
          {render_placeholder("staffing-hero-team.jpg", "ratio-21-9", "staffing-hero-team.jpg", 1920, 820, "Corporate recruitment and workforce team collaborating in modern office")}
        </div>

        <!-- Dual Pathways Component: Separate Employer and Candidate Journeys -->
        <div class="dual-pathways-container">
          <!-- Employer Pathway -->
          <div class="pathway-card employer-path">
            <div>
              <div class="pathway-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
              </div>
              <span class="pathway-badge">For Employers</span>
              <h3 style="margin-bottom: 0.75rem;">Looking for the Right Talent?</h3>
              <p class="text-muted" style="font-size: 0.95rem; margin-bottom: 1.5rem;">
                Find qualified workforce solutions for your business requirements. We support temporary, permanent, project-based, and high-volume recruitment models.
              </p>
            </div>
            <div>
              <a href="request-staff.html" class="btn btn-primary" style="width: 100%;">Request Staff &rarr;</a>
            </div>
          </div>

          <!-- Candidate Pathway -->
          <div class="pathway-card candidate-path">
            <div>
              <div class="pathway-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
              </div>
              <span class="pathway-badge">For Job Seekers</span>
              <h3 style="margin-bottom: 0.75rem;">Looking for Your Next Opportunity?</h3>
              <p class="text-muted" style="font-size: 0.95rem; margin-bottom: 1.5rem;">
                Explore job opportunities across different industries and career levels. Browse open demo listings or register your candidate profile today.
              </p>
            </div>
            <div>
              <a href="jobs.html" class="btn btn-teal" style="width: 100%;">Search Jobs &rarr;</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Staffing Services Overview Section -->
    <section class="section section-bg-light">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle">Comprehensive Capabilities</span>
          <h2>Specialized Staffing Services</h2>
          <p class="lead">
            Tailored recruitment and workforce architectures aligned with enterprise operational goals.
          </p>
        </div>

        <div class="grid-3">
          <div class="service-card">
            <span class="service-badge">Direct Hire</span>
            <div class="card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg>
            </div>
            <h3 class="card-title">Permanent Staffing</h3>
            <p class="card-body">Strategic end-to-end talent sourcing for full-time, long-term organizational roles across technical and administrative functions.</p>
            <a href="permanent-staffing.html" class="card-link">Explore Permanent Staffing &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">Flexible Staffing</span>
            <div class="card-icon teal">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 14"/></svg>
            </div>
            <h3 class="card-title">Temporary Staffing</h3>
            <p class="card-body">Scalable workforce solutions to accommodate seasonal peak demands, production surges, and temporary leave coverage.</p>
            <a href="temporary-staffing.html" class="card-link">Explore Temporary Staffing &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">Project Staffing</span>
            <div class="card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
            </div>
            <h3 class="card-title">Contract Staffing</h3>
            <p class="card-body">Specialized fixed-term professional engagements for time-bound initiatives, software milestones, and technical delivery.</p>
            <a href="contract-staffing.html" class="card-link">Explore Contract Staffing &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">Evaluation Model</span>
            <div class="card-icon teal">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            </div>
            <h3 class="card-title">Temp-to-Hire</h3>
            <p class="card-body">Assess on-the-job competency, cultural compatibility, and operational performance before extending a permanent employment offer.</p>
            <a href="temp-to-hire.html" class="card-link">Explore Temp-to-Hire &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">Leadership</span>
            <div class="card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </div>
            <h3 class="card-title">Executive Search</h3>
            <p class="card-body">Discreet, thorough talent mapping and headhunting for senior leadership, board-level, and mission-critical executive appointments.</p>
            <a href="executive-search.html" class="card-link">Explore Executive Search &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">High-Volume</span>
            <div class="card-icon teal">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </div>
            <h3 class="card-title">Bulk Hiring</h3>
            <p class="card-body">Rapid deployment workflows and screening funnels designed to mobilize large-scale staff volumes for plant setups or retail expansions.</p>
            <a href="bulk-hiring.html" class="card-link">Explore Bulk Hiring &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">Graduate Talent</span>
            <div class="card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
            </div>
            <h3 class="card-title">Campus Recruitment</h3>
            <p class="card-body">Coordinated university engagement campaigns and aptitude assessments to onboard promising entry-level graduate cohorts.</p>
            <a href="campus-recruitment.html" class="card-link">Explore Campus Recruitment &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">Engineering &amp; Cloud</span>
            <div class="card-icon teal">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
            </div>
            <h3 class="card-title">IT Staffing</h3>
            <p class="card-body">Technical vetting and placement of software engineers, cloud architects, DevOps specialists, data analysts, and QA professionals.</p>
            <a href="it-staffing.html" class="card-link">Explore IT Staffing &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">Clinical &amp; Support</span>
            <div class="card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            </div>
            <h3 class="card-title">Healthcare Staffing</h3>
            <p class="card-body">Credentialed support personnel, clinical assistants, nursing support, and administrative healthcare staffing services.</p>
            <a href="healthcare-staffing.html" class="card-link">Explore Healthcare Staffing &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">Manufacturing</span>
            <div class="card-icon teal">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
            </div>
            <h3 class="card-title">Industrial Staffing</h3>
            <p class="card-body">Reliable machine operators, maintenance technicians, safety coordinators, and plant supervisory personnel.</p>
            <a href="industrial-staffing.html" class="card-link">Explore Industrial Staffing &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">Operations &amp; Logistics</span>
            <div class="card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 12V8H6a2 2 0 0 1-2-2c0-1.1.9-2 2-2h12v4"/><path d="M4 6v12c0 1.1.9 2 2 2h14v-4"/></svg>
            </div>
            <h3 class="card-title">Blue-Collar Staffing</h3>
            <p class="card-body">Warehouse associates, assembly hands, material handlers, loaders, and ground workforce staff for supply chain hubs.</p>
            <a href="blue-collar-staffing.html" class="card-link">Explore Blue-Collar Staffing &rarr;</a>
          </div>

          <div class="service-card">
            <span class="service-badge">Managed Solutions</span>
            <div class="card-icon teal">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>
            </div>
            <h3 class="card-title">Recruitment Process Outsourcing</h3>
            <p class="card-body">Transfer part or all of your internal recruitment cycle—from sourcing and screening to offer administration—under SLA frameworks.</p>
            <a href="recruitment-process-outsourcing.html" class="card-link">Explore RPO &rarr;</a>
          </div>
        </div>

        <div class="text-center" style="margin-top: 3rem;">
          <a href="services.html" class="btn btn-outline">View All 17 Staffing Services &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Industries We Serve Section -->
    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle">Sector Alignment</span>
          <h2>Industries We Serve</h2>
          <p class="lead">Domain-focused talent pools structured to address sector-specific staffing challenges.</p>
        </div>

        <div class="grid-3">
          <div class="industry-card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="it-technology.html">IT &amp; Technology</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Software engineers, cybersecurity analysts, database administrators, and infrastructure managers.</p>
            <a href="it-technology.html" class="card-link">Industry Overview &rarr;</a>
          </div>
          <div class="industry-card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="healthcare.html">Healthcare</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Clinical support staff, laboratory technicians, medical record administrators, and clinic assistants.</p>
            <a href="healthcare.html" class="card-link">Industry Overview &rarr;</a>
          </div>
          <div class="industry-card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="manufacturing.html">Manufacturing</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Plant supervisors, quality inspectors, CNC machinists, and assembly line operators.</p>
            <a href="manufacturing.html" class="card-link">Industry Overview &rarr;</a>
          </div>
          <div class="industry-card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="banking-finance.html">Banking &amp; Finance</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Financial analysts, accounts managers, compliance executives, and ledger specialists.</p>
            <a href="banking-finance.html" class="card-link">Industry Overview &rarr;</a>
          </div>
          <div class="industry-card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="retail-ecommerce.html">Retail &amp; E-commerce</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Store associates, fulfillment pickers, customer care specialists, and merchandising coordinators.</p>
            <a href="retail-ecommerce.html" class="card-link">Industry Overview &rarr;</a>
          </div>
          <div class="industry-card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="construction.html">Construction</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Site safety supervisors, heavy machinery operators, field engineers, and tradespeople.</p>
            <a href="construction.html" class="card-link">Industry Overview &rarr;</a>
          </div>
          <div class="industry-card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="logistics-transportation.html">Logistics &amp; Transportation</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Dispatchers, freight coordinators, warehouse handlers, and distribution leads.</p>
            <a href="logistics-transportation.html" class="card-link">Industry Overview &rarr;</a>
          </div>
          <div class="industry-card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="hospitality.html">Hospitality</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Front desk managers, food &amp; beverage service staff, housekeeping, and event support.</p>
            <a href="hospitality.html" class="card-link">Industry Overview &rarr;</a>
          </div>
          <div class="industry-card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="telecommunications.html">Telecommunications</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Network engineers, fiber optic technicians, NOC coordinators, and commercial sales reps.</p>
            <a href="telecommunications.html" class="card-link">Industry Overview &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- How Our Recruitment Process Works (5 Visual Steps) -->
    <section class="section section-bg-light">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle teal">Systematic Workflow</span>
          <h2>How Our Recruitment Process Works</h2>
          <p class="lead">
            An illustrative multi-stage recruitment lifecycle engineered to ensure role clarity and thorough evaluation.
          </p>
        </div>

        <div class="demo-callout-box text-center" style="max-width: 800px; margin: 0 auto 2.5rem;">
          <strong>Illustrative Workflow Notice:</strong> The recruitment stages outlined below describe typical agency workflows. All hiring decisions, offers, and terms remain the prerogative of individual employer organizations.
        </div>

        <div class="process-timeline">
          <div class="process-step">
            <div class="step-number">1</div>
            <h3 class="step-title">Understand Hiring Requirements</h3>
            <p class="step-text">Define precise job parameters, technical competencies, organizational culture, and expected engagement timelines.</p>
          </div>
          <div class="process-step">
            <div class="step-number teal">2</div>
            <h3 class="step-title">Source Suitable Candidates</h3>
            <p class="step-text">Leverage specialized recruitment networks, talent databases, and targeted outreach to identify prospective talent.</p>
          </div>
          <div class="process-step">
            <div class="step-number">3</div>
            <h3 class="step-title">Screen and Evaluate</h3>
            <p class="step-text">Conduct preliminary competency reviews, resume validations, experience checks, and suitability assessments.</p>
          </div>
          <div class="process-step">
            <div class="step-number teal">4</div>
            <h3 class="step-title">Coordinate Interviews</h3>
            <p class="step-text">Facilitate structured interview sessions between shortlisted candidates and corporate hiring managers.</p>
          </div>
          <div class="process-step">
            <div class="step-number">5</div>
            <h3 class="step-title">Support Selection &amp; Onboarding</h3>
            <p class="step-text">Assist in offer communication, joining documentation, and initial induction facilitation.</p>
          </div>
        </div>

        <div class="text-center" style="margin-top: 3rem;">
          <a href="process.html" class="btn btn-primary">Learn More About Our Process &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Why Staffing Solutions? (Benefits Overview) -->
    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle">Operational Value</span>
          <h2>Why Consider Workforce Solutions?</h2>
          <p class="lead">
            Understanding the potential operational benefits of structured workforce partnerships.
          </p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Flexible Workforce Planning</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Adapt staffing headcounts dynamically to changing market demands without fixed long-term commitments.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Seasonal Peak Support</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Mobilize verified temporary personnel during holiday surges, fiscal year-ends, or production spikes.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Specialized Talent Access</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Reach niche professional skills and technical profiles that may not be actively browsing standard job boards.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Recruitment Process Support</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Outsource time-intensive resume screening, candidate communication, and initial vetting tasks.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Workforce Scalability</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Expand or scale down operational teams quickly across multi-site facilities with established recruitment pipelines.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Reduced Internal Workload</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Free internal HR and hiring managers to concentrate on core strategy, staff retention, and organizational development.</p>
          </div>
        </div>

        <div class="demo-callout-box" style="margin-top: 2rem;">
          <strong>Informational Statement:</strong> The potential benefits stated above are common recruitment advantages. Outcomes vary based on market conditions, specific requirements, and internal hiring policies; no guaranteed placement timeline or cost-reduction is implied.
        </div>
      </div>
    </section>

    <!-- Two Mid-page Action Callouts: Employer CTA & Candidate CTA -->
    <section class="section section-bg-navy">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3rem;">
          <!-- Employer CTA -->
          <div style="background: rgba(255, 255, 255, 0.05); padding: 2.5rem; border-radius: var(--radius-lg); border: 1px solid rgba(255, 255, 255, 0.1);">
            <span class="pathway-badge" style="background: var(--color-bright-blue); color: #FFF;">Employer Solutions</span>
            <h3 style="color: #FFF; font-size: 1.6rem; margin-top: 0.75rem; margin-bottom: 1rem;">Need People Who Can Move Your Business Forward?</h3>
            <p style="color: #C0CDDF; margin-bottom: 1.75rem;">
              Whether you need a single specialized engineer or an entire warehouse shift crew, our staffing consultants are ready to assist.
            </p>
            <a href="request-staff.html" class="btn btn-teal">Submit Staffing Requirement &rarr;</a>
          </div>

          <!-- Candidate CTA -->
          <div style="background: rgba(255, 255, 255, 0.05); padding: 2.5rem; border-radius: var(--radius-lg); border: 1px solid rgba(255, 255, 255, 0.1);">
            <span class="pathway-badge" style="background: var(--color-teal-accent); color: #FFF;">Candidate Portal</span>
            <h3 style="color: #FFF; font-size: 1.6rem; margin-top: 0.75rem; margin-bottom: 1rem;">Your Next Career Opportunity Starts Here</h3>
            <p style="color: #C0CDDF; margin-bottom: 1.75rem;">
              Browse our demo job listings, explore typical roles across 9 major industries, or register your profile for simulated vacancies.
            </p>
            <a href="jobs.html" class="btn btn-primary">Explore Jobs &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Case Studies Preview -->
    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle">Real-World Models</span>
          <h2>Illustrative Staffing Case Studies</h2>
          <p class="lead">Simulated case scenarios demonstrating how structured recruitment solves hiring bottlenecks.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <div class="demo-disclaimer-pill">ILLUSTRATIVE DEMO CASE STUDY</div>
            <h3 class="card-title">Manufacturing Workforce Planning</h3>
            <p class="card-body">A scenario examining how a mid-sized assembly facility addressed seasonal ramp-up challenges by engaging flexible temporary shifts.</p>
            <a href="case-studies.html" class="card-link">Read Case Scenario &rarr;</a>
          </div>

          <div class="card">
            <div class="demo-disclaimer-pill">ILLUSTRATIVE DEMO CASE STUDY</div>
            <h3 class="card-title">IT Talent Acquisition Workflow</h3>
            <p class="card-body">An analysis of specialized sourcing workflows required to identify senior full-stack developers in a competitive talent market.</p>
            <a href="case-studies.html" class="card-link">Read Case Scenario &rarr;</a>
          </div>

          <div class="card">
            <div class="demo-disclaimer-pill">ILLUSTRATIVE DEMO CASE STUDY</div>
            <h3 class="card-title">High-Volume Retail Recruitment</h3>
            <p class="card-body">A demonstration of high-throughput candidate screening funnels deployed ahead of major holiday retail shopping periods.</p>
            <a href="case-studies.html" class="card-link">Read Case Scenario &rarr;</a>
          </div>
        </div>

        <div class="text-center" style="margin-top: 2rem;">
          <a href="case-studies.html" class="btn btn-outline">Explore All Case Studies &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Latest Job Opportunities Preview -->
    <section class="section section-bg-light">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle teal">Career Opportunities</span>
          <h2>Sample Job Openings</h2>
          <p class="lead">Sample vacancies reflecting active roles currently sought by hiring employers.</p>
        </div>

        <div class="grid-3">
          <div class="job-card" style="flex-direction: column;">
            <div class="demo-disclaimer-pill">DEMO JOB LISTING — NOT A VERIFIED LIVE VACANCY</div>
            <h3 style="font-size: 1.25rem; margin: 0.5rem 0;"><a href="job-details.html?id=job-101">Software Developer</a></h3>
            <p class="text-muted" style="font-size: 0.85rem;">IT &amp; Technology • Hyderabad (Demo)</p>
            <p style="font-size: 0.9rem; margin: 0.75rem 0 1.25rem;">Support enterprise web applications, REST services, and modern frontend interfaces.</p>
            <a href="job-details.html?id=job-101" class="btn btn-outline btn-sm" style="width: 100%;">View Role Details</a>
          </div>

          <div class="job-card" style="flex-direction: column;">
            <div class="demo-disclaimer-pill">DEMO JOB LISTING — NOT A VERIFIED LIVE VACANCY</div>
            <h3 style="font-size: 1.25rem; margin: 0.5rem 0;"><a href="job-details.html?id=job-102">Data Analyst</a></h3>
            <p class="text-muted" style="font-size: 0.85rem;">Banking &amp; Finance • Bangalore (Demo)</p>
            <p style="font-size: 0.9rem; margin: 0.75rem 0 1.25rem;">Analyze financial data flows, build KPI dashboards, and support operational decisions.</p>
            <a href="job-details.html?id=job-102" class="btn btn-outline btn-sm" style="width: 100%;">View Role Details</a>
          </div>

          <div class="job-card" style="flex-direction: column;">
            <div class="demo-disclaimer-pill">DEMO JOB LISTING — NOT A VERIFIED LIVE VACANCY</div>
            <h3 style="font-size: 1.25rem; margin: 0.5rem 0;"><a href="job-details.html?id=job-106">Warehouse Associate</a></h3>
            <p class="text-muted" style="font-size: 0.85rem;">Logistics &amp; Transport • Hyderabad (Demo)</p>
            <p style="font-size: 0.9rem; margin: 0.75rem 0 1.25rem;">Assist with inventory receipt, packing, order dispatch, and physical stock sorting.</p>
            <a href="job-details.html?id=job-106" class="btn btn-outline btn-sm" style="width: 100%;">View Role Details</a>
          </div>
        </div>

        <div class="text-center" style="margin-top: 2.5rem;">
          <a href="jobs.html" class="btn btn-primary">Browse All Demo Jobs &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Final CTA Banner -->
    <section class="section" style="padding: 4.5rem 0;">
      <div class="container">
        <div style="background: linear-gradient(135deg, var(--color-primary-navy) 0%, var(--color-secondary-navy) 100%); padding: 3.5rem 2rem; border-radius: var(--radius-xl); text-align: center; color: #FFF;">
          <h2 style="color: #FFF; font-size: clamp(1.8rem, 3vw, 2.5rem); margin-bottom: 1rem;">Let's Connect Talent With Opportunity</h2>
          <p style="color: #D2DCE8; max-width: 650px; margin: 0 auto 2rem; font-size: 1.1rem;">
            Whether you are building a resilient corporate workforce or seeking your next career milestone, our generic staffing framework provides the tools you need.
          </p>
          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="request-staff.html" class="btn btn-teal btn-lg">Hire Staff</a>
            <a href="jobs.html" class="btn btn-outline-white btn-lg">Find Jobs</a>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("index.html", render_page(
        "Connecting Businesses With the Right Talent",
        "Flexible staffing and workforce solutions connecting employers with qualified talent and candidates with career opportunities.",
        "home", content
    ))

print("make_index defined.")
