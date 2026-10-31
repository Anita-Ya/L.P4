with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace sizes in ribbon section
replacements = [
    ("width: 104px;", "width: 120px;"),
    ("width: 96px;\n  height: 96px;", "width: 114px;\n  height: 114px;"),
    ("width: 96px;\r\n  height: 96px;", "width: 114px;\r\n  height: 114px;"),
    ("border: 3.5px solid var(--mint-accent);", "border: 4px solid var(--mint-accent);"),
    ("min-height: 96px;", "min-height: 114px;"),
    ("margin-left: -28px;", "margin-left: -32px;"),
    ("padding: 14px 48px 14px 38px;", "padding: 16px 52px 16px 42px;"),
    ("clip-path: polygon(28px 0%, calc(100% - 24px) 0%, 100% 50%, calc(100% - 24px) 100%, 0% 100%);",
     "clip-path: polygon(32px 0%, calc(100% - 28px) 0%, 100% 50%, calc(100% - 28px) 100%, 0% 100%);"),
    ("font-size: 20px;", "font-size: 23px;"),
    ("font-size: 15px;", "font-size: 16.5px;"),
    ("width: 40px;\n  height: 40px;", "width: 46px;\n  height: 46px;"),
    ("width: 40px;\r\n  height: 40px;", "width: 46px;\r\n  height: 46px;"),
    ("font-size: 14.5px;", "font-size: 16.5px;"),
    ("width: 86px;", "width: 104px;"),
    ("width: 80px;\n    height: 80px;", "width: 98px;\n    height: 98px;"),
    ("width: 80px;\r\n    height: 80px;", "width: 98px;\r\n    height: 98px;"),
    ("min-height: 86px;", "min-height: 102px;"),
    ("padding: 12px 42px 12px 30px;", "padding: 14px 46px 14px 34px;"),
    ("font-size: 18px;", "font-size: 21px;"),
    ("font-size: 13.5px;", "font-size: 15px;"),
    ("width: 35px;\n    height: 35px;", "width: 40px;\n    height: 40px;"),
    ("width: 35px;\r\n    height: 35px;", "width: 40px;\r\n    height: 40px;"),
    ("font-size: 13px;", "font-size: 14.5px;")
]

count = 0
for old, new in replacements:
    if old in css:
        css = css.replace(old, new)
        count += 1

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print(f"Applied {count} replacements to css/style.css!")

