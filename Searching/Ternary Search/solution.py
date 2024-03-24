class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key

    def ternarySearch(self, left, right):
        while right >= left:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            if (key == self.arr[mid1]):
                return mid1
            if (key == self.arr[mid2]):
                return mid2
            if (key < self.arr[mid1]):
                right = mid1 - 1
            elif (key > self.arr[mid2]):
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        return -1


arr, key = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5
search = Search(arr, key)
print(search.ternarySearch(0, len(arr) - 1))
