class Solution:                          
    def insertAtBottom(self, Sarr):
        final1 = [len(Sarr)] * len(Sarr)
        stack1 = []

        for i in range(len(Sarr)):
            while stack1 and Sarr[stack1[-1]] > Sarr[i]:
                top = stack1.pop()
                final1[top] = i
            stack1.append(i)
        print(final1)
        
        final2 = [-1] * len(Sarr)
        stack2 = []
        for i in range(len(Sarr) -1, -1, -1):
            while stack2 and Sarr[i] < Sarr[stack2[-1]]:
                temp = stack2.pop()
                final2[temp] = i
            stack2.append(i)
        print(final2)
        
        
        
sol = Solution()
arr = [2, 3, 4, 2, 6, 1, 4, 5, 3]
print(sol.insertAtBottom(arr))                                                                     
 
