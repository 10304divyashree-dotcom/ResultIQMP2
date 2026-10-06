import re
import os

filepath = 'c:\\Users\\Divyashree\\OneDrive\\Desktop\\MP2\\RESULTIQ\\RESULTIQ\\static\\css\\style.css'
with open(filepath, 'r', encoding='utf-8') as f:
    css = f.read()

# Palette replacement
css = re.sub(
    r':root \{.*?\/\* Typography \*\/',
    """:root {
  /* Palette */
  --color-bg:           #F5F9FC;
  --color-surface:      #FFFFFF;
  --color-surface-2:    #F8FAFC;
  --color-surface-3:    #E2E8F0;
  --color-border:       #D9E2EC;
  --color-border-light: #CBD5E1;

  --color-primary:      #1E3A5F;
  --color-primary-dark: #122642;
  --color-primary-glow: rgba(30, 58, 95, 0.25);
  --color-secondary:    #0F766E;

  --color-text:         #1F2937;
  --color-text-muted:   #64748B;
  --color-text-faint:   #94A3B8;

  --color-success:      #16A34A;
  --color-success-bg:   rgba(22, 163, 74, 0.12);
  --color-danger:       #DC2626;
  --color-danger-bg:    rgba(220, 38, 38, 0.12);
  --color-warning:      #D97706;
  --color-warning-bg:   rgba(217, 119, 6, 0.12);
  --color-info:         #0284C7;
  --color-info-bg:      rgba(2, 132, 199, 0.12);

  /* Classification badge colours */
  --cls-marks:    #1E3A5F;
  --cls-identity: #0F766E;
  --cls-category: #D97706;
  --cls-metadata: #4F46E5;
  --cls-empty:    #9CA3AF;
  --cls-text:     #6B7280;

  /* Typography */""",
    css,
    flags=re.DOTALL
)

# Mesh gradient on body
css = css.replace(
    "radial-gradient(ellipse 80% 50% at 20% 10%, rgba(79,114,255,.08) 0%, transparent 60%),\n    radial-gradient(ellipse 60% 40% at 80% 80%, rgba(124,58,237,.06) 0%, transparent 60%);",
    "radial-gradient(ellipse 80% 50% at 20% 10%, rgba(30,58,95,.04) 0%, transparent 60%),\n    radial-gradient(ellipse 60% 40% at 80% 80%, rgba(15,118,110,.04) 0%, transparent 60%);"
)

# Navbar background
css = css.replace(
    "background: rgba(26, 35, 64, 0.85);",
    "background: rgba(255, 255, 255, 0.85);"
)

# btn-primary
css = re.sub(
    r'\.btn-primary \{.*?\}',
    """.btn-primary {
  background: linear-gradient(135deg, var(--color-secondary), #0d635c);
  color: #fff;
  box-shadow: 0 2px 12px rgba(15, 118, 110, 0.25);
}""",
    css,
    flags=re.DOTALL,
    count=1
)

css = re.sub(
    r'\.btn-primary:hover \{.*?\}',
    """.btn-primary:hover {
  background: linear-gradient(135deg, #149c92, var(--color-secondary));
  box-shadow: 0 4px 20px rgba(15, 118, 110, 0.4);
  transform: translateY(-1px);
  color: #fff;
}""",
    css,
    flags=re.DOTALL,
    count=1
)

# btn-success
css = re.sub(
    r'\.btn-success \{.*?\}',
    """.btn-success {
  background: linear-gradient(135deg, #14803b, var(--color-success));
  color: #fff;
  box-shadow: 0 2px 12px rgba(22, 163, 74, 0.3);
}""",
    css,
    flags=re.DOTALL,
    count=1
)

css = re.sub(
    r'\.btn-success:hover \{.*?\}',
    """.btn-success:hover {
  background: linear-gradient(135deg, var(--color-success), #1eb858);
  transform: translateY(-1px);
  color: #fff;
}""",
    css,
    flags=re.DOTALL,
    count=1
)

# btn-danger
css = css.replace("linear-gradient(135deg, #DC2626, #EF4444)", "linear-gradient(135deg, #b91c1c, var(--color-danger))")
css = css.replace("linear-gradient(135deg, #EF4444, #F87171)", "linear-gradient(135deg, var(--color-danger), #ef4444)")

