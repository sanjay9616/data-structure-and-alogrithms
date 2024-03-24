class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key
        self.n = len(arr)

    def binarySearch(self):
        left, right = 0, self.n - 1
        while(left <= right):
            mid = (left + right) // 2
            if(self.arr[mid] == self.key):
                return mid
            elif(self.arr[mid] < self.key):
                left = mid + 1
            else:
                right = mid - 1
        return -1

search = Search([0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 9)
print(search.binarySearch())
# OutPut = 10