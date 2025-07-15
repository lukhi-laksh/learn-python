def SubSum(arr, index, n, temp, sum):
    
    if index == n:
        temp.append(sum)
        return
    
    SubSum(arr, index+1, n, temp, sum)
    SubSum(arr, index+1, n, temp, sum + arr[index])


arr = [4, 5, 6]
n = len(arr)
temp = []
index = 0
sum = 0
SubSum(arr, index, n, temp, sum)
print(temp)