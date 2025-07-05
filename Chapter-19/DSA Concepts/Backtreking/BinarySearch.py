def laksh(arr, start, end, x):
    if start > end:
        return False
    
    mid = int((end + start) // 2)
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        start = mid + 1
        return laksh(arr, start, end, x)
    else:
        end = mid - 1
        return laksh(arr, start, end, x)                                                                        
        
    
arr = [5, 6, 9, 12, 13, 17, 20, 22, 25]
print(laksh(arr, 0, len(arr) - 1, 22))