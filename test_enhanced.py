import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter

# Test openpyxl patch and styling
import openpyxl.worksheet._writer as ws_writer
from openpyxl.cell._writer import _set_attributes
from xml.etree.ElementTree import Element, SubElement
from openpyxl.compat import safe_string

_orig_write_cell = ws_writer.write_cell

def _patched_write_cell(xf, worksheet, cell, styled=None):
    formula_cache = getattr(worksheet, '_formula_values', {})
    coord = cell.coordinate
    if cell.data_type == 'f' and coord in formula_cache:
        cached = formula_cache[coord]
        value, attributes = _set_attributes(cell, styled)
        el = Element('c', attributes)
        formula = SubElement(el, 'f')
        formula.text = value[1:] if str(value).startswith('=') else str(value)
        v = SubElement(el, 'v')
        v.text = safe_string(cached)
        xf.write(el)
    else:
        _orig_write_cell(xf, worksheet, cell, styled)

ws_writer.write_cell = _patched_write_cell

from services.analyser import analyse_workbook
from services.reporter import generate_report

src = 'Reference/Original_1 ExcelSpreadsheet.xlsx'
ws_json = analyse_workbook(src)
out = 'scratch/test_out/enhanced_report.xlsx'

# Run generate_report with enhanced formatting
# Let's inspect what Output ExcelSpreadsheet has
ref_wb = openpyxl.load_workbook('Reference/Output ExcelSpreadsheet.xlsx', data_only=True)
ref_ws = ref_wb['Table 1']

print("Reference row 50:", [ref_ws.cell(50, c).value for c in range(1, 8)])
print("Reference row 52:", [ref_ws.cell(52, c).value for c in range(1, 8)])
