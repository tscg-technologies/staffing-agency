/**
 * STAFFING AGENCY — Searchable Job Board & Listings
 * Vanilla JavaScript (Demo Dataset & Interactive Filtering)
 */

const DEMO_JOBS = [
  {
    id: "job-101",
    title: "Software Developer",
    department: "Engineering & IT",
    industry: "IT & Technology",
    location: "Hyderabad (Illustrative Demo)",
    employmentType: "Permanent",
    experience: "3-5 Years",
    postedDate: "2 days ago",
    summary: "Seeking a Software Developer to support enterprise web applications, RESTful services, and modern frontend interfaces.",
    responsibilities: [
      "Collaborate with multi-functional teams to design, develop, and maintain clean software applications.",
      "Write well-structured, testable, and maintainable application code following standards.",
      "Participate in code reviews, technical discussions, and sprint planning sessions.",
      "Identify performance bottlenecks and troubleshoot software issues."
    ],
    skills: ["JavaScript", "HTML5", "CSS3", "REST APIs", "Git", "SQL"],
    education: "Bachelor's degree in Computer Science, Information Technology, or equivalent practical experience."
  },
  {
    id: "job-102",
    title: "Data Analyst",
    department: "Business Intelligence",
    industry: "Banking & Finance",
    location: "Bangalore (Illustrative Demo)",
    employmentType: "Permanent",
    experience: "2-4 Years",
    postedDate: "3 days ago",
    summary: "Analyze financial data flows, prepare KPI dashboards, and support operational decision-making processes.",
    responsibilities: [
      "Gather and process structured datasets from varied corporate data sources.",
      "Build insightful analytical reports and dashboard visualizations for stakeholders.",
      "Conduct exploratory trend analysis to support business performance tracking.",
      "Maintain data hygiene and validation standards."
    ],
    skills: ["SQL", "Excel / Spreadsheets", "BI Visualization", "Data Modeling", "Statistical Analysis"],
    education: "Degree in Statistics, Mathematics, Economics, Computer Science, or related analytical field."
  },
  {
    id: "job-103",
    title: "Customer Support Executive",
    department: "Customer Service",
    industry: "Retail & E-commerce",
    location: "Pune (Illustrative Demo)",
    employmentType: "Full-Time",
    experience: "1-3 Years",
    postedDate: "1 day ago",
    summary: "Provide courteous customer assistance across omnichannel ticket, email, and live communication channels.",
    responsibilities: [
      "Address client queries promptly with accurate product and order tracking information.",
      "Log ticket statuses within customer management systems following service standards.",
      "Escalate unresolved issues to specialized technical teams smoothly.",
      "Contribute to continuous improvement of customer satisfaction ratings."
    ],
    skills: ["Customer Communication", "CRM Tools", "Problem Resolution", "Active Listening"],
    education: "High school diploma or Bachelor's degree in any discipline."
  },
  {
    id: "job-104",
    title: "HR Executive",
    department: "Human Resources",
    industry: "Manufacturing",
    location: "Chennai (Illustrative Demo)",
    employmentType: "Permanent",
    experience: "2-5 Years",
    postedDate: "4 days ago",
    summary: "Support recruitment coordination, onboarding workflows, attendance tracking, and internal employee engagement.",
    responsibilities: [
      "Coordinate interview schedules and liaise between candidates and department heads.",
      "Facilitate employee onboarding documentation and induction briefings.",
      "Assist with HR administration, leave records, and policy communication.",
      "Support organizational welfare and employee relations initiatives."
    ],
    skills: ["HR Administration", "Candidate Screening", "Communication", "HRIS Basics"],
    education: "Bachelor's or Master's degree in Human Resources, Business, or related field."
  },
  {
    id: "job-105",
    title: "Accountant",
    department: "Finance & Accounting",
    industry: "Banking & Finance",
    location: "Mumbai (Illustrative Demo)",
    employmentType: "Permanent",
    experience: "3-6 Years",
    postedDate: "5 days ago",
    summary: "Manage ledger reconciliation, accounts payable and receivable, invoice documentation, and financial reporting.",
    responsibilities: [
      "Prepare monthly ledger reconciliations and verify transaction accuracy.",
      "Process vendor invoices, credit notes, and expense reimbursements.",
      "Assist senior financial controllers during periodic audit reviews.",
      "Maintain organized accounting records following standard compliance practices."
    ],
    skills: ["Financial Accounting", "Tally / ERP Software", "Taxation Principles", "Reconciliation"],
    education: "Bachelor of Commerce (B.Com) or related accounting certification."
  },
  {
    id: "job-106",
    title: "Warehouse Associate",
    department: "Supply Chain & Logistics",
    industry: "Logistics & Transportation",
    location: "Hyderabad (Illustrative Demo)",
    employmentType: "Contract",
    experience: "1-2 Years",
    postedDate: "Just now",
    summary: "Assist with inventory receipt, packing, order dispatch, and physical stock organization inside distribution hubs.",
    responsibilities: [
      "Receive inbound inventory, check packing slips, and report variances.",
      "Pick, pack, and label parcels according to dispatch schedules.",
      "Follow workplace safety, ergonomics, and material handling guidelines.",
      "Perform periodic cycle counts and inventory shelving maintenance."
    ],
    skills: ["Inventory Handling", "Barcode Scanning", "Physical Dexterity", "Teamwork"],
    education: "Secondary school education or equivalent vocational experience."
  },
  {
    id: "job-107",
    title: "Mechanical Engineer",
    department: "Operations & Maintenance",
    industry: "Manufacturing",
    location: "Gurugram (Illustrative Demo)",
    employmentType: "Permanent",
    experience: "3-6 Years",
    postedDate: "6 days ago",
    summary: "Oversee machinery performance, preventive plant maintenance schedules, and assembly line efficiency.",
    responsibilities: [
      "Inspect industrial machinery, hydraulic systems, and mechanical components regularly.",
      "Design preventative maintenance procedures to minimize production downtime.",
      "Diagnose technical faults and supervise prompt mechanical repairs.",
      "Maintain compliance with industrial health and workplace safety norms."
    ],
    skills: ["AutoCAD / CAD Tools", "Preventive Maintenance", "Troubleshooting", "Equipment Calibration"],
    education: "Bachelor's degree in Mechanical Engineering or related discipline."
  },
  {
    id: "job-108",
    title: "Production Operator",
    department: "Plant Operations",
    industry: "Manufacturing",
    location: "Ahmedabad (Illustrative Demo)",
    employmentType: "Temporary",
    experience: "1-3 Years",
    postedDate: "1 week ago",
    summary: "Operate automated packaging and manufacturing machinery while observing strict production safety standards.",
    responsibilities: [
      "Set up and monitor automated line machinery as per daily output quotas.",
      "Perform quality checks on finished goods and discard defective units.",
      "Maintain a tidy, safe, and organized workstation following 5S principles.",
      "Document daily production tallies and machine cycle logs accurately."
    ],
    skills: ["Machine Operation", "Quality Inspection", "Safety Compliance", "Production Logging"],
    education: "ITI diploma, high school diploma, or relevant vocational qualification."
  },
  {
    id: "job-109",
    title: "Sales Executive",
    department: "Commercial Sales",
    industry: "Telecommunications",
    location: "Kolkata (Illustrative Demo)",
    employmentType: "Permanent",
    experience: "2-4 Years",
    postedDate: "3 days ago",
    summary: "Drive enterprise customer outreach, demonstrate product capabilities, and achieve agreed quarterly revenue targets.",
    responsibilities: [
      "Identify prospective commercial leads and establish initial professional contact.",
      "Present telecommunications and connectivity service proposals to business clients.",
      "Negotiate contractual terms within approved corporate discount guidelines.",
      "Cultivate enduring long-term client relationships to support renewals."
    ],
    skills: ["B2B Sales", "Client Pitching", "Lead Pipeline Management", "Negotiation"],
    education: "Bachelor's degree in Business, Marketing, or related field."
  },
  {
    id: "job-110",
    title: "Digital Marketing Executive",
    department: "Marketing",
    industry: "Retail & E-commerce",
    location: "Noida (Illustrative Demo)",
    employmentType: "Full-Time",
    experience: "2-4 Years",
    postedDate: "4 days ago",
    summary: "Execute digital campaign strategy across search, email, content channels, and social media platforms.",
    responsibilities: [
      "Plan and monitor organic and paid customer acquisition marketing initiatives.",
      "Generate creative copy, marketing briefs, and campaign assets.",
      "Analyze channel performance metrics, bounce rates, and conversion funnels.",
      "Coordinate with web and design teams for continuous page enhancements."
    ],
    skills: ["SEO / SEM", "Content Strategy", "Email Marketing", "Web Analytics"],
    education: "Bachelor's degree in Marketing, Communications, or relevant field."
  },
  {
    id: "job-111",
    title: "Business Analyst",
    department: "Strategy & Technology",
    industry: "IT & Technology",
    location: "Hyderabad (Illustrative Demo)",
    employmentType: "Permanent",
    experience: "3-5 Years",
    postedDate: "2 days ago",
    summary: "Bridge business stakeholder requirements with technology implementation teams to streamline software delivery.",
    responsibilities: [
      "Document detailed business requirements and translate them into technical user stories.",
      "Map current and future-state operational workflow diagrams.",
      "Facilitate requirement discovery workshops with product owners and developers.",
      "Support user acceptance testing (UAT) and end-user feature validation."
    ],
    skills: ["Requirement Gathering", "User Stories", "UML / Flowcharts", "Agile Methodologies"],
    education: "Bachelor's or Master's degree in Information Systems, Business Administration, or Engineering."
  },
  {
    id: "job-112",
    title: "Quality Analyst",
    department: "Quality Assurance",
    industry: "Healthcare",
    location: "Bangalore (Illustrative Demo)",
    employmentType: "Contract",
    experience: "2-4 Years",
    postedDate: "5 days ago",
    summary: "Perform quality audits, documentation reviews, and testing protocols to ensure healthcare technology compliance.",
    responsibilities: [
      "Execute functional quality testing plans against healthcare system specifications.",
      "Identify, document, and track software defects within project tracking tools.",
      "Verify adherence to established healthcare data privacy and security guidelines.",
      "Collaborate with development teams to verify bug fixes and regression test releases."
    ],
    skills: ["QA Testing", "Test Case Documentation", "Defect Tracking", "Healthcare Standards Awareness"],
    education: "Degree in Computer Science, Health Informatics, or related technical discipline."
  }
];

