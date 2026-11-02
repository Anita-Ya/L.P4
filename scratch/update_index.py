with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update cachebuster
content = content.replace('css/style.css?v=big_heading_v2', 'css/style.css?v=form_clean_v3')
content = content.replace('js/main.js', 'js/main.js?v=form_clean_v3')

# Add id="nameBox"
content = content.replace('<div class="ayur-input-box">', '<div class="ayur-input-box" id="nameBox">')

# Add id="phoneBox"
content = content.replace('<div class="ayur-input-box phone-box">', '<div class="ayur-input-box phone-box" id="phoneBox">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully!")

