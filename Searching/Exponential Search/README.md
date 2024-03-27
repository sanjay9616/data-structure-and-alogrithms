**Exponential Search:**

Exponential search allows for searching through a **sorted**, **unbounded** list for a specified input value (the search "key"). The algorithm consists of two stages. The first stage determines a range in which the search key would reside if it were in the list. In the second stage, a binary search is performed on this range.

**Exponential search involves two steps**:</br>
1. Find range where element is present.</br>
2. Do Binary Search in above found range.</br>

**Iterative Approach:**

```python
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r-l) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        return binarySearch(arr, mid + 1, r, x)
    return -1

def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    return binarySearch(arr, i // 2, min(i, n-1), x)

arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
print(exponentialSearch(arr, n, x))
```

|                  | Best | Average   | Worst            |
| ---------------- | ---- | --------- | ---------------- |
| Time Complexity  | O(1) | O(log(N)) | O(1)             |
| Space Complexity | O(1) | O(1)      | O(1) or O(Log n) |

**Auxiliary Space**:
The above implementation of Binary Search is recursive and requires O(Log n) space. With iterative Binary Search, we need only O(1) space.


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/README.md"> 🔙 Back</a></h2>