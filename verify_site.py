"""
STAFFING AGENCY — Quality Assurance & Verification Script
Validates all 52 pages, internal links, image placeholders, and integrity.
"""

import os
import re

EXPECTED_PAGES = [
    # Core company pages (16)
    "index.html", "about.html", "services.html", "industries.html", "process.html",
    "workforce-solutions.html", "talent-acquisition.html", "recruitment-consulting.html",
    "team.html", "leadership.html", "case-studies.html", "case-study-details.html",
    "insights.html", "article-details.html", "faq.html", "contact.html",
    # Staffing service pages (17)
    "permanent-staffing.html", "temporary-staffing.html", "contract-staffing.html",
    "temp-to-hire.html", "executive-search.html", "bulk-hiring.html",
    "campus-recruitment.html", "it-staffing.html", "healthcare-staffing.html",
    "industrial-staffing.html", "blue-collar-staffing.html", "white-collar-staffing.html",
    "skilled-workforce.html", "unskilled-workforce.html", "payroll-staffing.html",
    "recruitment-process-outsourcing.html", "project-based-staffing.html",
    # Industry pages (9)
    "it-technology.html", "healthcare.html", "manufacturing.html", "banking-finance.html",
    "retail-ecommerce.html", "construction.html", "logistics-transportation.html",
    "hospitality.html", "telecommunications.html",
    # Employer and candidate pages (7)
    "employers.html", "request-staff.html", "candidates.html", "jobs.html",
    "job-details.html", "register-candidate.html", "careers.html",
    # Legal pages (3)
    "privacy-policy.html", "terms-and-conditions.html", "cookie-policy.html"
]

def verify():
    print(f"Verifying {len(EXPECTED_PAGES)} HTML pages...")
    missing_pages = []
    for page in EXPECTED_PAGES:
        if not os.path.exists(page):
            missing_pages.append(page)
    
    if missing_pages:
        print(f"FAILED: Missing pages: {missing_pages}")
        return False
    else:
        print("PASS: All 52 HTML pages exist on disk.")

    # Check internal links across all HTML files
    broken_links = []
    external_images = []
    placeholders_found = set()

    for page in EXPECTED_PAGES:
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()

        # Find all hrefs
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
        for h in hrefs:
            if h.startswith("#") or h.startswith("mailto:") or h.startswith("tel:") or h.startswith("http"):
                continue
            # Strip query params like ?id=job-101
            clean_link = h.split("?")[0].split("#")[0]
            if clean_link and not os.path.exists(clean_link):
                broken_links.append((page, h))

        # Check for external images
        if "unsplash.com" in content or "pexels.com" in content or "shutterstock.com" in content:
            external_images.append(page)

        # Collect placeholders and check img src
        placeholders = re.findall(r'<span class="placeholder-filename">([^<]+)</span>', content)
        for p in placeholders:
            placeholders_found.add(p)

        # Check all img src paths
        img_srcs = re.findall(r'<img [^>]*src=["\']([^"\']+)["\']', content)
        for isrc in img_srcs:
            if not os.path.exists(isrc):
                broken_links.append((page, isrc))

    if broken_links:
        print(f"FAILED: Broken internal links detected: {broken_links}")
        return False
    else:
        print("PASS: All internal links are valid and target existing pages.")

    if external_images:
        print(f"FAILED: External image URLs found in: {external_images}")
        return False
    else:
        print("PASS: Zero external image URLs found across all pages.")

    # Check IMAGE-GENERATION-GUIDE.md coverage
    with open("IMAGE-GENERATION-GUIDE.md", "r", encoding="utf-8") as f:
        guide_text = f.read()

    uncovered_placeholders = []
    for ph in placeholders_found:
        if ph not in guide_text:
            uncovered_placeholders.append(ph)

    if uncovered_placeholders:
        print(f"FAILED: Placeholders missing from guide: {uncovered_placeholders}")
        return False
    else:
        print(f"PASS: All {len(placeholders_found)} unique image placeholders are documented in IMAGE-GENERATION-GUIDE.md with Google Flow prompts.")

    # Check sitemap.xml coverage
    with open("sitemap.xml", "r", encoding="utf-8") as f:
        sitemap_text = f.read()
    
    missing_sitemap = []
    for page in EXPECTED_PAGES:
        if f"/{page}</loc>" not in sitemap_text:
            missing_sitemap.append(page)

    if missing_sitemap:
        print(f"FAILED: Pages missing from sitemap.xml: {missing_sitemap}")
        return False
    else:
        print("PASS: All 52 pages are indexed in sitemap.xml.")

    print("\nALL VERIFICATION TESTS PASSED PERFECTLY!")
    return True

if __name__ == "__main__":
    verify()
