"""
STAFFING AGENCY — Employer, Candidate & Legal Pages Generator
Generates:
1. employers.html
2. request-staff.html
3. candidates.html
4. jobs.html
5. job-details.html
6. register-candidate.html
7. careers.html
8. privacy-policy.html
9. terms-and-conditions.html
10. cookie-policy.html
"""

from generate_helpers import render_page, render_placeholder
from build_site_part1 import register_image, write_html

# ==============================================================================
# 1. EMPLOYERS LANDING PAGE — employers.html
# ==============================================================================
def make_employers():
    register_image(
        "staffing-employer-meeting.jpg", "employers.html", "Employer Hero",
        "Corporate executives reviewing flexible workforce proposals with recruitment account directors",
        "16:9", "1200x800", "Landscape",
        "Commercial photograph of business leaders in a contemporary glass-paneled meeting room reviewing staffing service level agreements. Confident postures, natural sunlight, business attire, tablet and notebook on table.",
        "Rule of thirds, corporate clients on left engaging with agency director on right", "Eye-level medium shot", "Soft balanced daylight",
        "Modern corporate boardroom with glass walls", "Corporate executive photography",
        "Navy, slate blue, warm walnut wood, white", "Subjects centered around meeting desk"
    )

    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Employer Solutions</span>
        <h1>Build Your Workforce With Flexible Staffing Solutions</h1>
        <p class="lead">
          Strategic talent acquisition, flexible staffing models, and dedicated recruitment management designed for organizational agility.
        </p>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
          <a href="request-staff.html" class="btn btn-teal btn-lg">Request Staffing Consultation</a>
          <a href="services.html" class="btn btn-outline-white btn-lg">Explore All Staffing Services</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem;">
          <div>
            <span class="section-subtitle">Client Value</span>
            <h2>Talent Acquisition Aligned With Business Goals</h2>
            <p>
              Securing qualified personnel requires more than standard resume matching. We work closely alongside HR directors, operations leaders, and hiring managers to understand operational timelines, technical criteria, and cultural expectations.
            </p>
            <p>
              Whether you need to scale production shifts with temporary workers, fill a mission-critical technology opening, or outsource your full recruitment cycle under an RPO framework, our structured processes provide reliable talent alignment.
            </p>
            <div class="demo-callout-box">
              <strong>Demonstration Notice:</strong> This employer portal showcases corporate workforce capabilities in simulated mode. Forms on this site validate client-side without storing or transmitting corporate information.
            </div>
          </div>
          <div>
            {render_placeholder("staffing-employer-meeting.jpg", "ratio-16-9", "staffing-employer-meeting.jpg", 1200, 800, "Corporate business leaders in workforce consultation")}
          </div>
        </div>
      </div>
    </section>

    <!-- Staffing Service Options for Employers -->
    <section class="section section-bg-light">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle teal">Engagement Models</span>
          <h2>Tailored Staffing Options</h2>
          <p class="lead">Choose the engagement model that best satisfies your operational timeframe and headcount needs.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;"><a href="permanent-staffing.html">Permanent Staffing</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Direct hire recruitment for core, long-term technical, corporate, and operational positions.</p>
            <a href="permanent-staffing.html" class="card-link">Learn More &rarr;</a>
          </div>

          <div class="card">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;"><a href="temporary-staffing.html">Temporary Staffing</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Contingent workers deployed for seasonal demand peaks, temporary leaves, or volume spikes.</p>
            <a href="temporary-staffing.html" class="card-link">Learn More &rarr;</a>
          </div>

          <div class="card">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;"><a href="contract-staffing.html">Contract Staffing</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Fixed-term technical contractors for dedicated milestones and specialized system rollouts.</p>
            <a href="contract-staffing.html" class="card-link">Learn More &rarr;</a>
          </div>

          <div class="card">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;"><a href="temp-to-hire.html">Temp-to-Hire</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Assess candidate skills and cultural compatibility on assignment prior to permanent offer.</p>
            <a href="temp-to-hire.html" class="card-link">Learn More &rarr;</a>
          </div>

          <div class="card">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;"><a href="bulk-hiring.html">Bulk Recruitment</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">High-volume candidate screening campaigns to staff facility launches or fulfillment centers.</p>
            <a href="bulk-hiring.html" class="card-link">Learn More &rarr;</a>
          </div>

          <div class="card">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;"><a href="recruitment-process-outsourcing.html">Recruitment Process Outsourcing</a></h3>
            <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Outsource end-to-end recruitment management and pipeline tracking under formal SLA terms.</p>
            <a href="recruitment-process-outsourcing.html" class="card-link">Learn More &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- How to Request Staff -->
    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle">Fulfillment Steps</span>
          <h2>How to Request Staff</h2>
          <p class="lead">Simple, structured requisition intake designed to accelerate candidate shortlisting.</p>
        </div>

        <div class="grid-3">
          <div class="card text-center">
            <div class="step-number" style="margin: 0 auto 1.25rem;">1</div>
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Submit Requisition</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Fill out our online Request Staff form with your role parameters, headcount, and timeline.</p>
          </div>

          <div class="card text-center">
            <div class="step-number teal" style="margin: 0 auto 1.25rem;">2</div>
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Discovery Consultation</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Our talent specialist contacts you to clarify technical criteria, compensation bands, and schedules.</p>
          </div>

          <div class="card text-center">
            <div class="step-number" style="margin: 0 auto 1.25rem;">3</div>
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Review Pre-Screened Profiles</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Receive thoroughly screened candidate dossiers ready for your management panel interviews.</p>
          </div>
        </div>

        <div class="text-center" style="margin-top: 3rem;">
          <a href="request-staff.html" class="btn btn-primary btn-lg">Submit a Staffing Requirement &rarr;</a>
        </div>
      </div>
    </section>
    """
    write_html("employers.html", render_page(
        "Employers — Flexible Staffing & Workforce Solutions",
        "Discover employer staffing services, flexible workforce models, and streamlined talent acquisition for organizations.",
        "employers", content,
        breadcrumbs=[("Home", "index.html"), ("Employers", None)]
    ))

# ==============================================================================
# 2. REQUEST STAFF FORM — request-staff.html
# ==============================================================================
def make_request_staff():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Employer Requisition</span>
        <h1>Request Staffing Consultation</h1>
        <p class="lead">
          Submit your workforce requirements. Our staffing specialists will analyze your role specifications and recommend an appropriate talent solution.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 900px;">
        <div class="demo-callout-box">
          <strong>Frontend Demonstration Notice:</strong> This employer staffing request form operates purely in local demo simulation. Form entries are validated using client-side JavaScript, but no data is transmitted or stored on any server or database.
        </div>

        <div class="form-card">
          <form id="employer-request-form" novalidate>
            <h3 style="margin-bottom: 1.5rem; border-bottom: 1px solid var(--color-border); padding-bottom: 0.75rem;">1. Organization &amp; Contact Information</h3>
            
            <div class="grid-2">
              <div class="form-group">
                <label class="form-label" for="emp-name">Full Name *</label>
                <input type="text" id="emp-name" class="form-control" placeholder="e.g. Jordan Smith" required>
                <div class="invalid-feedback">Please enter your full name.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="emp-email">Business Email *</label>
                <input type="email" id="emp-email" class="form-control" placeholder="jordan@company.com" required>
                <div class="invalid-feedback">Please enter a valid business email address.</div>
              </div>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label" for="emp-company">Company / Organization Name *</label>
                <input type="text" id="emp-company" class="form-control" placeholder="e.g. Acme Enterprises Ltd" required>
                <div class="invalid-feedback">Please enter your company name.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="emp-phone">Phone Number *</label>
                <input type="tel" id="emp-phone" class="form-control" placeholder="0000000000" required>
                <div class="invalid-feedback">Please enter a valid telephone number.</div>
              </div>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label" for="emp-industry">Industry Sector *</label>
                <select id="emp-industry" class="form-select" required>
                  <option value="">Select Industry...</option>
                  <option value="IT & Technology">IT &amp; Technology</option>
                  <option value="Healthcare">Healthcare</option>
                  <option value="Manufacturing">Manufacturing</option>
                  <option value="Banking & Finance">Banking &amp; Finance</option>
                  <option value="Retail & E-commerce">Retail &amp; E-commerce</option>
                  <option value="Construction">Construction</option>
                  <option value="Logistics & Transportation">Logistics &amp; Transportation</option>
                  <option value="Hospitality">Hospitality</option>
                  <option value="Telecommunications">Telecommunications</option>
                  <option value="Other">Other Commercial Sector</option>
                </select>
                <div class="invalid-feedback">Please select an industry sector.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="emp-location">Work Location (City / Facility) *</label>
                <input type="text" id="emp-location" class="form-control" placeholder="e.g. Hyderabad, On-site / Remote" required>
                <div class="invalid-feedback">Please specify the work location.</div>
              </div>
            </div>

            <h3 style="margin: 2rem 0 1.5rem; border-bottom: 1px solid var(--color-border); padding-bottom: 0.75rem;">2. Staffing Requisition Details</h3>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label" for="emp-role">Job Title / Role Required *</label>
                <input type="text" id="emp-role" class="form-control" placeholder="e.g. Senior Software Engineer" required>
                <div class="invalid-feedback">Please specify the required job role.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="emp-count">Number of Employees Required *</label>
                <input type="number" id="emp-count" class="form-control" min="1" max="1000" placeholder="e.g. 5" required>
                <div class="invalid-feedback">Please indicate headcount required.</div>
              </div>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label" for="emp-staffing-type">Staffing Engagement Model *</label>
                <select id="emp-staffing-type" class="form-select" required>
                  <option value="">Select Staffing Type...</option>
                  <option value="Permanent">Permanent Staffing (Direct Hire)</option>
                  <option value="Temporary">Temporary Staffing (Contingent)</option>
                  <option value="Contract">Contract Staffing (Fixed-Term)</option>
                  <option value="Temp-to-Hire">Temp-to-Hire (Trial Evaluation)</option>
                  <option value="Bulk Hiring">Bulk Hiring (Mass Recruitment)</option>
                  <option value="Executive Search">Executive Search (Leadership)</option>
                  <option value="Other">Other Customized Model</option>
                </select>
                <div class="invalid-feedback">Please select a staffing type.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="emp-start-date">Expected Start Date</label>
                <input type="date" id="emp-start-date" class="form-control">
              </div>
            </div>

            <div class="form-group">
              <label class="form-label" for="emp-exp">Experience Requirements</label>
              <input type="text" id="emp-exp" class="form-control" placeholder="e.g. 3-5 years relevant domain experience">
            </div>

            <div class="form-group">
              <label class="form-label" for="emp-details">Additional Details &amp; Mandatory Qualifications</label>
              <textarea id="emp-details" class="form-control" rows="4" placeholder="Detail any specific software tools, trade certifications, shift requirements, or technical criteria..."></textarea>
            </div>

            <div style="margin-top: 2rem;">
              <button type="submit" class="btn btn-teal btn-lg" style="width: 100%;">Submit Demo Staffing Requisition</button>
            </div>
          </form>
        </div>
      </div>
    </section>
    """
    write_html("request-staff.html", render_page(
        "Request Staff — Submit a Staffing Requisition",
        "Submit your workforce requirements for permanent, temporary, contract, or bulk staffing solutions. Client-side demo form.",
        "employers", content,
        breadcrumbs=[("Home", "index.html"), ("Employers", "employers.html"), ("Request Staff", None)]
    ))

