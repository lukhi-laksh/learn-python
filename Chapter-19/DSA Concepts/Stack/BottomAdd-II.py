#User function Template for python3
class Solution:
    def insertAtBottom(self,st,x):
        empty = []
        for i in range(len(st)):
            empty.append(st[-1])
            st.pop()
        st.append(x)
        for i in range(len(empty)):
            st.append(empty[-1])
            empty.pop()
        print(st)

sol = Solution()
st = [3, 4, 5, 6]
x = 2
sol.insertAtBottom(st, 2)