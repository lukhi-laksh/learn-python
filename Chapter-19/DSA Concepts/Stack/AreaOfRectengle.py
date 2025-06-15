class Solution:
    def insertAtBottom(self, Sarr):

        # Right side first larger
        right = [len(Sarr)] * len(Sarr)
        stack1 = []

        for i in range(len(Sarr)):
            while stack1 and Sarr[i] < Sarr[stack1[-1]]:
                top = stack1.pop()
                right[top] = i
            stack1.append(i)
        print(right)



        left = [-1] * len(Sarr)
        stack2 = []

        for i in range(len(Sarr) - 1, -1, -1):
            while stack2 and Sarr[i] < Sarr[stack2[-1]]:
                top = stack2.pop()
                left[top] = top
            stack2.append(i)
        
        while stack2:
            left[stack2[-1]] = -1
            stack2.pop()

        print(left)

        ans = []
        for i in range(len(Sarr)):
            store = Sarr[i] * (right[i] - left[i] - 1)
            ans.append(store)
        return max(ans)


sol = Solution()
arr = [2, 3, 4, 2, 6, 5, 4, 5, 3]
print(sol.insertAtBottom(arr))
