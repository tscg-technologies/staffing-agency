/**
 * STAFFING AGENCY — Main App Initialization
 * Vanilla JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
  // Console welcome note
  console.info('STAFFING AGENCY: Corporate Demonstration Website initialized.');
  console.info('Status: Pure static frontend mode. Forms operate in local simulation.');

  // Initialize interactive demo tabs if any exist
  const tabBtns = document.querySelectorAll('[data-tab-target]');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab-target');
      const container = btn.closest('.tabs-wrapper') || document;
      
      container.querySelectorAll('[data-tab-target]').forEach(b => b.classList.remove('active'));
      container.querySelectorAll('.tab-content-panel').forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPanel = container.querySelector(targetId);
      if (targetPanel) targetPanel.classList.add('active');
    });
  });
});
