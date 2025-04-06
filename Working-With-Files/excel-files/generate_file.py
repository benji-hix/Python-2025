from openpyxl import Workbook

def create_excel(filename: str = 'output.xlsx', sheet_title: str = 'DataSheet') -> Workbook:

    wb: Workbook = Workbook()

    ws = wb.active
    wb.title = sheet_title

    headers : list[str] = ['Item', 'Cost', 'Date']
    ws.append(headers)

    items : list[list] = [
        ['Fitness', 200, 'Date 3/2'],
        ['Coffee', 50, 'Date 3/4'],
        ['Social', 200, 'Date 3/6']
    ]

    for row in items:
        ws.append(row)

    wb.save(filename)

    return wb