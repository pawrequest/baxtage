# from baxtage.utils_pss.workbook_importer import Wkbook
import pickle
from pathlib import Path
import baxtage.utils_pss.workbook_importer as wi
from baxtage.utils_pss.utils_pss import Config


baxtage_config = r'E:\Dev\baxtage\lineup\static\baxtage.ods'
amdesp = r'E:\Dev\baxtage\lineup\static\amdespplay.ods'
pc = r'E:\Dev\baxtage\baxtage\flood.ods'
pickled = r'e:\dev\baxtage\lineup\static\pickeled'

wkbook = wi.Wkbook(baxtage_config)
# print(f"{wkbook.sheets=}")
# wkbook = wi.Wkbook(amdesp)
# c = Config(baxtage_config, 'artists')
# wkbook = wi.Wkbook(pc)
ami  = vars(wkbook.sheets.artists.items)
with open('pickled_wkbook.txt', 'wb') as fh:
    pickle.dump(wkbook, fh)
...
