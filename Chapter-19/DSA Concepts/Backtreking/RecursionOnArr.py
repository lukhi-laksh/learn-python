def laksh(arr, ind):

    if ind == len(arr):
        return
    
    print(arr[ind])
    laksh(arr, ind + 1)

arraa = [1, 3, 4, 5, 3, 2, 3, 3, 5]
laksh(arraa, 0)