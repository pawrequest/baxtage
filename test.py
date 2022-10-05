from dataclasses import make_dataclass

Position = make_dataclass('Position',['name','long','lat'])
oslo = Position('osloo','112','444')
...

name = 'dynnie'
attrs = ['blah','any']
Noma = make_dataclass(name,attrs)

nmoa = Noma()
...

