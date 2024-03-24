Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N)

**How Does Binary Search Algorithm Work**:

    • Every element is considered as a potential match for the key and checked for the same.
    • If any element is found equal to the key, the search is successful and the index of that element is returned.
    • If no element is found equal to the key, the search return -1.

```python
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
```

|                  | Best                                  | Average   | Worst                                     |
| ---------------- | ------------------------------------- | --------- | ----------------------------------------- |
| Time Complexity  | O(1) - key present at the first index | O(log(N)) | O(log(N)) - key present at the last index |
| Space Complexity | O(1)                                  | O(1)      | O(1)                                      |