import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('मिर्गी से जुड़ी चुनौतियों के बीच एक नई')
print("Found at idx:", idx)
if idx != -1:
    print(html[idx-250:idx+350])