# ==============================================================================
# 3. CANDIDATES LANDING PAGE — candidates.html
# ==============================================================================
def make_candidates():
    register_image(
        "staffing-candidate-registration.jpg", "candidates.html", "Candidates Hero",
        "Candidate speaking with a career advisor in a modern recruitment office lounge",
        "16:9", "1200x800", "Landscape",
        "Warm commercial photograph of a career counselor reviewing resume highlights with a job applicant in a comfortable, sunlit consultation area. Open notebook, coffee mugs, encouraging professional expressions, natural window light.",
        "Medium two-shot, counselor on left and candidate on right", "Eye-level medium angle", "Natural soft daylight",
        "Modern corporate recruitment agency consultation lounge", "Commercial editorial portraiture",
        "Navy, teal accent, soft amber wood, white", "Subjects seated across coffee table"
    )

    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Job Seeker Portal</span>
        <h1>Find Opportunities That Match Your Skills</h1>
        <p class="lead">
          Connect with career pathways across 9 major industries. Search illustrative vacancies or register your profile with our recruitment consultants.
        </p>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
          <a href="jobs.html" class="btn btn-teal btn-lg">Search Job Vacancies</a>
          <a href="register-candidate.html" class="btn btn-outline-white btn-lg">Register Your Resume</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem;">
          <div>
            <span class="section-subtitle">Career Advancement</span>
            <h2>Navigating Your Next Career Step</h2>
            <p>
              Whether you are a fresh university graduate stepping into the professional market, an experienced technical contributor seeking specialized contract work, or a seasoned corporate manager exploring full-time permanent roles, our staffing framework supports your journey.
            </p>
            <p>
              We provide transparent job criteria, objective interview briefings, and direct introductions to hiring managers looking for candidates with your qualifications.
            </p>
            <div class="demo-callout-box">
              <strong>Demonstration Candidate Notice:</strong> This candidate portal is an illustrative demonstration. Job listings and candidate registration operate in demo simulation mode without saving personal data or resumes.
            </div>
          </div>
          <div>
            {render_placeholder("staffing-candidate-registration.jpg", "ratio-16-9", "staffing-candidate-registration.jpg", 1200, 800, "Candidate discussing career opportunities with recruiter")}
          </div>
        </div>
      </div>
    </section>

    <!-- Candidate Registration Steps -->
    <section class="section section-bg-light">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle teal">Candidate Journey</span>
          <h2>How It Works for Job Seekers</h2>
          <p class="lead">Four straightforward steps to connect your experience with prospective employers.</p>
        </div>

        <div class="grid-4">
          <div class="card text-center">
            <div class="step-number" style="margin: 0 auto 1.25rem;">1</div>
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Register Profile</h3>
            <p class="text-muted" style="font-size: 0.875rem;">Submit your contact information, desired role preferences, and resume document.</p>
          </div>

          <div class="card text-center">
            <div class="step-number teal" style="margin: 0 auto 1.25rem;">2</div>
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Recruiter Review</h3>
            <p class="text-muted" style="font-size: 0.875rem;">Our recruiters match your background against active client requisitions.</p>
          </div>

          <div class="card text-center">
            <div class="step-number" style="margin: 0 auto 1.25rem;">3</div>
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Interview Briefing</h3>
            <p class="text-muted" style="font-size: 0.875rem;">Receive comprehensive briefings on company culture and role expectations prior to client meetings.</p>
          </div>

          <div class="card text-center">
            <div class="step-number teal" style="margin: 0 auto 1.25rem;">4</div>
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Selection &amp; Offer</h3>
            <p class="text-muted" style="font-size: 0.875rem;">Receive clear offer terms and supportive guidance through joining documentation.</p>
          </div>
        </div>

        <div class="text-center" style="margin-top: 3rem;">
          <a href="register-candidate.html" class="btn btn-teal btn-lg">Register Your Resume (Demo) &rarr;</a>
        </div>
      </div>
    </section>
    """
    write_html("candidates.html", render_page(
        "Candidates — Career Opportunities & Registration",
        "Explore job opportunities across 9 industries, learn about our recruitment process, and register your candidate profile.",
        "candidates", content,
        breadcrumbs=[("Home", "index.html"), ("Candidates", None)]
    ))

# ==============================================================================
# 4. JOB SEARCH BOARD — jobs.html
# ==============================================================================
def make_jobs():
    content = f"""
    <section class="page-hero" style="padding-bottom: 5rem;">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Explore Openings</span>
        <h1>Search Demo Job Vacancies</h1>
        <p class="lead">
          Browse illustrative role listings across technology, healthcare, manufacturing, finance, and logistics. Filter by domain or employment type.
        </p>
      </div>
    </section>

    <!-- Search Bar & Filters Card -->
    <div class="container">
      <div class="job-search-bar">
        <form id="job-search-form" novalidate>
          <div class="search-filters-grid">
            <div>
              <label class="form-label" for="search-keyword">Keyword / Role</label>
              <input type="text" id="search-keyword" class="form-control" placeholder="e.g. Developer, Analyst, Warehouse...">
            </div>

            <div>
              <label class="form-label" for="filter-industry">Industry</label>
              <select id="filter-industry" class="form-select">
                <option value="all">All Industries</option>
                <option value="IT & Technology">IT &amp; Technology</option>
                <option value="Banking & Finance">Banking &amp; Finance</option>
                <option value="Retail & E-commerce">Retail &amp; E-commerce</option>
                <option value="Manufacturing">Manufacturing</option>
                <option value="Logistics & Transportation">Logistics &amp; Transportation</option>
                <option value="Healthcare">Healthcare</option>
                <option value="Telecommunications">Telecommunications</option>
              </select>
            </div>

            <div>
              <label class="form-label" for="filter-type">Employment Type</label>
              <select id="filter-type" class="form-select">
                <option value="all">All Types</option>
                <option value="permanent">Permanent</option>
                <option value="contract">Contract</option>
                <option value="temporary">Temporary</option>
                <option value="full-time">Full-Time</option>
              </select>
            </div>

            <div>
              <label class="form-label" for="filter-experience">Experience</label>
              <select id="filter-experience" class="form-select">
                <option value="all">All Levels</option>
                <option value="entry">Entry (1-2 Yrs)</option>
                <option value="mid">Mid (3-4 Yrs)</option>
                <option value="senior">Senior (5+ Yrs)</option>
              </select>
            </div>

            <div style="display: flex; gap: 0.5rem;">
              <button type="submit" class="btn btn-primary" style="height: 42px;">Search</button>
              <button type="button" id="reset-filters-btn" class="btn btn-outline" style="height: 42px;" title="Reset filters">Reset</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <!-- Job Results Section -->
    <section class="section" style="padding-top: 3rem;">
      <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
          <h2 id="jobs-count" style="font-size: 1.25rem; margin-bottom: 0;">Showing Demo Vacancies</h2>
          <div class="demo-disclaimer-pill">DEMO VACANCIES — ILLUSTRATIVE SIMULATION</div>
        </div>

        <!-- Dynamic Jobs Container Rendered via Vanilla JS -->
        <div id="jobs-container">
          <!-- Fallback noscript or loading state -->
          <p class="text-muted">Loading demo vacancies...</p>
        </div>

        <!-- Load More Container -->
        <div class="text-center" style="margin-top: 2.5rem;">
          <button type="button" id="load-more-jobs-btn" class="btn btn-outline" style="display: none;">Load More Demo Vacancies</button>
        </div>
      </div>
    </section>
    """
    write_html("jobs.html", render_page(
        "Job Search — Explore Demo Vacancies & Roles",
        "Interactive searchable job board with filters for industry, experience, and employment type. Illustrative demo vacancies.",
        "candidates", content,
        breadcrumbs=[("Home", "index.html"), ("Candidates", "candidates.html"), ("Job Search", None)]
    ))

# ==============================================================================
# 5. JOB DETAILS PAGE — job-details.html
# ==============================================================================
def make_job_details():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Job Opportunity</span>
        <h1>Demo Vacancy Details</h1>
        <p class="lead">Explore role summary, responsibilities, technical competencies, and sample application instructions.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="grid-template-columns: 2.2fr 1fr; gap: 2.5rem; align-items: flex-start;">
          <!-- Left Main Container populated via job-search.js based on ?id= -->
          <div id="job-details-container">
            <div class="card" style="padding: 2.5rem;">
              <p class="text-muted">Loading role details...</p>
            </div>
          </div>

          <!-- Right Sidebar -->
          <div>
            <div class="card" style="margin-bottom: 1.5rem; padding: 1.5rem;">
              <h3 style="font-size: 1.15rem; margin-bottom: 0.75rem;">Quick Application Notes</h3>
              <p class="text-muted" style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 1rem;">
                This listing is created solely for user interface evaluation and applicant workflow testing.
              </p>
              <a href="register-candidate.html" class="btn btn-teal btn-sm" style="width: 100%;">Register Resume (Demo)</a>
            </div>

            <h3 style="font-size: 1.15rem; margin-bottom: 1rem;">Other Sample Openings</h3>
            <div id="similar-jobs-list">
              <!-- Rendered via JS -->
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("job-details.html", render_page(
        "Job Details — Demo Vacancy Profile",
        "Detailed view of sample job role, key responsibilities, educational requirements, and demo application instructions.",
        "candidates", content,
        breadcrumbs=[("Home", "index.html"), ("Job Search", "jobs.html"), ("Job Details", None)]
    ))

# ==============================================================================
# 6. CANDIDATE REGISTRATION — register-candidate.html
# ==============================================================================
def make_register_candidate():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Candidate Portal</span>
        <h1>Candidate Registration</h1>
        <p class="lead">
          Register your resume and career preferences with our recruitment consultants for future matching against client openings.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 900px;">
        <div class="demo-callout-box">
          <strong>Frontend Demonstration Notice:</strong> This candidate registration interface operates exclusively in frontend simulation mode. Resumes and candidate details are validated locally in your browser; <strong>no files or personal information are transmitted, uploaded, or stored in any recruitment database.</strong>
        </div>

        <div class="form-card">
          <form id="candidate-registration-form" novalidate>
            <h3 style="margin-bottom: 1.5rem; border-bottom: 1px solid var(--color-border); padding-bottom: 0.75rem;">1. Personal Information</h3>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label" for="cand-name">Full Name *</label>
                <input type="text" id="cand-name" class="form-control" placeholder="e.g. Taylor Reed" required>
                <div class="invalid-feedback">Please enter your full name.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="cand-email">Email Address *</label>
                <input type="email" id="cand-email" class="form-control" placeholder="taylor@example.com" required>
                <div class="invalid-feedback">Please enter a valid email address.</div>
              </div>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label" for="cand-phone">Phone Number *</label>
                <input type="tel" id="cand-phone" class="form-control" placeholder="0000000000" required>
                <div class="invalid-feedback">Please enter your contact phone number.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="cand-location">Current Location (City / Region) *</label>
                <input type="text" id="cand-location" class="form-control" placeholder="e.g. Hyderabad, India" required>
                <div class="invalid-feedback">Please state your current location.</div>
              </div>
            </div>

            <h3 style="margin: 2rem 0 1.5rem; border-bottom: 1px solid var(--color-border); padding-bottom: 0.75rem;">2. Professional Background &amp; Preferences</h3>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label" for="cand-role">Preferred Job Role *</label>
                <input type="text" id="cand-role" class="form-control" placeholder="e.g. Software Developer / Data Analyst" required>
                <div class="invalid-feedback">Please specify your target job role.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="cand-industry">Preferred Industry *</label>
                <select id="cand-industry" class="form-select" required>
                  <option value="">Select Target Industry...</option>
                  <option value="IT & Technology">IT &amp; Technology</option>
                  <option value="Healthcare">Healthcare</option>
                  <option value="Manufacturing">Manufacturing</option>
                  <option value="Banking & Finance">Banking &amp; Finance</option>
                  <option value="Retail & E-commerce">Retail &amp; E-commerce</option>
                  <option value="Construction">Construction</option>
                  <option value="Logistics & Transportation">Logistics &amp; Transportation</option>
                  <option value="Hospitality">Hospitality</option>
                  <option value="Telecommunications">Telecommunications</option>
                  <option value="Any Industry">Open to Any Sector</option>
                </select>
                <div class="invalid-feedback">Please select your preferred industry.</div>
              </div>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label" for="cand-experience">Total Experience *</label>
                <select id="cand-experience" class="form-select" required>
                  <option value="">Select Experience Level...</option>
                  <option value="Fresher / Graduate">Fresher / Recent Graduate (0-1 Year)</option>
                  <option value="Junior">Junior Professional (1-3 Years)</option>
                  <option value="Mid-Level">Mid-Level Professional (3-5 Years)</option>
                  <option value="Senior">Senior Professional (5-8 Years)</option>
                  <option value="Lead / Executive">Lead / Manager / Executive (8+ Years)</option>
                </select>
                <div class="invalid-feedback">Please select your experience range.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="cand-type">Employment Type Preference *</label>
                <select id="cand-type" class="form-select" required>
                  <option value="">Select Preference...</option>
                  <option value="Permanent">Permanent (Full-Time Direct Hire)</option>
                  <option value="Contract">Contract (Fixed-Term Project)</option>
                  <option value="Temporary">Temporary (Contingent Shift)</option>
                  <option value="Temp-to-Hire">Temp-to-Hire (Trial Period)</option>
                  <option value="Open to Any">Open to All Engagement Types</option>
                </select>
                <div class="invalid-feedback">Please select an employment preference.</div>
              </div>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label" for="cand-education">Highest Education Level</label>
                <input type="text" id="cand-education" class="form-control" placeholder="e.g. B.Tech in Computer Science / B.Com">
              </div>

              <div class="form-group">
                <label class="form-label" for="cand-status">Current Employment Status *</label>
                <select id="cand-status" class="form-select" required>
                  <option value="">Select Status...</option>
                  <option value="Immediately Available">Immediately Available</option>
                  <option value="Serving Notice">Serving Notice Period (15-30 Days)</option>
                  <option value="Employed but Looking">Employed (Exploring Opportunities)</option>
                  <option value="Student / Fresher">Student / Recent Graduate</option>
                </select>
                <div class="invalid-feedback">Please indicate your current employment status.</div>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label" for="cand-skills">Key Capabilities &amp; Skills</label>
              <input type="text" id="cand-skills" class="form-control" placeholder="e.g. JavaScript, SQL, Financial Reconciliation, Shift Management...">
            </div>

            <!-- Resume Upload Interface -->
            <h3 style="margin: 2rem 0 1rem; border-bottom: 1px solid var(--color-border); padding-bottom: 0.75rem;">3. Resume Upload (Demo Interface)</h3>
            <div class="form-group">
              <label class="form-label">Attach Resume Document (.pdf, .doc, .docx - Max 5MB)</label>
              <div class="file-upload-zone" id="file-drop-zone">
                <input type="file" id="cand-resume" accept=".pdf,.doc,.docx" aria-label="Upload resume document">
                <svg style="width: 40px; height: 40px; margin: 0 auto 0.75rem; color: var(--color-corporate-blue);" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                  <polyline points="17 8 12 3 7 8"></polyline>
                  <line x1="12" y1="3" x2="12" y2="15"></line>
                </svg>
                <div style="font-weight: 600; color: var(--color-primary-navy);">Click to Browse or Drag File Here</div>
                <div class="text-muted" style="font-size: 0.8rem; margin-top: 0.25rem;">Supported formats: PDF, DOC, DOCX up to 5MB</div>
              </div>

              <!-- File preview display -->
              <div class="file-preview" id="file-preview-zone">
                <div class="file-info">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--color-teal-accent);">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <polyline points="14 2 14 8 20 8"></polyline>
                  </svg>
                  <div>
                    <span class="file-name" id="file-name-display">resume.pdf</span>
                    <span class="file-size" id="file-size-display">1.2 MB</span>
                  </div>
                </div>
                <button type="button" class="btn-remove-file" id="remove-file-btn">Remove File</button>
              </div>
              <div id="file-upload-feedback" class="invalid-feedback" style="display: none;"></div>
            </div>

            <div class="form-group" style="margin-top: 1.5rem;">
              <label class="form-label" for="cand-notes">Additional Notes / Cover Summary</label>
              <textarea id="cand-notes" class="form-control" rows="3" placeholder="Briefly state your career aspirations or relocation constraints..."></textarea>
            </div>

            <div style="margin-top: 2rem;">
              <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">Submit Demo Candidate Registration</button>
            </div>
          </form>
        </div>
      </div>
    </section>
    """
    write_html("register-candidate.html", render_page(
        "Candidate Registration — Submit Resume (Demo Portal)",
        "Register your candidate profile and upload your resume for simulated matching against open client roles. Client-side demo validation.",
        "candidates", content,
        breadcrumbs=[("Home", "index.html"), ("Candidates", "candidates.html"), ("Candidate Registration", None)]
    ))

