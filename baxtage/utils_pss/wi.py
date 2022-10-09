from dataclasses import dataclass

from pyexcel_ods3 import get_data


class Wkbook:
    def __init__(self, ods_file):
        wkbook: dict = get_data(ods_file)  # empty cells fuck me up debug
        wkbook = {sheet_name: [row for row in sheet if row] for sheet_name, sheet in
                  wkbook.items()}  # remove empty rows
        self.meta = WkBookMeta(wkbook)
        sheets = [Sheet(rows, sheet_name) for sheet_name, rows in wkbook.items()]
        self.sheets = SheetCollection(sheets)

    def __str__(self):
        return f"{len(vars(self.sheets))} Sheet Objects: {[sheet_name for sheet_name in vars(self.sheets)]}"


class Sheet:
    def __init__(self, rows, sheet_name):
        self.sheet_name = sheet_name
        meta_row = rows[0]
        if meta_row[0] == 'cols':
            headers = False
        else:
            headers = True
        self.meta = SheetMeta(rows, headers=headers)
        self.meta.sheet_name=sheet_name
        self.items = {k: SheetItem(k, v) for k, v in self.meta.items_dict.items()}


    def __str__(self):
        return f"{self.sheet_name}"

@dataclass
class SheetItemCol:
    ...


@dataclass
class SheetItem:
    def __init__(self, k,v):
            setattr(self, k, v)

    def __str__(self):
        return f"{vars(self)}"

# for k, v in **kwargs.items(): # to allow multiple values?

@dataclass
class SheetCollection:
    def __init__(self,sheets):
        super(SheetCollection, self).__init__()
        for sheet in sheets:
            setattr(self, sheet.sheet_name, sheet)

    def __str__(self):
        return f'Sheet Collection with {len(vars(self))} sheets : {[sheet_name for sheet_name in vars(self)]}'

@dataclass
class WkBookMeta:
    def __init__(self, wkbook: dict):
        self.wkbook: dict = wkbook


class SheetMeta:
    def __init__(self, rows:list, headers=True):
        # break list of rows into [meta (. header), body]
        self.meta: list = rows[0]
        self.items_dict = {}
        if headers:
            self.headers: list = rows[1]
            self.body: list = rows[2:]
            for row in self.body:
                row_dict = {header: row[c] for c, header in enumerate(self.headers)}
                self.items_dict.update({row[0]: row_dict})

        else:
            self.headers = [row[0] for row in rows[1:]]
            self.body: list = [row[1:] for row in rows[1:] if row]
            for c, header in enumerate(self.headers):
                k = header
                v = self.body[c]
                self.items_dict.update({k: v})
    ...
    def __str__(self):
        return f"Sheet Meta info for {self.sheet_name}"

        # get meta tags from meta row if they exist
        # self.meta_tags = {cell: self.meta[c + 1] for c, cell in enumerate(self.meta) if c % 2 == 0}
