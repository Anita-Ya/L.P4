import shutil
import re

# 1. Overwrite assets/doctor-recommendation.jpg with clean version
shutil.copy2('scratch/doctor_recommendation_clean.jpg', 'assets/doctor-recommendation.jpg')
print("Replaced assets/doctor-recommendation.jpg with pristine single-bottle version!")

# 2. Update css/style.css to fix overlay bottle bottom cutoff
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'\.doctor-bottle-overlay\s*\{[^}]*\}',
    '''.doctor-bottle-overlay {
  position: absolute;
  right: 10px;
  bottom: 2px;
  width: 116px;
  z-index: 3;
  filter: drop-shadow(0 10px 18px rgba(0, 0, 0, 0.55));
}''',
    css
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated doctor-bottle-overlay in style.css!")

# 3. Update index.html image version
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'doctor-recommendation\.jpg(\?v=[^\"]*)?', 'doctor-recommendation.jpg?v=pristine_single_bottle_v5', html)
html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=doctor_clean_v2', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html cachebusters!")

