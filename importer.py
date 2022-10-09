from pyexcel_ods3 import get_data

from baxtage.baxtage_dataclasses import *

ods_file = r"E:\Dev\baxtage\lineup\static\baxtage.ods"


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
        wkbook = get_data(ods_file)
        # self.artist_dict = ArtistDict()
        performances = ...
        self.performance_dict = PerformanceDict()




wkbok = Wkbook(ods_file)

...
