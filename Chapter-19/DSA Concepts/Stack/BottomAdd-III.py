class Solution:
    def insertAtBottom(self, st, x):
        temp = []
        
        while st:
            temp.append(st.pop())

        st.append(x)
        
        while temp:
            st.append(temp.pop())
        
        print(st)

sol = Solution()
st = [3, 4, 5, 6]
x = 2
sol.insertAtBottom(st, x)
