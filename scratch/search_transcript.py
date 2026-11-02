import json

with open(r'C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        content = str(obj.get('content', '')) + str(obj.get('tool_calls', ''))
        if 'doctor-recommendation.jpg' in content:
            step = obj.get('step_index')
            print(f"Found in step {step}: {content[:200]}")

