with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('splitProductStage')
print(html[idx-100:idx+200])

