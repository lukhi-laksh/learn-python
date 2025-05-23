from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

        
sol = Solution()
lists = [1, 3, 4, 6, 3, 5]
target = 6
print(sol.twoSum(lists, target))