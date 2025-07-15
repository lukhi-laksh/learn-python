def subseq(arr, index, n, temp, ans):
    if index == n:
        ans.append(sum(temp[:]))
        return
    
    temp.append(arr[index])
    subseq(arr, index + 1, n, temp, ans)
    temp.pop()
    subseq(arr, index + 1, n, temp, ans)
    

arr = [1, 2, 3]
ans = []
temp = []
subseq(arr, 0, len(arr), temp, ans)
print(ans)
