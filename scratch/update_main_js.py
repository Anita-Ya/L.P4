import sys
sys.stdout.reconfigure(encoding='utf-8')

js_code = """// Smooth Intersection Observer for Scroll Animations
document.addEventListener('DOMContentLoaded', () => {
  const animatedItems = document.querySelectorAll(
    '.support-trail-row, .split-product-hero-wrap, .product-info-card, .feature-node-item, .ingredient-ribbon-card, .hex-item-wrap, .order-form-card, .disclaimer-card'
  );

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

  // Mobile number input enforcement (digits only, max 10)
  const phoneInput = document.getElementById('userPhone');
  if (phoneInput) {
    phoneInput.addEventListener('input', (e) => {
      e.target.value = e.target.value.replace(/[^0-9]/g, '').slice(0, 10);
    });
  }
});

// Order Form Submission Handler
function handleOrderSubmit(event) {
  event.preventDefault();
  
  const nameInput = document.getElementById('userName');
  const phoneInput = document.getElementById('userPhone');
  const submitBtn = document.getElementById('orderSubmitBtn');
  const successMsg = document.getElementById('orderSuccessMsg');
  const confirmedPhone = document.getElementById('confirmedPhone');

  const name = nameInput ? nameInput.value.trim() : '';
  const phone = phoneInput ? phoneInput.value.trim() : '';

  if (!name) {
    alert('कृपया अपना नाम दर्ज करें');
    if (nameInput) nameInput.focus();
    return false;
  }

  if (!phone || phone.length !== 10) {
    alert('कृपया 10 अंकों का सही मोबाइल नंबर दर्ज करें');
    if (phoneInput) phoneInput.focus();
    return false;
  }

  // Button state update
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.style.opacity = '0.75';
    submitBtn.innerHTML = `
      <span class="btn-text">Order कन्फर्म हो रहा है...</span>
    `;
  }

  // Simulate fast confirmation
  setTimeout(() => {
    if (confirmedPhone) {
      confirmedPhone.textContent = `+91-${phone}`;
    }
    if (successMsg) {
      successMsg.style.display = 'flex';
      successMsg.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    if (submitBtn) {
      submitBtn.innerHTML = `
        <span class="btn-text">✓ Order Confirmed!</span>
      `;
      submitBtn.style.background = '#28a745';
    }
  }, 600);

  return false;
}
"""

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Successfully updated js/main.js!")

