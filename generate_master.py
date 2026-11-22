"""
STAFFING AGENCY — Master Build Execution Script
Runs all generator modules, creates 52 HTML pages, sitemap.xml, robots.txt,
IMAGE-GENERATION-GUIDE.md, and README.md.
"""

import os
from build_site_part1 import make_index, IMAGE_INVENTORY
from build_site_part2 import make_about
from build_site_part3 import (
    make_services, make_industries, make_process, make_workforce_solutions
)
from build_site_part4 import (
    make_talent_acquisition, make_recruitment_consulting, make_team, make_leadership,
    make_case_studies, make_case_study_details, make_insights, make_article_details,
    make_faq, make_contact
)
from build_services_pages import make_all_service_pages
from build_industry_pages import make_all_industry_pages
from build_portal_pages import (
    make_employers, make_request_staff, make_candidates, make_jobs,
    make_job_details, make_register_candidate, make_careers,
    make_privacy_policy, make_terms_and_conditions, make_cookie_policy
)

def run_build():
    print("Starting Staffing Agency static website build...")
    
    # Core pages (16)
    make_index()
    make_about()
    make_services()
    make_industries()
    make_process()
    make_workforce_solutions()
    make_talent_acquisition()
    make_recruitment_consulting()
    make_team()
    make_leadership()
    make_case_studies()
    make_case_study_details()
    make_insights()
    make_article_details()
    make_faq()
    make_contact()

    # Staffing Service pages (17)
    make_all_service_pages()

    # Industry pages (9)
    make_all_industry_pages()

    # Portal & Legal pages (10)
    make_employers()
    make_request_staff()
    make_candidates()
    make_jobs()
    make_job_details()
    make_register_candidate()
    make_careers()
    make_privacy_policy()
    make_terms_and_conditions()
    make_cookie_policy()

    # Generate sitemap.xml
    make_sitemap()

    # Generate robots.txt
    make_robots()

    # Generate IMAGE-GENERATION-GUIDE.md
    make_image_guide()

    # Generate README.md
    make_readme()

    print("\nBUILD COMPLETE!")
    print(f"Total Unique Images Registered: {len(IMAGE_INVENTORY)}")

ALL_52_PAGES = [
    # Core (16)
    "index.html", "about.html", "services.html", "industries.html", "process.html",
    "workforce-solutions.html", "talent-acquisition.html", "recruitment-consulting.html",
    "team.html", "leadership.html", "case-studies.html", "case-study-details.html",
    "insights.html", "article-details.html", "faq.html", "contact.html",
    # Services (17)
    "permanent-staffing.html", "temporary-staffing.html", "contract-staffing.html",
    "temp-to-hire.html", "executive-search.html", "bulk-hiring.html",
    "campus-recruitment.html", "it-staffing.html", "healthcare-staffing.html",
    "industrial-staffing.html", "blue-collar-staffing.html", "white-collar-staffing.html",
    "skilled-workforce.html", "unskilled-workforce.html", "payroll-staffing.html",
    "recruitment-process-outsourcing.html", "project-based-staffing.html",
    # Industries (9)
    "it-technology.html", "healthcare.html", "manufacturing.html", "banking-finance.html",
    "retail-ecommerce.html", "construction.html", "logistics-transportation.html",
    "hospitality.html", "telecommunications.html",
    # Portal & Legal (10)
    "employers.html", "request-staff.html", "candidates.html", "jobs.html",
    "job-details.html", "register-candidate.html", "careers.html",
    "privacy-policy.html", "terms-and-conditions.html", "cookie-policy.html"
]

def make_sitemap():
    base_url = "https://example.com"
    urls_xml = ""
    for page in ALL_52_PAGES:
        priority = "1.0" if page == "index.html" else ("0.8" if page in ["employers.html", "candidates.html", "jobs.html", "request-staff.html"] else "0.6")
        urls_xml += f"""  <url>
    <loc>{base_url}/{page}</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls_xml}</urlset>"""

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Generated: sitemap.xml")

