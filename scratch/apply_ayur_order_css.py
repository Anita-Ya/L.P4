import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

css_snippet = """

/* ==========================================================================
   SECTION 11: AYURVANI-STYLE ORDER FORM (Exact Screenshot Match)
   ========================================================================== */
.ayur-order-card {
  position: relative;
  background: #FFFFFF;
  border: 2px solid rgba(11, 60, 93, 0.12);
  border-radius: 24px;
  padding: 30px 20px 24px 20px;
  box-shadow: 0 14px 38px rgba(11, 60, 93, 0.08);
  box-sizing: border-box;
  text-align: center;
}

/* 1. Header Title: "Order Your Product" */
.ayur-order-title {
  font-family: 'Poppins', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: #0B3C5D;
  margin: 0 0 18px 0;
  line-height: 1.25;
}

/* 2. Product Thumbnail Box */
.ayur-product-thumb-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  margin-bottom: 18px;
}

.ayur-thumb-box {
  width: 96px;
  height: 96px;
  background: #F2F8FB;
  border: 1.5px solid rgba(51, 195, 165, 0.35);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 18px rgba(11, 60, 93, 0.08);
  overflow: hidden;
}

.ayur-thumb-img {
  max-width: 82%;
  max-height: 82%;
  object-fit: contain;
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.25));
}

.ayur-product-brand {
  font-family: 'Poppins', sans-serif;
  font-size: 26px;
  font-weight: 800;
  color: #0B3C5D;
  margin: 0;
  letter-spacing: 0.5px;
}

/* 3. Leaf Divider: ─── 🍃 ─── */
.ayur-leaf-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  width: 100%;
  max-width: 280px;
  margin: 0 auto 22px auto;
}

.leaf-line {
  flex: 1;
  height: 1px;
  background: #D9E4EC;
}

.leaf-icon-wrap {
  color: #33C3A5;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 4. Form Fields */
.ayur-actual-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ayur-field-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  text-align: left;
}

.ayur-label {
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 16px;
  font-weight: 700;
  color: #0B3C5D;
  margin: 0;
}

.ayur-input-box {
  position: relative;
  display: flex;
  align-items: center;
  background: #F8FBFC;
  border: 1.5px solid #C0392B;
  border-radius: 14px;
  height: 52px;
  padding: 0 14px;
  box-sizing: border-box;
  transition: all 0.2s ease;
}

.ayur-input-icon {
  color: #C0392B;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 10px;
  flex-shrink: 0;
}

.ayur-input-box.phone-box {
  background: #EDF4FB;
}

.ayur-input {
  flex: 1;
  height: 100%;
  background: transparent;
  border: none;
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 15.5px;
  font-weight: 600;
  color: #07253B;
  outline: none;
  box-sizing: border-box;
}

.ayur-input::placeholder {
  color: #7B8F9E;
  font-weight: 400;
}

.ayur-hint-error {
  font-family: 'Mukta', sans-serif;
  font-size: 12.5px;
  color: #C0392B;
  font-weight: 600;
  margin-top: 1px;
}

/* 5. Submit Button: "Place My Order" */
.ayur-submit-btn {
  width: 100%;
  height: 56px;
  background: #0B3C5D;
  color: #FFFFFF;
  border: none;
  border-radius: 50px;
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 18.5px;
  font-weight: 800;
  letter-spacing: 0.4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  box-shadow: 0 8px 24px rgba(11, 60, 93, 0.35);
  margin-top: 6px;
  transition: transform 0.2s, background 0.2s, box-shadow 0.2s;
}

.ayur-submit-btn:hover {
  background: #07253B;
  transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(11, 60, 93, 0.45);
}

.btn-cart-icon {
  display: flex;
  align-items: center;
}

.btn-arrow-icon {
  font-size: 18px;
  margin-left: 2px;
}

/* 6. Support Callout */
.ayur-support-callout {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-top: 8px;
  text-align: left;
}

.callout-check-circle {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #33C3A5;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.callout-text {
  font-family: 'Mukta', sans-serif;
  font-size: 13px;
  color: #4A6072;
  line-height: 1.45;
  font-weight: 500;
}

/* 7. Trust Row */
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
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_snippet)

print("Appended ayur order card styles to style.css!")

# Bump cachebuster in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=ayur_order_v1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Bumped cachebuster to ayur_order_v1 in index.html!")

