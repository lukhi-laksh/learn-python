class Solution:
    def removeAdj(self, Sarr):
        empty = []
        for i in Sarr:
            if len(empty) == 0:
                empty.append(i)
            elif i == empty[-1]:
                empty.pop()
            else:
                empty.append(i)
        return len(empty)        

sol = Solution()
arr = ["ab", "ac", "da", "da", "ac", "db", "ea"]
print(sol.removeAdj(arr))