import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Let's draft the new Section 11 HTML
new_order_html = """    <!-- ==============================================
         SECTION 11: ORDER FORM (EXACT SCREENSHOT REFERENCE)
         ============================================== -->
    <section class="order-form-section" id="orderForm">
      <div class="ayur-order-card">

        <!-- 1. Header Title -->
        <h2 class="ayur-order-title">Order Your Product</h2>

        <!-- 2. Product Thumbnail Box -->
        <div class="ayur-product-thumb-wrap">
          <div class="ayur-thumb-box">
            <img src="assets/real-bottle-clean-hd.png" alt="Mirgi Mukti" class="ayur-thumb-img">
          </div>
          <h3 class="ayur-product-brand">Mirgi Mukti</h3>
        </div>

        <!-- 3. Leaf Divider Line -->
        <div class="ayur-leaf-divider">
          <span class="leaf-line left"></span>
          <span class="leaf-icon-wrap">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
              <path d="M17 8C8 10 5.9 16.17 3.82 21.34L5.71 22l1-2.3A4.49 4.49 0 0 0 8 20C19 20 22 3 22 3c-1 2-8 2-11 5 4-2 11-1 11-1s-.3 3.5-3 5.5"/>
            </svg>
          </span>
          <span class="leaf-line right"></span>
        </div>

        <!-- 4. The Form -->
        <form class="ayur-actual-form" id="actualOrderForm" onsubmit="handleOrderSubmit(event)">

          <!-- Field 1: Name -->
          <div class="ayur-field-group">
            <label for="userName" class="ayur-label">माता-पिता / अभिभावक का नाम</label>
            <div class="ayur-input-box">
              <span class="ayur-input-icon">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </span>
              <input 
                type="text" 
                id="userName" 
                name="userName" 
                class="ayur-input" 
                placeholder="Enter Your Name" 
                required 
                autocomplete="name"
              >
            </div>
            <span class="ayur-hint-error" id="nameHint">कृपया अपना नाम दर्ज करें</span>
          </div>

          <!-- Field 2: Mobile Number -->
          <div class="ayur-field-group">
            <label for="userPhone" class="ayur-label">मोबाइल नंबर</label>
            <div class="ayur-input-box phone-box">
              <span class="ayur-input-icon phone-icon">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
              </span>
              <input 
                type="tel" 
                id="userPhone" 
                name="userPhone" 
                class="ayur-input" 
                placeholder="10 अंकों का मोबाइल नंबर" 
                pattern="[6-9][0-9]{9}" 
                maxlength="10" 
                inputmode="numeric" 
                required 
                autocomplete="tel"
              >
            </div>
            <span class="ayur-hint-error" id="phoneHint">कृपया 6-9 से शुरू होने वाला 10 अंकों का मान्य मोबाइल नंबर दर्ज करें</span>
          </div>

          <!-- Submit Button (Place My Order) -->
          <button type="submit" class="ayur-submit-btn" id="orderSubmitBtn">
            <span class="btn-cart-icon">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="9" cy="21" r="1"></circle>
                <circle cx="20" cy="21" r="1"></circle>
                <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
              </svg>
            </span>
            <span class="btn-label-text">Place My Order</span>
            <span class="btn-arrow-icon">➔</span>
          </button>

          <!-- Support Guarantee Callout -->
          <div class="ayur-support-callout">
            <span class="callout-check-circle">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </span>
            <span class="callout-text">हमारी team order confirmation और delivery details के लिए आपसे संपर्क करेगी।</span>
          </div>

          <!-- Success Alert Message (Shown on submit) -->
          <div class="order-success-msg" id="orderSuccessMsg" style="display: none;">
            <div class="success-icon-box">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#33C3A5" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
            <div class="success-text-box">
              <h4>बधाई हो! आपका Order प्राप्त हो गया है।</h4>
              <p>हमारी सपोर्ट टीम पुष्टि के लिए शीघ्र ही आपसे <strong id="confirmedPhone">+91-XXXXXXXXXX</strong> पर संपर्क करेगी।</p>
            </div>
          </div>

        </form>

        <!-- Trust Badges Row Below -->
        <div class="order-trust-row ayur-trust-row">
          <div class="trust-item">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
            <span>Secure Order</span>
          </div>
          <span class="trust-divider">|</span>
          <div class="trust-item">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="6" width="20" height="12" rx="2"></rect>
              <circle cx="12" cy="12" r="2"></circle>
              <path d="M6 12h.01M18 12h.01"></path>
            </svg>
            <span>Cash on Delivery (यदि उपलब्ध हो)</span>
          </div>
          <span class="trust-divider">|</span>
          <div class="trust-item">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="1" y="3" width="15" height="13"></rect>
              <polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon>
              <circle cx="5.5" cy="18.5" r="2.5"></circle>
              <circle cx="18.5" cy="18.5" r="2.5"></circle>
            </svg>
            <span>Pan-India Delivery (यदि उपलब्ध हो)</span>
          </div>
        </div>

      </div>
    </section>"""

# Replace in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

order_form_regex = r'<section class="order-form-section" id="orderForm">.*?</section>'
html = re.sub(order_form_regex, new_order_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with exact screenshot structure!")

