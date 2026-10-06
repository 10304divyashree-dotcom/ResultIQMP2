"""Update the database record with the corrected worksheets JSON."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.analyser import analyse_workbook
import sqlite3

filepath = 'uploads/531a290cd0894b9196de8a1116a6296e.xlsx'
new_worksheets = analyse_workbook(filepath)

conn = sqlite3.connect('resultiq.db')
c = conn.cursor()
c.execute('UPDATE uploaded_files SET worksheets = ?, is_valid = 1 WHERE id = ?',
          (json.dumps(new_worksheets), 'ceb5da42-4ccd-4919-80bd-f45e598fe599'))
conn.commit()
print('Updated worksheets JSON in database.')

# Verify
row = c.execute('SELECT worksheets FROM uploaded_files WHERE id = ?',
                ('ceb5da42-4ccd-4919-80bd-f45e598fe599',)).fetchone()
ws = json.loads(row[0])
for s in ws:
    marks = [col['name'] for col in s.get('columns', []) if col.get('classification') == 'marks']
    print("Sheet:", s['name'], "marks_cols:", marks)
conn.close()
