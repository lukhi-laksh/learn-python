class Solution():
    def popMinNumber(self, Sarr):
        final = [0] * len(Sarr)
        final[0] = Sarr[0]
        for i in range(1, len(Sarr)):
            if Sarr[i] < final[i - 1]:
                final[i] = Sarr[i]
            else:
                final[i] = final[i - 1]

        fullFinal = []
        while final:
            fullFinal.append(final.pop())

        return fullFinal

sol = Solution()
Sarr = [2, 1, 3, 5, 0, 6]
print(sol.popMinNumber(Sarr))