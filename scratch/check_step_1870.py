import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        step = obj.get('step_index')
        if step and 1865 <= step <= 1875:
            print(f"Step {step}:")
            print(obj.get('tool_calls', ''))

