from baxtage.utils_pss.utils_pss import ImportedWkbook
from pathlib import Path


baxtage_config = r'E:\Dev\baxtage\lineup\static\baxtage.ods'

# ods_file = Path.joinpath()


# imps = get_workbook(baxtage_config)
# for artist in imps:

#     artist.
# ters = testy(r'E:\Dev\baxtage\lineup\static\test.ods')
# baxtage = testy(baxtage_config)

amdesp = r'E:\Dev\baxtage\lineup\static\amdespplay.ods'

# # imps = ImportedWkbook(amdesp)
# imps = ImportedWkbook(baxtage_config, headers = True, meta=True)
# imps.get_rows(baxtage_config)
# ...

# imps = ImportedWkbook(baxtage_config,meta=True)
imps = ImportedWkbook(amdesp)
print (imps)
...

'''


'''



'''
get workbook from sheet using package
'''

'''


    def sheet_maker(self, sheet):
        sheet_data = self.get_rows(sheet)
        sheet_list = [{k: v} for k, v in sheet_data.items()]  # if k[0] != '_' # is needed? #
        for sheet in sheet_list:
            sheet_obj = self.Sheet(sheet_list)
                
                
    class Sheet:
        def __init__(self, dict):
            for k, v in dict.items():
                setattr(self, k, v)

    def get_sheet_objs(self):
        ods_file = self.ods_file
        wkbook_dict = get_data(ods_file)
        if len(wkbook_dict.keys())==1:

            ...
        for sheet in wkbook_dict.keys():
            wkbook_sheet = self.Sheet(self, sheet)
            if len(wkbook_dict.keys())==1:
                setattr(self, f"Sheet :{sheet}", wkbook_sheet)  # debug
            else:
                setattr(self.wkbook, sheet, wkbook_sheet) # debug


'''