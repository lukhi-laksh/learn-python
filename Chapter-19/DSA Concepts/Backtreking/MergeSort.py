def laksh(arr, start, end):
    def Merge(arr, start, mid, end):
        temp = [0] * (end - start + 1)
        left = start
        right = mid + 1
        index = 0
        
        while left <= mid and right <= end:
            if arr[left] <= arr[right]:
                temp[index] = arr[left]
                left += 1
            else:
                temp[index] = arr[right]
                right += 1
            index += 1
        
        while left <= mid:
            temp[index] = arr[left]
            left += 1
            index += 1
        
        while right <= end:
            temp[index] = arr[right]
            right += 1
            index += 1
        
        
        
        return arr
    
    def MergeSort(arr, start, end):
        if start >= end:
            return
        
        mid = start + (end - start) // 2
        
        MergeSort(arr, start, mid)
        MergeSort(arr, mid + 1, end)
        Merge(arr, start, mid, end)
    
        return arr

    return MergeSort(arr, start, end) or arr

arr = [2, 7, 4, 6, 1, 3, 5, 7, 9, 8]
print(laksh(arr, 0, len(arr)-1))