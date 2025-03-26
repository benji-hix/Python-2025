"""Roman to Integer"""

import numbers

# O(N) Solution
def roman_to_integer(s: str) -> int:
    """
    Given a Roman numeral, convert to a string.

    Args:
        s (str): Number in roman numeral form.

    Returns:
        int: Number as integer.
    """
    roman_values = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
    }
    usable_string = s[::-1]
    number = 0
    for index, character in enumerate(usable_string):
        if index == 0: # guard clause for first character
            number += roman_values[character]
            continue
        if character == 'I' and usable_string[index - 1] in ['V', 'X']:
            number -= roman_values[character]
            continue
        if character == 'X' and usable_string[index - 1] in ['L', 'C']:
            number -= roman_values[character]
            continue
        if character == 'C' and usable_string[index - 1] in ['D', 'M']:
            number -= roman_values[character]
            continue
        else:
            number += roman_values[character]
    return number

print(roman_to_integer('LVIII'))