# alert colors
css = css.replace("color: #34D399;", "color: #15803d;")
css = css.replace("color: #FCA5A5;", "color: #b91c1c;")
css = css.replace("color: #FCD34D;", "color: #b45309;")
css = css.replace("color: #93C5FD;", "color: #0369a1;")

# Stat cards
css = css.replace("linear-gradient(90deg, #059669, #10B981)", "linear-gradient(90deg, #15803d, #16A34A)")
css = css.replace("linear-gradient(90deg, #DC2626, #EF4444)", "linear-gradient(90deg, #b91c1c, #DC2626)")
css = css.replace("linear-gradient(90deg, #7C3AED, #A78BFA)", "linear-gradient(90deg, #0d635c, #0F766E)")
css = css.replace("linear-gradient(90deg, #D97706, #FBBF24)", "linear-gradient(90deg, #b45309, #D97706)")
css = css.replace("linear-gradient(90deg, #DB2777, #F472B6)", "linear-gradient(90deg, #be123c, #E11D48)")

# Badges
css = css.replace("rgba(79,114,255,.15); color: #93B4FF;", "rgba(30,58,95,.15); color: #1E3A5F;")
css = css.replace("rgba(16,185,129,.15); color: #6EE7B7;", "rgba(22,163,74,.15); color: #16A34A;")
css = css.replace("rgba(245,158,11,.15); color: #FCD34D;", "rgba(217,119,6,.15); color: #D97706;")
css = css.replace("rgba(239,68,68,.15);  color: #FCA5A5;", "rgba(220,38,38,.15);  color: #DC2626;")
css = css.replace("rgba(124,58,237,.15); color: #C4B5FD;", "rgba(15,118,110,.15); color: #0F766E;")
css = css.replace("rgba(107,114,128,.15); color: #9CA3AF;", "rgba(100,116,139,.15); color: #64748B;")

# Cls badges
css = css.replace("rgba(79,114,255,.3)", "rgba(30,58,95,.3)")
css = css.replace("rgba(16,185,129,.3)", "rgba(22,163,74,.3)")
css = css.replace("rgba(245,158,11,.3)", "rgba(217,119,6,.3)")
css = css.replace("rgba(124,58,237,.3)", "rgba(15,118,110,.3)")
css = css.replace("rgba(107,114,128,.1)", "rgba(100,116,139,.1)")
css = css.replace("rgba(107,114,128,.2)", "rgba(100,116,139,.2)")

# Result pass/fail
css = css.replace("rgba(16,185,129,.4)", "rgba(22,163,74,.4)")
css = css.replace("rgba(239,68,68,.4)", "rgba(220,38,38,.4)")

# Tables
css = css.replace("border-bottom: 1px solid rgba(46, 61, 107, 0.4);", "border-bottom: 1px solid var(--color-border);")
css = css.replace("background: rgba(33, 45, 74, 0.4);", "background: var(--color-surface-2);")
css = css.replace("border-bottom: 1px solid rgba(46,61,107,.4);", "border-bottom: 1px solid var(--color-border);")

# Data table specific columns
css = css.replace("color: #93B4FF;", "color: #1E3A5F;")
css = css.replace("color: #C4B5FD;", "color: #0F766E;")
css = css.replace("color: #6EE7B7;", "color: #16A34A;")

# Drop zone hover
css = css.replace("rgba(79,114,255,.05)", "rgba(30,58,95,.05)")

# classify-chip
css = css.replace("rgba(79,114,255,.4)", "rgba(30,58,95,.4)")
css = css.replace("rgba(79,114,255,.08)", "rgba(30,58,95,.08)")

# generate-section
css = css.replace("rgba(124,58,237,.06)", "rgba(15,118,110,.06)")
css = css.replace("rgba(79,114,255,.25)", "rgba(30,58,95,.25)")

# report-hero
css = css.replace("rgba(79,114,255,.1)", "rgba(30,58,95,.1)")
css = css.replace("rgba(124,58,237,.08)", "rgba(15,118,110,.08)")
css = css.replace("rgba(79,114,255,.2)", "rgba(30,58,95,.2)")

# hero title
css = css.replace("background: linear-gradient(135deg, #fff 40%, #93B4FF);", "background: linear-gradient(135deg, var(--color-primary) 40%, #64748B);")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated successfully")