def make_robots():
    robots_content = """# robots.txt for Staffing Agency Demonstration Website
User-agent: *
Allow: /

# Sitemaps
Sitemap: https://example.com/sitemap.xml
"""
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_content)
    print("Generated: robots.txt")

def make_image_guide():
    # Deduplicate image inventory by filename while aggregating pages
    unique_images = {}
    for item in IMAGE_INVENTORY:
        fn = item["filename"]
        if fn not in unique_images:
            unique_images[fn] = item
            unique_images[fn]["pages_used"] = [item["page"]]
        else:
            if item["page"] not in unique_images[fn]["pages_used"]:
                unique_images[fn]["pages_used"].append(item["page"])

    landscape_count = sum(1 for img in unique_images.values() if img["orientation"] == "Landscape")
    portrait_count = sum(1 for img in unique_images.values() if img["orientation"] == "Portrait")
    square_count = sum(1 for img in unique_images.values() if img["orientation"] == "Square")

    guide_md = f"""# Comprehensive Image Generation Guide for Staffing Agency Website
**Document Version:** 1.0  
**Target Platform:** Google Flow Image Generator  
**Website Context:** Generic Staffing Agency & Workforce Solutions Multi-Page Website  

---

## 1. Executive Summary & Status
All 52 HTML pages of the **STAFFING AGENCY** website utilize structured, responsive CSS/SVG placeholders with fixed aspect ratios (`16:9`, `4:3`, `1:1`, `21:9`) and fallback styling. This eliminates Cumulative Layout Shift (CLS) and ensures that zero broken image icons appear in the browser.

This guide provides **individual, copy-ready Google Flow prompts** for every image asset across the entire site. Once generated, place the resulting image files directly into `assets/images/<filename>` to immediately activate full photographic rendering.

---

## 2. Image Asset Inventory Table

| Image # | Filename | Primary Pages | Aspect Ratio | Resolution | Orientation | Subject Description |
|:---:|:---|:---|:---:|:---:|:---:|:---|
"""
    for idx, (fn, data) in enumerate(unique_images.items(), 1):
        pages_str = ", ".join(data["pages_used"][:2]) + ("..." if len(data["pages_used"]) > 2 else "")
        guide_md += f"| {idx} | `{fn}` | {pages_str} | {data['ratio']} | {data['resolution']} | {data['orientation']} | {data['desc'][:50]}... |\n"

    guide_md += f"""
---

## 3. Inventory Breakdown & Statistics
- **Total Unique Images:** {len(unique_images)}
- **Landscape Images:** {landscape_count}
- **Portrait Images:** {portrait_count}
- **Square Images:** {square_count}
- **Target Folder:** `assets/images/`

---

## 4. Page-by-Page Detailed Image Prompts

"""

    for idx, (fn, data) in enumerate(unique_images.items(), 1):
        pages_list = ", ".join(data["pages_used"])
        guide_md += f"""### Image {idx}: `{fn}`
- **Target Filename:** `{fn}`
- **Used on HTML Pages:** {pages_list}
- **Website Section:** {data['section']}
- **Subject Description:** {data['desc']}
- **Aspect Ratio:** {data['ratio']}
- **Resolution:** {data['resolution']} pixels
- **Orientation:** {data['orientation']}
- **Composition:** {data['composition']}
- **Camera Angle:** {data['angle']}
- **Lighting:** {data['lighting']}
- **Background:** {data['bg']}
- **Photography Style:** {data['style']}
- **Color Palette:** {data['palette']}
- **Subject Positioning:** {data['subject_pos']}
- **Negative Space:** Subtle breathing space on outer perimeter for responsive UI framing.

#### Copy-Ready Google Flow Prompt:
```text
{data['prompt']}
```

---
"""

    guide_md += """## 5. Recommended Image Generation Order
1. **Tier 1 (High Visibility Heroes):** `staffing-hero-team.jpg`, `staffing-employer-meeting.jpg`, `staffing-candidate-registration.jpg`, `staffing-recruitment-consultation.jpg`.
2. **Tier 2 (Service Verticals):** `staffing-it-professionals.jpg`, `staffing-healthcare-workers.jpg`, `staffing-industrial-workforce.jpg`, `staffing-warehouse-workers.jpg`, `staffing-manufacturing-workers.jpg`.
3. **Tier 3 (Operational Support):** `staffing-permanent-recruitment.jpg`, `staffing-temporary-workforce.jpg`, `staffing-contract-staffing.jpg`, `staffing-executive-search.jpg`, `staffing-bulk-hiring.jpg`, `staffing-recruitment-process.jpg`.
4. **Tier 4 (Advisory & Office):** `staffing-office-team.jpg`, `staffing-workforce-planning.jpg`, `staffing-talent-acquisition.jpg`, `staffing-recruitment-consulting.jpg`, `staffing-contact-advisory.jpg`.

---

## 6. Instructions for Replacing Placeholders
1. Generate the image using the exact prompt in Google Flow.
2. Export or download the image as JPEG/JPG or WebP at the specified resolution.
3. Rename the file to match the exact **Target Filename** (e.g. `staffing-hero-team.jpg`).
4. Save the file into the `assets/images/` directory within this project.
5. In your HTML files, simply ensure the image is linked inside the placeholder element:
   ```html
   <div class="img-placeholder ratio-16-9">
     <img src="assets/images/staffing-hero-team.jpg" alt="Corporate recruitment team" loading="lazy">
   </div>
   ```
6. The CSS will immediately render the high-resolution photo with perfect `object-fit: cover` and no layout shift!
"""

    with open("IMAGE-GENERATION-GUIDE.md", "w", encoding="utf-8") as f:
        f.write(guide_md)
    print("Generated: IMAGE-GENERATION-GUIDE.md")

