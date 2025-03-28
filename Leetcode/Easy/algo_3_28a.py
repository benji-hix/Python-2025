"""Remove Duplicates"""

# O(NlogN) Solution
def remove_duplicates(nums : list[int]) -> int:
    """
    Given an integer array nums sorted in non-decreasing order, remove the duplicates 
    in-place such that each unique element appears only once. The relative order of the 
    elements should be kept the same. Then return the number of unique elements in nums.

    Args:
        nums (list[int]): Ordered list of ints.

    Returns:
        int: Number of unique values.
    """
    queue = []

    for item in nums:
        if item not in queue:
            queue.append(item)
    queue.sort()
    for index, entry in enumerate(queue):
        nums[index] = entry

    print(nums)
    return len(queue)

print(remove_duplicates([2, 2, 5, 1, 3, 4, 3, 4, 6, 8, 7, 7, 9, 0]))
