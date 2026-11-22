/**
 * STAFFING AGENCY — Form Validation & Demo Handlers
 * Vanilla JavaScript (Zero Backend, Frontend Simulation Only)
 */

document.addEventListener('DOMContentLoaded', () => {
  initEmployerRequestForm();
  initCandidateRegistrationForm();
  initContactForm();
  initModalCloseHandlers();
});

// Helper: Show standard Demo Confirmation Modal
function showDemoModal(title, message) {
  let modalOverlay = document.getElementById('demo-modal-overlay');
  if (!modalOverlay) {
    modalOverlay = document.createElement('div');
    modalOverlay.id = 'demo-modal-overlay';
    modalOverlay.className = 'demo-modal-overlay';
    modalOverlay.innerHTML = `
      <div class="demo-modal" role="dialog" aria-modal="true">
        <svg class="modal-icon-success" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"></circle>
          <polyline points="9 12 11 14 15 10"></polyline>
        </svg>
        <h3 id="modal-title" style="margin-bottom: 0.5rem; font-size: 1.4rem;">Demo Submission Successful</h3>
        <p id="modal-message" class="text-muted" style="margin-bottom: 1.5rem; line-height: 1.6;"></p>
        <div style="background: #F8FAFC; border: 1px solid var(--color-border); padding: 0.75rem; border-radius: var(--radius-sm); font-size: 0.8rem; color: #64748B; margin-bottom: 1.5rem;">
          <strong>Demo Notice:</strong> This website operates in demonstration mode. No user data, contact details, or resumes are sent over the network or saved to any database.
        </div>
        <button type="button" class="btn btn-primary" id="modal-close-btn" style="min-width: 140px;">Close Window</button>
      </div>
    `;
    document.body.appendChild(modalOverlay);

    const closeBtn = modalOverlay.querySelector('#modal-close-btn');
    closeBtn.addEventListener('click', () => {
      modalOverlay.classList.remove('active');
    });

    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) {
        modalOverlay.classList.remove('active');
      }
    });
  }

  document.getElementById('modal-title').textContent = title;
  document.getElementById('modal-message').textContent = message;
  modalOverlay.classList.add('active');
}

function initModalCloseHandlers() {
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const modal = document.getElementById('demo-modal-overlay');
      if (modal && modal.classList.contains('active')) {
        modal.classList.remove('active');
      }
    }
  });
}

// 1. Employer Request Staff Form
function initEmployerRequestForm() {
  const form = document.getElementById('employer-request-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    let isValid = true;
    const requiredFields = [
      'emp-name', 'emp-email', 'emp-company', 'emp-phone', 
      'emp-industry', 'emp-role', 'emp-count', 'emp-staffing-type', 'emp-location'
    ];

    requiredFields.forEach(id => {
      const field = document.getElementById(id);
      if (field) {
        if (!field.value.trim()) {
          field.classList.add('is-invalid');
          isValid = false;
        } else {
          field.classList.remove('is-invalid');
        }
      }
    });

    // Email check
    const emailField = document.getElementById('emp-email');
    if (emailField && emailField.value.trim()) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailField.value.trim())) {
        emailField.classList.add('is-invalid');
        isValid = false;
      }
    }

    if (!isValid) {
      const firstInvalid = form.querySelector('.is-invalid');
      if (firstInvalid) firstInvalid.focus();
      return;
    }

    // Success response
    form.reset();
    showDemoModal(
      "Staffing Request Received",
      "Demo staffing request submitted. No information has been transmitted or stored."
    );
  });
}

