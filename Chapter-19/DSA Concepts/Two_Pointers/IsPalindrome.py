import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = re.sub(r'[^a-z0-9]', '', s.lower())
        return new_str == new_str[::-1]

sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw ?"))