# ==============================================================================
# 7. CAREERS AT AGENCY — careers.html
# ==============================================================================
def make_careers():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Join Our Agency</span>
        <h1>Careers at Staffing Agency</h1>
        <p class="lead">
          Explore internal professional roles within our staffing and recruitment operations team.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="demo-callout-box text-center" style="max-width: 800px; margin: 0 auto 3rem;">
          <strong>Demonstration Roles Notice:</strong> The career opportunities listed below illustrate typical internal positions within a professional staffing agency. They are sample profiles for demonstration purposes.
        </div>

        <div class="grid-3">
          <div class="card">
            <span class="pathway-badge" style="background: #EBF2FA; color: var(--color-corporate-blue); margin-bottom: 0.75rem;">Internal Recruiter</span>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.35rem;">Technical Recruitment Consultant</h3>
            <p class="text-muted" style="font-size: 0.85rem; margin-bottom: 1rem;">Full-Time • Hyderabad (Demo)</p>
            <p style="font-size: 0.9rem; margin-bottom: 1.25rem;">Lead end-to-end IT talent acquisition mandates for enterprise client technology portfolios.</p>
            <a href="register-candidate.html" class="btn btn-outline btn-sm">Apply for Role (Demo)</a>
          </div>

          <div class="card">
            <span class="pathway-badge" style="background: #E6F6F4; color: var(--color-teal-accent); margin-bottom: 0.75rem;">Operations</span>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.35rem;">Workforce Staffing Coordinator</h3>
            <p class="text-muted" style="font-size: 0.85rem; margin-bottom: 1rem;">Full-Time • Hyderabad (Demo)</p>
            <p style="font-size: 0.9rem; margin-bottom: 1.25rem;">Manage shift rosters, attendance reconciliation, and client logistics for industrial contingent staff.</p>
            <a href="register-candidate.html" class="btn btn-outline btn-sm">Apply for Role (Demo)</a>
          </div>

          <div class="card">
            <span class="pathway-badge" style="background: #EBF2FA; color: var(--color-corporate-blue); margin-bottom: 0.75rem;">Client Partnerships</span>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.35rem;">Client Account Manager</h3>
            <p class="text-muted" style="font-size: 0.85rem; margin-bottom: 1rem;">Full-Time • Hyderabad (Demo)</p>
            <p style="font-size: 0.9rem; margin-bottom: 1.25rem;">Cultivate enduring corporate client partnerships and oversee SLA delivery for large staffing programs.</p>
            <a href="register-candidate.html" class="btn btn-outline btn-sm">Apply for Role (Demo)</a>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("careers.html", render_page(
        "Careers at the Agency — Internal Recruitment Roles",
        "Explore internal career pathways within our staffing agency operations including recruitment consultant, coordinator, and account manager roles.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("Careers at Agency", None)]
    ))

