class Solution:
    def removeAdj(self, str1, str2):
        empty1 = []
        for first in str1:
            if first == "#":
                if empty1:
                    empty1.pop()
            else:
                empty1.append(first)

        empty2 = []
        for second in str2:
            if second == "#":
                if empty2:
                    empty2.pop()
            else:
                empty2.append(second)
        
        return empty1 == empty2


sol = Solution()
str1 = "abc##c"
str2 = "#ad#c"
print(sol.removeAdj(str1, str2))