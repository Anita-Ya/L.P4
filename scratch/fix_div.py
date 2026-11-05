import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# line 956 is the extra </div>
if lines[955].strip() == '</div>' and lines[954].strip() == '</div>':
    print(f"Removing duplicate </div> at line 956: {repr(lines[955])}")
    del lines[955]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Cleaned duplicate div!")

