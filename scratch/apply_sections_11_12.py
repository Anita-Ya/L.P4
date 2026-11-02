# Script to inject Section 11 & Section 12 into index.html and update style.css
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the HTML snippet for Section 11 & Section 12
sections_html = """
    <!-- ==============================================
         SECTION 11: ORDER FORM (अपना Mirgi Mukti Order करें)
         ============================================== -->
    <section class="order-form-section" id="orderForm">
      <div class="order-form-card">
        
        <!-- Form Header Badge & Title -->
        <div class="order-card-header">
          <div class="order-deal-pill">
            <span class="pill-badge-pulse"></span>
            <span>⚡ स्पेशल 10% डिस्काउंट ऑफर सक्रिय</span>
          </div>
          <h2 class="order-form-title">अपना Mirgi Mukti Order करें</h2>
          <p class="order-form-subtitle">सीधे निर्माता से प्राप्त करें 100% प्रामाणिक हर्बल फॉर्मूलेशन</p>
        </div>

        <!-- Product Preview Strip -->
        <div class="order-product-strip">
          <div class="strip-img-wrap">
            <img src="assets/real-bottle-clean-hd.png" alt="Mirgi Mukti Bottle" class="strip-product-img">
          </div>
          <div class="strip-details">
            <div class="strip-title-row">
              <span class="strip-name">Mirgi Mukti</span>
              <span class="strip-capsules">(30 Capsules)</span>
            </div>
            <span class="strip-herbs">Giloy • Tulsi • Baheda • Ashwagandha</span>
            <div class="strip-price-row">
              <span class="strip-tag">10% OFF APPLIED</span>
              <span class="strip-badge-cod">Cash on Delivery</span>
            </div>
          </div>
        </div>

        <!-- The Order Form -->
        <form class="order-actual-form" id="actualOrderForm" onsubmit="handleOrderSubmit(event)">
          
          <!-- Field 1: Name -->
          <div class="form-group">
            <label for="userName" class="form-label">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
              <span>आपका नाम</span>
              <span class="required-star">*</span>
            </label>
            <div class="input-wrapper">
              <input 
                type="text" 
                id="userName" 
                name="userName" 
                class="form-control" 
                placeholder="अपना नाम दर्ज करें" 
                required 
                autocomplete="name"
              >
            </div>
          </div>

          <!-- Field 2: Mobile Number -->
          <div class="form-group">
            <label for="userPhone" class="form-label">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
              </svg>
              <span>मोबाइल नंबर</span>
              <span class="required-star">*</span>
            </label>
            <div class="input-wrapper phone-input-wrapper">
              <span class="phone-country-code">+91</span>
              <input 
                type="tel" 
                id="userPhone" 
                name="userPhone" 
                class="form-control phone-input" 
                placeholder="10 Digit Mobile Number" 
                pattern="[0-9]{10}"
                maxlength="10" 
                inputmode="numeric"
                required 
                autocomplete="tel"
              >
            </div>
          </div>

          <!-- CTA Button -->
          <button type="submit" class="order-submit-btn" id="orderSubmitBtn">
            <span class="btn-shine"></span>
            <span class="btn-text">मेरा Order Confirm करें</span>
            <svg class="btn-check-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </button>

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

        <!-- Trust Badges Row -->
        <div class="order-trust-row">
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
    </section>

    <!-- ==============================================
         SECTION 12: DISCLAIMER & FOOTER
         ============================================== -->
    <footer class="site-footer" id="disclaimerSection">
      <div class="disclaimer-card">
        
        <div class="disclaimer-header">
          <div class="disclaimer-badge">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="8" x2="12" y2="12"></line>
              <line x1="12" y1="16" x2="12.01" y2="16"></line>
            </svg>
            <span>DISCLAIMER (अस्वीकरण)</span>
          </div>
        </div>

        <div class="disclaimer-content">
          <p class="disclaimer-para">
            यह उत्पाद मिर्गी या किसी अन्य neurological condition के निदान, उपचार, रोकथाम या इलाज के लिए प्रमाणित विकल्प नहीं है। मिर्गी के लिए qualified healthcare professional से परामर्श लें और prescribed anti-seizure medicines को स्वयं बंद या परिवर्तित न करें। Herbal ingredients भी side effects और drug interactions पैदा कर सकते हैं। Product की suitability के लिए डॉक्टर से सलाह लें।
          </p>
          <p class="disclaimer-para legal-para">
            Product claims और advertising सामग्री को लागू AYUSH, FSSAI (जहां लागू हो), Drugs and Cosmetics तथा advertising regulations के अनुसार सत्यापित करें।
          </p>
        </div>

        <div class="footer-bottom-line">
          <p class="copyright-text">© 2026 Mirgi Mukti. सर्वाधिकार सुरक्षित (All Rights Reserved).</p>
          <div class="footer-links">
            <span class="footer-link">Privacy Policy</span>
            <span class="footer-dot">•</span>
            <span class="footer-link">Terms of Use</span>
            <span class="footer-dot">•</span>
            <span class="footer-link">AYUSH Compliance</span>
          </div>
        </div>

      </div>
    </footer>
"""

# Insert before </main>
if '</main>' in html:
    html = html.replace('</main>', sections_html + '\n  </main>')
    # Update cachebuster in link
    html = html.replace('style.css?v=faq_section_v1', 'style.css?v=final_launch_v1')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated index.html with Section 11 & Section 12!")
else:
    print("ERROR: </main> not found in index.html")

