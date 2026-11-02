import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the .live-order-toast block
old_toast_block = """.live-order-toast {
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
}"""

new_toast_block = """.live-order-toast {
  position: fixed;
  bottom: 18px;
  left: 50%;
  transform: translate(-50%, 140%);
  width: calc(100% - 24px);
  max-width: 410px;
  z-index: 1000;
  display: flex;
  align-items: center;
  gap: 12px;
  background: #FFFFFF;
  border: 1.5px solid rgba(51, 195, 165, 0.45);
  border-radius: 18px;
  padding: 10px 34px 10px 12px;
  box-shadow: 0 10px 32px rgba(11, 60, 93, 0.2), 0 2px 8px rgba(0, 0, 0, 0.05);
  cursor: pointer;
  opacity: 0;
  pointer-events: none;
  transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.45s ease, box-shadow 0.25s ease, border-color 0.25s ease;
  user-select: none;
  box-sizing: border-box;
}

.live-order-toast.is-active {
  transform: translate(-50%, 0);
  opacity: 1;
  pointer-events: auto;
}

.live-order-toast.is-active:hover {
  transform: translate(-50%, -2px);
  box-shadow: 0 14px 40px rgba(11, 60, 93, 0.25), 0 3px 10px rgba(0, 0, 0, 0.08);
  border-color: #33C3A5;
}"""

# Update media query block as well
old_media_block = """@media (max-width: 480px) {
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
}"""

new_media_block = """@media (max-width: 480px) {
  .live-order-toast {
    bottom: 14px;
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
}"""

css_norm = css.replace('\r\n', '\n')
old_toast_norm = old_toast_block.replace('\r\n', '\n')
new_toast_norm = new_toast_block.replace('\r\n', '\n')
old_media_norm = old_media_block.replace('\r\n', '\n')
new_media_norm = new_media_block.replace('\r\n', '\n')

assert old_toast_norm in css_norm, "old_toast_block not found in css!"
css_norm = css_norm.replace(old_toast_norm, new_toast_norm)

assert old_media_norm in css_norm, "old_media_block not found in css!"
css_norm = css_norm.replace(old_media_norm, new_media_norm)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_norm)

print("css/style.css updated with centered live-order-toast!")

