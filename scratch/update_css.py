with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find start of .ayur-input-box (line 3479, index 3478) and end of .ayur-hint-error (line 3530, index 3529)
start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if line.strip() == '.ayur-input-box {':
        start_idx = i
    if start_idx is not None and '/* 5. Submit Button:' in line:
        end_idx = i
        break

print(f"Replacing lines {start_idx+1} to {end_idx}")

new_block = """.ayur-input-box {
  position: relative;
  display: flex;
  align-items: center;
  background: #FFFFFF;
  border: 1.5px solid #D0DFE8;
  border-radius: 14px;
  height: 52px;
  padding: 0 14px;
  box-sizing: border-box;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
}

.ayur-input-box:focus-within {
  border-color: #33C3A5;
  box-shadow: 0 0 0 3px rgba(51, 195, 165, 0.2);
  background: #FFFFFF;
}

.ayur-input-icon {
  color: #0B3C5D;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 10px;
  flex-shrink: 0;
  transition: color 0.2s ease;
}

.ayur-input-box:focus-within .ayur-input-icon {
  color: #33C3A5;
}

.ayur-input-box.phone-box {
  background: #FFFFFF;
}

.ayur-input {
  flex: 1;
  height: 100%;
  background: transparent;
  border: none;
  font-family: 'Mukta', 'Poppins', sans-serif;
  font-size: 15.5px;
  font-weight: 600;
  color: #07253B;
  outline: none;
  box-sizing: border-box;
}

.ayur-input::placeholder {
  color: #8A9CA8;
  font-weight: 400;
}

.ayur-hint-error {
  display: none;
  font-family: 'Mukta', sans-serif;
  font-size: 12.5px;
  color: #D93829;
  font-weight: 600;
  margin-top: 4px;
  padding-left: 2px;
}

.ayur-hint-error.is-visible {
  display: block;
}

/* Dynamic error state: only applied when validation fails */
.ayur-input-box.has-error {
  border-color: #D93829 !important;
  background: #FFF8F8 !important;
  box-shadow: 0 0 0 2px rgba(217, 56, 41, 0.15) !important;
}

.ayur-input-box.has-error .ayur-input-icon {
  color: #D93829 !important;
}

"""

lines[start_idx:end_idx] = [new_block + '\n']

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Updated style.css successfully!")