// 2. Candidate Registration Form & Resume Upload Handler
function initCandidateRegistrationForm() {
  const form = document.getElementById('candidate-registration-form');
  const fileInput = document.getElementById('cand-resume');
  const filePreview = document.getElementById('file-preview-zone');
  const fileNameDisplay = document.getElementById('file-name-display');
  const fileSizeDisplay = document.getElementById('file-size-display');
  const removeFileBtn = document.getElementById('remove-file-btn');
  const fileFeedback = document.getElementById('file-upload-feedback');

  if (fileInput && filePreview) {
    const allowedExtensions = ['pdf', 'doc', 'docx'];
    const maxSizeBytes = 5 * 1024 * 1024; // 5 MB

    fileInput.addEventListener('change', () => {
      if (!fileInput.files || fileInput.files.length === 0) {
        filePreview.style.display = 'none';
        return;
      }

      const file = fileInput.files[0];
      const extension = file.name.split('.').pop().toLowerCase();

      if (!allowedExtensions.includes(extension)) {
        if (fileFeedback) {
          fileFeedback.textContent = "Please select a valid PDF, DOC, or DOCX document.";
          fileFeedback.style.display = 'block';
        }
        fileInput.value = '';
        filePreview.style.display = 'none';
        return;
      }

      if (file.size > maxSizeBytes) {
        if (fileFeedback) {
          fileFeedback.textContent = "File size exceeds 5MB limit. Please choose a smaller file.";
          fileFeedback.style.display = 'block';
        }
        fileInput.value = '';
        filePreview.style.display = 'none';
        return;
      }

      // Valid file selected
      if (fileFeedback) fileFeedback.style.display = 'none';
      if (fileNameDisplay) fileNameDisplay.textContent = file.name;
      if (fileSizeDisplay) {
        const sizeFormatted = (file.size / (1024 * 1024)).toFixed(2) + ' MB';
        fileSizeDisplay.textContent = sizeFormatted;
      }
      filePreview.style.display = 'flex';
    });

    if (removeFileBtn) {
      removeFileBtn.addEventListener('click', (e) => {
        e.preventDefault();
        fileInput.value = '';
        filePreview.style.display = 'none';
        if (fileFeedback) fileFeedback.style.display = 'none';
      });
    }
  }

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      let isValid = true;
      const requiredFields = [
        'cand-name', 'cand-email', 'cand-phone', 'cand-location',
        'cand-role', 'cand-industry', 'cand-experience', 'cand-type', 'cand-status'
      ];

      requiredFields.forEach(id => {
        const field = document.getElementById(id);
        if (field) {
          if (!field.value.trim()) {
            field.classList.add('is-invalid');
            isValid = false;
          } else {
            field.classList.remove('is-invalid');
          }
        }
      });

      // Email check
      const emailField = document.getElementById('cand-email');
      if (emailField && emailField.value.trim()) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(emailField.value.trim())) {
          emailField.classList.add('is-invalid');
          isValid = false;
        }
      }

      if (!isValid) {
        const firstInvalid = form.querySelector('.is-invalid');
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      form.reset();
      if (filePreview) filePreview.style.display = 'none';
      showDemoModal(
        "Candidate Registration Received",
        "Demo candidate registration submitted. No resume or personal information has been transmitted or stored."
      );
    });
  }
}

// 3. Contact Form
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    let isValid = true;
    const requiredFields = ['contact-name', 'contact-email', 'contact-phone', 'contact-type', 'contact-message'];

    requiredFields.forEach(id => {
      const field = document.getElementById(id);
      if (field) {
        if (!field.value.trim()) {
          field.classList.add('is-invalid');
          isValid = false;
        } else {
          field.classList.remove('is-invalid');
        }
      }
    });

    const emailField = document.getElementById('contact-email');
    if (emailField && emailField.value.trim()) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailField.value.trim())) {
        emailField.classList.add('is-invalid');
        isValid = false;
      }
    }

    if (!isValid) {
      const firstInvalid = form.querySelector('.is-invalid');
      if (firstInvalid) firstInvalid.focus();
      return;
    }

    form.reset();
    showDemoModal(
      "Enquiry Received",
      "Demo enquiry submitted successfully. No information has been transmitted or stored."
    );
  });
}
