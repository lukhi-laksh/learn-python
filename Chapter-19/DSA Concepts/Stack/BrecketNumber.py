class Solution:
    def insertAtBottom(self, st):
        number = 0
        count = []
        final = []
        for i in st:
            if i == "(":
                number += 1
                count.append(number)
                final.append(number)
            else:
                if count:
                    final.append(count.pop())

        print(final)


sol = Solution()
st = "(aa(bdc))p(de)"
print(sol.insertAtBottom(st))