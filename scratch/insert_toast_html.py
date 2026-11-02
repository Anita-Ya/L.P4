import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

toast_html = """  <!-- ==============================================
       LIVE SOCIAL PROOF ORDER POPUP (Recent Orders Toast)
       ============================================== -->
  <div class="live-order-toast" id="liveOrderToast" onclick="scrollToOrder(event)">
    <button type="button" class="toast-close-btn" id="closeToastBtn" onclick="dismissLiveToast(event)" aria-label="Close notification">
      <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
      </svg>
    </button>
    <div class="toast-thumb-wrap">
      <img src="assets/real-bottle-clean-hd.png" alt="Mirgi Mukti" class="toast-product-img">
      <span class="toast-live-pulse" title="Live order"></span>
    </div>
    <div class="toast-content-wrap">
      <div class="toast-buyer-row">
        <span class="toast-buyer-name" id="toastBuyerName">पूजा गुप्ता</span>
        <span class="toast-buyer-city" id="toastBuyerCity">(जयपुर)</span>
        <span class="toast-time-badge" id="toastTimeBadge">अभी-अभी</span>
      </div>
      <div class="toast-product-action">
        ने <strong class="toast-brand-name">Mirgi Mukti</strong> का ऑर्डर दिया
      </div>
      <div class="toast-status-row">
        <span class="toast-verified-tag">
          <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="#33C3A5" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
          Verified Order • Cash on Delivery
        </span>
      </div>
    </div>
  </div>
"""

if 'id="liveOrderToast"' not in content:
    # Insert right before </body>
    idx = content.rfind('</body>')
    if idx != -1:
        updated = content[:idx] + toast_html + '\n' + content[idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(updated)
        print("Live toast HTML inserted before </body>!")
    else:
        print("</body> tag not found!")
else:
    print("liveOrderToast already present in index.html")

