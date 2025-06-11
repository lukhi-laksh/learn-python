class Solution:
    def insertAtBottom(self, st):
        count = 0
        for single in st:
            if single == "(":
                count += 1
            elif single == ")":
                count -= 1
                if count == -1:
                    return False
        
        if count == 0:
            return True
        else:
            return False
            

sol = Solution()
st = "(((()())))"
print(sol.insertAtBottom(st))