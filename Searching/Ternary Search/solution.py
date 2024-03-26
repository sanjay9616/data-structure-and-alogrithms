class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key
        self.n = len(arr)

    def jumpSearch(self):
        import math
        step = int(math.sqrt(self.n))
        left = 0
        right = self.n - 1
        for i in range(0, self.n, step):
            if (self.arr[i] < self.key):
                left = i
            if (self.arr[i] == self.key):
                return i
            elif (self.arr[i] > self.key):
                right = i
                break
        for i in range(left, right + 1, 1):
            if (self.arr[i] == self.key):
                return i
        return -1

search = Search([0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 0)
print(search.jumpSearch())
# Output = 0
