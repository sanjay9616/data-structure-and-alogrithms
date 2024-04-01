from queue import Queue
q = Queue(maxsize=3) # Number of items allowed in the queue.
print(q.qsize())
q.put('a') # Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
q.put('b') # Return the number of items in the queue.
q.put('c')
print("\nFull: ", q.full())
print("\nElements dequeued from the queue")
print(q.get()) # Remove and return an item from the queue. If queue is empty, wait until an item is available.
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty()) # Return True if the queue is empty, False otherwise.
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full()) # Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
