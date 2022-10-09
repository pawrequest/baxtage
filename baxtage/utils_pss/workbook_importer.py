from dataclasses import dataclass

from pyexcel_ods3 import get_data

from baxtage.utils_pss.utils_pss import strip_strings


@dataclass()
class WkBookMeta:
    # def __init__(self, header, meta, wkbook, sheet_name):
    def __init__(self, header_bool, meta_bool, ods_file, sheet_name):
        self.header_bool: bool = header_bool
        self.meta_bool: bool = meta_bool
        self.wkbook = get_data(ods_file)
        self.sheet_name: str = sheet_name
        self.meta_tags: dict = {}


@dataclass
class SheetMeta:
    def __init__(self, ods_file, sheet_name, header_bool=False, meta_bool=False):
        rows: list = get_data(ods_file)[sheet_name]
        if meta_bool and header_bool:
            self.meta: list = rows[0]
            self.headers = rows[1]
            self.body = rows[2]
        elif meta_bool:
            self.meta: list = rows[0]
            self.headers: list = [row[0] for row in rows[1:]]
            self.body = [row[1:] for row in rows[1:]]
        elif header_bool:
            self.headers: list = rows[0]
            self.body: list = rows[1:]
        else:
            self.headers: list = [row[0] for row in rows]
            self.body: list = [row[1:] for row in rows]


@dataclass
class MetaTag:
    def __init__(self, k: str, v):
        setattr(self, k, v)


@dataclass
class Meta_list:
    tags: list[MetaTag]  # doesnt work? debug


@dataclass
class MetaDict:
    tags: dict[MetaTag]


def make_meta_tags(meta_list):
    for e, cell in iter(enumerate(meta_list)):
        if cell:  # purge empty
            if e == 0 or e % 2 == 0:  # if there is text in a cell, and that cell is either the first or an even numbered one
                yield MetaTag(cell, meta_list[e + 1])


class Wkbook:
    def __init__(self, ods_file, headers=True, meta=False):
        ...
    def __str__(self):
        ...
        # return f'Workbook Importer with {len(self.sheets)} sheets'

    def __repr__(self):
        ...
        # return f'Workbook Importer with {len(self.sheets)} sheets'


@dataclass()
class SheetItem:
    def __init__(self, attr_name, attr):
        setattr(self, attr_name, attr)


class Sheet:
    def __init__(self, sheet_name: str, sheet, meta_bool: bool = False, header_bool: bool = True):
        # self.meta_dict = WkBookMeta(header, meta, sheet, sheet_name)
        self.run()

    def __str__(self):
        return f'Sheet Object: {self.meta_dict.sheet_name}'

    def __repr__(self):
        return f'Sheet Object: {self.meta_dict.sheet_name}'

    def run(self):
        # setattr(self.meta_dict, 'rows', self.get_rows())
        # self.get_meta_dict()
        # self.get_items()
        ...


def get_items(self):  # makes sheet objects for each cell in body
    for item in self.meta_dict.body:
        for c, attribute in enumerate(item):
            k = self.meta_dict.headers[c]
            v = attribute
            obj = SheetItem(k, v)
            setattr(self, item[0], obj)


# def get_rows(self):  # uses get_data from pyexcel_ods3,  takes sheetname)
#     wkbook = self.meta_dict.wkbook
#     sheet_name = self.meta_dict.sheet_name
#     rows = wkbook[sheet_name]
#     rows = [row for row in rows if len(row) > 0]
#     rows = strip_strings(rows)  # remove leading and trailing whitepsace from any string fields
#     return rows


def get_meta_dict(self):  # makles self.headers meta and body attrrs
    metab = self.meta_dict.meta_bool
    headersb = self.meta_dict.headers
    rows = self.meta_dict.rows

    if metab and headersb:  # assign row-numbers for meta, headers, and start of body
        meta_row, header_row, body_row = 0, 1, 2
    elif metab:
        meta_row, header_row, body_row = 0, None, 1
    elif headersb:
        meta_row, header_row, body_row = None, 0, 1
    else:
        meta_row, header_row, body_row = None, None, 0
    if metab:
        meta_list = self.meta_dict.rows[meta_row]
        meta_dict = self.get_meta_tags(meta_list)
        for k, v in meta_dict.items():
            meta_tag = MetaTag(k, v)
            setattr(self.meta_dict.meta_tags, k, meta_tag)
        # setattr(self.meta_dict, 'meta_tags', meta_row_content)

    if headersb:
        headers = [cell for cell in rows[header_row]]
        setattr(self.meta_dict, 'headers', headers)
    body = [cell for cell in rows[body_row:]]
    setattr(self.meta_dict, 'body', body)

    # def get_meta_tags(self, meta_list):
    #     if not self.meta_dict.meta:
    #         return False
    #     meta_dict = {}
    #     for e, cell in enumerate(meta_list):
    #         if cell:
    #             if e == 0 or e % 2 == 0:  # if there is text in a cell, and that cell is either the first or an even numbered one
    #                 meta_dict.update({cell: meta_list[e + 1]})
    #                 # setattr(self.meta, cell, meta_list[e + 1])
    #     # self.meta = meta_dict
    #     return meta_dict

    def get_body(self):
        for row in self.meta_dict.body:
            cells = [cell for cell in row if len(row) > 0]
            for c, cell in enumerate(cells):
                if self.meta_dict.headers:  # if we have headers
                    k = self.meta_dict.headers[c]  # then use them as keys and all cols as vals
                    setattr(self, k, cell)
                else:
                    for d, ocell in enumerate(cells[1:]):
                        k = cells[0]  # otherwise we use the first column as keys and other cols as vals
                        setattr(self, k, ocell)
