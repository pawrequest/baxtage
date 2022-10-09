# from baxtage.utils_pss.workbook_importer import Wkbook
from pathlib import Path
import baxtage.utils_pss.wi as wi

baxtage_config = r'E:\Dev\baxtage\lineup\static\baxtage.ods'
amdesp = r'E:\Dev\baxtage\lineup\static\amdespplay.ods'

wkbook = wi.Wkbook(baxtage_config)
# print(f"{wkbook.sheets=}")
# wkbook = wi.Wkbook(amdesp)
...
