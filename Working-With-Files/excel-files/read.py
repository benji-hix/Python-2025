"""Read/Write Excel File"""

from openpyxl import Workbook, load_workbook
from pathlib import Path

wkbk_name = ''

def clean_str(str: str) -> str:
    return str.strip("'").strip('"')

def get_dir_path() -> Path:
    while True:
        try:
            dir_str = clean_str(input('\n| Paste directory path:\n| '))
            target_dir = Path(dir_str)
            if not target_dir.is_dir():
                raise FileNotFoundError(f'| {dir_str} not found.')
            else:
                print('| Directory loaded successfully.')
                break
        except FileNotFoundError as e:
            print(f'| Error: {e}')

    return target_dir

def print_dir_files(dir: Path) -> None:
    dir_files = [
        f for f in dir.iterdir() 
        if f.is_file() and f.suffix == '.xlsx' and not f.name.startswith('~$')
        ] 
    if not dir_files:
        print('| No files found.')
    else:
        print('| Files found:')
        for f in dir_files:
            print(f'|····{f.name}')
    return None

def get_wkbk_path(dir: Path) -> str:
    print_dir_files(dir)
    while True:
        try:
            wkbk_name = clean_str(input('\n| Select file:\n| '))
            if not wkbk_name.endswith('.xlsx'):
                wkbk_name += '.xlsx'
            wkbk_path = dir / wkbk_name
            if not wkbk_path.exists():
                raise FileNotFoundError(f'| {wkbk_name} not found.')
            else:
                break
        except FileNotFoundError as e:
            print(f'| Error: {e}')
    return wkbk_path

def open_wkbk(wkbk_path: Path) -> Workbook:
    print(f'| {wkbk_name} loaded successfully')
    return load_workbook(str(wkbk_path))

def print_wksheets(wkbk: Workbook) -> None:
    print('| Worksheets found:')
    for s in wkbk.sheetnames:
        print(f'|····{s}')
    return None

def open_wksheet(wkbk_path: Path) -> Workbook:
    current_wkbk = open_wkbk(wkbk_path)
    print_wksheets(current_wkbk)
    while True:
        try:
            sheet_name = clean_str(input('\n| Select worksheet:\n| '))
            if sheet_name not in current_wkbk.sheetnames:
                raise FileNotFoundError(f'{sheet_name} not found.')
            else:
                sheet = current_wkbk[f'{sheet_name}']
                break
        except FileNotFoundError as e:
            print(f'| Error: {e}')
        
    print(f'| {sheet_name} loaded successfully.')
    return sheet

def open_workbook() -> Workbook:
    """
    Open correct file and return

    Args:
        file_name (str): Name of file

    Returns:
        Workbook: Workbook to work with
    """

    dir_path = get_dir_path()
    wkbk_path = get_wkbk_path(dir_path)
    current_wksht = open_wksheet(wkbk_path) 

    return current_wksht