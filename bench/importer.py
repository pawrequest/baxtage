# import openpyxl as openpyxl
# from pyexcel_ods3 import get_data
import pandas as pd

ods_file = r"/lineup/static/baxtage.ods"

# def UseOpenpyxl(file_name):
#     wb = openpyxl.load_workbook(file_name, read_only=True)
#     sheet = wb.active
#     rows = sheet.rows
#     # first_row = [float(cell.value) for cell in next(rows)]
#     first_row = [cell.value for cell in next(rows)]
#     data = []
#     for row in rows:
#         record = {}
#         for key, cell in zip(first_row, row):
#             if cell.data_type == 's':
#                 record[key] = cell.value.strip()
#             else:
#                 record[key] = float(cell.value)
#         data.append(record)
#     return data

def get_artist_dict(wkbook):
    for artist in wkbook['artists'][2:]:
        if not artist:
            break
        name, phone, instrument = artist[0], artist[1], artist[2]
        artist_obj = Artist(name=name, phone=phone, instrument=instrument)


# def make_perfobj_dict(wkbook):
#     headers = wkbook['performances'][1]
#     performances = wkbook['performances'][2:]
#     # performances_dict = {
#     #     act_name:attrs for act_name, attrs in performances
#     # }
#
#     attr_headers = headers[1:]
#
#     for performance in performances:
#         if not performance:  # purge empty rows
#             continue
#         act_name = performance[0]
#         perf_dict = {attr_headers[c]: attr for c, attr in enumerate(performance[1:])}
#         perf_obj = Performance(**perf_dict)
#
#
#         perf_obj_dict.performances.update({act_name: perf_obj})

def make_perfobj_dict(self,wkbook):
    meta_data = wkbook['performances'[0]]
    headers = wkbook['performances'][1]
    attr_headers = headers[1:]
    performances = wkbook['performances'][2:]

    for performance in performances:
        if not performance:  # purge empty rows
            continue
        act_name = performance[0]
        perf_dict = {attr_headers[c]: attr for c, attr in enumerate(performance[1:])}
        perf_obj = Performance(**perf_dict)

        self.performances.update({act_name: perf_obj})

class Wkbook:
    def __init__(self, ods_file):
        # wb = openpyxl.load_workbook(ods_file, read_only=True)
        # wkbook = get_data(ods_file)

        wkbook = pd.read_excel(ods_file, index_col=None, header=None)
        # self.artist_dict = ArtistDict()
        performances = ...
        self.performance_dict = PerformanceDict()




wkbok = Wkbook(ods_file)

...