document.addEventListener('DOMContentLoaded', () => {
  // If on jobs.html, initialize search interface
  if (document.getElementById('jobs-container')) {
    initJobSearch();
  }

  // If on job-details.html, initialize details renderer
  if (document.getElementById('job-details-container')) {
    initJobDetails();
  }
});

function initJobSearch() {
  const container = document.getElementById('jobs-container');
  const countEl = document.getElementById('jobs-count');
  const keywordInput = document.getElementById('search-keyword');
  const industrySelect = document.getElementById('filter-industry');
  const typeSelect = document.getElementById('filter-type');
  const experienceSelect = document.getElementById('filter-experience');
  const resetBtn = document.getElementById('reset-filters-btn');
  const searchForm = document.getElementById('job-search-form');

  let currentJobs = [...DEMO_JOBS];
  const itemsPerPage = 6;
  let visibleCount = itemsPerPage;

  function renderJobs() {
    container.innerHTML = '';

    if (currentJobs.length === 0) {
      container.innerHTML = `
        <div class="card text-center" style="padding: 3rem 1.5rem;">
          <svg style="width: 48px; height: 48px; margin: 0 auto 1rem; color: var(--color-muted-text);" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <h3 style="margin-bottom: 0.5rem;">No Demo Vacancies Match Your Criteria</h3>
          <p class="text-muted" style="max-width: 480px; margin: 0 auto 1.5rem;">Try relaxing your filters or resetting the keyword search to view illustrative demo roles.</p>
          <div>
            <button type="button" class="btn btn-outline" id="empty-reset-btn">Reset All Filters</button>
          </div>
        </div>
      `;
      if (countEl) countEl.textContent = "Showing 0 demo vacancies";
      const emptyReset = document.getElementById('empty-reset-btn');
      if (emptyReset) emptyReset.addEventListener('click', resetFilters);
      const loadMoreBtn = document.getElementById('load-more-jobs-btn');
      if (loadMoreBtn) loadMoreBtn.style.display = 'none';
      return;
    }

    if (countEl) {
      countEl.textContent = `Showing ${Math.min(visibleCount, currentJobs.length)} of ${currentJobs.length} demo vacancies`;
    }

    const slice = currentJobs.slice(0, visibleCount);
    slice.forEach(job => {
      const card = document.createElement('div');
      card.className = 'job-card';
      card.innerHTML = `
        <div style="flex-grow: 1;">
          <div class="demo-disclaimer-pill">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            DEMO JOB LISTING — NOT A VERIFIED LIVE VACANCY
          </div>
          <h3 class="job-title"><a href="job-details.html?id=${job.id}">${job.title}</a></h3>
          <div class="job-meta-list">
            <span class="job-meta-item">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              ${job.location}
            </span>
            <span class="job-meta-item">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
              ${job.industry}
            </span>
            <span class="job-meta-item">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              ${job.experience}
            </span>
          </div>
          <p style="font-size: 0.9rem; margin-bottom: 0.75rem; color: var(--color-body-text);">${job.summary}</p>
          <div class="job-tags">
            <span class="tag-badge">${job.employmentType}</span>
            <span class="tag-badge teal">${job.department}</span>
            ${job.skills.slice(0, 3).map(s => `<span class="tag-badge">${s}</span>`).join('')}
          </div>
        </div>
        <div style="flex-shrink: 0; align-self: center;">
          <a href="job-details.html?id=${job.id}" class="btn btn-outline btn-sm">View Details</a>
        </div>
      `;
      container.appendChild(card);
    });

    const loadMoreBtn = document.getElementById('load-more-jobs-btn');
    if (loadMoreBtn) {
      if (visibleCount >= currentJobs.length) {
        loadMoreBtn.style.display = 'none';
      } else {
        loadMoreBtn.style.display = 'inline-flex';
      }
    }
  }

  function applyFilters() {
    const keyword = (keywordInput?.value || '').trim().toLowerCase();
    const industry = industrySelect?.value || 'all';
    const type = typeSelect?.value || 'all';
    const exp = experienceSelect?.value || 'all';

    currentJobs = DEMO_JOBS.filter(job => {
      const matchKeyword = !keyword || 
        job.title.toLowerCase().includes(keyword) || 
        job.summary.toLowerCase().includes(keyword) ||
        job.skills.some(s => s.toLowerCase().includes(keyword));

      const matchIndustry = industry === 'all' || job.industry === industry;
      const matchType = type === 'all' || job.employmentType.toLowerCase() === type.toLowerCase();
      
      let matchExp = true;
      if (exp === 'entry') matchExp = job.experience.includes('1-') || job.experience.includes('2-');
      if (exp === 'mid') matchExp = job.experience.includes('3-') || job.experience.includes('4-');
      if (exp === 'senior') matchExp = job.experience.includes('5') || job.experience.includes('6');

      return matchKeyword && matchIndustry && matchType && matchExp;
    });

    visibleCount = itemsPerPage;
    renderJobs();
  }

  function resetFilters() {
    if (keywordInput) keywordInput.value = '';
    if (industrySelect) industrySelect.value = 'all';
    if (typeSelect) typeSelect.value = 'all';
    if (experienceSelect) experienceSelect.value = 'all';
    currentJobs = [...DEMO_JOBS];
    visibleCount = itemsPerPage;
    renderJobs();
  }

  if (searchForm) {
    searchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      applyFilters();
    });
  }

  [keywordInput, industrySelect, typeSelect, experienceSelect].forEach(el => {
    if (el) el.addEventListener('input', applyFilters);
    if (el) el.addEventListener('change', applyFilters);
  });

  if (resetBtn) resetBtn.addEventListener('click', resetFilters);

  const loadMoreBtn = document.getElementById('load-more-jobs-btn');
  if (loadMoreBtn) {
    loadMoreBtn.addEventListener('click', () => {
      visibleCount += itemsPerPage;
      renderJobs();
    });
  }

  // Initial render
  renderJobs();
}

