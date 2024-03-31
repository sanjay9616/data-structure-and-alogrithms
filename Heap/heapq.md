In Python, it is available using the “heapq” module. The property of this data structure in Python is that each time the smallest heap element is popped(min-heap). Whenever elements are pushed or popped, heap structure is maintained. The heap[0] element also returns the smallest element each time. Let’s see various Operations on the heap in Python.

**heapify(iterable)**: This function is used to convert the iterable into a heap data structure. i.e. in heap order.

**heappush(heap, ele)**: This function is used to insert the element mentioned in its arguments into a heap. The order is adjusted, so that heap structure is maintained.

**heappop(heap)**: This function is used to remove and return the smallest element from the heap. The order is adjusted, so that heap structure is maintained.

**heappushpop(heap, ele)**:- This function combines the functioning of both push and pop operations in one statement, increasing efficiency. Heap order is maintained after this operation.

**heapreplace(heap, ele)**:- This function also inserts and pops elements in one statement, but it is different from the above function. In this, the element is first popped, then the element is pushed. i.e, the value larger than the pushed value can be returned. heapreplace() returns the smallest value originally in the heap regardless of the pushed element as opposed to heappushpop().

**nlargest(k, iterable, key = fun)**: This function is used to return the k largest elements from the iterable specified and satisfy the key if mentioned.

**nsmallest(k, iterable, key = fun)**: This function is used to return the k smallest elements from the iterable specified and satisfy the key if mentioned.

```python
import heapq
li = [5, 7, 9, 1, 3]
heapq.heapify(li)
print ("The created heap is : ",(list(li))) # Output = The created heap is :  [1, 3, 9, 7, 5]
```

```python
import heapq
li = [5, 7, 9, 1, 3]
heapq.heapify(li)
print("The created heap is : ", list(li)) # Output = The created heap is : [1, 3, 9, 7, 5]
heapq.heappush(li, 4)
print("The modified heap after push is : ", list(li)) # Output = The modified heap after push is : [1, 3, 4, 7, 5, 9]
print("The popped and smallest element is : ", heapq.heappop(li)) #Output = The popped and smallest element is : 1
```

```python
import heapq
li1 = [5, 1, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]
heapq.heapify(li1)
heapq.heapify(li2)
print("The popped item using heappushpop() is : ", heapq.heappushpop(li1, 2)) # Output = The popped item using heappushpop() is :  1
print("The popped item using heapreplace() is : ", heapq.heapreplace(li2, 2)) # Output = The popped item using heapreplace() is :  3
```

```python
import heapq
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(li1)
print("The 3 largest numbers in list are : ", heapq.nlargest(3, li1)) # Output = The 3 largest numbers in list are :  [10, 9, 8]
print("The 3 smallest numbers in list are : ", heapq.nsmallest(3, li1)) # Output = The 3 smallest numbers in list are :  [1, 3, 4]
```

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Heap/README.md"> 🔙 Back</a></h2>