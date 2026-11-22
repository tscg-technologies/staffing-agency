"""
STAFFING AGENCY — Website Generator
Generates all 52 HTML pages, sitemap.xml, robots.txt, and IMAGE-GENERATION-GUIDE.md.
"""

import os

# Base URL placeholder
BASE_URL = "https://example.com"

# Abstract Logo SVG
LOGO_SVG = """<svg class="logo-symbol" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <circle cx="20" cy="11" r="5" fill="#3167C5"/>
  <circle cx="10" cy="28" r="4.5" fill="#25A69A"/>
  <circle cx="30" cy="28" r="4.5" fill="#4F8DF7"/>
  <path d="M20 16V22M18 22L12 25M22 22L28 25" stroke="#1D3553" stroke-width="2.5" stroke-linecap="round"/>
</svg>"""

def get_header(active_nav="home"):
    return f"""
  <!-- Main Sticky Header -->
  <header class="site-header" role="banner">
    <div class="container header-main">
      <a href="index.html" class="brand-logo" aria-label="STAFFING AGENCY Home">
        {LOGO_SVG}
        <div class="brand-text">
          <span class="brand-name">STAFFING AGENCY</span>
          <span class="brand-subtext">Workforce Solutions</span>
        </div>
      </a>

      <!-- Clean 4-Item Navigation Menu -->
      <nav class="header-nav" id="primary-navigation" aria-label="Main Navigation">
        <ul class="nav-list">
          <li class="nav-item {'active' if active_nav == 'home' else ''}">
            <a href="index.html" class="nav-link">Home</a>
          </li>
          <li class="nav-item {'active' if active_nav == 'about' else ''}">
            <a href="about.html" class="nav-link">About</a>
          </li>
          <li class="nav-item {'active' if active_nav == 'services' else ''}">
            <a href="services.html" class="nav-link">Services</a>
          </li>
          <li class="nav-item {'active' if active_nav == 'contact' else ''}">
            <a href="contact.html" class="nav-link">Contact</a>
          </li>
        </ul>

        <!-- Mobile Drawer CTA Action Buttons -->
        <div class="mobile-header-actions">
          <a href="jobs.html" class="btn btn-outline btn-sm">Find Jobs</a>
          <a href="request-staff.html" class="btn btn-primary btn-sm">Hire Staff</a>
        </div>
      </nav>

      <!-- Right-side Action CTAs -->
      <div class="header-actions">
        <a href="jobs.html" class="btn btn-outline btn-sm">Find Jobs</a>
        <a href="request-staff.html" class="btn btn-primary btn-sm">Hire Staff</a>
      </div>

      <!-- Mobile Hamburger Button -->
      <button class="mobile-nav-toggle" aria-controls="primary-navigation" aria-expanded="false" aria-label="Toggle navigation menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </header>
"""

