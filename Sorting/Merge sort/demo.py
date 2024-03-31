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
