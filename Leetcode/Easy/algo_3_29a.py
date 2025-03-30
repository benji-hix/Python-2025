"""Remove Element"""

# O(n) solution
def remove_element(nums: list[int], val: int) -> int:
    """
    Given an integer array nums and an integer val, 
    remove all occurrences of val in nums in-place. 
    The order of the elements may be changed. 
    Then return the number of elements in nums which are not equal to val.

    Args:
        nums (list[int]): Input array.
        val (int): Value to remove.
    Returns:
        int: Number of values not equal to val.
    """
    fast = slow = 0
    while fast < len(nums):
        if nums[fast] == val:
            fast += 1
            continue
        nums[slow] = nums[fast]
        slow += 1
        fast += 1
    return slow

test = [0,1,2,2,3,0,4,2]
test_val = 2
print(remove_element(test, test_val))