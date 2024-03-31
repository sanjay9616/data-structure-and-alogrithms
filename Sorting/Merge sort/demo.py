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