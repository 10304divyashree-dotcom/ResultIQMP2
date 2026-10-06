import os
import re

filepath = 'c:\\Users\\Divyashree\\OneDrive\\Desktop\\MP2\\RESULTIQ\\RESULTIQ\\static\\css\\style.css'
with open(filepath, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Enhance Shadows (Modern, soft layered shadows)
css = re.sub(r'--shadow-sm:\s*.*?;', '--shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);', css)
css = re.sub(r'--shadow-md:\s*.*?;', '--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);', css)
css = re.sub(r'--shadow-lg:\s*.*?;', '--shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);', css)

# 2. Add font smoothing to body
if '-webkit-font-smoothing' not in css:
    css = css.replace('body {', 'body {\n  -webkit-font-smoothing: antialiased;\n  -moz-osx-font-smoothing: grayscale;')

# 3. Enhance Button Styles (Subtle inner shadow/gradient for depth)
btn_primary_replacement = """.btn-primary {
  background: linear-gradient(180deg, #11877d 0%, var(--color-secondary) 100%);
  color: #fff;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1), inset 0 1px 0 rgba(255,255,255,0.15);
  border: 1px solid #0d635c;
}
.btn-primary:hover {
  background: linear-gradient(180deg, #149c92 0%, #11877d 100%);
  box-shadow: 0 4px 12px rgba(15, 118, 110, 0.25), inset 0 1px 0 rgba(255,255,255,0.2);
  transform: translateY(-1px);
  color: #fff;
}"""
css = re.sub(r'\.btn-primary \{.*?\n\}\n\.btn-primary:hover \{.*?\n\}', btn_primary_replacement, css, flags=re.DOTALL)

# Refine Card Borders
css = css.replace('--color-border:       #D9E2EC;', '--color-border:       #E2E8F0;')
css = css.replace('--color-bg:           #F5F9FC;', '--color-bg:           #F1F5F9;')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS Enhanced Successfully")
