**Interpolation Search:**

Interpolation Search is defined as is an efficient searching algorithm for **sorted** collections of data, such as arrays or lists. It is an improvement over Binary Search, particularly when the data is uniformly distributed.

Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.

**How Does Jump Search Algorithm Work**:

    • In a loop, calculate the value of “pos” using the probe position formula. 
    • If it is a match, return the index of the item, and exit. 
    • If the item is less than arr[pos], calculate the probe position of the left sub-array.Otherwise, calculate the same in the right sub-array. 
    • Repeat until a match is found or the sub-array reduces to zero.

**Iterative Approach:**

```python
class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key
        self.n = len(arr)

    def interpolationSearch(self):
        left, right = 0, self.n - 1
        while(left <= right and self.arr[left] <= self.key and self.arr[right] >= self.key):
            mid = left + ((self.key - self.arr[left]) * (right - left)) // (self.arr[right] - self.arr[left])
            if(self.arr[mid] == self.key):
                return mid
            elif(self.arr[mid] < self.key):
                left = mid + 1
            else:
                right = mid - 1
        return -1

search = Search([0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5)
print(search.interpolationSearch())
# OutPut = 5
```

```python
class Search:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key

    def interpolationSearch(self, left, right):
        mid = left + ((self.key - self.arr[left]) * (right - left)) // (self.arr[right] - self.arr[left])
        if(left <= right and self.arr[left] <= self.key and self.arr[right] >= self.key):
            if (self.arr[mid] == self.key):
                return mid
            elif (self.arr[mid] < self.key):
                return self.binarySearch(mid + 1, right)
            else:
                return self.binarySearch(left, mid - 1)
        return -1

arr, key = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5
search = Search(arr, key)
print(search.interpolationSearch(0, len(arr) - 1))
# Output = 5
```

|                  | Best | Average                              | Worst |
| ---------------- | ---- | ------------------------------------ | ----- |
| Time Complexity  | O(1) | O(log<sub>2</sub>(log<sub>2</sub>N)) | O(N)  |
| Space Complexity | O(1) | O(1)                                 | O(1)  |


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/README.md"> 🔙 Back</a></h2>