import sys
sys.stdout.reconfigure(encoding='utf-8')

js_code = """// Smooth Intersection Observer for Scroll Animations
document.addEventListener('DOMContentLoaded', () => {
  const animatedItems = document.querySelectorAll(
    '.support-trail-row, .split-product-hero-wrap, .product-info-card, .feature-node-item, .ingredient-ribbon-card, .hex-item-wrap, .ref-order-card, .disclaimer-card'
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
      // Remove any numbers or special punctuation
      const cleanVal = e.target.value.replace(/[0-9!@#$%^&*()_+=\\[\\]{};':"\\\\|,.<>\\/?]/g, '');
      if (cleanVal !== e.target.value) {
        e.target.value = cleanVal;
        if (nameHint) nameHint.style.color = '#B3261E';
      }
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
          phoneHint.style.color = '#B3261E';
          phoneHint.style.fontWeight = '700';
        }
      } else {
        if (phoneHint) {
          phoneHint.style.color = '#8C2D2D';
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
  const successMsg = document.getElementById('orderSuccessMsg');
  const confirmedPhone = document.getElementById('confirmedPhone');
  const nameHint = document.getElementById('nameHint');
  const phoneHint = document.getElementById('phoneHint');

  const name = nameInput ? nameInput.value.trim() : '';
  const phone = phoneInput ? phoneInput.value.trim() : '';

  if (!name || name.length < 2) {
    if (nameHint) {
      nameHint.style.color = '#B3261E';
      nameHint.style.fontWeight = '700';
    }
    if (nameInput) {
      nameInput.style.borderColor = '#B3261E';
      nameInput.focus();
    }
    return false;
  }

  if (!phone || phone.length !== 10 || !['6', '7', '8', '9'].includes(phone[0])) {
    if (phoneHint) {
      phoneHint.style.color = '#B3261E';
      phoneHint.style.fontWeight = '700';
    }
    if (phoneInput) {
      phoneInput.style.borderColor = '#B3261E';
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
      submitBtn.innerHTML = `<span>✓ Order Confirmed!</span>`;
      submitBtn.style.background = '#28a745';
      submitBtn.style.color = '#FFFFFF';
    }
  }, 600);

  return false;
}
"""

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Updated js/main.js with complete reference form validation!")

