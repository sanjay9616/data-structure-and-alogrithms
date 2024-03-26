**Ternary Search:**

Ternary Search is defined as a searching algorithm based on **divide and conquer** technique like Binary Search used in a **sorted array** that divides the search space into **three parts** instead of two.

**How Does Ternary Search Algorithm Work**:

    • Calculate two midpoints, mid1 and mid2, dividing the current search space into three roughly equal parts:
    • mid1 = left + (right – left) / 3
    • mid2 = right – (right – left) / 3
    • The array is now effectively divided into [left, mid1], (mid1, mid2), and [mid2, right].
    • If the target is equal to the element at mid1 or mid2, the search is successful, and the index is returned
    • If the target is less than the element at mid1, update the right pointer to mid1 – 1.
    • If the target is greater than the element at mid2, update the left pointer to mid2 + 1.
    • If the target is between the elements at mid1 and mid2, update the left pointer to mid1 + 1 and the right pointer to mid2 – 1.
    • Repeat the process with the reduced search space until the target is found or the search space becomes empty.
    • If the search space is empty and the target is not found, return a value indicating that the target is not present in the array.

**Iterative Approach:**

```python
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
# OutPut = 6 (2nd element)
```
**Recursive Approach:**

```python
class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key

    def ternarySearch(self, left, right):
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if (key == self.arr[mid1]):
            return mid1
        if (key == self.arr[mid2]):
            return mid2
        if (key < self.arr[mid1]):
            return self.ternarySearch(left, mid1 - 1)
        elif (key > self.arr[mid2]):
            return self.ternarySearch(mid2 + 1, right)
        else:
            return self.ternarySearch(mid1 + 1, mid2 - 1)
        return -1


arr, key = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5
search = Search(arr, key)
print(search.ternarySearch(0, len(arr) - 1))
# Output = 6 (2nd element)
```

|                  | Best                                | Average               | Worst                 |
| ---------------- | ----------------------------------- | --------------------- | --------------------- |
| Time Complexity  | O(1) - key present at the mid index | O(log<sub>3</sub>(N)) | O(log<sub>3</sub>(N)) |
| Space Complexity | O(1)                                | O(1)                  | O(1)                  |

**Note**: O(1), If the recursive call stack is considered then the auxiliary space will be O(logN).

**Advantages:**

1. Ternary search can find maxima/minima for unimodal functions, where binary search is not applicable. </br>
2. Ternary Search has a time complexity of O(2 * log3n), which is more efficient than linear search and comparable to binary search. </br>
3. Fits well with optimization problems. </br>

**Drawbacks:**

1. The array should be sorted. </br>
2. Ternay search requires that the elements of the array be comparable, meaning that they must be able to be ordered. </br>
3. Ternary Search takes more time to find maxima/minima of monotonic functions as compared to Binary Search. </br>

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/README.md"> 🔙 Back</a></h2>