"""Valid Parentheses"""


def test_valid_parentheses(s: str) -> bool:
    dict = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    stack = []
    for char in s:
        if char in dict.keys():
            stack += dict[char]
        if char in dict.values():
            if stack.pop() != char:
                return False
    return stack == []

print(test_valid_parentheses('()[{]}'))
