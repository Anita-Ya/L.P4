// Smooth Intersection Observer for Scroll Animations
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
  const nameBox = document.getElementById('nameBox');
  const nameHint = document.getElementById('nameHint');
  if (nameInput) {
    nameInput.addEventListener('input', (e) => {
      const cleanVal = e.target.value.replace(/[0-9!@#$%^&*()_+=\[\]{};':"\\|,.<>\/?]/g, '');
      if (cleanVal !== e.target.value) {
        e.target.value = cleanVal;
      }
      if (e.target.value.trim().length >= 2) {
        if (nameBox) nameBox.classList.remove('has-error');
        if (nameHint) nameHint.classList.remove('is-visible');
      }
    });

    nameInput.addEventListener('blur', () => {
      const val = nameInput.value.trim();
      if (val.length > 0 && val.length < 2) {
        if (nameBox) nameBox.classList.add('has-error');
        if (nameHint) {
          nameHint.textContent = 'कृपया अपना पूरा नाम दर्ज करें';
          nameHint.classList.add('is-visible');
        }
      }
    });
  }

  // Mobile number input enforcement (digits only, max 10)
  const phoneInput = document.getElementById('userPhone');
  const phoneBox = document.getElementById('phoneBox');
  const phoneHint = document.getElementById('phoneHint');
  if (phoneInput) {
    phoneInput.addEventListener('input', (e) => {
      e.target.value = e.target.value.replace(/[^0-9]/g, '').slice(0, 10);
      const val = e.target.value;
      if (val.length > 0) {
        if (!['6', '7', '8', '9'].includes(val[0])) {
          if (phoneBox) phoneBox.classList.add('has-error');
          if (phoneHint) {
            phoneHint.textContent = 'मोबाइल नंबर 6, 7, 8 या 9 से शुरू होना चाहिए';
            phoneHint.classList.add('is-visible');
          }
        } else {
          if (phoneBox) phoneBox.classList.remove('has-error');
          if (phoneHint) phoneHint.classList.remove('is-visible');
        }
      } else {
        if (phoneBox) phoneBox.classList.remove('has-error');
        if (phoneHint) phoneHint.classList.remove('is-visible');
      }
    });

    phoneInput.addEventListener('blur', () => {
      const val = phoneInput.value.trim();
      if (val.length > 0 && (val.length !== 10 || !['6', '7', '8', '9'].includes(val[0]))) {
        if (phoneBox) phoneBox.classList.add('has-error');
        if (phoneHint) {
          phoneHint.textContent = 'कृपया 10 अंकों का मान्य मोबाइल नंबर दर्ज करें (6-9 से शुरू)';
          phoneHint.classList.add('is-visible');
        }
      }
    });
  }

  // Initialize Live Order Social Proof Toast
  initLiveOrderToast();
});

// ==============================================
// LIVE SOCIAL PROOF ORDER POPUP (Recent Orders Toast)
// ==============================================
const recentOrdersData = [
  { name: "पूजा गुप्ता", city: "(जयपुर)", time: "अभी-अभी" },
  { name: "राजेश शर्मा", city: "(इंदौर)", time: "1 मिनट पहले" },
  { name: "अमित वर्मा", city: "(लखनऊ)", time: "2 मिनट पहले" },
  { name: "सुनीता पटेल", city: "(अहमदाबाद)", time: "अभी-अभी" },
  { name: "राहुल यादव", city: "(वाराणसी)", time: "1 मिनट पहले" },
  { name: "मनोज सिंह", city: "(पटना)", time: "3 मिनट पहले" },
  { name: "रेखा देवी", city: "(कानपुर)", time: "अभी-अभी" },
  { name: "विक्रम जोशी", city: "(पुणे)", time: "2 मिनट पहले" },
  { name: "कविता यादव", city: "(दिल्ली)", time: "अभी-अभी" },
  { name: "सुरेश कुमार", city: "(भोपाल)", time: "4 मिनट पहले" }
];

let liveToastIndex = 0;
let liveToastTimer = null;
let isToastPaused = false;

function initLiveOrderToast() {
  const toast = document.getElementById('liveOrderToast');
  if (!toast) return;

  // First popup shows after 3.5 seconds
  setTimeout(() => {
    cycleLiveToast();
  }, 3500);
}

