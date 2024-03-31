**Counting Sort:**

Counting Sort is a non-comparison-based sorting algorithm that works well when there is limited range of input values. It is particularly efficient when the range of input values is small compared to the number of elements to be sorted. The basic idea behind Counting Sort is to count the frequency of each distinct element in the input array and use that information to place the elements in their correct sorted positions.

**Algorithm**:

1. Declare an auxiliary array countArray[] of size max(inputArray[])+1 and initialize it with 0. </br>
2. Traverse array inputArray[] and map each element of inputArray[] as an index of countArray[] array, i.e., execute countArray[inputArray[i]]++ for 0 <= i < N.</br>
3. Calculate the prefix sum at every index of array inputArray[].</br>
4. Create an array outputArray[] of size N.</br>
5. Traverse array inputArray[] from end and update outputArray[ countArray[ inputArray[i] ] – 1] = inputArray[i]. Also, update countArray[ inputArray[i] ] = countArray[ inputArray[i] ]- – .</br>


```python
def countSort(arr):
	M = max(arr)
	count_array = [0] * (M + 1)
	for num in arr:
		count_array[num] += 1
	for i in range(1, M + 1):
		count_array[i] += count_array[i - 1]
	output_array = [0] * len(arr)
	for i in range(len(arr) - 1, -1, -1):
		output_array[count_array[arr[i]] - 1] = arr[i]
		count_array[arr[i]] -= 1
	return output_array

arr = [4, 3, 12, 1, 5, 5, 3, 9]
print(countSort(arr)) # Output = [1, 3, 3, 4, 5, 5, 9, 12]
```


|                  | Best   | Average | Worst  |
| ---------------- | ------ | ------- | ------ |
| Time Complexity  | O(N+M) | O(N+M)  | O(N+M) |
| Space Complexity | O(N+M) | O(N+M)  | O(N+M) |

where N and M are the space taken by outputArray[] and countArray[] respectively.

**Advantages:**

1. Counting sort generally performs faster than all comparison-based sorting algorithms, such as merge sort and quicksort, if the range of input is of the order of the number of input. </br>
2. Counting sort is easy to code </br>
3. Counting sort is a stable algorithm.</br>

**Disadvantages:**

1. Counting sort doesn’t work on decimal values.</br>
2. Counting sort is inefficient if the range of values to be sorted is very large.</br>
3. Counting sort is not an In-place sorting algorithm, It uses extra space for sorting the array elements. </br>


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Sorting/README.md"> 🔙 Back</a></h2>
