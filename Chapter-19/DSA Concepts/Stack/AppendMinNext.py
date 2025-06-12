class Solution():
    def popMinNumber(self, Sarr):
        final = [-1] * len(Sarr)
        stack = []
        for i in range(len(Sarr)):
            while stack and Sarr[stack[-1]] > Sarr[i]:
                final[stack[-1]] = Sarr[i]
                stack.pop()
            stack.append(i)
        return final


sol = Solution()
Sarr = [7, 9, 12, 10, 14, 8, 3, 6, 9]
print(sol.popMinNumber(Sarr))