**QuickSort Sort:**

QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

It follows divides, conquer and combine approach.

**How does QuickSort work:**

The key process in quickSort is a partition(). The target of partitions is to place the pivot (any element can be chosen to be a pivot) at its correct position in the sorted array and put all smaller elements to the left of the pivot, and all greater elements to the right of the pivot.

Partition is done recursively on each side of the pivot after the pivot is placed in its correct position and this finally sorts the array.


```python
def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if (arr[j] <= pivot):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def quickSort(arr, left, right):
    if (left < right):
        pi = partition(arr, left, right)
        quickSort(arr, left, pi - 1)
        quickSort(arr, pi + 1, right)

arr = [8, 7, 2, 1, 0, 9, 6]
quickSort(arr, 0, len(arr) - 1)
print(arr)

```


|                  | Best        | Average     | Worst  |
| ---------------- | ----------- | ----------- | ------ |
| Time Complexity  | O(N log(N)) | O(N log(N)) | O(N^2) |
| Space Complexity | O(1)        | O(1)        | O(1)   |

**Advantages:**

1. It is a divide-and-conquer algorithm that makes it easier to solve problems.</br>
2. It is efficient on large data sets.</br>
3. It has a low overhead, as it only requires a small amount of memory to function.</br>

**Disadvantages:**

1. It has a worst-case time complexity of O(N2), which occurs when the pivot is chosen poorly.</br>
2. It is not a good choice for small data sets.</br>
3. It is not a stable sort, meaning that if two elements have the same key, their relative order will not be preserved in the sorted output in case of quick sort, because here we are swapping elements according to the pivot’s position (without considering their original positions).</br>


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Sorting/README.md"> 🔙 Back</a></h2>
