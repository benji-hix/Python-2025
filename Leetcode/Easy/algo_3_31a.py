"""Find the Index of the First Occurence in a String"""

# O(N*M) Solution
def find_first_occurence(haystack: str, needle: str) -> int:
    """
    Given two strings needle and haystack, return the index of the first 
    occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Args:
        haystack (str): Input string.
        needle (str): Substring to find.

    Returns:
        int: Index of first occurence of needle.
    """
    
    print('\n')
    slow = 0
    while slow < len(haystack):
        print(f'| Current char: {haystack[slow]}')
        print(f'| Current index: {slow}\n')
        # If the start of substring is identified, start comparing character
        if haystack[slow] == needle[0]:
            print('| Initiate substring check.')
            if len(haystack[slow:]) >= len(needle) and all(char == haystack[index + slow] for index, char in enumerate(needle)):
                print('| Substring check successful.')
                print(f'\n| Returned index: {slow}\n')
                return slow
            else:
                print('| Substring check failed. \n| Continue haystack loop.')
                slow += 1
                continue
        print('| Continue haystack loop.')
        slow += 1
    print('\n| Returned index: -1\n')
    return -1

test = "nsadfneasdfnennuiasdp"
test1 = "ennui"
find_first_occurence(test, test1)