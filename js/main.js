// Smooth Intersection Observer for Scroll Animations
document.addEventListener('DOMContentLoaded', () => {
  const animatedItems = document.querySelectorAll('.support-trail-row, .split-product-hero-wrap, .product-info-card, .feature-node-item, .ingredient-ribbon-card, .hex-item-wrap');

  if ('IntersectionObserver' in window) {
    const observerOptions = {
      root: null,
      rootMargin: '0px 0px -50px 0px',
      threshold: 0.15
    };

    const itemObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          // Once visible, keep it visible
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    animatedItems.forEach(item => {
      itemObserver.observe(item);
    });
  } else {
    // Fallback for older browsers
    animatedItems.forEach(item => {
      item.classList.add('is-visible');
    });
  }
});
