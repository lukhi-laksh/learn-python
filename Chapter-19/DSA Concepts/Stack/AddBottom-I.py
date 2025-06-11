#User function Template for python3
class Solution:
    def insertAtBottom(self,st,x):
        empty = []
        empty.append(x)
        j = 0
        while j != len(st):
            empty.append(st[j])
            j += 1
        return empty


sol = Solution()
st = [3, 4, 5, 6]
x = 2
sol.insertAtBottom(st, 2)
