class Solution:
    def insertAtBottom(self, st):
        # create stack
        empty = []

        # Each letter Compare
        for i in st:
            if i == "(" or i == "[" or i == "{":
                empty.append(i)
            else:
                if len(empty) == 0:
                    return False
                elif i == ")":
                    if empty[-1] != "(":
                        return False
                    else:
                        empty.pop()
                elif i == "}":
                    if empty[-1] != "{":
                        return False
                    else:
                        empty.pop()
                elif i == "]":
                    if empty[-1] != "[":
                        return False
                    else:
                        empty.pop()
        return len(empty) == 0



sol = Solution()
st = "()[()]{{()[}}"
print(sol.insertAtBottom(st))
