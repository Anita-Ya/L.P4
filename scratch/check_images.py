import os
from PIL import Image

print("Root images:")
for f in os.listdir('.'):
    if f.lower().endswith(('.jpg', '.jpeg', '.png')):
        try:
            im = Image.open(f)
            print(f"  {f}: {im.size}, mode={im.mode}")
        except Exception as e:
            print(f"  {f}: error {e}")

print("\nAssets images:")
if os.path.exists('assets'):
    for f in os.listdir('assets'):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                im = Image.open(os.path.join('assets', f))
                print(f"  assets/{f}: {im.size}, mode={im.mode}")
            except Exception as e:
                print(f"  assets/{f}: error {e}")

