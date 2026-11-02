import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert 'liveOrderToast' in html
assert 'toastBuyerName' in html
assert 'toastBuyerCity' in html
assert 'toastTimeBadge' in html
assert 'closeToastBtn' in html

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

assert '.live-order-toast' in css
assert '.live-order-toast.is-active' in css
assert 'toastPulse' in css

with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

assert 'recentOrdersData' in js
assert 'initLiveOrderToast' in js
assert 'dismissLiveToast' in js
assert 'scrollToOrder' in js

print("All elements, CSS, and JS routines verified successfully!")

