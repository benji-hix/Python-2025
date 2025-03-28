"""Valid Parentheses"""


def test_valid_parentheses(s: str) -> bool:
    """Check a string for sets of complete parentheses.

    Args:
        s (str): Str containing some number of parentheses.

    Returns:
        bool: True or false depending on whether parentheses match criteria.
    """
    parentheses_key = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    stack = []
    for char in s:
        if char in parentheses_key:
            stack += parentheses_key[char]
        if char in parentheses_key.values():
            if stack.pop() != char:
                return False
    return stack == []

print(test_valid_parentheses('()[{]}'))
