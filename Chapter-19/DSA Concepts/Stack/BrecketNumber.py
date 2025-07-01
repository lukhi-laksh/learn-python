class Solution:
    def insertAtBottom(self, st):
        # create variable 
        number = 0
        # create enpty array
        count = []
        # Create empty variable 
        final = []
        for i in st:
            if i == "(":
                number += 1
                count.append(number)
                final.append(number)
            else:
                if count:
                    final.append(count.pop())
        # Print output 
        print(final)


sol = Solution()
st = "(aa(bdc))p(de)"
print(sol.insertAtBottom(st))
