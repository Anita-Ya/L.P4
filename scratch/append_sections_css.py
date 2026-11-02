import sys
sys.stdout.reconfigure(encoding='utf-8')

css_content = """

/* ==========================================================================
   SECTION 11: ORDER FORM (अपना Mirgi Mukti Order करें)
   ========================================================================== */
.order-form-section {
  position: relative;
  width: 100%;
  max-width: 450px;
  margin: 0 auto;
  padding: 10px 16px 36px 16px;
  background: #FFFFFF;
  box-sizing: border-box;
}

.order-form-card {
  position: relative;
  background: linear-gradient(175deg, #0B3C5D 0%, #062338 100%);
  border: 1.5px solid rgba(51, 195, 165, 0.4);
  border-radius: 24px;
  padding: 28px 20px 22px 20px;
  box-shadow: 0 16px 40px rgba(7, 37, 59, 0.28), 0 0 24px rgba(51, 195, 165, 0.16);
  box-sizing: border-box;
  overflow: hidden;
}

/* Ambient glow accent */
.order-form-card::before {
  content: '';
  position: absolute;
  top: -60px;
  right: -60px;
  width: 160px;
  height: 160px;
  background: radial-gradient(circle, rgba(51, 195, 165, 0.3) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

.order-card-header {
  position: relative;
  z-index: 1;
  text-align: center;
  margin-bottom: 20px;
}

.order-deal-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(51, 195, 165, 0.16);
  border: 1px solid rgba(51, 195, 165, 0.45);
  border-radius: 50px;
  padding: 6px 14px;
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 12.5px;
  font-weight: 700;
  color: #33C3A5;
  margin-bottom: 12px;
}

.pill-badge-pulse {
  width: 8px;
  height: 8px;
  background: #33C3A5;
  border-radius: 50%;
  box-shadow: 0 0 10px #33C3A5;
  animation: pulseDot 1.8s infinite;
}

@keyframes pulseDot {
  0% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(51, 195, 165, 0.7);
  }
  70% {
    transform: scale(1.15);
    box-shadow: 0 0 0 8px rgba(51, 195, 165, 0);
  }
  100% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(51, 195, 165, 0);
  }
}

.order-form-title {
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 25px;
  font-weight: 800;
  color: #FFFFFF;
  margin: 0 0 6px 0;
  line-height: 1.25;
}

.order-form-subtitle {
  font-family: 'Mukta', sans-serif;
  font-size: 13.5px;
  color: #C0D6E4;
  margin: 0;
  line-height: 1.4;
  font-weight: 500;
}

/* Product Preview Strip */
.order-product-strip {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 14px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 16px;
  padding: 10px 14px;
  margin-bottom: 22px;
}

.strip-img-wrap {
  width: 52px;
  height: 68px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.strip-product-img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.4));
}

.strip-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.strip-title-row {
  display: flex;
  align-items: baseline;
  gap: 6px;
}

.strip-name {
  font-family: 'Poppins', sans-serif;
  font-size: 15px;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: 0.3px;
}

.strip-capsules {
  font-family: 'Poppins', sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: #A0C2D6;
}

.strip-herbs {
  font-family: 'Mukta', sans-serif;
  font-size: 11.5px;
  color: #33C3A5;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.strip-price-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 2px;
}

.strip-tag {
  background: #E58325;
  color: #FFFFFF;
  font-family: 'Poppins', sans-serif;
  font-size: 10px;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: 6px;
  letter-spacing: 0.4px;
}

.strip-badge-cod {
  background: rgba(51, 195, 165, 0.2);
  color: #33C3A5;
  border: 1px solid rgba(51, 195, 165, 0.35);
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 10.5px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 6px;
}

/* The Form */
.order-actual-form {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 7px;
  text-align: left;
}

.form-label {
  display: flex;
  align-items: center;
  gap: 7px;
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 14px;
  font-weight: 700;
  color: #FFFFFF;
}

.form-label svg {
  color: #33C3A5;
  flex-shrink: 0;
}

.required-star {
  color: #FF5A5F;
  font-weight: 800;
  margin-left: 2px;
}

.input-wrapper {
  position: relative;
  width: 100%;
}

.form-control {
  width: 100%;
  height: 50px;
  padding: 0 16px;
  background: #FFFFFF;
  border: 1.5px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 15px;
  font-weight: 600;
  color: #07253B;
  box-sizing: border-box;
  outline: none;
  transition: all 0.25s ease;
}

.form-control::placeholder {
  color: #8C9CA8;
  font-weight: 400;
}

.form-control:focus {
  border-color: #33C3A5;
  box-shadow: 0 0 0 3.5px rgba(51, 195, 165, 0.3);
}

/* Phone input with country code */
.phone-input-wrapper {
  display: flex;
  align-items: stretch;
  background: #FFFFFF;
  border-radius: 12px;
  overflow: hidden;
  border: 1.5px solid rgba(255, 255, 255, 0.2);
  transition: all 0.25s ease;
}

.phone-input-wrapper:focus-within {
  border-color: #33C3A5;
  box-shadow: 0 0 0 3.5px rgba(51, 195, 165, 0.3);
}

.phone-country-code {
  background: #EBF3F7;
  color: #0B3C5D;
  font-family: 'Poppins', sans-serif;
  font-weight: 800;
  font-size: 14.5px;
  padding: 0 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid #D5E4EC;
  user-select: none;
}

.phone-input {
  border: none !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  height: 50px;
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  letter-spacing: 0.5px;
  font-weight: 700;
}

/* Submit Button */
.order-submit-btn {
  position: relative;
  width: 100%;
  height: 54px;
  background: #33C3A5;
  border: none;
  border-radius: 14px;
  color: #FFFFFF;
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 18px;
  font-weight: 800;
  letter-spacing: 0.3px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  box-shadow: 0 10px 28px rgba(51, 195, 165, 0.4);
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
  margin-top: 6px;
}

.order-submit-btn:hover {
  background: #2cb296;
  transform: translateY(-2px);
  box-shadow: 0 14px 34px rgba(51, 195, 165, 0.5);
}

.order-submit-btn:active {
  transform: translateY(1px);
}

.order-submit-btn .btn-shine {
  position: absolute;
  top: 0;
  left: -120%;
  width: 60%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
  transform: skewX(-20deg);
  animation: submitShine 3.2s infinite;
}

@keyframes submitShine {
  0% {
    left: -120%;
  }
  30%, 100% {
    left: 140%;
  }
}

.btn-check-icon {
  stroke-width: 3;
}

/* Success Alert Box */
.order-success-msg {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  background: rgba(51, 195, 165, 0.16);
  border: 1.5px solid #33C3A5;
  border-radius: 14px;
  padding: 14px 16px;
  margin-top: 8px;
  animation: successSlideDown 0.4s ease-out;
}

@keyframes successSlideDown {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.success-icon-box {
  width: 36px;
  height: 36px;
  background: rgba(51, 195, 165, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.success-text-box h4 {
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 15px;
  font-weight: 800;
  color: #FFFFFF;
  margin: 0 0 4px 0;
}

.success-text-box p {
  font-family: 'Mukta', sans-serif;
  font-size: 13px;
  color: #D3E7F2;
  margin: 0;
  line-height: 1.45;
}

/* Trust Badges Row */
.order-trust-row {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 6px 10px;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.14);
}

.trust-item {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: 'Mukta', sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: #C0D6E4;
}

.trust-item svg {
  color: #33C3A5;
  flex-shrink: 0;
}

.trust-divider {
  color: rgba(255, 255, 255, 0.25);
  font-size: 11px;
}


/* ==========================================================================
   SECTION 12: DISCLAIMER & FOOTER
   ========================================================================== */
.site-footer {
  position: relative;
  width: 100%;
  max-width: 450px;
  margin: 0 auto;
  background: #F2F8FB;
  padding: 24px 16px 42px 16px;
  box-sizing: border-box;
}

.disclaimer-card {
  background: #FFFFFF;
  border: 1.5px solid #E1EDF4;
  border-radius: 20px;
  padding: 22px 18px 20px 18px;
  box-shadow: 0 6px 20px rgba(11, 60, 93, 0.05);
  box-sizing: border-box;
}

.disclaimer-header {
  margin-bottom: 14px;
}

.disclaimer-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #FFF6E8;
  border: 1px solid #FFE4B5;
  border-radius: 50px;
  padding: 4px 12px;
  color: #C27803;
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: 0.6px;
}

.disclaimer-badge svg {
  color: #C27803;
}

.disclaimer-content {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.disclaimer-para {
  font-family: 'Mukta', sans-serif;
  font-size: 13px;
  line-height: 1.65;
  color: #4A6072;
  margin: 0;
  text-align: justify;
  font-weight: 500;
}

.legal-para {
  font-size: 12px;
  line-height: 1.6;
  color: #6C8294;
  padding-top: 10px;
  border-top: 1px dashed #E2ECF2;
}

.footer-bottom-line {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid #EAF1F5;
  text-align: center;
}

.copyright-text {
  font-family: 'Mukta', sans-serif;
  font-size: 12.5px;
  color: #7A8E9E;
  font-weight: 600;
  margin: 0 0 8px 0;
}

.footer-links {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  font-family: 'Poppins', sans-serif;
  font-size: 11.5px;
  color: #0B3C5D;
  font-weight: 600;
}

.footer-dot {
  color: #A0B2C0;
}

.footer-link {
  color: #0B3C5D;
  text-decoration: none;
  cursor: pointer;
  transition: color 0.2s;
}

.footer-link:hover {
  color: #33C3A5;
}

/* Extra small screen adjustments */
@media (max-width: 380px) {
  .order-form-title {
    font-size: 22px;
  }
  .order-submit-btn {
    font-size: 16px;
    height: 50px;
  }
  .order-product-strip {
    padding: 8px 10px;
    gap: 10px;
  }
  .strip-name {
    font-size: 14px;
  }
  .order-trust-row {
    font-size: 11px;
  }
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

print("Successfully appended CSS for Section 11 & Section 12 to style.css!")

