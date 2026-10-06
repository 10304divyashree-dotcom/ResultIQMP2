import sys
sys.path.insert(0, '.')
import os
from services.analyser import analyse_workbook
from services.reporter import generate_report

files_to_test = [
    'Reference/Original_1 ExcelSpreadsheet.xlsx',
    'uploads/f2172c492a00475fafa8d49a74846ee2.xls',
    'uploads/fea5a48088bd4c03ae4f0108ad7d0d54.xlsx',
]

for f in files_to_test:
    if not os.path.exists(f):
        print(f"Skipping {f}, does not exist")
        continue
    print(f"\n=================== Testing {f} ===================")
    sheets_info = analyse_workbook(f)
    print(f"Analysed sheets: {len(sheets_info)}")
    for s in sheets_info:
        name = s['name']
        marks_cols = [c['name'] for c in s.get('columns', []) if c.get('classification') == 'marks']
        print(f"  Sheet '{name}': rows={s.get('row_count')}, marks cols ({len(marks_cols)}): {marks_cols}")
        if marks_cols:
            out_file = f"scratch/test_out_{os.path.basename(f)}_{name}.xlsx"
            stats = generate_report(f, sheets_info, name, out_file)
            print(f"    Report generated: total={stats['total_students']}, appeared={stats['appeared']}, pass={stats['pass_count']}, fail={stats['fail_count']}, pass_rate={stats['pass_rate']}%")
