import shutil
import re

# 1. Copy to assets
shutil.copy2('scratch/doctor_recommendation_perfect.jpg', 'assets/doctor-recommendation.jpg')
print("Updated assets/doctor-recommendation.jpg!")

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'doctor-recommendation\.jpg(\?v=[^\"]*)?', 'doctor-recommendation.jpg?v=single_clean_bottle_final', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html cachebuster to single_clean_bottle_final!")

