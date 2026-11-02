import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update cachebuster for step images
html = re.sub(r'assets/step([1-6]-[a-z\-]+)\.jpg(\?v=[^\"]*)?', r'assets/step\1.jpg?v=ultra_hd_v1', html)

# Bump style.css cachebuster
html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=hd_sharp_v1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated cachebuster for step images and style.css in index.html!")

# Update css/style.css to optimize contrast for trail images
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'\.trail-circle-img\s*\{[^}]*\}',
    '''.trail-circle-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  transform: translateZ(0);
  backface-visibility: hidden;
}''',
    css
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Optimized .trail-circle-img in style.css!")

