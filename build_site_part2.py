"""
STAFFING AGENCY — Comprehensive Page Generation Engine
Builds all 52 HTML pages, sitemap.xml, robots.txt, and IMAGE-GENERATION-GUIDE.md.
"""

import os
from generate_helpers import render_page, render_placeholder, LOGO_SVG
from build_site_part1 import register_image, IMAGE_INVENTORY, write_html, make_index

# ==============================================================================
# 2. ABOUT US — about.html
# ==============================================================================
def make_about():
    register_image(
        "staffing-recruitment-consultation.jpg", "about.html", "Philosophy Section",
        "Senior talent advisor conducting a strategic workforce consultation with corporate HR directors",
        "16:9", "1200x800", "Landscape",
        "Professional commercial photograph of a recruitment consultant consulting with two corporate business leaders across a contemporary marble conference desk in a brightly lit glass office. Clean modern styling, confident postures, notebook and digital tablet on table, soft background blur, warm daylight.",
        "Rule of thirds, consultant on right speaking with clients on left", "Eye-level medium-close angle", "Natural soft diffused corporate lighting",
        "High-end corporate meeting room with glass architectural panels", "Executive editorial portrait style",
        "Navy, steel blue, charcoal grey, pristine white", "Balanced foreground meeting table with subjects in midground"
    )

    content = f"""
    <section class="page-hero">
      <div class="container">
        <span class="pathway-badge" style="background: rgba(255, 255, 255, 0.15); color: #FFF;">About Our Agency</span>
        <h1>About Staffing Agency</h1>
        <p class="lead">
          Understanding the role of structured recruitment and workforce solutions in connecting enterprise needs with professional capabilities.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem;">
          <div>
            <span class="section-subtitle">Our Purpose</span>
            <h2>What Is a Staffing Agency?</h2>
            <p>
              A staffing agency serves as a professional intermediary between companies seeking qualified personnel and individuals seeking temporary or permanent employment. By maintaining active networks of talent and understanding specific employer requisites, staffing agencies streamline recruitment operations, reduce administrative burden, and facilitate faster talent alignment.
            </p>
            <p>
              Modern workforce management requires agility. Organizations encounter seasonal demand shifts, sudden project expansions, or specialized skill shortages that require rapid, flexible staffing models without expanding fixed overheads.
            </p>
            <div class="demo-callout-box">
              <strong>Demonstration Profile Notice:</strong> This website represents a generic corporate model for staffing and talent acquisition operations. It does not reflect an actual operating agency, real client engagements, or historical placement figures.
            </div>
          </div>
          <div>
            {render_placeholder("staffing-recruitment-consultation.jpg", "ratio-16-9", "staffing-recruitment-consultation.jpg", 1200, 800, "Talent consultant in consultation meeting with corporate HR directors")}
          </div>
        </div>
      </div>
    </section>

    <section class="section section-bg-light">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle teal">Service Philosophy</span>
          <h2>Our Recruitment Philosophy</h2>
          <p class="lead">A balanced dual-focus model dedicated equally to employer success and candidate career progression.</p>
        </div>

        <div class="grid-2">
          <div class="card" style="border-top: 4px solid var(--color-corporate-blue);">
            <div class="card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </div>
            <h3 class="card-title">Employer-Focused Recruitment</h3>
            <p class="card-body">
              Every organization operates with distinct organizational cultures, delivery benchmarks, and team dynamics. Our employer-focused sourcing model emphasizes rigorous candidate screening, role-specific competency mapping, and proactive communication to ensure every recommended candidate aligns with the company's operational objectives.
            </p>
            <ul style="list-style: disc; padding-left: 1.25rem; font-size: 0.9rem; color: var(--color-body-text);">
              <li>Tailored workforce sizing and shift planning.</li>
              <li>Verification of technical credentials and work authorization.</li>
              <li>SLA-driven candidate shortlisting and interview logistics.</li>
            </ul>
          </div>

          <div class="card" style="border-top: 4px solid var(--color-teal-accent);">
            <div class="card-icon teal">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>
            </div>
            <h3 class="card-title">Candidate-Focused Support</h3>
            <p class="card-body">
              Job seekers deserve clear role expectations, respectful feedback, and transparent hiring processes. Our candidate engagement principles ensure job applicants receive complete job descriptions, realistic compensation expectations, and timely updates throughout their recruitment lifecycle.
            </p>
            <ul style="list-style: disc; padding-left: 1.25rem; font-size: 0.9rem; color: var(--color-body-text);">
              <li>Direct role alignment based on actual experience and skills.</li>
              <li>Objective interview guidance and preparation notes.</li>
              <li>Clear communication regarding contract terms and work schedules.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Professional Values Section -->
    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-subtitle">Guiding Standards</span>
          <h2>Professional Values</h2>
          <p class="lead">The foundational principles that guide recruitment consulting and workforce stewardship.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem; color: var(--color-primary-navy);">Integrity</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Upholding strict honesty and confidentiality in all interactions with client employers and job seekers.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem; color: var(--color-primary-navy);">Transparency</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Providing clear, realistic timelines, terms, and expectations regarding candidate availability and hiring outcomes.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem; color: var(--color-primary-navy);">Accountability</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Taking ownership of screening standards, candidate coordination, and responsiveness at every stage of the process.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem; color: var(--color-primary-navy);">Professionalism</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Delivering courteous, structured, and consistent service across all industry sectors and engagement levels.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem; color: var(--color-primary-navy);">Collaboration</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Working closely alongside client hiring managers and candidate pools as trusted talent advisors.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem; color: var(--color-primary-navy);">Continuous Improvement</h3>
            <p class="text-muted" style="font-size: 0.9rem;">Refining recruitment methodologies, evaluation frameworks, and communication channels based on feedback.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Talent Sourcing Approach -->
    <section class="section section-bg-light">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3rem;">
          <div>
            <span class="section-subtitle teal">Strategic Methodology</span>
            <h2>Our Talent Sourcing Approach</h2>
            <p>
              Effective staffing relies on a multi-tiered sourcing engine combining targeted industry outreach, passive talent discovery, professional networking, and academic partnerships. By utilizing systematic vetting rather than generic keyword searches, we identify candidates with verifiable skills suited to organizational roles.
            </p>
            <p>
              Whether identifying specialized cloud engineers or assembling high-volume manufacturing crews, the process remains rooted in disciplined evaluation and prompt coordination.
            </p>
            <div style="margin-top: 1.5rem;">
              <a href="process.html" class="btn btn-primary">Review Full Recruitment Process &rarr;</a>
            </div>
          </div>
          <div>
            <div class="card" style="padding: 2rem;">
              <h3 style="margin-bottom: 1rem; font-size: 1.25rem;">Multi-Tiered Sourcing Pillars</h3>
              <ul style="display: flex; flex-direction: column; gap: 1rem;">
                <li style="display: flex; gap: 0.75rem; align-items: flex-start;">
                  <span class="step-number" style="width: 28px; height: 28px; font-size: 0.85rem; flex-shrink: 0;">1</span>
                  <div>
                    <strong>Specialized Database Sourcing:</strong>
                    <p class="text-muted" style="font-size: 0.85rem; margin-bottom: 0;">Curated industry talent pools categorized by verified competencies.</p>
                  </div>
                </li>
                <li style="display: flex; gap: 0.75rem; align-items: flex-start;">
                  <span class="step-number teal" style="width: 28px; height: 28px; font-size: 0.85rem; flex-shrink: 0;">2</span>
                  <div>
                    <strong>Proactive Talent Mapping:</strong>
                    <p class="text-muted" style="font-size: 0.85rem; margin-bottom: 0;">Identifying experienced professionals not actively looking on open job boards.</p>
                  </div>
                </li>
                <li style="display: flex; gap: 0.75rem; align-items: flex-start;">
                  <span class="step-number" style="width: 28px; height: 28px; font-size: 0.85rem; flex-shrink: 0;">3</span>
                  <div>
                    <strong>Community &amp; Campus Outreach:</strong>
                    <p class="text-muted" style="font-size: 0.85rem; margin-bottom: 0;">Partnerships with vocational institutions and universities for entry talent.</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Navigation Next Steps CTA -->
    <section class="section" style="padding: 4rem 0;">
      <div class="container text-center">
        <h2>Explore Staffing Solutions or Opportunities</h2>
        <p class="lead" style="max-width: 600px; margin: 0 auto 2rem;">Discover our comprehensive recruitment offerings or browse available demo job listings.</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="services.html" class="btn btn-primary">Browse Services</a>
          <a href="employers.html" class="btn btn-outline">Employer Overview</a>
          <a href="candidates.html" class="btn btn-teal">Candidate Portal</a>
        </div>
      </div>
    </section>
    """

    write_html("about.html", render_page(
        "About Us — Corporate Recruitment & Workforce Philosophy",
        "Learn about our generic staffing agency model, service philosophy, talent sourcing methodology, and professional recruitment values.",
        "about", content,
        breadcrumbs=[("Home", "index.html"), ("About Us", None)]
    ))

print("make_about defined.")
