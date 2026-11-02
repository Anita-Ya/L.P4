import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = 'ने <strong class="toast-brand-name">Mirgi Mukti</strong> का ऑर्डर दिया'
replacement = 'ने <strong class="toast-brand-name">Mirgi Mukti</strong> ऑर्डर किया'

assert target in content, f"Target '{target}' not found in index.html"
content = content.replace(target, replacement)

# Bump cachebuster as well
content = content.replace('v=live_toast_center_v2', 'v=live_toast_center_v3')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully!")

