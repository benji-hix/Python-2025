"""Count K Difference"""

class Solution:
    @staticmethod
    def count_k_difference(nums: list[int], k: int) -> int:
        """
        Given a list of integers, return the possible number of integers
        for which the absolute difference is equal to a target number k.

        Args:
            nums (list[int]): List of integers.
            k (int): Target absolute difference.

        Returns:
            int: Number of possible combinations.
        """
        count = 0
        for index, num in enumerate(nums):
            for subtracted_num in nums[(index+1):]:
                if abs(num - subtracted_num) == k:
                    count += 1
                else:
                    continue
        return count

print(Solution.count_k_difference([1, 2, 2, 1], 1))
