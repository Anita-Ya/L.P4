import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the hex-content and hex-badge styling
pattern = r'/\* Inside Content \*/.*?(?=\.hex-item-wrap:hover)'

replacement = '''/* Inside Content */
.hex-content {
  position: relative;
  z-index: 3;
  padding: 18px 14px 14px 14px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}

.hex-badge-box {
  width: 108px;
  height: 108px;
  margin-bottom: 0px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: none;
  box-shadow: none;
  padding: 0;
  position: relative;
}

.hex-badge-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  mix-blend-mode: multiply; /* Removes any white rectangular background! */
  filter: contrast(1.06);
  transition: transform 0.3s ease;
}

.hex-card-title {
  font-family: 'Poppins', sans-serif;
  color: var(--navy-primary);
  font-size: 17px;
  font-weight: 800;
  letter-spacing: 0.8px;
  margin: 6px 0 0 0;
  text-transform: uppercase;
  line-height: 1.2;
}

'''

text = re.sub(pattern, replacement, text, flags=re.DOTALL)

# Also update responsive block at bottom
resp_pattern = r'  \.hex-badge-box {\s*width: 84px;\s*height: 84px;\s*margin-bottom: 2px;\s*}\s*\.hex-badge-img {\s*transform: scale\(1.42\);\s*}\s*\.hex-card-title {\s*font-size: 14.5px;\s*}\s*\.hex-card-desc {\s*font-size: 10.5px;\s*}'

resp_replacement = '''  .hex-badge-box {
    width: 96px;
    height: 96px;
    margin-bottom: 0px;
  }
  .hex-badge-img {
    mix-blend-mode: multiply;
  }
  .hex-card-title {
    font-size: 15px;
    margin-top: 4px;
  }'''

text = re.sub(resp_pattern, resp_replacement, text)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: updated css/style.css!")

