class Solution():
    def popMinNumber(self, Sarr):
        final = [1] * len(Sarr)
        stack = []

        for i in range(len(Sarr)-1, -1, -1):
            while stack and Sarr[i] > Sarr[stack[-1]]:
                final[-1] = stack[-1] - 1
                stack.pop()
            stack.append(i)

        while stack:
            final[-1] = final[-1] + 1


sol = Solution()
Sarr = [2, 1, 3, 5, 0, 6]
print(sol.popMinNumber(Sarr))