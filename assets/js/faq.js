/**
 * STAFFING AGENCY — FAQ Accordion Interactions
 * Vanilla JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
  initFaqAccordion();
});

function initFaqAccordion() {
  const accordionHeaders = document.querySelectorAll('.accordion-header');

  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.closest('.accordion-item');
      const isCurrentlyActive = item.classList.contains('active');

      // Close other accordions in the same group if requested (clean accordion behavior)
      const parentGroup = item.closest('.accordion-group');
      if (parentGroup) {
        const siblings = parentGroup.querySelectorAll('.accordion-item');
        siblings.forEach(sibling => {
          if (sibling !== item) {
            sibling.classList.remove('active');
            const siblingBtn = sibling.querySelector('.accordion-header');
            if (siblingBtn) siblingBtn.setAttribute('aria-expanded', 'false');
          }
        });
      }

      // Toggle current item
      if (isCurrentlyActive) {
        item.classList.remove('active');
        header.setAttribute('aria-expanded', 'false');
      } else {
        item.classList.add('active');
        header.setAttribute('aria-expanded', 'true');
      }
    });

    // Keyboard navigation (Enter / Space already trigger button click natively)
    header.setAttribute('aria-expanded', header.closest('.accordion-item').classList.contains('active') ? 'true' : 'false');
  });
}
