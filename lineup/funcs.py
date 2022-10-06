from baxtage.utils_pss.utils_pss import get_from_ods

class Importer:
    def __init__(self, input_format):
        self.input_format = input_format
    def get_data(self):
        inform = self.input_format
        if inform == 'ods':
            self.perf_dict = get_from_ods(r'E:\Dev\baxtage\lineup\static\baxtage.ods', 'performances', meta=True, headers=True)
        elif inform == ' excel':
            ... # go get excel
        elif inform == ' email':
            ... # factory method i guess


imp=Importer('ods')
imp.get_data()
...