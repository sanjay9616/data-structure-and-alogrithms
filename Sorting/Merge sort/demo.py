class Queue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = capacity - 1
        self.size = 0
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enQueue(self, data):
        if (self.isFull()):
            print("Queue is full.")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.queue[self.rear] = data
        self.size = self.size + 1

    def deQueue(self):
        if (self.isEmpty()):
            print("Queue is empty")
            return
        x = self.queue[self.front]
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1
        return x

    def getFront(self):
        if (self.isEmpty()):
            print("Queue is empty")
            return
        return self.queue[self.front]

    def getRear(self):
        if (self.isEmpty()):
            print("Queue is empty")
            return
        return self.queue[self.rear]

    def displayQueue(self):
        if (self.isEmpty()):
            print("Queue is empty")
            return
        return self.queue[self.front: self.rear + 1]


queue = Queue(5)
queue.enQueue(1)
print(queue.getFront(), queue.getRear(), queue.displayQueue())
queue.enQueue(2)
print(queue.getFront(), queue.getRear(), queue.displayQueue())
queue.enQueue(3)
print(queue.getFront(), queue.getRear(), queue.displayQueue())
queue.deQueue()
print(queue.getFront(), queue.getRear(), queue.displayQueue())
queue.deQueue()
print(queue.getFront(), queue.getRear(), queue.displayQueue())
queue.deQueue()
print(queue.getFront(), queue.getRear(), queue.displayQueue())
