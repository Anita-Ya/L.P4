import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

ref_form_css = """

/* ==========================================================================
   SECTION 11: EXACT REFERENCE ORDER FORM (Requested by User)
   ========================================================================== */
.order-form-container-box {
  position: relative;
  width: 100%;
  background: #0B3C5D;
  border: 2px solid #33C3A5;
  border-radius: 24px;
  padding: 38px 16px 20px 16px;
  box-shadow: 0 16px 40px rgba(11, 60, 93, 0.28);
  box-sizing: border-box;
}

.ref-order-card {
  position: relative;
  background: #FFFFFF;
  border-radius: 20px;
  padding: 32px 18px 22px 18px;
  box-shadow: 0 8px 26px rgba(0, 0, 0, 0.12);
  box-sizing: border-box;
}

.ref-rec-badge {
  position: absolute;
  top: -18px;
  left: 50%;
  transform: translateX(-50%);
  background: #E0A638;
  color: #07253B;
  font-family: 'Poppins', sans-serif;
  font-size: 15px;
  font-weight: 800;
  padding: 6px 22px;
  border-radius: 50px;
  box-shadow: 0 4px 14px rgba(224, 166, 56, 0.4);
  display: inline-flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
  z-index: 2;
}

.badge-star {
  font-size: 15px;
  color: #07253B;
}

.ref-order-form {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ref-input-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
  text-align: left;
}

.ref-label {
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 16px;
  font-weight: 700;
  color: #07253B;
  margin: 0;
}

.ref-input {
  width: 100%;
  height: 50px;
  padding: 0 16px;
  background: #FAF8F3;
  border: 1.5px solid #8C2D2D;
  border-radius: 12px;
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 16px;
  font-weight: 600;
  color: #07253B;
  box-sizing: border-box;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.ref-input::placeholder {
  color: #7B8A95;
  font-weight: 400;
}

.ref-input:focus {
  border-color: #0B3C5D;
  box-shadow: 0 0 0 3px rgba(11, 60, 93, 0.15);
}

.ref-hint-msg {
  font-family: 'Mukta', sans-serif;
  font-size: 12px;
  color: #8C2D2D;
  font-weight: 500;
  margin-top: 2px;
}

.ref-submit-btn {
  width: 100%;
  height: 54px;
  background: #E0A638;
  color: #07253B;
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 21px;
  font-weight: 800;
  border: none;
  border-radius: 14px;
  box-shadow: 0 8px 24px rgba(224, 166, 56, 0.35);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 6px;
  transition: transform 0.2s, background 0.2s, box-shadow 0.2s;
}

.ref-submit-btn:hover {
  background: #cf9528;
  transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(224, 166, 56, 0.45);
}

.ref-submit-btn:active {
  transform: translateY(1px);
}

.ref-trust-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px 12px;
  margin-top: 18px;
  font-size: 12px;
  color: #F2F8FB;
  flex-wrap: wrap;
}

.ref-trust-row .trust-item {
  color: #F2F8FB;
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(ref_form_css)

print("Appended reference form styles to style.css!")

# Bump cachebuster in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=ref_order_card_v1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Bumped cachebuster to ref_order_card_v1!")

