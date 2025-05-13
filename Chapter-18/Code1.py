class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums[i+1:]:
                return [i, nums.index(temp, i+1)]
        return []

sol = Solution()
nums = [3,3]
target = 6
print(sol.twoSum(nums, target))