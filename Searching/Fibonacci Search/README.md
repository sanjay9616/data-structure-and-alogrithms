**Fibonacci Search:**

Fibonacci Search is a comparison-based (Divide and Conquer Algorithm) technique that uses Fibonacci numbers to search an element in a **sorted array**.

**Iterative Approach:**

```python
def FibonacciGenerator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)

def FibonacciSearch(arr, x):
    m = 0
    while FibonacciGenerator(m) < len(arr):
        m = m + 1
    offset = -1
    while (FibonacciGenerator(m) > 1):
        i = min(offset + FibonacciGenerator(m - 2), len(arr) - 1)
        if (x > arr[i]):
            m = m - 1
            offset = i
        elif (x < arr[i]):
            m = m - 2
        else:
            return i
    if (FibonacciGenerator(m - 1) and arr[offset + 1] == x):
        return offset + 1
    return -1


arr = [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130]
x = 60
print(FibonacciSearch(arr, x))

```

|                  | Best | Average   | Worst     |
| ---------------- | ---- | --------- | --------- |
| Time Complexity  | O(1) | O(log(N)) | O(log(N)) |
| Space Complexity | O(1) | O(1)      | O(1)      |


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/README.md"> 🔙 Back</a></h2>