''' Two Sum'''


def two_sum(nums: list[int], target: int) -> list[int]:
    '''
    Find the indexes of two integers whose sum is a given integer.
    
    Args:
        nums (list[int]): List of integers.
        target (int): The target sum of two integers.

    Returns:
        list[int]: The indexes of the only two integers in nums whose 
        sum is equal to target.
    '''
    for num in nums:
        index = nums.index(num)
        target_num = target - num
        if target_num in nums[index + 1:]:
            target_index = nums[index + 1:].index(target_num) + index + 1
            return [index, target_index]
    return None

# Optimized version using dictionary
def two_sum_optimized(nums: list[int], target: int) -> list[int]:
    '''
    Find the indexes of two integers whose sum is a given integer.
    
    Args:
        nums (list[int]): List of integers.
        target (int): The target sum of two integers.

    Returns:
        list[int]: The indexes of the only two integers in nums whose 
        sum is equal to target.
    '''

    stored_numbers = {}
    for index, value in enumerate(nums):
        difference = target - value
        if difference in stored_numbers:
            return [stored_numbers[difference], index]
        stored_numbers[value] = index

print(two_sum_optimized([9, 8, 7, 3, 5, 8, 3, 9], 6))
