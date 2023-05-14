"""
sheet row #1 is meta.
if headers=True (default) then row#2 is headers
otherwise column A is headers

if A1 == 'cols' then headers = False
B1 reserved for unknown meta use in future
C1 onwards are meta tags - even cells are keys, odds are values
"""

from dataclasses import dataclass

from pyexcel_ods3 import get_data


##
##
# TODO: empty cells fuck me right up, need to fix upstream as imporssible to recreate list order once empty cells removed


class Wkbook:
    def __init__(self, ods_file):
        wkbook: dict = get_data(ods_file, keep_trailing_empty_cells=True)  # empty cells debug
        wkbook = {sheet_name: [row for row in sheet if row] for sheet_name, sheet in
                  wkbook.items()}  # remove empty rows
        self.meta = WkBookMeta(wkbook)
        sheets = [Sheet(sheet, sheet_name) for sheet_name, sheet in wkbook.items()]
        self.sheets = SheetCollection(sheets)

    def __str__(self):
        return f"{len(vars(self.sheets))} Sheet Objects: {[sheet_name for sheet_name in vars(self.sheets)]}"


class Sheet:
    def __init__(self, sheet, sheet_name):
        self.sheet_name = sheet_name
        meta_row = sheet[0]
        if meta_row[0] == 'cols':
            headers = False
        else:
            headers = True
        self.meta = SheetMeta(sheet, headers=headers)
        self.meta.sheet_name = sheet_name
        # self.items = {k: SheetItem(k, v) for k, v in self.meta.items_dict.items()}
        self.items = SheetItemCol(self.meta.items_dict)

    def __str__(self):
        return f"{self.sheet_name}"


@dataclass
class SheetItemCol: # all the items (rows) on a sheet
    def __init__(self, items_dict:dict):
        for k, v in items_dict.items():
            if not k:
                continue
            sheet_item = SheetItem(k,v)
            setattr(self,k,sheet_item)

    def __str__(self):
        return f"Collection of {len(vars(self))} SheetItems"


@dataclass
class SheetItem: # an item on the sheet
    def __init__(self, k, v:dict):
        for x, y in v.items():
            if not x:
                continue
            sheet_prop = SheetProp(x,y)
            setattr(self, x, sheet_prop)

    def __str__(self):
        return f"{len(vars(self))} SheetProps"

@dataclass
class SheetProp: # a property  (column) of the item
    def __init__(self, k, v):
        if k:
            setattr(self, k, v)
    def __str__(self):
        return f"SheetProp - {vars(self)}"

# for k, v in **kwargs.items(): # to allow multiple values?

@dataclass
class SheetCollection:
    def __init__(self, sheets):
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
    def __init__(self, rows: list, headers=True):
        # break list of rows into [meta (. header), body]
        self.meta: list = rows[0]
        self.items_dict = {}
        if headers:
            self.headers: list = rows[1]
            self.body: list = rows[2:]

            """
            # zip useful here?
            for row in self.body:
                zippy = zip(self.headers, row)
                 print(set(zippy))
            """

            for row in self.body:
                if len(row) == len(self.headers):
                    row_dict = {header: row[c] for c, header in enumerate(self.headers) if row[c]}
                    if row[0]:
                        self.items_dict.update({row[0]: row_dict})
                else:
                    print(
                        f"Error - length mismatch, skipped row \n (there are {len(self.headers)} header(s) and {row} has {len(row)} item(s)")
                    continue

            ## THIS COMP DOES ABOVE LOOP...but no valueerror because can't make 'else' work?
            # sd = {header:row[c] for c, header in enumerate(self.headers) for row in self.body if len(row) == len(self.headers)}


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
