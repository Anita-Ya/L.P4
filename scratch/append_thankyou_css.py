import sys
sys.stdout.reconfigure(encoding='utf-8')

css_modal = """

/* ==========================================================================
   THANK YOU / ORDER CONFIRMATION MODAL & PAGE (Exact Reference Match)
   ========================================================================== */
.thankyou-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(7, 37, 59, 0.78);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  z-index: 99999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  box-sizing: border-box;
  animation: modalFadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes modalFadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.thankyou-modal-card {
  position: relative;
  width: 100%;
  max-width: 410px;
  background: #FFFFFF;
  border-radius: 28px;
  padding: 34px 22px 26px 22px;
  box-shadow: 0 24px 60px rgba(7, 37, 59, 0.38);
  box-sizing: border-box;
  text-align: center;
  animation: cardSlideUp 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes cardSlideUp {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.96);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.modal-close-btn {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  border: 1.5px solid #E1EDF4;
  background: #FFFFFF;
  color: #6C8294;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  padding: 0;
}

.modal-close-btn:hover {
  background: #F2F8FB;
  color: #07253B;
  border-color: #0B3C5D;
}

/* Success Checkmark Circle */
.thankyou-check-outer {
  width: 82px;
  height: 82px;
  border-radius: 50%;
  background: rgba(51, 195, 165, 0.14);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px auto;
}

.thankyou-check-inner {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: rgba(51, 195, 165, 0.22);
  border: 1.5px solid rgba(51, 195, 165, 0.55);
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Pill Tag */
.thankyou-pill-tag {
  display: inline-block;
  padding: 5px 18px;
  border-radius: 50px;
  background: rgba(51, 195, 165, 0.16);
  border: 1px solid rgba(51, 195, 165, 0.45);
  color: #0B3C5D;
  font-family: 'Poppins', sans-serif;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.5px;
  margin-bottom: 14px;
}

/* Greeting Title */
.thankyou-greet-title {
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: #07253B;
  margin: 0 0 6px 0;
  line-height: 1.25;
}

.thankyou-user-name {
  color: #33C3A5;
}

.thankyou-greet-sub {
  font-family: 'Mukta', sans-serif;
  font-size: 14.5px;
  color: #4A6072;
  margin: 0 0 18px 0;
  line-height: 1.5;
  font-weight: 500;
}

/* Summary Box */
.thankyou-details-box {
  background: #F8FBFC;
  border: 1.5px solid #E1EDF4;
  border-radius: 18px;
  padding: 14px 18px;
  margin-bottom: 16px;
  box-sizing: border-box;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 14px;
}

.detail-label {
  color: #6C8294;
  font-weight: 600;
}

.detail-value {
  color: #07253B;
  font-weight: 800;
}

.detail-value.order-id-val {
  font-family: 'Poppins', monospace;
  letter-spacing: 0.5px;
}

.detail-value.delivery-val {
  color: #33C3A5;
  font-weight: 800;
}

.detail-divider {
  border-top: 1px dashed #D5E4EC;
  margin: 10px 0;
}

/* Callout Note */
.thankyou-callout-note {
  font-family: 'Mukta', sans-serif;
  font-size: 13px;
  color: #6C8294;
  margin: 0 0 18px 0;
  line-height: 1.45;
  font-weight: 500;
}

/* Action Button: "धन्यवाद, ठीक है" */
.thankyou-confirm-btn {
  width: 100%;
  height: 52px;
  background: #0B3C5D;
  color: #FFFFFF;
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 18px;
  font-weight: 800;
  border: none;
  border-radius: 50px;
  box-shadow: 0 8px 24px rgba(11, 60, 93, 0.35);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.2s, background 0.2s;
}

.thankyou-confirm-btn:hover {
  background: #07253B;
  transform: translateY(-2px);
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_modal)

print("Appended Thank You modal CSS to style.css!")

