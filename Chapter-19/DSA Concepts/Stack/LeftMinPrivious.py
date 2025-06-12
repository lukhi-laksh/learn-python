class Solution:
    def LeftMinPrivious(self, Sarr):
        final = [-1] * len(Sarr)
        stack = []

        for i in range(len(Sarr) - 1, -1, -1):
                while stack and Sarr[stack[-1]] > Sarr[i]:
                    final[stack[-1]] = Sarr[i]
                    stack.pop()
                stack.append(i)
        return final

sol = Solution()
arr = [4, 13, 11, 5, 9, 7, 8, 6]
print(sol.LeftMinPrivious(arr))