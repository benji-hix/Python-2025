from openpyxl import Workbook
from datetime import datetime

def get_user_input(data_type: str):
    if data_type == 'str':
        while True:
            try:
                user_input = input("| Enter text: ").strip()
                
                if not user_input:
                    raise ValueError("Input cannot be empty.")
                
                print(f"| You entered: {user_input}")
                break

            except ValueError as e:
                print(f"| Error: {e}")
        return user_input
    
    elif data_type == 'int':
        while True:
            try:
                user_input = input("| Enter number: ").strip()
                user_number = int(user_input)  # Will raise ValueError if input is not a valid integer
                print(f"| You entered: {user_number}")
                break
            except ValueError:
                print("| Error: please input a number.")
        return user_number

    elif data_type == 'datetime':
        while True:
            try:
                user_input = input("| Enter a date (YYYY-MM-DD): ").strip()
                user_date = datetime.strptime(user_input, "%Y-%m-%d")  # Will raise ValueError if format is wrong
                print(f"| You entered: {user_date.date()}")
                break
            except ValueError:
                print("| Invalid date format. Please use YYYY-MM-DD.")
        return user_date
    return None