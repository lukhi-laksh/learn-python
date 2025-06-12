class Solution():
    def popMaxNumber(self, Sarr):
        final = [-1] * len(Sarr)
        store_index = []
        for i in range(len(Sarr)):
            while store_index and Sarr[store_index[-1]] < Sarr[i]:
                final[store_index[-1]] = Sarr[i]
                store_index.pop()
            store_index.append(i)
                    
        print(final)


sol = Solution()
Sarr = [8, 6, 4, 7, 4, 9, 10, 8, 12]
print(sol.popMaxNumber(Sarr))