import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app
from models import db, User, UploadedFile, Report
from services.analyser import analyse_workbook
from services.reporter import generate_report
import os, json, shutil, openpyxl

app = create_app('development')
with app.app_context():
    # 1. Analyse
    src = 'Reference/Original_1 ExcelSpreadsheet.xlsx'
    ws_json = analyse_workbook(src)
    print('Worksheets JSON:')
    for s in ws_json:
        print('Sheet:', s['name'], 'header_row:', s.get('header_row_index'))
        for col in s.get('columns', []):
            print(f"  Col: {col['name']} -> {col.get('classification')}")

    # 2. Generate report
    os.makedirs('scratch/test_out', exist_ok=True)
    out_path = 'scratch/test_out/downloaded_report.xlsx'
    stats = generate_report(src, ws_json, 'Table 1', out_path)
    print('Generated successfully.')

    # 3. Inspect the generated report
    wb = openpyxl.load_workbook(out_path, data_only=False)
    ws = wb['Table 1']
    print(f'max_row={ws.max_row}, max_col={ws.max_column}')
    for r in range(48, ws.max_row + 1):
        row_vals = [ws.cell(r, c).value for c in range(1, ws.max_column + 1)]
        print(f'Row {r}: {row_vals}')

    # Check with data_only=True
    wb_data = openpyxl.load_workbook(out_path, data_only=True)
    ws_data = wb_data['Table 1']
    print('\nWith data_only=True:')
    for r in range(48, ws_data.max_row + 1):
        row_vals = [ws_data.cell(r, c).value for c in range(1, ws_data.max_column + 1)]
        print(f'Row {r}: {row_vals}')
