class Solution():
    def popMaxNumber(self, Sarr):
        final = [-1] * len(Sarr)
        stack = []
        for i in range(len(Sarr)):
            while stack and Sarr[stack[-1]] < Sarr[i]:
                final[stack[-1]] = Sarr[i]
                stack.pop()
            stack.append(i)
        
        for j in stack:
            for k in range(len(Sarr) % j):
                if Sarr[j] < Sarr[k]:
                    final[j] = Sarr[k]
                    break
        return final

            


sol = Solution()
Sarr = [6, 10, 7, 4, 8, 9, 4]
print(sol.popMaxNumber(Sarr))