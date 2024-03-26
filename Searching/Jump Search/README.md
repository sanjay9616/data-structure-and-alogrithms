**Jump Search:**

Jump Search is defined as a searching algorithm used in a **sorted array** and the basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements

**How Does Jump Search Algorithm Work**:

    • Jump Search is an algorithm for finding a specific value in a sorted array by jumping through certain steps in the array.
    • The steps are determined by the sqrt of the length of the array.
    • Here is a step-by-step algorithm for the jump search:
    • Determine the step size m by taking the sqrt of the length of the array n.
    • Start at the first element of the array and jump m steps until the value at that position is greater than the target value.
    • Once a value greater than the target is found, perform a linear search starting from the previous step until the target is found or it is clear that the target is not in the array. If the target is found, return its index. If not, return -1 to indicate that the target was not found in the array.

**Iterative Approach:**

```python
class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key
        self.n = len(arr)

    def jumpSearch(self):
        import math
        step = int(math.sqrt(self.n))
        left = 0
        right = self.n - 1
        for i in range(0, self.n, step):
            if (self.arr[i] < self.key):
                left = i
            elif (self.arr[i] == self.key):
                return i
            elif (self.arr[i] > self.key):
                right = i
                break
        for i in range(left, right + 1, 1):
            if (self.arr[i] == self.key):
                return i
        return -1

search = Search([0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 0)
print(search.jumpSearch())
# Output = 0
```

|                  | Best | Average | Worst |
| ---------------- | ---- | ------- | ----- |
| Time Complexity  | O(1) | O(√N)   | O(√N) |
| Space Complexity | O(1) | O(1)    | O(1)  |

**Advantages:**

1. Better than a linear search for arrays where the elements are uniformly distributed. </br>
2. It is easier to implement compared to other search algorithms like binary search or ternary search. </br>
3. Binary search is well-suited for searching large datasets that are stored in external memory, such as on a hard drive or in the cloud. </br>


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/README.md"> 🔙 Back</a></h2>