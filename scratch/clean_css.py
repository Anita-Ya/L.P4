with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''.hex-item-wrap:hover .hex-badge-img {
  transform: scale(1.58);
}

.hex-card-title {
  font-family: 'Poppins', sans-serif;
  color: var(--navy-primary);
  font-size: 15px;
  font-weight: 800;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
  text-transform: uppercase;
  line-height: 1.2;
}

.hex-card-desc {
  font-family: 'Mukta', 'Poppins', sans-serif;
  color: #4A6B82;
  font-size: 11px;
  line-height: 1.35;
  font-weight: 500;
  margin: 0;
}'''

replacement = '''.hex-item-wrap:hover .hex-badge-img {
  transform: scale(1.08);
}'''

if target in text:
    text = text.replace(target, replacement)
    print("SUCCESS: cleaned up duplicate rules!")
elif target.replace('\n', '\r\n') in text:
    text = text.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))
    print("SUCCESS (CRLF)")
else:
    print("ERROR: target not found")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(text)

