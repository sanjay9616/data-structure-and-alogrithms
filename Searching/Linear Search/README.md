**Linear Search:**

Linear Search, also known as Sequential Search, is one of the simplest and most straightforward searching algorithms. It works by sequentially examining each element in a collection of data(array or list) until a match is found or the entire collection has been traversed.

**How Does Linear Search Algorithm Work**:

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

|                  | Best                                  | Average | Worst                                |
| ---------------- | ------------------------------------- | ------- | ------------------------------------ |
| Time Complexity  | O(1) - key present at the first index | O(N)    | O(N) - key present at the last index |
| Space Complexity | O(1)                                  | O(1)    | O(1)                                 |

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/README.md"> 🔙 Back</a></h2>