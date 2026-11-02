import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Anita Yadav\.gemini\antigravity\brain\e76b744e-f198-4291-b1c8-bd2224d68612\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        step = obj.get('step_index')
        if step and step in [1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655]:
            print(f"Step {step}:")
            print(obj.get('content', '')[:300])
            print(obj.get('tool_calls', ''))

