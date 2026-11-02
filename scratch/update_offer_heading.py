import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<p class="offer-top-subtitle">अपनी देखभाल के लिए सही जानकारी के साथ शुरुआत करें</p>',
    '<h2 class="offer-top-heading">अपनी देखभाल के लिए सही जानकारी के साथ शुरुआत करें</h2>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html to use h2.offer-top-heading!")

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_heading_css = """.offer-top-heading {
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 23px;
  font-weight: 800;
  color: #FFFFFF;
  margin: 0 0 22px 0;
  line-height: 1.35;
  text-align: center;
  letter-spacing: -0.2px;
  padding: 0 8px;
}

.offer-top-subtitle {
  font-family: 'Poppins', 'Mukta', sans-serif;
  font-size: 23px;
  font-weight: 800;
  color: #FFFFFF;
  margin: 0 0 22px 0;
  line-height: 1.35;
  text-align: center;
}"""

# Replace old .offer-top-subtitle rule
css = re.sub(
    r'\.offer-top-subtitle\s*\{[^}]*\}',
    new_heading_css,
    css
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with bold large heading style for offer-top-heading!")

# 3. Bump cachebuster
html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=big_heading_v2', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Bumped cachebuster to big_heading_v2!")

