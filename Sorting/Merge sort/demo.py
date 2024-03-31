class minHeap:
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

    def getMim(self):
        return self.heap[0]

    def currSize(self):
        return self.heapSize

    def minHeapify(self, i):
        leftIndex = self.leftChild(i)
        rightIndex = self.rightChild(i)
        smallest = i
        if (leftIndex < self.heapSize and self.heap[leftIndex] < self.heap[smallest]):
            smallest = leftIndex
        if (rightIndex < self.heapSize and self.heap[rightIndex] < self.heap[i]):
            smallest = rightIndex
        if (smallest != i):
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest)

    def removeMin(self):
        if (self.heapSize <= 0):
            return None
        if (self.heapSize == 1):
            self.heapSize -= 1
            return self.heap[0]
        root = self.heap[0]
        self.heap[0] = self.heap[self.heapSize - 1]
        self.heapSize -= 1
        self.minHeapify(0)
        return root

    def decreaseKey(self, i, newValue):
        self.heap[i] = newValue
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def insertKey(self, key):
        if (self.heapSize == self.maxSize):
            print("Overflow: Could not insertKey")
            return
        self.heapSize += 1
        i = self.heapSize - 1
        self.heap[i] = key
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def deleteKey(self, i):
        self.decreaseKey(i, float('-inf'))
        self.removeMin()


heap = minHeap(5)
heap.insertKey(14)
heap.insertKey(12)
heap.insertKey(10)
heap.removeMin()
print(heap.heap[:heap.heapSize])