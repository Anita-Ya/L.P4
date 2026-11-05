import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = None
end_idx = None
for i, l in enumerate(lines):
    if '<!-- Trust Badges Row Below -->' in l:
        start_idx = i
    if start_idx is not None and '</div>' in l and i > start_idx + 20:
        end_idx = i + 1
        break

print(f"Replacing lines {start_idx+1} to {end_idx} in index.html")
new_trust_block = """        <!-- Trust Badges Row Below -->
        <div class="ayur-trust-row">
          <div class="ayur-trust-item">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
            <span>100% Secure Order</span>
          </div>
          <span class="ayur-trust-sep">•</span>
          <div class="ayur-trust-item">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="6" width="20" height="12" rx="2"></rect>
              <circle cx="12" cy="12" r="2"></circle>
              <path d="M6 12h.01M18 12h.01"></path>
            </svg>
            <span>Cash on Delivery</span>
          </div>
          <span class="ayur-trust-sep">•</span>
          <div class="ayur-trust-item">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <rect x="1" y="3" width="15" height="13"></rect>
              <polygon points="16 8 20 8 23 11 23 16 16 16 8"></polygon>
              <circle cx="5.5" cy="18.5" r="2.5"></circle>
              <circle cx="18.5" cy="18.5" r="2.5"></circle>
            </svg>
            <span>Pan-India Delivery</span>
          </div>
        </div>
"""

lines[start_idx:end_idx] = [new_trust_block]

full_html = "".join(lines)
full_html = full_html.replace('v=swap_order_faq_v1', 'v=clean_trust_spacing_v2')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("index.html updated successfully!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .order-form-section padding
old_order_sec = """.order-form-section {
  position: relative;
  width: 100%;
  max-width: 450px;
  margin: 0 auto;
  padding: 10px 16px 36px 16px;
  background: #FFFFFF;
  box-sizing: border-box;
}"""

new_order_sec = """.order-form-section {
  position: relative;
  width: 100%;
  max-width: 450px;
  margin: 0 auto;
  padding: 10px 16px 14px 16px;
  background: #FFFFFF;
  box-sizing: border-box;
}"""

# Update .faq-section padding
old_faq_sec = """.faq-section {
  position: relative;
  width: 100%;
  max-width: 450px;
  margin: 0 auto;
  padding: 20px 14px 24px 14px;
  background: #FFFFFF;
  box-sizing: border-box;
}"""

new_faq_sec = """.faq-section {
  position: relative;
  width: 100%;
  max-width: 450px;
  margin: 0 auto;
  padding: 14px 14px 24px 14px;
  background: #FFFFFF;
  box-sizing: border-box;
}"""

# Update .ayur-trust-row
old_ayur_trust = """/* 7. Trust Row */
.ayur-trust-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px 12px;
  margin-top: 20px;
  padding-top: 14px;
  border-top: 1px solid #E5EEF3;
  font-size: 11.5px;
  color: #6C8294;
  flex-wrap: wrap;
}

.ayur-trust-row .trust-item svg {
  color: #33C3A5;
}"""

new_ayur_trust = """/* 7. Trust Row */
.ayur-trust-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px 10px;
  margin-top: 18px;
  padding-top: 14px;
  border-top: 1px solid #E5EEF3;
  flex-wrap: wrap;
}

.ayur-trust-item {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 12.5px;
  font-weight: 700;
  color: #0B3C5D;
  white-space: nowrap;
}

.ayur-trust-item svg {
  color: #33C3A5;
  flex-shrink: 0;
}

.ayur-trust-sep {
  color: #B2CAD8;
  font-size: 13px;
  font-weight: 700;
}"""

css_norm = css.replace('\r\n', '\n')
old_order_sec_norm = old_order_sec.replace('\r\n', '\n')
new_order_sec_norm = new_order_sec.replace('\r\n', '\n')
old_faq_sec_norm = old_faq_sec.replace('\r\n', '\n')
new_faq_sec_norm = new_faq_sec.replace('\r\n', '\n')
old_ayur_trust_norm = old_ayur_trust.replace('\r\n', '\n')
new_ayur_trust_norm = new_ayur_trust.replace('\r\n', '\n')

assert old_order_sec_norm in css_norm, "old_order_sec not found!"
css_norm = css_norm.replace(old_order_sec_norm, new_order_sec_norm)

assert old_faq_sec_norm in css_norm, "old_faq_sec not found!"
css_norm = css_norm.replace(old_faq_sec_norm, new_faq_sec_norm)

assert old_ayur_trust_norm in css_norm, "old_ayur_trust not found!"
css_norm = css_norm.replace(old_ayur_trust_norm, new_ayur_trust_norm)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_norm)

print("css/style.css updated successfully!")
