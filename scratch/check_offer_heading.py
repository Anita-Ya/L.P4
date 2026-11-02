import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('अपनी देखभाल के लिए सही जानकारी')
print("Found at idx:", idx)
if idx != -1:
    print(html[idx-150:idx+250])

