# from baxtage.utils_pss.workbook_importer import Wkbook
from pathlib import Path
import baxtage.utils_pss.workbook_importer as wi
from baxtage.utils_pss.utils_pss import Config

baxtage_config = r'E:\Dev\baxtage\lineup\static\baxtage.ods'
amdesp = r'E:\Dev\baxtage\lineup\static\amdespplay.ods'
pc = r'E:\Dev\baxtage\baxtage\flood.ods'


wkbook = wi.Wkbook(baxtage_config)
# print(f"{wkbook.sheets=}")
# wkbook = wi.Wkbook(amdesp)
# c = Config(baxtage_config, 'artists')
# wkbook = wi.Wkbook(pc)

...