def make_readme():
    readme_md = f"""# STAFFING AGENCY — Complete Corporate Demonstration Website

A modern, responsive, multi-page static website for a generic **STAFFING AGENCY**, built strictly using **HTML5, CSS3, and Vanilla JavaScript**.

## Project Highlights
- **Strictly Framework-Free:** Zero dependencies on React, Next.js, Vue, Angular, Bootstrap, Tailwind, jQuery, PHP, MySQL, or Node.js.
- **Hostinger Compatible:** 100% static frontend, ready for drag-and-drop deployment to Hostinger static hosting or any web server.
- **52 Complete HTML Pages:** Full sitemap covering Core Company pages (16), Staffing Services (17), Industry Portals (9), Employer & Candidate Portals (7), and Legal Policies (3).
- **Two Separate User Journeys:** Dedicated employer and candidate landing pages, navigation pathways, and forms.
- **Zero Broken Images:** Responsive CSS/SVG placeholder architecture with zero layout shifts (CLS).
- **Comprehensive Image Generation Guide:** `IMAGE-GENERATION-GUIDE.md` containing individual copy-ready Google Flow prompts for every visual placeholder.
- **Interactive Vanilla JS:**
  - Sticky header with scroll detection.
  - Accessible mobile drawer navigation with multi-level dropdowns.
  - Accessible FAQ accordions.
  - Searchable client-side job board with multi-facet filters, dynamic counts, and load more pagination.
  - Employer request form with client-side validation and simulated confirmation modal.
  - Candidate registration form with resume file validation (PDF, DOC, DOCX up to 5MB), size display, and remove handler.
  - Contact form with validation and demo modal.
  - Back-to-top smooth scrolling.

## Directory Structure
```
staffing-agency-website/
├── index.html                           # Home
├── about.html                           # About Us
├── services.html                        # All Staffing Services Directory
├── industries.html                      # All Industries Directory
├── process.html                         # 6-Step Recruitment Timeline
├── workforce-solutions.html             # Workforce Planning & Allocation
├── talent-acquisition.html              # Sourcing Methodology
├── recruitment-consulting.html          # Advisory Services
├── team.html                            # Recruitment Team Roles (Demo)
├── leadership.html                      # Functional Leadership Governance
├── case-studies.html                    # 3 Illustrative Scenarios
├── case-study-details.html              # In-Depth Scenario Breakdown
├── insights.html                        # Articles & Knowledge Base
├── article-details.html                 # Sample Article
├── faq.html                             # Dual-Audience FAQ Accordion
├── contact.html                         # Contact & Office Details
│
├── permanent-staffing.html              # 1. Permanent Staffing
├── temporary-staffing.html              # 2. Temporary Staffing
├── contract-staffing.html               # 3. Contract Staffing
├── temp-to-hire.html                    # 4. Temp-to-Hire Staffing
├── executive-search.html                # 5. Executive Search
├── bulk-hiring.html                     # 6. Bulk Recruitment
├── campus-recruitment.html              # 7. Campus Recruitment
├── it-staffing.html                     # 8. IT Staffing
├── healthcare-staffing.html             # 9. Healthcare Staffing
├── industrial-staffing.html             # 10. Industrial Staffing
├── blue-collar-staffing.html            # 11. Blue-Collar Staffing
├── white-collar-staffing.html           # 12. White-Collar Staffing
├── skilled-workforce.html               # 13. Skilled Workforce
├── unskilled-workforce.html             # 14. General Workforce
├── payroll-staffing.html                # 15. Payroll Administration
├── recruitment-process-outsourcing.html # 16. Recruitment Process Outsourcing (RPO)
├── project-based-staffing.html          # 17. Project-Based Staffing
│
├── it-technology.html                   # Industry: IT & Technology
├── healthcare.html                      # Industry: Healthcare
├── manufacturing.html                   # Industry: Manufacturing
├── banking-finance.html                 # Industry: Banking & Finance
├── retail-ecommerce.html                # Industry: Retail & E-commerce
├── construction.html                    # Industry: Construction
├── logistics-transportation.html        # Industry: Logistics & Transportation
├── hospitality.html                     # Industry: Hospitality
├── telecommunications.html              # Industry: Telecommunications
│
├── employers.html                       # Employer Portal Landing
├── request-staff.html                   # Employer Staffing Requisition Form
├── candidates.html                      # Candidate Portal Landing
├── jobs.html                            # Searchable Job Board
├── job-details.html                     # Detailed Role View
├── register-candidate.html              # Candidate Registration & Resume Upload
├── careers.html                         # Internal Agency Careers
│
├── privacy-policy.html                  # Privacy Policy
├── terms-and-conditions.html            # Terms of Use
├── cookie-policy.html                   # Cookie Disclosure
│
├── assets/
│   ├── css/
│   │   ├── style.css                    # Main design system & layout
│   │   ├── responsive.css               # Breakpoints & mobile drawer
│   │   └── animations.css               # Subtle transitions
│   ├── js/
│   │   ├── navigation.js                # Sticky header & menu toggles
│   │   ├── faq.js                       # Accessible accordion handler
│   │   ├── job-search.js                # Client-side search engine
│   │   ├── forms.js                     # Validation & demo modals
│   │   └── main.js                      # Main initialization
│   └── images/
│       └── README.md                    # Asset deployment guide
│
├── sitemap.xml                          # 52 URL sitemap
├── robots.txt                           # Search engine directive
├── IMAGE-GENERATION-GUIDE.md            # Detailed Google Flow image prompts
└── README.md                            # Complete documentation
```

## Color Palette
- **Primary Navy:** `#14243A`
- **Secondary Navy:** `#1D3553`
- **Corporate Blue:** `#3167C5`
- **Bright Blue:** `#4F8DF7`
- **Teal Accent:** `#25A69A`
- **Light Background:** `#F4F7FB`
- **White:** `#FFFFFF`
- **Body Text:** `#45546A`
- **Muted Text:** `#7C899A`

## Deployment Instructions (Hostinger Static Hosting)
1. Upload all files from this directory to Hostinger's `public_html` directory using Hostinger File Manager or FTP.
2. Confirm that `index.html` is located directly in the root of `public_html`.
3. Your staffing agency demonstration website is now live!

## Disclaimer
This is an illustrative demonstration website for a generic staffing agency. All job openings, candidate profiles, case studies, and corporate credentials operate in local simulation mode. No user data, inquiries, or resumes are transmitted or stored.
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_md)
    print("Generated: README.md")

if __name__ == "__main__":
    run_build()
"""
"""
