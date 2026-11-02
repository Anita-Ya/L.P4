with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.support-trail-circle')
print(css[idx:idx+1000])

