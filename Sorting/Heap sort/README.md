**Heap Sort:**

Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to the selection sort where we first find the minimum element and place the minimum element at the beginning. Repeat the same process for the remaining elements.

**Algorithm**:

First convert the array into heap data structure using heapify, then one by one delete the root node of the Max-heap and replace it with the last node in the heap and then heapify the root of the heap. Repeat this process until size of heap is greater than 1. </br>
1. Build a heap from the given input array. </br>
2. Repeat the following steps until the heap contains only one element:</br>
    - Swap the root element of the heap (which is the largest element) with the last element of the heap. </br>
    - Remove the last element of the heap (which is now in the correct position).</br>
3. Heapify the remaining elements of the heap.</br>
4. The sorted array is obtained by reversing the order of the elements in the input array.</br>


```python
def heapify(arr, size, i):
    largest = i
    leftChildIndex = 2 * i + 1
    rightChildIndex = 2 * i + 2
    if (leftChildIndex < size and arr[largest] < arr[leftChildIndex]):
        largest = leftChildIndex
    if (rightChildIndex < size and arr[largest] < arr[rightChildIndex]):
        largest = rightChildIndex
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)

def heapSort(arr):
    N = len(arr)
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
N = len(arr)

print("Sorted array is", arr)  # Output = Sorted array is [5, 6, 7, 11, 12, 13]
```


|                  | Best        | Average     | Worst       |
| ---------------- | ----------- | ----------- | ----------- |
| Time Complexity  | O(N log(N)) | O(N log(N)) | O(N log(N)) |
| Space Complexity | O(log(N))   | O(log(N))   | O(log(N))   |

**Advantages:**

1. **Efficient Time Complexity:** Heap Sort has a time complexity of O(n log n) in all cases. This makes it efficient for sorting large datasets. The log n factor comes from the height of the binary heap, and it ensures that the algorithm maintains good performance even with a large number of elements.</br>
2. **Memory Usage** – Memory usage can be minimal (by writing an iterative heapify() instead of a recursive one). So apart from what is necessary to hold the initial list of items to be sorted, it needs no additional memory space to work.</br>
3. **Simplicity** –  It is simpler to understand than other equally efficient sorting algorithms because it does not use advanced computer science concepts such as recursion.</br>

**Disadvantages:**

1. **Costly:** Heap sort is costly as the constants are higher compared to merge sort even if the time complexity is O(n Log n) for both.</br>
2. **Unstable:** Heap sort is unstable. It might rearrange the relative order.</br>
3. **Efficient:** Heap Sort is not very efficient when working with highly complex data. </br>


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Sorting/README.md"> 🔙 Back</a></h2>
