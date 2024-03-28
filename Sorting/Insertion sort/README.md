**Insertion Sort:**

Insertion sort is a simple sorting algorithm that works similarly to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed in the correct position in the sorted part

**Algorithm**:

To sort an array of size N in ascending order iterate over the array and compare the current element (key) to its predecessor, if the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

```python
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i-1
        while (j >= 0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

print(insertionSort([5, 3, 0, 0, 1, 2]))
```

|                  | Best | Average | Worst  |
| ---------------- | ---- | ------- | ------ |
| Time Complexity  | O(N) | O(N^2)  | O(N^2) |
| Space Complexity | O(1) | O(1)    | O(1)   |

**Characteristics:**

1. This algorithm is one of the simplest algorithms with a simple implementation.</br>
2. Basically, Insertion sort is efficient for small data values.</br>
2. Insertion sort is adaptive in nature, i.e. it is appropriate for data sets that are already partially sorted.</br>


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Sorting/README.md"> 🔙 Back</a></h2>