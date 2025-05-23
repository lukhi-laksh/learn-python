from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty = set()
        for i in nums:
            if i in empty:
                return False
            empty.add(i)
        return True
num = [7, 1, 5, 4, 2]
solutions = Solution()
print(solutions.hasDuplicate(num))