function initJobDetails() {
  const container = document.getElementById('job-details-container');
  if (!container) return;

  const urlParams = new URLSearchParams(window.location.search);
  const jobId = urlParams.get('id') || "job-101";

  const job = DEMO_JOBS.find(j => j.id === jobId) || DEMO_JOBS[0];

  document.title = `${job.title} — Demo Job Details | STAFFING AGENCY`;

  container.innerHTML = `
    <div class="card" style="margin-bottom: 2rem; border-top: 4px solid var(--color-corporate-blue);">
      <div class="demo-callout-box" style="margin-top: 0;">
        <strong>Notice:</strong> DEMO JOB LISTING — NOT A VERIFIED LIVE VACANCY. This role profile is created solely to demonstrate staffing search functionality and applicant experience.
      </div>

      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.5rem;">
        <div>
          <h1 style="font-size: 2rem; margin-bottom: 0.5rem;">${job.title}</h1>
          <p class="text-muted" style="margin-bottom: 0;">Department: <strong>${job.department}</strong> | Industry: <strong>${job.industry}</strong></p>
        </div>
        <div>
          <a href="#apply-section" class="btn btn-primary btn-lg">Apply Now (Demo)</a>
        </div>
      </div>

      <div class="grid-4" style="background: var(--color-light-bg); padding: 1.25rem; border-radius: var(--radius-md); margin-bottom: 2rem;">
        <div>
          <span class="text-muted" style="font-size: 0.8rem; display: block;">Employment Type</span>
          <strong>${job.employmentType}</strong>
        </div>
        <div>
          <span class="text-muted" style="font-size: 0.8rem; display: block;">Location</span>
          <strong>${job.location}</strong>
        </div>
        <div>
          <span class="text-muted" style="font-size: 0.8rem; display: block;">Experience</span>
          <strong>${job.experience}</strong>
        </div>
        <div>
          <span class="text-muted" style="font-size: 0.8rem; display: block;">Listing Status</span>
          <span class="text-teal" style="font-weight: 700;">Demo Profile</span>
        </div>
      </div>

      <h3 style="margin-bottom: 1rem;">Role Summary</h3>
      <p style="margin-bottom: 1.75rem;">${job.summary}</p>

      <h3 style="margin-bottom: 1rem;">Illustrative Key Responsibilities</h3>
      <ul style="list-style: disc; padding-left: 1.5rem; margin-bottom: 2rem; color: var(--color-body-text);">
        ${job.responsibilities.map(r => `<li style="margin-bottom: 0.5rem;">${r}</li>`).join('')}
      </ul>

      <h3 style="margin-bottom: 1rem;">Required Capabilities & Skills</h3>
      <div class="job-tags" style="margin-bottom: 2rem;">
        ${job.skills.map(s => `<span class="tag-badge" style="font-size: 0.85rem; padding: 0.35rem 0.85rem;">${s}</span>`).join('')}
      </div>

      <h3 style="margin-bottom: 0.75rem;">Educational Qualifications</h3>
      <p style="margin-bottom: 2rem;">${job.education}</p>

      <div id="apply-section" style="border-top: 1px solid var(--color-border); padding-top: 2rem;">
        <h3>Submit Demo Application</h3>
        <p class="text-muted">Register your interest in this sample role. As this is a generic demonstration site, no resume data or contact details will be stored or shared.</p>
        <a href="register-candidate.html" class="btn btn-teal">Proceed to Candidate Registration Form</a>
      </div>
    </div>
  `;

  // Similar demo jobs sidebar / list
  const similarContainer = document.getElementById('similar-jobs-list');
  if (similarContainer) {
    const similar = DEMO_JOBS.filter(j => j.id !== job.id).slice(0, 3);
    similarContainer.innerHTML = similar.map(sj => `
      <div class="card" style="padding: 1.25rem; margin-bottom: 1rem;">
        <h4 style="font-size: 1.05rem; margin-bottom: 0.35rem;"><a href="job-details.html?id=${sj.id}">${sj.title}</a></h4>
        <p class="text-muted" style="font-size: 0.8rem; margin-bottom: 0.5rem;">${sj.industry} • ${sj.experience}</p>
        <a href="job-details.html?id=${sj.id}" class="card-link" style="font-size: 0.85rem;">View Profile &rarr;</a>
      </div>
    `).join('');
  }
}
