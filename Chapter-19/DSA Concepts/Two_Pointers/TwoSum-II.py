from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            if (numbers[start] + numbers[end]) > target:
                end = end - 1
            elif (numbers[start] + numbers[end]) < target:
                start = start + 1
            else:
                return [start + 1, end + 1]
        return []        

sol = Solution()
numbers = [1, 3, 4, 5 ,7, 10, 11]
target = 9
print(sol.twoSum(numbers, target))