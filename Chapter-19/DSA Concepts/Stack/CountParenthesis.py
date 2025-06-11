class Solution:
    def insertAtBottom(self, st):
        empty = []
        count = 0
        for i in st:
            if i == "(":
                empty.append(i)
            else:
                if i == ")":
                    if len(empty) == 0:
                        count += 1
                    else:
                        empty.pop()
                
        return len(empty) + count
           
                
sol = Solution()
st = "((()"
print(sol.insertAtBottom(st))

[]