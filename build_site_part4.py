"""
STAFFING AGENCY — Core Pages Part 4
Generates talent-acquisition.html, recruitment-consulting.html, team.html, leadership.html,
case-studies.html, case-study-details.html, insights.html, article-details.html, faq.html, contact.html.
"""

from generate_helpers import render_page, render_placeholder, LOGO_SVG
from build_site_part1 import register_image, write_html

# ==============================================================================
# 7. TALENT ACQUISITION — talent-acquisition.html
# ==============================================================================
def make_talent_acquisition():
    register_image(
        "staffing-talent-acquisition.jpg", "talent-acquisition.html", "Acquisition Strategies",
        "Talent acquisition specialist conducting structured candidate evaluation interview",
        "16:9", "1200x800", "Landscape",
        "Professional commercial photograph of a recruitment specialist conducting a video interview on a sleek laptop with notepad and stylus in an executive office. Bright natural light, focused expression, modern minimal decor, navy corporate background palette.",
        "Medium shot, subject centered slightly right with laptop on left", "Eye-level medium shot", "Clean daylight with gentle rim light",
        "Contemporary corporate glass meeting pod", "Modern executive commercial style",
        "Navy, white, soft gold accent", "Recruiter focused on screen engagement"
    )

    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Strategic Sourcing</span>
        <h1>Talent Acquisition</h1>
        <p class="lead">
          Strategic talent acquisition approaches engineered to discover, engage, and evaluate specialized candidates in competitive employment markets.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3rem;">
          <div>
            <span class="section-subtitle">Proactive Pipeline</span>
            <h2>Beyond Standard Job Postings</h2>
            <p>
              Traditional reactive recruitment relies on active job seekers responding to public advertisements. Modern talent acquisition requires proactive engagement with passive professionals who are not actively reading job boards.
            </p>
            <p>
              By combining market intelligence, targeted candidate outreach, and structured assessment criteria, our talent acquisition methodology helps organizations build sustainable candidate pools for critical business functions.
            </p>
            <div class="demo-callout-box">
              <strong>Illustrative Information:</strong> Sourcing timelines and candidate availability depend on market factors, role specifications, and employer brand resonance.
            </div>
          </div>
          <div>
            {render_placeholder("staffing-talent-acquisition.jpg", "ratio-16-9", "staffing-talent-acquisition.jpg", 1200, 800, "Talent acquisition specialist conducting candidate evaluation")}
          </div>
        </div>
      </div>
    </section>

    <!-- 4 Pillars of Talent Acquisition -->
    <section class="section section-bg-light">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle teal">Operational Framework</span>
          <h2>Four Pillars of Talent Acquisition</h2>
          <p class="lead">Structured stages for developing dependable talent pipelines.</p>
        </div>

        <div class="grid-4">
          <div class="card">
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Market Mapping</h3>
            <p class="text-muted" style="font-size: 0.875rem;">Analyzing competitive talent landscapes, prevailing compensation bands, and skill availability.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Direct Outreach</h3>
            <p class="text-muted" style="font-size: 0.875rem;">Engaging passive industry professionals with clear, customized value propositions.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Competency Vetting</h3>
            <p class="text-muted" style="font-size: 0.875rem;">Conducting structured skill and cultural compatibility evaluations prior to client presentation.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.15rem; margin-bottom: 0.5rem;">Candidate Stewardship</h3>
            <p class="text-muted" style="font-size: 0.875rem;">Maintaining transparent, respectful communication through all stages of hiring.</p>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("talent-acquisition.html", render_page(
        "Talent Acquisition — Strategic Sourcing & Candidate Engagement",
        "Learn about proactive talent acquisition strategies, passive candidate engagement, and competency evaluation workflows.",
        "services", content,
        breadcrumbs=[("Home", "index.html"), ("Staffing Services", "services.html"), ("Talent Acquisition", None)]
    ))

