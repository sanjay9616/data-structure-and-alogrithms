class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key
        self.n = len(arr)

    def linearSearch(self):
        for i in range(self.n):
            if (self.arr[i] == self.key):
                return i
        return -1


search = Search([1, 2, 32], 32)
print(search.linearSearch())
# OutPut = 2