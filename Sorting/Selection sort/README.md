**Selection Sort:**

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

**Algorithm**:

    • Set the first element as minimum.
    • Find smallest element in right array (unsorted array) and swap with smallest.
    • This process is then continued, so on until the data is sorted.

```python
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if (arr[j] < arr[minimum]):
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

print(selectionSort([5, 3, 0, 0, 1, 2]))
```

|                  | Best | Average | Worst  |
| ---------------- | ---- | ------- | ------ |
| Time Complexity  | O(N) | O(N^2)  | O(N^2) |
| Space Complexity | O(1) | O(1)    | O(1)   |

**Advantages:**

1. Simple and easy to understand.</br>
2. Works well with small datasets.</br>

**Disadvantages:**

1. Selection sort has a time complexity of O(n^2) in the worst and average case.</br>
2. Does not work well on large datasets.</br>
3. Does not preserve the relative order of items with equal keys which means it is not stable.</br>

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Sorting/README.md"> 🔙 Back</a></h2>