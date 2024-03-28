**Bubble Sort:**

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.


**Algorithm**:

    • traverse from left and compare adjacent elements and the higher one is placed at right side.
    • In this way, the largest element is moved to the rightmost end at first.
    • This process is then continued to find the second largest and place it and so on until the data is sorted.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230526103842/1.webp" alt="not found">

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230526103914/2.webp" alt="not found">

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230526103949/3.webp" alt="not found">

```python
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort([5, 3, 3, 6, 7, 2]))
```

|                  | Best | Average | Worst  |
| ---------------- | ---- | ------- | ------ |
| Time Complexity  | O(N) | O(N^2)  | O(N^2) |
| Space Complexity | O(1) | O(1)    | O(1)   |

**Advantages:**

1. Bubble sort is easy to understand and implement.</br>
2. It does not require any additional memory space.</br>
3. It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.</br>

**Disadvantages:**

1. Bubble sort has a time complexity of O(N^2) which makes it very slow for large data sets.</br>
2. It does not require any additional memory space.</br>
3. Bubble sort is a comparison-based sorting algorithm, which means that it requires a comparison operator to determine the relative order of elements in the input data set. It can limit the efficiency of the algorithm in certain cases.</br>


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Sorting/README.md"> 🔙 Back</a></h2>