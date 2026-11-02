import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

toast_css = """

/* ===================================================
   LIVE ORDER SOCIAL PROOF POPUP / TOAST (Navy + Mint)
   =================================================== */
.live-order-toast {
  position: fixed;
  bottom: 24px;
  left: 20px;
  z-index: 1000;
  display: flex;
  align-items: center;
  gap: 12px;
  background: #FFFFFF;
  border: 1.5px solid rgba(51, 195, 165, 0.45);
  border-radius: 18px;
  padding: 10px 34px 10px 12px;
  box-shadow: 0 10px 32px rgba(11, 60, 93, 0.16), 0 2px 8px rgba(0, 0, 0, 0.05);
  cursor: pointer;
  transform: translateY(140%);
  opacity: 0;
  pointer-events: none;
  transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.45s ease, box-shadow 0.25s ease, border-color 0.25s ease;
  max-width: 380px;
  user-select: none;
}

.live-order-toast.is-active {
  transform: translateY(0);
  opacity: 1;
  pointer-events: auto;
}

.live-order-toast:hover {
  box-shadow: 0 14px 40px rgba(11, 60, 93, 0.22), 0 3px 10px rgba(0, 0, 0, 0.08);
  border-color: #33C3A5;
}

.toast-close-btn {
  position: absolute;
  top: 7px;
  right: 8px;
  width: 22px;
  height: 22px;
  background: rgba(11, 60, 93, 0.06);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7B8F9E;
  cursor: pointer;
  padding: 0;
  transition: background 0.2s, color 0.2s, transform 0.2s;
  z-index: 2;
}

.toast-close-btn:hover {
  background: rgba(192, 57, 43, 0.15);
  color: #C0392B;
  transform: scale(1.1);
}

.toast-thumb-wrap {
  position: relative;
  width: 48px;
  height: 48px;
  flex-shrink: 0;
  background: #F2F8FB;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #D0DFE8;
}

.toast-product-img {
  width: 32px;
  height: 42px;
  object-fit: contain;
}

.toast-live-pulse {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 10px;
  height: 10px;
  background: #33C3A5;
  border: 2px solid #FFFFFF;
  border-radius: 50%;
  box-shadow: 0 0 0 0 rgba(51, 195, 165, 0.7);
  animation: toastPulse 1.8s infinite;
}

@keyframes toastPulse {
  0% {
    box-shadow: 0 0 0 0 rgba(51, 195, 165, 0.7);
  }
  70% {
    box-shadow: 0 0 0 6px rgba(51, 195, 165, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(51, 195, 165, 0);
  }
}

.toast-content-wrap {
  display: flex;
  flex-direction: column;
  gap: 2px;
  text-align: left;
}

.toast-buyer-row {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
  line-height: 1.2;
}

.toast-buyer-name {
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 14.5px;
  font-weight: 800;
  color: #0B3C5D;
}

.toast-buyer-city {
  font-family: 'Mukta', sans-serif;
  font-size: 12.5px;
  font-weight: 600;
  color: #5A738E;
}

.toast-time-badge {
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 10.5px;
  font-weight: 700;
  color: #0B3C5D;
  background: rgba(51, 195, 165, 0.18);
  padding: 1px 6px;
  border-radius: 6px;
  letter-spacing: 0.2px;
}

.toast-product-action {
  font-family: 'Mukta', sans-serif;
  font-size: 13px;
  color: #07253B;
  line-height: 1.25;
}

.toast-brand-name {
  color: #0B3C5D;
  font-weight: 800;
}

.toast-status-row {
  display: flex;
  align-items: center;
  margin-top: 1px;
}

.toast-verified-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 11px;
  font-weight: 700;
  color: #10846A;
}

@media (max-width: 480px) {
  .live-order-toast {
    left: 12px;
    right: 12px;
    bottom: 16px;
    max-width: calc(100% - 24px);
    padding: 9px 30px 9px 10px;
    border-radius: 16px;
  }
  .toast-buyer-name {
    font-size: 13.5px;
  }
  .toast-buyer-city {
    font-size: 12px;
  }
  .toast-product-action {
    font-size: 12.5px;
  }
}
"""

if '.live-order-toast' not in css_content:
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css_content + toast_css)
    print("Toast CSS appended to style.css!")
else:
    print("Toast CSS already in style.css!")

