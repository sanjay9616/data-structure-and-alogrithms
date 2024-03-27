**The Ubiquitous Binary Search:**

**Iterative Approach:**

```python
def ubiquitous_binary_search(arr, key):
    left = 0
    right = len(arr)
    while (right - left > 1):
        mid = left + (right - left) // 2

        if (arr[mid] <= key):
            left = mid
        else:
            right = mid
    if (arr[left] == key):
        return left
    else:
        return -1

print(ubiquitous_binary_search([1, 2, 3, 4, 5], 1))
```

|                  | Best | Average   | Worst     |
| ---------------- | ---- | --------- | --------- |
| Time Complexity  | O(1) | O(log(N)) | O(log(N)) |
| Space Complexity | O(1) | O(1)      | O(1)      |


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/README.md"> 🔙 Back</a></h2>