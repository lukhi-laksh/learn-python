class Solution:
    def insertAtBottom(self, Sarr):
        empty = []
        for i in Sarr:
            if len(empty) == 0:
                empty.append(i)
            elif i > 0:
                if empty[-1] >= 0:
                    empty.append(i)
                else:
                    empty.pop()
            else:
                if empty[-1] < 0:
                    empty.append(i) 
                else:
                    empty.pop()
        
        print(empty)

sol = Solution()
arr = [-2, 3, 5, 5, 5, 5, -4, 6, -2, -8, 9]
sol.insertAtBottom(arr)