function cycleLiveToast() {
  if (isToastPaused) return;

  const toast = document.getElementById('liveOrderToast');
  const modal = document.getElementById('thankyouModal');

  // Do not show if thankyou modal is currently open
  if (!toast || (modal && modal.style.display === 'flex')) {
    liveToastTimer = setTimeout(cycleLiveToast, 6000);
    return;
  }

  const order = recentOrdersData[liveToastIndex % recentOrdersData.length];
  liveToastIndex++;

  const nameEl = document.getElementById('toastBuyerName');
  const cityEl = document.getElementById('toastBuyerCity');
  const timeEl = document.getElementById('toastTimeBadge');

  if (nameEl) nameEl.textContent = order.name;
  if (cityEl) cityEl.textContent = order.city;
  if (timeEl) timeEl.textContent = order.time;

  // Show Toast
  toast.classList.add('is-active');

  // Hide after 4.5 seconds
  liveToastTimer = setTimeout(() => {
    toast.classList.remove('is-active');

    // Wait 6.5 seconds before next popup
    liveToastTimer = setTimeout(cycleLiveToast, 6500);
  }, 4500);
}

// Dismiss Toast when user clicks the '×' button
function dismissLiveToast(event) {
  if (event) event.stopPropagation();

  const toast = document.getElementById('liveOrderToast');
  if (toast) {
    toast.classList.remove('is-active');
  }

  // Pause notifications for 40 seconds on user manual dismissal
  isToastPaused = true;
  clearTimeout(liveToastTimer);
  setTimeout(() => {
    isToastPaused = false;
    cycleLiveToast();
  }, 40000);
}

// Click on toast to scroll smoothly to order form
function scrollToOrder(event) {
  if (event) event.preventDefault();

  const orderSection = document.getElementById('order') || document.querySelector('.ayur-order-card');
  if (orderSection) {
    orderSection.scrollIntoView({ behavior: 'smooth', block: 'center' });
    const nameInput = document.getElementById('userName');
    if (nameInput) {
      setTimeout(() => nameInput.focus(), 600);
    }
  }
}

// ==============================================
// Order Form Submission Handler
// ==============================================
function handleOrderSubmit(event) {
  event.preventDefault();
  
  const nameInput = document.getElementById('userName');
  const phoneInput = document.getElementById('userPhone');
  const nameBox = document.getElementById('nameBox') || (nameInput ? nameInput.closest('.ayur-input-box') : null);
  const phoneBox = document.getElementById('phoneBox') || (phoneInput ? phoneInput.closest('.ayur-input-box') : null);
  const submitBtn = document.getElementById('orderSubmitBtn');
  const nameHint = document.getElementById('nameHint');
  const phoneHint = document.getElementById('phoneHint');

  const name = nameInput ? nameInput.value.trim() : '';
  const phone = phoneInput ? phoneInput.value.trim() : '';

  let hasError = false;

  // Validate Name
  if (!name || name.length < 2) {
    if (nameBox) nameBox.classList.add('has-error');
    if (nameHint) {
      nameHint.textContent = 'कृपया अपना नाम दर्ज करें';
      nameHint.classList.add('is-visible');
    }
    hasError = true;
  } else {
    if (nameBox) nameBox.classList.remove('has-error');
    if (nameHint) nameHint.classList.remove('is-visible');
  }

  // Validate Phone
  if (!phone || phone.length !== 10 || !['6', '7', '8', '9'].includes(phone[0])) {
    if (phoneBox) phoneBox.classList.add('has-error');
    if (phoneHint) {
      phoneHint.textContent = 'कृपया 6-9 से शुरू होने वाला 10 अंकों का मान्य मोबाइल नंबर दर्ज करें';
      phoneHint.classList.add('is-visible');
    }
    if (!hasError && phoneInput) {
      phoneInput.focus();
    }
    hasError = true;
  } else {
    if (phoneBox) phoneBox.classList.remove('has-error');
    if (phoneHint) phoneHint.classList.remove('is-visible');
  }

  if (hasError) {
    if (!name || name.length < 2) {
      if (nameInput) nameInput.focus();
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