# ==============================================================================
# 8. RECRUITMENT CONSULTING — recruitment-consulting.html
# ==============================================================================
def make_recruitment_consulting():
    register_image(
        "staffing-recruitment-consulting.jpg", "recruitment-consulting.html", "Advisory Services",
        "Workforce consultant advising business leaders on organizational talent structure",
        "16:9", "1200x800", "Landscape",
        "Commercial photograph of a corporate recruitment advisor in discussion with senior executives in a glass boardroom overlooking an urban cityscape. Professional attire, digital tablet presenting workforce trend graphics, natural diffused daylight, sophisticated executive ambiance.",
        "Wide shot, advisor gesturing toward presentation tablet with executives listening attentively", "Eye-level medium-wide angle", "Soft balanced daylight",
        "Modern corporate boardroom with city panorama", "Executive corporate consulting photography",
        "Navy, steel, white, charcoal", "Advisor seated midground with executive peers"
    )

    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Workforce Advisory</span>
        <h1>Recruitment Consulting</h1>
        <p class="lead">
          Strategic workforce advisory services helping organizations optimize hiring structures, benchmark compensation, and refine talent acquisition workflows.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem;">
          <div>
            <span class="section-subtitle">Advisory Scope</span>
            <h2>Optimizing Recruitment Architecture</h2>
            <p>
              Recruitment consulting goes beyond filling immediate openings. We partner with leadership teams to diagnose recruitment bottlenecks, assess employer value propositions, evaluate candidate experience touchpoints, and benchmark industry salary data.
            </p>
            <p>
              By transforming fragmented hiring practices into structured, data-informed workflows, organizations achieve greater hiring consistency and improved retention.
            </p>
            <div class="demo-callout-box">
              <strong>Advisory Notice:</strong> Advisory recommendations are illustrative insights based on general industry benchmarks. Organizations should conduct internal evaluations tailored to their operational parameters.
            </div>
          </div>
          <div>
            {render_placeholder("staffing-recruitment-consulting.jpg", "ratio-16-9", "staffing-recruitment-consulting.jpg", 1200, 800, "Recruitment consultant reviewing workforce architecture with corporate executives")}
          </div>
        </div>
      </div>
    </section>
    """
    write_html("recruitment-consulting.html", render_page(
        "Recruitment Consulting — Workforce Architecture Advisory",
        "Strategic recruitment advisory services supporting hiring process optimization, market benchmarking, and talent workflow design.",
        "services", content,
        breadcrumbs=[("Home", "index.html"), ("Staffing Services", "services.html"), ("Recruitment Consulting", None)]
    ))

# ==============================================================================
# 9. TEAM — team.html (Generic placeholders, no invented names)
# ==============================================================================
def make_team():
    register_image(
        "staffing-office-team.jpg", "team.html", "Team Collaboration",
        "Recruitment operations team collaborating across open workspace desks",
        "16:9", "1200x800", "Landscape",
        "Authentic corporate documentary photograph of four staffing team members working collaboratively in a modern, sunlit open-plan office. Laptops open, papers neatly arranged, cheerful yet professional teamwork, soft architectural depth of field.",
        "Horizontal group composition across wooden shared desk", "Eye-level medium shot", "Bright natural light from large adjacent windows",
        "Modern corporate workspace with green plants and glass walls", "Editorial corporate documentary",
        "Navy, white, subtle timber, green foliage", "Team members arranged naturally across midground"
    )

    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Our People</span>
        <h1>Our Recruitment Team</h1>
        <p class="lead">
          A dedicated team of recruitment consultants, talent acquisition specialists, and staffing coordinators supporting seamless workforce execution.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="demo-callout-box text-center" style="max-width: 800px; margin: 0 auto 3rem;">
          <strong>Demonstration Profiles Notice:</strong> To adhere to generic demonstrator website guidelines, all staff profiles below display illustrative functional roles rather than actual individuals, qualifications, or personal names.
        </div>

        <div style="margin-bottom: 3.5rem;">
          {render_placeholder("staffing-office-team.jpg", "ratio-21-9", "staffing-office-team.jpg", 1200, 520, "Staffing operations team collaborating in open modern office")}
        </div>

        <div class="grid-3">
          <div class="card text-center">
            <div class="card-icon" style="margin: 0 auto 1.25rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.25rem;">Recruitment Consultant</h3>
            <span class="text-teal" style="font-weight: 600; font-size: 0.85rem; display: block; margin-bottom: 0.75rem;">Demo Profile — Technical Staffing</span>
            <p class="text-muted" style="font-size: 0.9rem;">Specializes in client requirement mapping, technical competency vetting, and candidate coordination across software engineering roles.</p>
          </div>

          <div class="card text-center">
            <div class="card-icon teal" style="margin: 0 auto 1.25rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.25rem;">Talent Acquisition Specialist</h3>
            <span class="text-teal" style="font-weight: 600; font-size: 0.85rem; display: block; margin-bottom: 0.75rem;">Demo Profile — Sourcing &amp; Research</span>
            <p class="text-muted" style="font-size: 0.9rem;">Focuses on passive candidate mapping, competitive talent benchmarking, and outreach campaigns for specialized functions.</p>
          </div>

          <div class="card text-center">
            <div class="card-icon" style="margin: 0 auto 1.25rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.25rem;">Staffing Coordinator</h3>
            <span class="text-teal" style="font-weight: 600; font-size: 0.85rem; display: block; margin-bottom: 0.75rem;">Demo Profile — Flexible Workforce</span>
            <p class="text-muted" style="font-size: 0.9rem;">Manages temporary worker shift scheduling, attendance logging, and assignment logistics for industrial and retail clients.</p>
          </div>

          <div class="card text-center">
            <div class="card-icon teal" style="margin: 0 auto 1.25rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.25rem;">Candidate Relationship Executive</h3>
            <span class="text-teal" style="font-weight: 600; font-size: 0.85rem; display: block; margin-bottom: 0.75rem;">Demo Profile — Job Seeker Support</span>
            <p class="text-muted" style="font-size: 0.9rem;">Guides candidates through resume registration, preliminary interview preparation, and post-interview debriefs.</p>
          </div>

          <div class="card text-center">
            <div class="card-icon" style="margin: 0 auto 1.25rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.25rem;">HR Operations Specialist</h3>
            <span class="text-teal" style="font-weight: 600; font-size: 0.85rem; display: block; margin-bottom: 0.75rem;">Demo Profile — Administration</span>
            <p class="text-muted" style="font-size: 0.9rem;">Administers candidate verification records, joining checklist compliance, timesheet coordination, and client reporting.</p>
          </div>

          <div class="card text-center">
            <div class="card-icon teal" style="margin: 0 auto 1.25rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.25rem;">Account Executive</h3>
            <span class="text-teal" style="font-weight: 600; font-size: 0.85rem; display: block; margin-bottom: 0.75rem;">Demo Profile — Client Relations</span>
            <p class="text-muted" style="font-size: 0.9rem;">Serves as dedicated liaison for corporate client HR managers, ensuring SLA adherence and timely candidate pipeline delivery.</p>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("team.html", render_page(
        "Our Recruitment Team — Professional Staffing Roles",
        "Overview of recruitment team functions including recruitment consultants, talent acquisition specialists, and staffing coordinators.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("About Us", "about.html"), ("Recruitment Team", None)]
    ))

# ==============================================================================
# 10. LEADERSHIP — leadership.html
# ==============================================================================
def make_leadership():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Governance</span>
        <h1>Leadership Overview</h1>
        <p class="lead">
          Illustrative organizational governance structure steering workforce strategy, quality compliance, and client service standards.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="demo-callout-box text-center" style="max-width: 800px; margin: 0 auto 3rem;">
          <strong>Governance Notice:</strong> Leadership entries represent functional agency leadership tiers. In compliance with demo standards, no fictional names or fabricated executive bios are displayed.
        </div>

        <div class="grid-3">
          <div class="card">
            <span class="pathway-badge" style="background: #EBF2FA; color: var(--color-corporate-blue); margin-bottom: 0.75rem;">Executive Function</span>
            <h3 style="font-size: 1.3rem; margin-bottom: 0.25rem;">Head of Client Solutions</h3>
            <p class="text-teal" style="font-weight: 600; font-size: 0.85rem; margin-bottom: 1rem;">Demo Role — Enterprise Workforce Programs</p>
            <p class="text-muted" style="font-size: 0.9rem;">Oversees client partnership frameworks, workforce model design, and multi-location staffing deployment strategies.</p>
          </div>

          <div class="card">
            <span class="pathway-badge" style="background: #E6F6F4; color: var(--color-teal-accent); margin-bottom: 0.75rem;">Operations Function</span>
            <h3 style="font-size: 1.3rem; margin-bottom: 0.25rem;">Director of Talent Operations</h3>
            <p class="text-teal" style="font-weight: 600; font-size: 0.85rem; margin-bottom: 1rem;">Demo Role — Sourcing &amp; Screening Infrastructure</p>
            <p class="text-muted" style="font-size: 0.9rem;">Leads recruiter enablement, applicant screening methodologies, and adherence to sourcing best practices.</p>
          </div>

          <div class="card">
            <span class="pathway-badge" style="background: #EBF2FA; color: var(--color-corporate-blue); margin-bottom: 0.75rem;">Quality &amp; Standards</span>
            <h3 style="font-size: 1.3rem; margin-bottom: 0.25rem;">Compliance &amp; Quality Lead</h3>
            <p class="text-teal" style="font-weight: 600; font-size: 0.85rem; margin-bottom: 1rem;">Demo Role — Verification &amp; Service Standards</p>
            <p class="text-muted" style="font-size: 0.9rem;">Maintains screening consistency, documentation verification policies, and ethical recruitment adherence across all sectors.</p>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("leadership.html", render_page(
        "Leadership Overview — Recruitment Governance Structure",
        "Overview of functional leadership tiers responsible for workforce strategy, quality compliance, and recruitment operations.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("About Us", "about.html"), ("Leadership Overview", None)]
    ))

# ==============================================================================
# 11. CASE STUDIES — case-studies.html
# ==============================================================================
def make_case_studies():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Real-World Scenarios</span>
        <h1>Illustrative Staffing Case Studies</h1>
        <p class="lead">
          Hypothetical workforce scenarios illustrating how structured staffing and recruitment workflows resolve complex operational hiring bottlenecks.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="demo-callout-box text-center" style="max-width: 840px; margin: 0 auto 3rem;">
          <strong>MANDATORY DEMO DISCLAIMER:</strong> Every case study below is an <strong>ILLUSTRATIVE DEMO SCENARIO — NOT A REAL CLIENT PROJECT</strong>. No fictional client logos, real client identities, fabricated placement numbers, or commercial endorsements are used.
        </div>

        <div style="display: flex; flex-direction: column; gap: 2.5rem;">
          <!-- Case Study 1 -->
          <div class="card" style="border-top: 4px solid var(--color-corporate-blue);">
            <div class="demo-disclaimer-pill">ILLUSTRATIVE DEMO SCENARIO — NOT A REAL CLIENT PROJECT</div>
            <h2 style="font-size: 1.6rem; margin: 0.5rem 0 1rem;">Manufacturing Workforce Planning</h2>
            <div class="grid-2" style="gap: 2rem;">
              <div>
                <h4 style="color: var(--color-corporate-blue);">Business Context &amp; Challenge</h4>
                <p class="text-muted" style="font-size: 0.95rem;">
                  A mid-scale consumer goods manufacturing plant anticipated a 40% production surge over a four-month holiday cycle. Internal HR lacked the bandwidth to screen and onboard 80 shift operators without compromising core plant maintenance operations.
                </p>
                <h4 style="color: var(--color-corporate-blue);">Recruitment Approach</h4>
                <p class="text-muted" style="font-size: 0.95rem;">
                  The agency developed a tiered temporary staffing pipeline. Initial skills verification was conducted at a regional screening center, followed by basic safety orientation before candidate presentation to the plant management team.
                </p>
              </div>
              <div>
                <h4 style="color: var(--color-teal-accent);">Illustrative Lessons Learned</h4>
                <ul style="list-style: disc; padding-left: 1.25rem; font-size: 0.9rem; color: var(--color-body-text);">
                  <li>Advance shift modeling prevents mid-cycle operator attrition.</li>
                  <li>Standardized safety orientation checklists speed up line integration.</li>
                  <li>Clear assignment durations manage candidate expectations effectively.</li>
                </ul>
                <div style="margin-top: 1.5rem;">
                  <a href="case-study-details.html" class="btn btn-outline btn-sm">Read Full Scenario Analysis &rarr;</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Case Study 2 -->
          <div class="card" style="border-top: 4px solid var(--color-teal-accent);">
            <div class="demo-disclaimer-pill">ILLUSTRATIVE DEMO SCENARIO — NOT A REAL CLIENT PROJECT</div>
            <h2 style="font-size: 1.6rem; margin: 0.5rem 0 1rem;">IT Talent Acquisition Workflow</h2>
            <div class="grid-2" style="gap: 2rem;">
              <div>
                <h4 style="color: var(--color-corporate-blue);">Business Context &amp; Challenge</h4>
                <p class="text-muted" style="font-size: 0.95rem;">
                  An enterprise SaaS software provider needed 12 senior full-stack developers proficient in microservices and cloud infrastructure within an aggressive 60-day migration timeframe amidst fierce market competition.
                </p>
                <h4 style="color: var(--color-corporate-blue);">Recruitment Approach</h4>
                <p class="text-muted" style="font-size: 0.95rem;">
                  The recruitment team utilized passive talent mapping, targeting specialized engineering communities with detailed technical briefs. Technical screening panels conducted preliminary code reviews prior to client interviews.
                </p>
              </div>
              <div>
                <h4 style="color: var(--color-teal-accent);">Illustrative Lessons Learned</h4>
                <ul style="list-style: disc; padding-left: 1.25rem; font-size: 0.9rem; color: var(--color-body-text);">
                  <li>Senior engineers respond favorably to transparent technical challenges over generic job posts.</li>
                  <li>Consolidating interview rounds from four to two significantly improves offer acceptance rates.</li>
                  <li>Transparent remote/hybrid policy communication avoids late-stage dropouts.</li>
                </ul>
                <div style="margin-top: 1.5rem;">
                  <a href="case-study-details.html" class="btn btn-outline btn-sm">Read Full Scenario Analysis &rarr;</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Case Study 3 -->
          <div class="card" style="border-top: 4px solid var(--color-secondary-navy);">
            <div class="demo-disclaimer-pill">ILLUSTRATIVE DEMO SCENARIO — NOT A REAL CLIENT PROJECT</div>
            <h2 style="font-size: 1.6rem; margin: 0.5rem 0 1rem;">High-Volume Retail Recruitment</h2>
            <div class="grid-2" style="gap: 2rem;">
              <div>
                <h4 style="color: var(--color-corporate-blue);">Business Context &amp; Challenge</h4>
                <p class="text-muted" style="font-size: 0.95rem;">
                  A regional retail chain opening six new department store locations required 150 customer-facing store associates and cashier staff across a 30-day staggered opening schedule.
                </p>
                <h4 style="color: var(--color-corporate-blue);">Recruitment Approach</h4>
                <p class="text-muted" style="font-size: 0.95rem;">
                  A multi-day walk-in drive framework was organized with standardized customer service aptitude assessments, background verification stations, and immediate conditional offer issuing.
                </p>
              </div>
              <div>
                <h4 style="color: var(--color-teal-accent);">Illustrative Lessons Learned</h4>
                <ul style="list-style: disc; padding-left: 1.25rem; font-size: 0.9rem; color: var(--color-body-text);">
                  <li>Batch assessment days dramatically reduce per-hire administrative overhead.</li>
                  <li>Location-specific transport feasibility checks reduce initial-week dropouts.</li>
                  <li>Digital onboarding checklists accelerate customer service training completion.</li>
                </ul>
                <div style="margin-top: 1.5rem;">
                  <a href="case-study-details.html" class="btn btn-outline btn-sm">Read Full Scenario Analysis &rarr;</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("case-studies.html", render_page(
        "Illustrative Staffing Case Studies — Scenario Analysis",
        "Explore 3 illustrative recruitment case scenarios covering manufacturing workforce ramp-up, IT talent acquisition, and high-volume retail hiring.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("Case Studies", None)]
    ))

# ==============================================================================
# 12. CASE STUDY DETAILS — case-study-details.html
# ==============================================================================
def make_case_study_details():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">In-Depth Scenario</span>
        <h1>Case Study: Manufacturing Workforce Planning</h1>
        <p class="lead">
          An illustrative breakdown of workforce capacity planning, temporary shift deployment, and coordination logistics.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 900px;">
        <div class="demo-callout-box">
          <strong>Notice:</strong> ILLUSTRATIVE DEMO SCENARIO — NOT A REAL CLIENT PROJECT. All organizations, operational parameters, and metrics are simulated for demonstration purposes.
        </div>

        <div class="card" style="margin-bottom: 2.5rem;">
          <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">1. Operational Context</h2>
          <p>
            During peak manufacturing seasons, production facilities often face sudden demand increases driven by consumer purchasing cycles. Maintaining permanent headcount year-round to satisfy brief production peaks is cost-prohibitive, making a temporary contingent workforce model the preferred strategic alternative.
          </p>

          <h2 style="font-size: 1.5rem; margin-top: 1.5rem; margin-bottom: 1rem;">2. Identification of Bottlenecks</h2>
          <ul style="list-style: disc; padding-left: 1.5rem; margin-bottom: 1.5rem; color: var(--color-body-text);">
            <li>High volume of applicants requiring rapid verification of physical suitability and mechanical aptitude.</li>
            <li>Plant managers overwhelmed by interview scheduling during intense operational schedules.</li>
            <li>Risk of line downtime if shift operators failed to report on scheduled shifts.</li>
          </ul>

          <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">3. Recruitment Methodology Deployed</h2>
          <p>
            The staffing agency structured a dedicated regional mobilization center. Candidates were pre-screened using standardized testing for spatial reasoning, tool identification, and safety protocol comprehension. Successful candidates were grouped into pre-scheduled shifts with stand-by reserves to accommodate unplanned absences.
          </p>

          <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">4. Key Strategic Takeaways</h2>
          <p>
            This scenario demonstrates that high-volume temporary staffing relies heavily on pre-shift orientation and transparent communication regarding assignment duration, working conditions, and compensation terms.
          </p>

          <div style="border-top: 1px solid var(--color-border); padding-top: 1.5rem; margin-top: 2rem;">
            <a href="case-studies.html" class="btn btn-outline">&larr; Return to All Case Studies</a>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("case-study-details.html", render_page(
        "Case Study Details — Manufacturing Workforce Planning",
        "In-depth illustrative scenario analysis examining manufacturing workforce planning and temporary shift deployment.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("Case Studies", "case-studies.html"), ("Manufacturing Scenario", None)]
    ))

# ==============================================================================
# 13. INSIGHTS — insights.html
# ==============================================================================
def make_insights():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Knowledge Base</span>
        <h1>Recruitment Insights &amp; Resources</h1>
        <p class="lead">
          Educational articles, industry guides, and hiring perspectives for corporate talent leaders and ambitious job seekers.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="demo-callout-box text-center" style="max-width: 800px; margin: 0 auto 3rem;">
          <strong>Demonstration Content Notice:</strong> All articles below represent sample educational content. They do not claim proprietary research, academic authorship, or verified statistical claims.
        </div>

        <div class="grid-3">
          <div class="card">
            <span class="pathway-badge" style="background: #EBF2FA; color: var(--color-corporate-blue); margin-bottom: 0.75rem;">Staffing Fundamentals</span>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="article-details.html">What Is Staffing? A Comprehensive Guide</a></h3>
            <p class="text-muted" style="font-size: 0.875rem; margin-bottom: 1.25rem;">Explore how modern staffing agencies bridge talent gaps and facilitate workforce mobility for enterprises.</p>
            <a href="article-details.html" class="card-link">Read Guide &rarr;</a>
          </div>

          <div class="card">
            <span class="pathway-badge" style="background: #E6F6F4; color: var(--color-teal-accent); margin-bottom: 0.75rem;">Workforce Models</span>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="article-details.html">Permanent vs. Temporary Staffing Explained</a></h3>
            <p class="text-muted" style="font-size: 0.875rem; margin-bottom: 1.25rem;">Compare cost considerations, retention factors, and flexibility across permanent and contingent hiring.</p>
            <a href="article-details.html" class="card-link">Read Guide &rarr;</a>
          </div>

          <div class="card">
            <span class="pathway-badge" style="background: #EBF2FA; color: var(--color-corporate-blue); margin-bottom: 0.75rem;">Contract Work</span>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="article-details.html">Understanding Contract Staffing Engagements</a></h3>
            <p class="text-muted" style="font-size: 0.875rem; margin-bottom: 1.25rem;">How time-bound contract staffing empowers companies to execute specialized technical and strategic deliverables.</p>
            <a href="article-details.html" class="card-link">Read Guide &rarr;</a>
          </div>

          <div class="card">
            <span class="pathway-badge" style="background: #E6F6F4; color: var(--color-teal-accent); margin-bottom: 0.75rem;">Job Seekers</span>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="article-details.html">Preparing for Recruitment Agency Interviews</a></h3>
            <p class="text-muted" style="font-size: 0.875rem; margin-bottom: 1.25rem;">Practical guidance for candidates on effectively articulating practical skills and experience to agency recruiters.</p>
            <a href="article-details.html" class="card-link">Read Guide &rarr;</a>
          </div>

          <div class="card">
            <span class="pathway-badge" style="background: #EBF2FA; color: var(--color-corporate-blue); margin-bottom: 0.75rem;">High Volume</span>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="article-details.html">How Bulk Recruitment Operates at Scale</a></h3>
            <p class="text-muted" style="font-size: 0.875rem; margin-bottom: 1.25rem;">An examination of logistics, screening workflows, and verification systems for large cohort hiring.</p>
            <a href="article-details.html" class="card-link">Read Guide &rarr;</a>
          </div>

          <div class="card">
            <span class="pathway-badge" style="background: #E6F6F4; color: var(--color-teal-accent); margin-bottom: 0.75rem;">Technology</span>
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;"><a href="article-details.html">Understanding IT Staffing Trends &amp; Roles</a></h3>
            <p class="text-muted" style="font-size: 0.875rem; margin-bottom: 1.25rem;">Key insights into developer sourcing, technical vetting, and cloud engineering talent market dynamics.</p>
            <a href="article-details.html" class="card-link">Read Guide &rarr;</a>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("insights.html", render_page(
        "Recruitment Insights — Staffing Articles & Resources",
        "Explore educational resources and insights on permanent vs temporary staffing, contract engagements, interview tips, and bulk hiring.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("Recruitment Insights", None)]
    ))

# ==============================================================================
# 14. ARTICLE DETAILS — article-details.html
# ==============================================================================
def make_article_details():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Educational Guide</span>
        <h1>What Is Staffing? A Comprehensive Guide</h1>
        <p class="lead">Understanding the mechanics, service models, and strategic advantages of workforce solutions.</p>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 860px;">
        <div class="demo-callout-box">
          <strong>Notice:</strong> This article is an illustrative educational sample provided for website demonstration purposes.
        </div>

        <div class="card" style="padding: 2.5rem; line-height: 1.75;">
          <h2 style="font-size: 1.6rem; margin-bottom: 1rem;">Introduction to Modern Workforce Staffing</h2>
          <p>
            At its core, staffing refers to the systematic process of acquiring, deploying, and managing human resources within an organization. While internal human resource teams manage existing employee relations, benefits, and development, external staffing agencies specialize in the sourcing, initial screening, and supply of talent.
          </p>

          <h3 style="font-size: 1.3rem; margin-top: 2rem; margin-bottom: 0.75rem;">Core Staffing Models</h3>
          <p>
            Enterprises leverage distinct staffing formats depending on their business trajectory:
          </p>
          <ul style="list-style: disc; padding-left: 1.5rem; margin-bottom: 1.5rem;">
            <li><strong>Permanent Staffing:</strong> Filling core long-term roles intended for ongoing career progression within the client company.</li>
            <li><strong>Temporary Staffing:</strong> Contracting talent for specified weeks or months to manage operational volume fluctuations.</li>
            <li><strong>Contract Staffing:</strong> Engaging specialized technical contributors for fixed project milestones.</li>
            <li><strong>Temp-to-Hire:</strong> An evaluation model permitting both employer and worker to assess fit prior to permanent employment.</li>
          </ul>

          <h3 style="font-size: 1.3rem; margin-top: 2rem; margin-bottom: 0.75rem;">Strategic Value for Businesses</h3>
          <p>
            Engaging an established staffing partner grants businesses immediate access to broad talent databases, specialized sourcing expertise, and pre-screened talent pools, dramatically reducing the time-to-hire and freeing internal teams to focus on core operations.
          </p>

          <div style="border-top: 1px solid var(--color-border); padding-top: 1.5rem; margin-top: 2.5rem;">
            <a href="insights.html" class="btn btn-outline">&larr; Back to Insights Hub</a>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("article-details.html", render_page(
        "What Is Staffing? Comprehensive Guide | Insights",
        "Educational guide exploring modern staffing mechanics, workforce models, and strategic value for corporate employers.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("Insights", "insights.html"), ("Article Details", None)]
    ))

# ==============================================================================
# 15. FAQ — faq.html (Both Employer & Candidate FAQs with Accordion)
# ==============================================================================
def make_faq():
    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Answers &amp; Support</span>
        <h1>Frequently Asked Questions</h1>
        <p class="lead">
          Find answers to common questions about our staffing services, recruitment workflows, and candidate registration.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <!-- Dual Audience Jump Navigation -->
        <div style="display: flex; gap: 1rem; justify-content: center; margin-bottom: 3rem;">
          <a href="#employer-faqs" class="btn btn-primary">Employer FAQs</a>
          <a href="#candidate-faqs" class="btn btn-teal">Candidate FAQs</a>
        </div>

        <!-- Section 1: Employer FAQs -->
        <div id="employer-faqs" style="margin-bottom: 4rem;">
          <div class="section-header">
            <span class="section-subtitle">For Hiring Managers</span>
            <h2>Employer Frequently Asked Questions</h2>
            <p class="text-muted">Common inquiries from HR managers, department heads, and business owners.</p>
          </div>

          <div class="accordion-group">
            <div class="accordion-item active">
              <button class="accordion-header" type="button" aria-expanded="true">
                <span>What is a staffing agency?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                A staffing agency acts as a professional intermediary between employers seeking qualified workers and job seekers seeking employment. Staffing agencies maintain active talent pipelines, perform preliminary candidate screenings, and manage interview logistics to streamline hiring.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>What staffing services are available?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                We support 17 distinct staffing services organized across Permanent Recruitment (Direct Hire, Executive Search, White-Collar), Flexible Staffing (Temporary, Contract, Temp-to-Hire, Project-Based), High-Volume (Bulk Hiring, Campus Recruitment), Specialized Verticals (IT, Healthcare, Industrial, Blue-Collar, Skilled, General Workforce), and Operations (RPO, Payroll Administration).
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>What is the difference between permanent and temporary staffing?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                Permanent staffing focuses on sourcing full-time direct employees who join your organization's regular payroll for long-term careers. Temporary staffing provides contingent workers engaged for specific days, weeks, or months to cover seasonal peaks, leaves of absence, or short-term operational workloads.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>What is contract staffing?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                Contract staffing involves engaging specialized professionals for a defined fixed duration or specific project deliverables. This model is commonly used in IT, engineering, and corporate restructuring projects where niche expertise is required without long-term organizational overhead.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>What is a temp-to-hire arrangement?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                Temp-to-hire allows an employer to observe a worker's technical capability, attendance, and cultural compatibility on the job during an agreed temporary evaluation period before determining whether to extend a permanent employment offer. Conversion to permanent employment remains optional and subject to performance.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>How does bulk hiring work?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                Bulk hiring utilizes high-throughput recruitment funnels, structured assessment days, and parallel verification stations to recruit tens or hundreds of candidates concurrently. It is widely deployed for retail expansions, new factory plant rollouts, and seasonal logistics surges.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>What information is required to request staff?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                To request staff, an employer provides company details, job title or role description, required headcount, desired engagement type (permanent, contract, temporary), work location, target start date, and mandatory qualifications via our Request Staff form.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>How are candidates screened?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                Candidates undergo resume verification, structured interviews, previous employment cross-checks, and role-specific technical or trade aptitude assessments. Regulated positions (such as healthcare) require additional verification of valid professional registrations and jurisdiction authorizations.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>Can businesses request specialized talent?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                Yes. Our specialized staffing practices cover technical verticals including software engineers, cloud architects, credentialed clinical staff, precision machinists, financial controllers, and executive leadership.
              </div>
            </div>
          </div>
        </div>

        <!-- Section 2: Candidate FAQs -->
        <div id="candidate-faqs">
          <div class="section-header">
            <span class="section-subtitle teal">For Job Seekers</span>
            <h2>Candidate Frequently Asked Questions</h2>
            <p class="text-muted">Answers for fresh graduates, experienced candidates, and contract workers.</p>
          </div>

          <div class="accordion-group">
            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>How can I search for jobs?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                You can browse our searchable job board on the Job Search page, where you can filter illustrative vacancies by keyword, industry sector, department, experience level, and employment type.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>How can I register my resume?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                Visit our Candidate Registration page to fill in your contact information, preferred job roles, experience level, and upload your resume document (PDF, DOC, or DOCX format under 5MB). In this demonstration site, registration functions in simulated mode without saving data.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>Can freshers or recent graduates apply?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                Yes. We support entry-level candidates and campus graduates across varied domains, including customer support, junior software engineering, operations assistance, and sales coordination.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>What documents might be required for employment?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                Typical employer verification documents include updated resumes, government identity cards, educational certificates, previous employment release or experience letters, and relevant trade licenses or clinical credentials where mandated by law.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>How does the recruitment process work for candidates?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                After profile submission, our recruiters screen credentials against open client requisitions. If shortlisted, you participate in an agency screening interview, followed by coordinated client interviews, feedback debriefs, and onboarding guidance upon selection.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" type="button" aria-expanded="false">
                <span>Are all displayed jobs live vacancies?</span>
                <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="accordion-body">
                No. Because this website is an illustrative demonstration platform, all job listings are sample profiles created for evaluation and interface demonstration. None represent live open vacancies.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("faq.html", render_page(
        "Frequently Asked Questions — Employer & Candidate FAQs",
        "Comprehensive answers to common questions for both employers requesting staffing solutions and candidates searching for career opportunities.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("FAQ", None)]
    ))

# ==============================================================================
# 16. CONTACT US — contact.html
# ==============================================================================
def make_contact():
    register_image(
        "staffing-contact-advisory.jpg", "contact.html", "Contact Office",
        "Reception and consultation desk in modern recruitment agency office",
        "16:9", "1200x800", "Landscape",
        "Clean architectural commercial photograph of a sleek corporate staffing agency reception and inquiry lounge. Minimalist front desk with subtle agency emblem, comfortable seating area with navy and teal accent pillows, polished concrete floor, soft architectural lighting.",
        "Wide symmetrical composition of reception area", "Eye-level wide shot", "Warm ambient architectural interior lighting",
        "Corporate reception foyer and inquiry lounge", "Architectural interior photography",
        "Navy, teal, charcoal, warm wood", "Reception desk in midground with spacious welcoming foreground"
    )

    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">Get In Touch</span>
        <h1>Contact Us</h1>
        <p class="lead">
          Connect with our staffing team for employer consultations, candidate assistance, or general workforce inquiries.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="gap: 3.5rem;">
          <!-- Contact Info & Details -->
          <div>
            <span class="section-subtitle">Reach Our Office</span>
            <h2>We Are Ready to Assist</h2>
            <p>
              Whether you need to discuss a confidential leadership search, request a flexible workforce proposal, or understand candidate registration, our consultants provide professional guidance.
            </p>

            <div class="demo-callout-box">
              <strong>Demonstration Contact Notice:</strong> The contact details displayed below are generic dummy credentials provided for interface demonstration. No real emails or calls are received.
            </div>

            <div style="display: flex; flex-direction: column; gap: 1.25rem; margin: 2rem 0;">
              <div class="card" style="padding: 1.25rem; display: flex; align-items: flex-start; gap: 1rem;">
                <div class="card-icon" style="margin-bottom: 0; width: 44px; height: 44px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                </div>
                <div>
                  <strong>Phone Numbers (Illustrative Demo)</strong>
                  <p class="text-muted" style="margin-bottom: 0; font-size: 0.9rem;">Primary: 0000000000<br>Alternative: 0000000000</p>
                </div>
              </div>

              <div class="card" style="padding: 1.25rem; display: flex; align-items: flex-start; gap: 1rem;">
                <div class="card-icon teal" style="margin-bottom: 0; width: 44px; height: 44px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                </div>
                <div>
                  <strong>Email Inquiries</strong>
                  <p class="text-muted" style="margin-bottom: 0; font-size: 0.9rem;">demo@example.com</p>
                </div>
              </div>

              <div class="card" style="padding: 1.25rem; display: flex; align-items: flex-start; gap: 1rem;">
                <div class="card-icon" style="margin-bottom: 0; width: 44px; height: 44px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                </div>
                <div>
                  <strong>Office Location</strong>
                  <p class="text-muted" style="margin-bottom: 0; font-size: 0.9rem;">Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000</p>
                </div>
              </div>

              <div class="card" style="padding: 1.25rem; display: flex; align-items: flex-start; gap: 1rem;">
                <div class="card-icon teal" style="margin-bottom: 0; width: 44px; height: 44px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                </div>
                <div>
                  <strong>Business Hours (Demo)</strong>
                  <p class="text-muted" style="margin-bottom: 0; font-size: 0.9rem;">Monday – Saturday: 9:00 AM – 6:00 PM</p>
                </div>
              </div>
            </div>

            <div>
              {render_placeholder("staffing-contact-advisory.jpg", "ratio-16-9", "staffing-contact-advisory.jpg", 1200, 800, "Corporate reception and inquiry lounge")}
            </div>
          </div>

          <!-- General Contact Form with JS Validation -->
          <div>
            <div class="form-card">
              <h3 style="margin-bottom: 0.5rem;">Send a Demo Message</h3>
              <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1.5rem;">Fill out this form to test our simulated validation.</p>

              <form id="contact-form" novalidate>
                <div class="form-group">
                  <label class="form-label" for="contact-name">Your Full Name *</label>
                  <input type="text" id="contact-name" class="form-control" placeholder="e.g. Alex Morgan" required>
                  <div class="invalid-feedback">Please enter your name.</div>
                </div>

                <div class="form-group">
                  <label class="form-label" for="contact-email">Email Address *</label>
                  <input type="email" id="contact-email" class="form-control" placeholder="name@company.com" required>
                  <div class="invalid-feedback">Please enter a valid email address.</div>
                </div>

                <div class="form-group">
                  <label class="form-label" for="contact-phone">Phone Number *</label>
                  <input type="tel" id="contact-phone" class="form-control" placeholder="0000000000" required>
                  <div class="invalid-feedback">Please enter a contact phone number.</div>
                </div>

                <div class="form-group">
                  <label class="form-label" for="contact-type">Inquiry Category *</label>
                  <select id="contact-type" class="form-select" required>
                    <option value="">Select Category...</option>
                    <option value="employer">Employer / Staffing Requirement</option>
                    <option value="candidate">Candidate / Job Application Question</option>
                    <option value="general">General Workforce Inquiry</option>
                  </select>
                  <div class="invalid-feedback">Please select an inquiry category.</div>
                </div>

                <div class="form-group">
                  <label class="form-label" for="contact-message">Message *</label>
                  <textarea id="contact-message" class="form-control" rows="5" placeholder="Please describe your staffing or inquiry requirements..." required></textarea>
                  <div class="invalid-feedback">Please provide your message.</div>
                </div>

                <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Demo Message</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    write_html("contact.html", render_page(
        "Contact Us — Staffing Agency Inquiries & Consultations",
        "Contact our staffing agency for employer staffing consultations, candidate assistance, and workforce solutions.",
        "contact", content,
        breadcrumbs=[("Home", "index.html"), ("Contact Us", None)]
    ))

print("Part 4 functions defined.")
