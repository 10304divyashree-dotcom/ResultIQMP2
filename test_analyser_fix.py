"""Quick test of analyser fix for multi-row headers."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.analyser import analyse_workbook

filepath = 'uploads/531a290cd0894b9196de8a1116a6296e.xlsx'
results = analyse_workbook(filepath)

for s in results:
    sheet_name = s.get('name', '?')
    hdr = s.get('header_row_index', '?')
    rc = s.get('row_count', '?')
    print(f"Sheet: {sheet_name}, header_row={hdr}, row_count={rc}")
    for col in s.get('columns', []):
        cn = col.get('name', '?')
        cl = col.get('classification', 'N/A')
        print(f"  {cn} -> {cl}")
