**Sentinel Linear Search:**

Sentinel Linear Search as the name suggests is a type of Linear Search where the number of comparisons is reduced as compared to a traditional linear search. In a traditional linear search, only N comparisons are made, and in a Sentinel Linear Search, the sentinel value is used to avoid any out-of-bounds comparisons, but there is no additional comparison made specifically for the index of the element being searched.

**Iterative Approach:**

```python
def sentinelSearch(arr, n, key):
    last = arr[n - 1]
    arr[n - 1] = key
    i = 0
    while (arr[i] != key):
        i += 1
    arr[n - 1] = last
    if ((i < n - 1) or (arr[n - 1] == key)):
        return i
    else:
        return -1
arr = [0,1,2,3,4,5,5,6,7,8,9]
n = len(arr)
key = 9
print(sentinelSearch(arr, n, key))
```

|                  | Best | Average | Worst |
| ---------------- | ---- | ------- | ----- |
| Time Complexity  | O(1) | O(N)    | O(N)  |
| Space Complexity | O(1) | O(1)    | O(1)  |


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/README.md"> 🔙 Back</a></h2>