# ==============================================================================
# 8. PRIVACY POLICY — privacy-policy.html
# ==============================================================================
def make_privacy_policy():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Legal Compliance</span>
        <h1>Privacy Policy</h1>
        <p class="lead">Demonstration website privacy notice and future operational compliance framework.</p>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 860px;">
        <div class="demo-callout-box">
          <strong>DEMONSTRATION WEBSITE NOTICE:</strong> This website is a frontend generic staffing prototype. Demonstration forms do not transmit, collect, or store any personal information, resumes, or employer inquiries on any server or database.
        </div>

        <div class="card" style="padding: 2.5rem; line-height: 1.75;">
          <h2 style="font-size: 1.4rem; margin-bottom: 0.75rem;">1. Demonstration Data Handling</h2>
          <p>
            All interactive forms across this website (including the Employer Staffing Request form, Candidate Registration form, and General Contact form) are configured to execute in browser-side demo simulation only. No network requests are dispatched to external APIs, and no candidate resumes or contact credentials are stored.
          </p>

          <h2 style="font-size: 1.4rem; margin-top: 2rem; margin-bottom: 0.75rem;">2. Mandatory Requirements for Live Deployment</h2>
          <p>
            If this website architecture is later connected to live recruitment databases, Applicant Tracking Systems (ATS), or real operational servers by an authorized agency operator, the operator must establish:
          </p>
          <ul style="list-style: disc; padding-left: 1.5rem; margin-bottom: 1.5rem;">
            <li>A comprehensive data privacy policy conforming to applicable regional data protection regulations (such as GDPR, DPDP, or local labor laws).</li>
            <li>Explicit candidate consent mechanisms for resume parsing, storage, and presentation to client employers.</li>
            <li>Documented data retention and secure erasure schedules.</li>
            <li>Secure encrypted transmission protocols (HTTPS/TLS) and role-based database access controls.</li>
          </ul>

          <h2 style="font-size: 1.4rem; margin-top: 2rem; margin-bottom: 0.75rem;">3. Cookies &amp; Local Storage</h2>
          <p>
            This demonstration site does not deploy third-party advertising or tracking cookies. Any temporary session state utilized for interface rendering operates purely within your local browser session.
          </p>
        </div>
      </div>
    </section>
    """
    write_html("privacy-policy.html", render_page(
        "Privacy Policy — Demonstration Website Data Notice",
        "Privacy policy explaining local demo data handling and operational requirements before connecting to live systems.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("Privacy Policy", None)]
    ))

# ==============================================================================
# 9. TERMS & CONDITIONS — terms-and-conditions.html
# ==============================================================================
def make_terms_and_conditions():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Terms of Use</span>
        <h1>Terms &amp; Conditions</h1>
        <p class="lead">Demonstration prototype terms of use and website guidelines.</p>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 860px;">
        <div class="card" style="padding: 2.5rem; line-height: 1.75;">
          <h2 style="font-size: 1.4rem; margin-bottom: 0.75rem;">1. Nature of the Website</h2>
          <p>
            This website is provided as an illustrative, generic demonstration of a corporate staffing and workforce solutions portal. It does not represent an actual operating business entity, licensed recruitment agency, or employer-of-record service.
          </p>

          <h2 style="font-size: 1.4rem; margin-top: 2rem; margin-bottom: 0.75rem;">2. No Guarantee of Placement or Employment</h2>
          <p>
            Sample job listings, candidate profiles, and case studies are published strictly for user interface demonstration. The website makes no representation, warranty, or guarantee regarding live vacancies, candidate placements, employment offers, or operational outcomes.
          </p>

          <h2 style="font-size: 1.4rem; margin-top: 2rem; margin-bottom: 0.75rem;">3. Intellectual Property &amp; Technology Stack</h2>
          <p>
            This static website is authored using standard semantic HTML5, CSS3, and Vanilla JavaScript. It contains zero external framework dependencies and operates independently without server-side processing.
          </p>
        </div>
      </div>
    </section>
    """
    write_html("terms-and-conditions.html", render_page(
        "Terms & Conditions — Demonstration Terms of Use",
        "Terms and conditions governing the use of this generic staffing agency demonstration website.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("Terms & Conditions", None)]
    ))

