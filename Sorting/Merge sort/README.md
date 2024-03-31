**Merge Sort:**

Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.

In simple terms, we can say that the process of merge sort is to divide the array into two halves, sort each half, and then merge the sorted halves back together. This process is repeated until the entire array is sorted.

It follows divides, conquer and combine approach.

**Algorithm**:

Merge sort is a recursive algorithm that continuously splits the array in half until it cannot be further divided i.e., the array has only one element left (an array with one element is always sorted). Then the sorted subarrays are merged into one sorted array.

```python
def mergeSort(arr):
    if (len(arr) > 1):
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while (i < len(L) and j < len(R)):
            if (L[i] <= R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while (i < len(L)):
            arr[k] = L[i]
            i += 1
            k += 1
        while (j < len(R)):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

print(mergeSort([9, 8, 7, 6, 5, 3]))
```

**Complexity Analysis of Merge Sort:** = T(n) = 2T(n/2) + θ(n)

![Screenshot from 2024-03-28 22-26-57](https://github.com/sanjay9616/data-structure-and-alogrithms/assets/87460579/faa8e270-aca2-4b2c-81eb-c871cfda818e)


|                  | Best        | Average     | Worst       |
| ---------------- | ----------- | ----------- | ----------- |
| Time Complexity  | O(N log(N)) | O(N log(N)) | O(N log(N)) |
| Space Complexity | O(N)        | O(N)        | O(N)        |

**Advantages:**

1. Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal elements in the input array.</br>
2. Merge sort has a worst-case time complexity of O(N logN), which means it performs well even on large datasets.</br>
3. Merge sort is a naturally parallelizable algorithm, which means it can be easily parallelized to take advantage of multiple processors or threads.</br>

**Disadvantages:**

1. Merge sort requires additional memory to store the merged sub-arrays during the sorting process.</br>
2. Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.</br>
3. For small datasets, Merge sort has a higher time complexity than some other sorting algorithms, such as insertion sort. This can result in slower performance for very small datasets.</br>


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Sorting/README.md"> 🔙 Back</a></h2>
