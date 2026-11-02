import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('css/style.css?v=form_clean_v3', 'css/style.css?v=live_toast_v1')
c = c.replace('js/main.js?v=form_clean_v3', 'js/main.js?v=live_toast_v1')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Bumped cachebusters in index.html")