# ==============================================================================
# 10. COOKIE POLICY — cookie-policy.html
# ==============================================================================
def make_cookie_policy():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Cookie Information</span>
        <h1>Cookie Policy</h1>
        <p class="lead">Information on cookies and client-side storage mechanisms utilized on this demonstration site.</p>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 860px;">
        <div class="card" style="padding: 2.5rem; line-height: 1.75;">
          <h2 style="font-size: 1.4rem; margin-bottom: 0.75rem;">1. What Are Cookies?</h2>
          <p>
            Cookies are small text files placed on your computer or mobile device when you browse websites. They are commonly used to remember preferences, enhance navigation, and analyze web traffic.
          </p>

          <h2 style="font-size: 1.4rem; margin-top: 2rem; margin-bottom: 0.75rem;">2. Demonstration Website Usage</h2>
          <p>
            This static demonstration website does not employ commercial advertising cookies, tracking pixels, or third-party profiling mechanisms. Any temporary state utilized by client-side JavaScript operates within your local session to facilitate navigation and demonstration form interactions.
          </p>
        </div>
      </div>
    </section>
    """
    write_html("cookie-policy.html", render_page(
        "Cookie Policy — Client-Side Storage Information",
        "Overview of cookie usage and local session handling on this generic staffing agency demonstration website.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("Cookie Policy", None)]
    ))

print("Portal and legal generator functions defined.")
