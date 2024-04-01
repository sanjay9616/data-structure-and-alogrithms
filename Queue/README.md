<h2>Queue</h2>

A Queue Data Structure is a fundamental concept in computer science used for storing and managing data in a specific order. It follows the principle of “First in, First out” (FIFO), where the first element added to the queue is the first one to be removed. Queues are commonly used in various algorithms and applications for their simplicity and efficiency in managing data flow.

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230726165642/Queue-Data-structure1.png" alt="not found">

**Basic Operations of Queue Data Structure**

| Operations       | Best                                                                    | Time Complexiy | Space Complexity |
| ---------------- | ----------------------------------------------------------------------- | -------------- | ---------------- |
| Enqueue (Insert) | Adds an element to the rear of the queue.                               | O(1)           | O(N)             |
| Dequeue (Delete) | Removes and returns the element from the front of the queue.            | O(1)           | O(N)             |
| Peek or Front    | Returns the element at the front of the queue without removing it.      | O(1)           | O(N)             |
| Rear             | This operation returns the element at the rear end without removing it. | O(1)           | O(N)             |
| isEmpty          | Checks if the queue is empty.                                           | O(1)           | O(N)             |
| isFull           | Checks if the queue is full.                                            | O(1)           | O(N)             |
| Size             | Checks if the queue is full.                                            | O(1)           | O(N)             |

```python
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

```

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/README.md"> 🔙 Back</a></h2>