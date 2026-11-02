import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace review stars color #FFB800 with #33C3A5
css = css.replace('color: #FFB800;', 'color: #33C3A5;')

# Replace feature-check-icon yellow #F0BF58 with #33C3A5
css = css.replace('background: #F0BF58;', 'background: #33C3A5;')
css = css.replace('rgba(240, 191, 88, 0.35)', 'rgba(51, 195, 165, 0.35)')

# Replace strip-tag #E58325 with #33C3A5
css = css.replace('background: #E58325;', 'background: #33C3A5;')

# Replace required-star #FF5A5F with #33C3A5
css = css.replace('color: #FF5A5F;', 'color: #33C3A5;')

# Replace old disclaimer badge colors if any
css = css.replace('background: #FFF6E8;', 'background: rgba(51, 195, 165, 0.15);')
css = css.replace('border: 1px solid #FFE4B5;', 'border: 1px solid rgba(51, 195, 165, 0.4);')
css = css.replace('color: #C27803;', 'color: #0B3C5D;')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with exact Navy + Mint palette!")

# 2. Update js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("submitBtn.style.background = '#28a745';", "submitBtn.style.background = '#33C3A5';")

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated js/main.js with exact brand color!")

# 3. Bump cachebuster in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=pure_navy_mint_v1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Bumped cachebuster to pure_navy_mint_v1 in index.html!")

