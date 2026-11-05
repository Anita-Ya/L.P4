import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Verify bounds
faq_start = 806 # line 807: '    <!-- 10. FAQ SECTION -->\n'
faq_end = 928   # line 928: '    </section>\n'
order_start = 930 # line 931: '    <!-- ==============================================\n'
order_end = 1082  # line 1082: '    </section>\n'

faq_block = lines[faq_start:faq_end]
order_block = lines[order_start:order_end]

# Verify start and end of slices
assert 'FAQ SECTION' in faq_block[0]
assert '</section>' in faq_block[-1]
assert 'ORDER FORM' in order_block[1]
assert '</section>' in order_block[-1]

# Update comments in order_block to reflect section 10
order_block_updated = []
for l in order_block:
    l_mod = l.replace('SECTION 11: ORDER FORM', 'SECTION 10: ORDER FORM')
    order_block_updated.append(l_mod)

# Update comments in faq_block to reflect section 11
faq_block_updated = []
for l in faq_block:
    l_mod = l.replace('<!-- 10. FAQ SECTION -->', '<!-- 11. FAQ SECTION -->')
    faq_block_updated.append(l_mod)

new_lines = (
    lines[:faq_start] +
    order_block_updated +
    ['\n\n'] +
    faq_block_updated +
    lines[order_end:]
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Successfully swapped Order Form and FAQ sections in index.html!")

