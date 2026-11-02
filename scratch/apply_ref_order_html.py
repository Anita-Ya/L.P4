import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace #orderForm section with exact reference design
order_form_regex = r'<section class="order-form-section" id="orderForm">.*?</section>'

new_order_form_html = """<section class="order-form-section" id="orderForm">
      <div class="order-form-container-box">

        <!-- White Form Card matching reference image -->
        <div class="ref-order-card">

          <!-- Overlapping Top Badge -->
          <div class="ref-rec-badge">
            <span class="badge-star">★</span> Recommended
          </div>

          <form class="ref-order-form" id="actualOrderForm" onsubmit="handleOrderSubmit(event)">

            <!-- Field 1: Full Name -->
            <div class="ref-input-group">
              <label for="userName" class="ref-label">पूरा नाम</label>
              <input type="text" id="userName" name="userName" class="ref-input" placeholder="जैसे: Riya Sharma"
                required autocomplete="name">
              <span class="ref-hint-msg" id="nameHint">कृपया केवल अक्षरों में नाम लिखें</span>
            </div>

            <!-- Field 2: Mobile Number -->
            <div class="ref-input-group">
              <label for="userPhone" class="ref-label">मोबाइल नंबर</label>
              <input type="tel" id="userPhone" name="userPhone" class="ref-input" placeholder="10 अंकों का मोबाइल नंबर"
                pattern="[6-9][0-9]{9}" maxlength="10" inputmode="numeric" required autocomplete="tel">
              <span class="ref-hint-msg" id="phoneHint">10 अंकों का सही मोबाइल नंबर डालें (6-9 से शुरू)</span>
            </div>

            <!-- Submit Button -->
            <button type="submit" class="ref-submit-btn" id="orderSubmitBtn">
              <span>ऑर्डर करें</span>
            </button>

            <!-- Success Alert Message (Shown on submit) -->
            <div class="order-success-msg" id="orderSuccessMsg" style="display: none;">
              <div class="success-icon-box">
                <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#0B3C5D" stroke-width="3"
                  stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
              </div>
              <div class="success-text-box">
                <h4>बधाई हो! आपका Order प्राप्त हो गया है।</h4>
                <p>हमारी सपोर्ट टीम पुष्टि के लिए शीघ्र ही आपसे <strong id="confirmedPhone">+91-XXXXXXXXXX</strong> पर
                  संपर्क करेगी।</p>
              </div>
            </div>

          </form>

        </div>

        <!-- Trust Badges Row Below Card -->
        <div class="order-trust-row ref-trust-row">
          <div class="trust-item">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
            <span>Secure Order</span>
          </div>
          <span class="trust-divider">|</span>
          <div class="trust-item">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="6" width="20" height="12" rx="2"></rect>
              <circle cx="12" cy="12" r="2"></circle>
              <path d="M6 12h.01M18 12h.01"></path>
            </svg>
            <span>Cash on Delivery (यदि उपलब्ध हो)</span>
          </div>
          <span class="trust-divider">|</span>
          <div class="trust-item">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <rect x="1" y="3" width="15" height="13"></rect>
              <polygon points="16 8 20 8 23 11 23 16 16 16 8"></polygon>
              <circle cx="5.5" cy="18.5" r="2.5"></circle>
              <circle cx="18.5" cy="18.5" r="2.5"></circle>
            </svg>
            <span>Pan-India Delivery (यदि उपलब्ध हो)</span>
          </div>
        </div>

      </div>
    </section>"""

html = re.sub(order_form_regex, new_order_form_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with exact reference order form!")

