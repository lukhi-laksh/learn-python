class Solution():
    def popMinNumber(self, Sarr):
        final = []
        while len(Sarr) > 1:
            Sarr.pop()
            final.append(min(Sarr))
        return final
    
    
sol = Solution()
Sarr = [2, 1, 3, 5, 0, 6]
print(sol.popMinNumber(Sarr))