**Ternary Search:**

Binary Search is defined as a searching algorithm used in a sorted array that divides the search space into three parts instead of two, as in Binary Search.

**How Does Binary Search Algorithm Work**:

    • Divide the search space into two halves by finding the middle index “mid”.
    • Compare the middle element of the search space with the key.
    • If the key is found at middle element, the process is terminated.
    • If the key is not found at middle element, choose which half will be used as the next search space.
        1. If the key is smaller than the middle element, then the left side is used for next search.
        2. If the key is larger than the middle element, then the right side is used for next search.
    • This process is continued until the key is found or the total search space is exhausted.

**Iterative Approach:**

```python
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
```
**Recursive Approach:**

```python
class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key

    def binarySearch(self, left, right):
        mid = (left + right) // 2
        if (self.arr[mid] == self.key):
            return mid
        elif (self.arr[mid] < self.key):
            return self.binarySearch(mid + 1, right)
        else:
            return self.binarySearch(left, mid - 1)
        return -1

arr, key = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 9
search = Search(arr, key)
print(search.binarySearch(0, len(arr) - 1))
# Output - 10
```

|                  | Best                                | Average   | Worst     |
| ---------------- | ----------------------------------- | --------- | --------- |
| Time Complexity  | O(1) - key present at the mid index | O(log(N)) | O(log(N)) |
| Space Complexity | O(1)                                | O(1)      | O(1)      |

**Note**: O(1), If the recursive call stack is considered then the auxiliary space will be O(logN).

**Advantages:**

1. Binary search is faster than linear search, especially for large arrays. </br>
2. More efficient than other searching algorithms with a similar time complexity, such as interpolation search or exponential search. </br>
3. Binary search is well-suited for searching large datasets that are stored in external memory, such as on a hard drive or in the cloud. </br>

**Drawbacks:**

1. The array should be sorted. </br>
1. Binary search requires that the elements of the array be comparable, meaning that they must be able to be ordered. </br>

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/README.md"> 🔙 Back</a></h2>