class Solution:                          
    def insertAtBottom(self, Sarr):
        final1 = [len(Sarr)] * len(Sarr)
        stack1 = []

        for i in range(len(Sarr)):
            while stack1 and Sarr[stack1[-1]] > Sarr[i]:
                top = stack1.pop()
                final1[top] = i - top - 1
            stack1.append(i)
        print(final1)
        
        final2 = [0] * len(Sarr)
        stack2 = []
        for i in range(len(Sarr) -1, -1, -1):
            while stack2 and Sarr[i] < Sarr[stack2[-1]]:
                temp = stack2.pop()
                final2[temp] = temp - i - 1
            stack2.append(i)
        while stack2:
            temp = stack2.pop()
            final2[temp] = temp
        print(final2)
        
        ans = []
        for i in range(len(Sarr)):
            store = Sarr[i] * (final1[i] + final2[i] + 1)
            ans.append(store)
        return max(ans)
        
        
sol = Solution()
arr = [2, 3, 4, 2, 6, 1, 4, 5, 3]
print(sol.insertAtBottom(arr))
 
