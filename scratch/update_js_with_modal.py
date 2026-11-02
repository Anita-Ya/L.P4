import sys
sys.stdout.reconfigure(encoding='utf-8')

js_code = """// Smooth Intersection Observer for Scroll Animations
document.addEventListener('DOMContentLoaded', () => {
  const animatedItems = document.querySelectorAll(
    '.support-trail-row, .split-product-hero-wrap, .product-info-card, .feature-node-item, .ingredient-ribbon-card, .hex-item-wrap, .ayur-order-card, .disclaimer-card'
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
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    animatedItems.forEach(item => {
      itemObserver.observe(item);
    });
  } else {
    animatedItems.forEach(item => {
      item.classList.add('is-visible');
    });
  }

  // Name input enforcement (allow letters, spaces, devanagari)
  const nameInput = document.getElementById('userName');
  const nameHint = document.getElementById('nameHint');
  if (nameInput) {
    nameInput.addEventListener('input', (e) => {
      const cleanVal = e.target.value.replace(/[0-9!@#$%^&*()_+=\\[\\]{};':"\\\\|,.<>\\/?]/g, '');
      if (cleanVal !== e.target.value) {
        e.target.value = cleanVal;
      }
      if (nameHint) {
        nameHint.style.color = '#7B8F9E';
      }
      nameInput.style.borderColor = '#C0392B';
    });
  }

  // Mobile number input enforcement (digits only, max 10)
  const phoneInput = document.getElementById('userPhone');
  const phoneHint = document.getElementById('phoneHint');
  if (phoneInput) {
    phoneInput.addEventListener('input', (e) => {
      e.target.value = e.target.value.replace(/[^0-9]/g, '').slice(0, 10);
      if (e.target.value.length > 0 && !['6', '7', '8', '9'].includes(e.target.value[0])) {
        if (phoneHint) {
          phoneHint.style.color = '#C0392B';
          phoneHint.style.fontWeight = '700';
        }
      } else {
        if (phoneHint) {
          phoneHint.style.color = '#7B8F9E';
          phoneHint.style.fontWeight = '500';
        }
      }
    });
  }
});

// Order Form Submission Handler
function handleOrderSubmit(event) {
  event.preventDefault();
  
  const nameInput = document.getElementById('userName');
  const phoneInput = document.getElementById('userPhone');
  const submitBtn = document.getElementById('orderSubmitBtn');
  const nameHint = document.getElementById('nameHint');
  const phoneHint = document.getElementById('phoneHint');

  const name = nameInput ? nameInput.value.trim() : '';
  const phone = phoneInput ? phoneInput.value.trim() : '';

  if (!name || name.length < 2) {
    if (nameHint) {
      nameHint.style.color = '#C0392B';
      nameHint.style.fontWeight = '700';
    }
    if (nameInput) {
      nameInput.focus();
    }
    return false;
  }

  if (!phone || phone.length !== 10 || !['6', '7', '8', '9'].includes(phone[0])) {
    if (phoneHint) {
      phoneHint.style.color = '#C0392B';
      phoneHint.style.fontWeight = '700';
    }
    if (phoneInput) {
      phoneInput.focus();
    }
    return false;
  }

  // Button state update
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.style.opacity = '0.85';
    submitBtn.innerHTML = `<span>ऑर्डर दर्ज हो रहा है...</span>`;
  }

  // Generate unique Order ID
  const randomId = 'MM-' + Math.floor(100000 + Math.random() * 900000);

  // Store in sessionStorage
  try {
    sessionStorage.setItem('orderName', name);
    sessionStorage.setItem('orderPhone', phone);
    sessionStorage.setItem('orderId', randomId);
  } catch (e) {}

  // Open Thank You Modal with fast smooth delay
  setTimeout(() => {
    const modal = document.getElementById('thankyouModal');
    const modalName = document.getElementById('modalUserName');
    const modalPhone = document.getElementById('modalUserPhone');
    const modalOrderId = document.getElementById('modalOrderId');

    if (modalName) modalName.textContent = name;
    if (modalPhone) modalPhone.textContent = `+91 ${phone}`;
    if (modalOrderId) modalOrderId.textContent = randomId;

    if (modal) {
      modal.style.display = 'flex';
      document.body.style.overflow = 'hidden';
    }

    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.style.opacity = '1';
      submitBtn.innerHTML = `
        <span class="btn-cart-icon">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="9" cy="21" r="1"></circle>
            <circle cx="20" cy="21" r="1"></circle>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
          </svg>
        </span>
        <span class="btn-label-text">Place My Order</span>
        <span class="btn-arrow-icon">➔</span>
      `;
    }
  }, 450);

  return false;
}

// Close Thank You Modal
function closeThankYouModal() {
  const modal = document.getElementById('thankyouModal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

// Close modal when clicking dark backdrop
function handleModalOverlayClick(event) {
  if (event.target.id === 'thankyouModal') {
    closeThankYouModal();
  }
}
"""

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Updated js/main.js with complete Thank You modal workflow!")

