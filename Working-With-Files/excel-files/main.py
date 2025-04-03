from venv import create
from generate_file import create_excel

def main() -> None:
    filename = input('Enter filename: \n')
    sheetname = input('Enter sheet title: \n')
    create_excel(filename,sheetname)

if __name__ == "__main__":
    main()
