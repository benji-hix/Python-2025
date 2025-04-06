"""Read/Write Excel File"""

from openpyxl import Workbook, load_workbook
from pathlib import Path

def get_path() -> Path:
    while True:
        try:
            dir_str = input('\n| Paste directory path:\n| ').strip('"').strip("'")
            target_dir = Path(dir_str)
            if not target_dir.is_dir():
                raise FileNotFoundError(f'| The directory {dir_str} does not exist.')
            print('| Directory loaded successfully.')
            break

        except FileNotFoundError as e:
            print(f'Error: {e}')

    return target_dir

def print_dir_files(dir: Path) -> None:
    dir_files = [
        f for f in dir.iterdir() 
        if f.is_file() and f.suffix == '.xlsx' and not f.name.startswith('~$')
        ] 
    print('| Files found:')
    for f in dir_files:
        print(f'    | {f.name}')
    return None

def clean_str(str: str) -> str:
    return str.strip("'").strip('"')

def get_wkbk(dir: Path) -> str:
    print_dir_files(dir)
    wkbk_name = clean_str(input('\n| Select file:\n| '))
    if not wkbk_name.endswith('.xlsx'):
        wkbk_name += '.xlsx'
    return wkbk_name

def get_wksheet(wkbk_name: str, dir: Path) -> Workbook:
    wkbk_path = str(dir) + '\\' + wkbk_name


    workbook = load_workbook(wkbk_path)
    print(f'\n| {wkbk_name} loaded successfully.')
    print('| Worksheets found:')
    for s in workbook.sheetnames:
        print(f'    | {s}')

    sheet_name = input('\n| Select worksheet:\n| ')
    sheet = workbook[f'{sheet_name}']
    print(f'| {sheet_name} loaded successfully.')
    return sheet

def open_workbook(wkbk_name: str='') -> Workbook:
    """
    Open correct file and return

    Args:
        file_name (str): Name of file

    Returns:
        Workbook: Workbook to work with
    """

    dir = get_path()

    wkbk_name = get_wkbk(dir)

    wksht = get_wksheet(wkbk_name, dir) 

    print('\n')