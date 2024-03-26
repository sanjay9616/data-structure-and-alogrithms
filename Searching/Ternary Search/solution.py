class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key
        self.n = len(arr)

    def binarySearch(self):
        left, right = 0, self.n - 1
        while(left <= right and self.arr[left] <= self.key and self.arr[right] >= self.key):
            mid = left + ((self.key - self.arr[left]) * (right - left)) // (self.arr[right] - self.arr[left])
            if(self.arr[mid] == self.key):
                return mid
            elif(self.arr[mid] < self.key):
                left = mid + 1
            else:
                right = mid - 1
        return -1

search = Search([0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5)
print(search.binarySearch())
# OutPut = 5