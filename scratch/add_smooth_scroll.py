with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'scroll-behavior' not in css:
    css = "html {\n  scroll-behavior: smooth;\n}\n\n" + css
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added scroll-behavior: smooth to html in style.css!")
else:
    print("Already present.")

