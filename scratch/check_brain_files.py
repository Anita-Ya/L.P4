import os

brain = r"C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612"

files = [
    "step1_public_fear_1793437212289.jpg",
    "step2_alone_help_1793437238688.jpg",
    "card_career_fear_1793435999167.jpg",
    "step4_social_hesitation_1793437229619.jpg",
    "step5_family_concern_1793437249813.jpg",
    "card_mental_tension_1793435208262.jpg"
]

for f in files:
    p = os.path.join(brain, f)
    if os.path.exists(p):
        print(f"{f}: size {os.path.getsize(p)} bytes")
    else:
        print(f"{f}: NOT FOUND")
