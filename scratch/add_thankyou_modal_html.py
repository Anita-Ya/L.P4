import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html to add the modal before </body>
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modal_html = """
  <!-- ==============================================
       THANK YOU / ORDER CONFIRMATION MODAL POPUP (Exact Reference Match)
       ============================================== -->
  <div class="thankyou-modal-overlay" id="thankyouModal" style="display: none;" onclick="handleModalOverlayClick(event)">
    <div class="thankyou-modal-card" onclick="event.stopPropagation()">
      
      <!-- Close Button -->
      <button type="button" class="modal-close-btn" onclick="closeThankYouModal()" aria-label="Close">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>

      <!-- Success Checkmark Circle with concentric rings -->
      <div class="thankyou-check-outer">
        <div class="thankyou-check-inner">
          <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#33C3A5" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
        </div>
      </div>

      <!-- Pill Tag -->
      <div class="thankyou-pill-tag">
        <span>Order Confirmed!</span>
      </div>

      <!-- Greeting & Product Line -->
      <h3 class="thankyou-greet-title">बधाई हो, <span class="thankyou-user-name" id="modalUserName">ग्राहक</span>!</h3>
      <p class="thankyou-greet-sub">
        आपके लिए <strong>Mirgi Mukti</strong> का ऑर्डर सफलतापूर्वक स्वीकार कर लिया गया है।
      </p>

      <!-- Order Details Summary Box -->
      <div class="thankyou-details-box">
        <div class="detail-row">
          <span class="detail-label">Order ID:</span>
          <strong class="detail-value order-id-val" id="modalOrderId">MM-758921</strong>
        </div>
        <div class="detail-divider"></div>
        <div class="detail-row">
          <span class="detail-label">Mobile:</span>
          <strong class="detail-value phone-val" id="modalUserPhone">+91 9675658678</strong>
        </div>
        <div class="detail-divider"></div>
        <div class="detail-row">
          <span class="detail-label">Delivery:</span>
          <strong class="detail-value delivery-val">FREE Express Delivery</strong>
        </div>
      </div>

      <!-- Expert Callout Note -->
      <p class="thankyou-callout-note">
        हमारे विशेषज्ञ जल्द ही डिलीवरी कन्फर्मेशन के लिए आपसे संपर्क करेंगे।
      </p>

      <!-- Action Button -->
      <button type="button" class="thankyou-confirm-btn" onclick="closeThankYouModal()">
        <span>धन्यवाद, ठीक है</span>
      </button>

    </div>
  </div>
"""

# Insert modal before </main> or </body>
if '<div class="thankyou-modal-overlay"' not in html:
    html = html.replace('</body>', modal_html + '\n</body>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added Thank You modal to index.html!")
else:
    print("Modal already present in index.html.")

