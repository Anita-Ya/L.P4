from html.parser import HTMLParser
import sys
sys.stdout.reconfigure(encoding='utf-8')

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f"Unexpected end tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack.pop()
        if last_tag != tag_lower:
            self.errors.append(f"Mismatched tag: expected </{last_tag}> (from line {pos[0]}), got </{tag}> at line {self.getpos()[0]}")

for file_name in ['index.html', 'thankyou.html']:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    parser = TagValidator()
    parser.feed(content)

    print(f"[{file_name}] Unclosed tags: {len(parser.stack)}, Errors: {len(parser.errors)}")
    if parser.errors:
        for err in parser.errors[:5]:
            print(f"  {err}")

