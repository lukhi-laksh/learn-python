class Solution():
    def popMinNumber(self, Sarr):
        final = [1] * len(Sarr)
        stack = []

        for i in range(len(Sarr)):
            while stack and Sarr[i] > Sarr[stack[-1]]:
                top = stack.pop()
                final[top] = i - top + 1
            stack.append(i)

        return final

sol = Solution()
Sarr = [98, 99, 100, 80, 55, 70, 60, 75, 85]
print(sol.popMinNumber(Sarr))
