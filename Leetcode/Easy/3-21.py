class Solution:
    @staticmethod
    def countKdifference(nums: list[int], k: int) -> int:
        count = 0
        for index, num in enumerate(nums):
            for subtracted_num in nums[(index+1):]:
                if abs(num - subtracted_num) == k:
                    count += 1
                else:
                    continue
        return count

print(Solution.countKdifference([1, 2, 2, 1], 1))