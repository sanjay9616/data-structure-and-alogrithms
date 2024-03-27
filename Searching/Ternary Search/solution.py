def sentinelSearch(arr, n, key):
    last = arr[n - 1]
    arr[n - 1] = key
    i = 0
    while (arr[i] != key):
        i += 1
    arr[n - 1] = last
    if ((i < n - 1) or (arr[n - 1] == key)):
        return i
    else:
        return -1
arr = [0,1,2,3,4,5,5,6,7,8,9]
n = len(arr)
key = 9
print(sentinelSearch(arr, n, key))