def get_footer():
    return f"""
  <!-- Global Multi-Column Footer -->
  <footer class="site-footer" role="contentinfo">
    <div class="container footer-top">
      <!-- Column 1: Identity -->
      <div class="footer-col">
        <a href="index.html" class="brand-logo" style="margin-bottom: 1.25rem;">
          {LOGO_SVG}
          <div class="brand-text">
            <span class="brand-name">STAFFING AGENCY</span>
            <span class="brand-subtext">Workforce Solutions</span>
          </div>
        </a>
        <p style="font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
          Connecting businesses with qualified talent and helping job seekers discover meaningful career pathways across diverse industries.
        </p>
        <div class="demo-disclaimer-pill" style="margin-bottom: 0;">
          ILLUSTRATIVE DEMO WEBSITE
        </div>
      </div>

      <!-- Column 2: Company -->
      <div class="footer-col">
        <h4>Company</h4>
        <ul class="footer-links">
          <li><a href="about.html">About Us</a></li>
          <li><a href="services.html">Staffing Services</a></li>
          <li><a href="industries.html">Industries We Serve</a></li>
          <li><a href="process.html">Our Process</a></li>
          <li><a href="case-studies.html">Case Studies</a></li>
          <li><a href="contact.html">Contact Us</a></li>
        </ul>
      </div>

      <!-- Column 3: Staffing Services -->
      <div class="footer-col">
        <h4>Staffing Services</h4>
        <ul class="footer-links">
          <li><a href="permanent-staffing.html">Permanent Staffing</a></li>
          <li><a href="temporary-staffing.html">Temporary Staffing</a></li>
          <li><a href="contract-staffing.html">Contract Staffing</a></li>
          <li><a href="executive-search.html">Executive Search</a></li>
          <li><a href="bulk-hiring.html">Bulk Hiring</a></li>
          <li><a href="it-staffing.html">IT Staffing</a></li>
        </ul>
      </div>

      <!-- Column 4: Candidates -->
      <div class="footer-col">
        <h4>Candidates</h4>
        <ul class="footer-links">
          <li><a href="jobs.html">Find Jobs</a></li>
          <li><a href="register-candidate.html">Candidate Registration</a></li>
          <li><a href="careers.html">Careers at Agency</a></li>
          <li><a href="insights.html">Recruitment Insights</a></li>
          <li><a href="faq.html">Candidate FAQ</a></li>
        </ul>
      </div>

      <!-- Column 5: Employers & Contact -->
      <div class="footer-col">
        <h4>Employers</h4>
        <ul class="footer-links" style="margin-bottom: 1.5rem;">
          <li><a href="employers.html">Hire Staff</a></li>
          <li><a href="request-staff.html">Request Staff Form</a></li>
          <li><a href="workforce-solutions.html">Workforce Solutions</a></li>
          <li><a href="recruitment-consulting.html">Recruitment Consulting</a></li>
        </ul>
        <h4>Contact (Demo)</h4>
        <div class="footer-contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>Phone: 0000000000</span>
        </div>
        <div class="footer-contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          <span>demo@example.com</span>
        </div>
        <div class="footer-contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <span>Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000</span>
        </div>
      </div>
    </div>

    <!-- Bottom Copyright & Legal Links -->
    <div class="container footer-bottom">
      <p>&copy; 2026 STAFFING AGENCY. Demonstration website. All rights reserved.</p>
      <div class="footer-legal-links">
        <a href="privacy-policy.html">Privacy Policy</a>
        <a href="terms-and-conditions.html">Terms &amp; Conditions</a>
        <a href="cookie-policy.html">Cookie Policy</a>
      </div>
    </div>
  </footer>
"""

def render_placeholder(filename, ratio_class="ratio-16-9", label_text=None, width=1200, height=800, alt_text="Staffing Agency Corporate Photography"):
    label = label_text if label_text else filename
    ratio_str = "16:9" if "16-9" in ratio_class else ("4:3" if "4-3" in ratio_class else ("1:1" if "1-1" in ratio_class else "21:9"))
    return f"""
    <div class="img-placeholder {ratio_class} has-image" role="img" aria-label="{alt_text}">
      <img src="assets/images/{filename}" alt="{alt_text}" loading="lazy" onerror="this.parentElement.classList.remove('has-image'); this.style.display='none';">
      <div class="placeholder-content">
        <svg class="placeholder-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
          <circle cx="8.5" cy="8.5" r="1.5"></circle>
          <polyline points="21 15 16 10 5 21"></polyline>
        </svg>
        <span class="placeholder-tag">Image Placeholder</span>
        <span class="placeholder-filename">{filename}</span>
        <span class="placeholder-ratio">{ratio_str} • {width} &times; {height}</span>
      </div>
    </div>
"""

def render_page(title, meta_desc, active_nav, body_content, breadcrumbs=None):
    breadcrumb_html = ""
    if breadcrumbs:
        items = []
        for i, (name, link) in enumerate(breadcrumbs):
            if link:
                items.append(f'<li class="breadcrumb-item"><a href="{link}">{name}</a></li>')
            else:
                items.append(f'<li class="breadcrumb-item active" aria-current="page">{name}</li>')
        breadcrumb_html = f"""
  <nav class="breadcrumb-nav" aria-label="Breadcrumb">
    <div class="container">
      <ol class="breadcrumb-list">
        {'<li class="breadcrumb-item" style="color: #A0B2C8;">/</li>'.join(items)}
      </ol>
    </div>
  </nav>
"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{meta_desc}">
  <title>{title} | STAFFING AGENCY</title>
  
  <!-- Open Graph Metadata -->
  <meta property="og:title" content="{title} | STAFFING AGENCY">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="STAFFING AGENCY">
  
  <!-- CSS Stylesheets -->
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/responsive.css">
  <link rel="stylesheet" href="assets/css/animations.css">
</head>
<body>
  {get_header(active_nav)}
  {breadcrumb_html}
  <main id="main-content">
    {body_content}
  </main>
  {get_footer()}

  <!-- Core JavaScript Modules -->
  <script src="assets/js/navigation.js"></script>
  <script src="assets/js/faq.js"></script>
  <script src="assets/js/job-search.js"></script>
  <script src="assets/js/forms.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>"""

print("Generator module loaded successfully.")
