**Implementation of Max Heap:**

```python
class maxHeap:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.heapSize = 0
        self.heap = [None] * self.maxSize

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def getMax(self):
        return self.heap[0]

    def currSize(self):
        return self.heapSize

    def maxHeapify(self, i):
        leftIndex = self.leftChild(i)
        rightIndex = self.rightChild(i)
        largest = i
        if (leftIndex < self.heapSize and self.heap[leftIndex] > self.heap[i]):
            largest = leftIndex
        if (rightIndex < self.heapSize and self.heap[rightIndex] > self.heap[i]):
            largest = rightIndex
        if (largest != i):
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)

    def removeMax(self):
        if (self.heapSize <= 0):
            return None
        if (self.heapSize == 1):
            self.heapSize -= 1
            return self.heap[0]
        root = self.heap[0]
        self.heap[0] = self.heap[self.heapSize - 1]
        self.heapSize -= 1
        self.maxHeapify(0)
        return root

    def increaseKey(self, i, newValue):
        self.heap[i] = newValue
        while (i != 0 and self.heap[self.parent(i)] < self.heap[i]):
            self.heap[self.parent(
                i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def insertKey(self, key):
        if (self.heapSize == self.maxSize):
            print("Overflow: Could not insertKey")
            return
        self.heapSize += 1
        i = self.heapSize - 1
        self.heap[i] = key
        while (i != 0 and self.parent(i) < self.heap[i]):
            self.heap[self.parent(
                i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def deleteKey(self, i):
        self.increaseKey(i, float('inf'))
        self.removeMax()


heap = maxHeap(5)
heap.insertKey(10)
heap.insertKey(12)
heap.insertKey(14)
heap.deleteKey(1)
print(heap.heap[:heap.heapSize])
```

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Heap/README.md"> 🔙 Back</a></h2>