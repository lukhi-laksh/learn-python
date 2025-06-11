class Solution:
    def insertAtBottom(self, st):
        empty = []
        for i in st:
            if i == "(":
                empty.append(i)
            else:
                if len(empty) == 0:
                    return False
                else:
                    empty.pop()

        if len(empty) == 0:
            return True
        else:
            return False

sol = Solution()
st = "(((()()))"
print(sol.insertAtBottom(st))