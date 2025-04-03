"""Search Insert Position"""

# O(Log(N)) Solution
def search_insert(nums: list[int], target: int) -> int:
    """
    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.

    Args:
        nums (list[int]): List to search through.
        target (int): Int to search for.

    Returns:
        int: If target is found, index of target. If
        target is not found, index of where it would be inserted.
    """
    for index in range(len(nums) - 1):
        if nums[index] == target:
            return index
        if nums[index] < target and nums[index + 1] > target:
            return index + 1
    return len(nums)


def search_insert_optimized(nums: list[int], target: int) -> int:
    """
    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.

    Args:
        nums (list[int]): List to search through.
        target (int): Int to search for.

    Returns:
        int: If target is found, index of target. If
        target is not found, index of where it would be inserted.
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
    return left
    
print(search_insert_optimized([], 4))
print(search_insert_optimized([1], 1))
print(search_insert_optimized([1, 2], 2))
print(search_insert_optimized([1, 2, 3, 4], 7))
print(search_insert_optimized([1, 2, 3, 4], 3))
