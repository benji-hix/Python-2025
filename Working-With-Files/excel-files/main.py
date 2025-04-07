from open import open_spreadsheet
from read import print_row

def main() -> None:
    current_wksht = open_spreadsheet()
    print_row(current_wksht)

if __name__ == "__main__":
    main()
