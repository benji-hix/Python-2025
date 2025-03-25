"""Palindrome Number"""

def is_palindrome(x: int) -> bool:
    '''
    Given an integer, return true if it is a palindrome and
    false otherwise.
    
    Args:
        x: Integer

    Returns:
        bool
    '''

    if x < 0: # Guard clause
        return False
    
    digit_list = list(map(int, str(x)))

    # This solution failed because of time constraints
    # index = 0
    # while index <= len(digit_list)/2:
    #     if index == len(digit_list) / 2:
    #         continue
    #     if digit_list[index] != digit_list[-1 - index]:
    #         return False
    #     index += 1
    # return True

    left = 0
    right = len(digit_list) - 1

    while left < right:
        if digit_list[left] != digit_list[right]:
            return False
        left += 1
        right -= 1

    return True

# Cleaner solution with faster runtime
def is_palindrome_optimized(x: int) -> bool:
    """
    Determine whether a number is a palindrome

    Args:
        x (int): Integer value

    Returns:
        bool: True or False
    """
    if x < 0: 
            return False
    original = str(x)
    return original == original[::-1]
