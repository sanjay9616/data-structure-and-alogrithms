<h2>Heap</h2>

A Heap is a complete binary tree data structure that satisfies the heap property: for every node, the value of its children is less than or equal to its own value. Heaps are often used to implement priority queues, where the smallest (or largest) element is always at the root of the tree.

**Types of Heap Data Structure:**

**Max heap:** In this heap, the value of the root node must be the greatest among all its child nodes and the same thing must be done for its left and right sub-tree also. <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Heap/maxHeap.md">View Implementation</a>

The total number of comparisons required in the max heap is according to the height of the tree. The height of the complete binary tree is always logn; therefore, the time complexity would also be O(logn).

**Min heap:** In this heap, the value of the root node must be the smallest among all its child nodes and the same thing must be done for its left and right sub-tree also. <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Heap/minHeap.md">View Implementation</a>

The total number of comparisons required in the min heap is according to the height of the tree. The height of the complete binary tree is always logn; therefore, the time complexity would also be O(logn).

<a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Heap/heapq.md">View - Heap queue (or heapq) in Python</a>

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221220165711/MinHeapAndMaxHeap1.png" alt="not found">

**Properties of Heap:**

**1. Complete Binary Tree:** A heap tree is a complete binary tree, meaning all levels of the tree are fully filled except possibly the last level, which is filled from left to right. This property ensures that the tree is efficiently represented using an array. </br>
**2. Heap Property:** This property ensures that the minimum (or maximum) element is always at the root of the tree according to the heap type. </br>
**3. Parent-Child Relationship:** The relationship between a parent node at index ‘i’ and its children is given by the formulas: left child at index 2i+1 and right child at index 2i+2 for 0-based indexing of node numbers. </br>
**4. Efficient Insertion and Removal:** Insertion and removal operations in heap trees are efficient. New elements are inserted at the next available position in the bottom-rightmost level, and the heap property is restored by comparing the element with its parent and swapping if necessary. Removal of the root element involves replacing it with the last element and heapifying down. </br>
**5. Efficient Access to Extremal Elements:** The minimum or maximum element is always at the root of the heap, allowing constant-time access </br>

**Operations Supported by Heap:**

| Algorithm                                            | Best    | Average | Worst   | Space Complexity |
| ---------------------------------------------------- | ------- | ------- | ------- | ---------------- |
| Heapify                                              | O(1)    | O(logN) | O(logN) | O(1)             |
| Insertion                                            | O(1)    | O(logN) | O(logN) | O(1)             |
| Deletion                                             | O(1)    | O(logN) | O(N^2)  | O(1)             |
| getMax (For max-heap) or getMin (For min-heap)       | O(1)    | O(1)    | O(1)    | O(1)             |
| removeMax (For max-heap) or removeMin (For min-heap) | O(logN) | O(logN) | O(logN) | O(1)             |

**Applications of Heap Data Structure:**

**1. Priority Queues:** Priority queues can be efficiently implemented using Binary Heap because it supports insert(), delete() and extractmax(), decreaseKey() operations in O(log N) time. </br>
1. **Binomial** Heap and **Fibonacci** Heap are variations of Binary Heap. These variations perform union also in O(log N) time which is an O(N) operation in Binary Heap. </br>
**3. Order statistics:** The Heap data structure can be used to efficiently find the kth smallest (or largest) element in an array. You can see this gfg article to know more about the kth smallest or largest element.</br>

**Advantages:**

1. Fast access to maximum/minimum element (O(1)). </br>
2. Efficient Insertion and Deletion operations (O(log n)) Flexible size. </br>
3. Can be efficiently implemented as an array. </br>
4. Suitable for real-time applications. </br>

**Disadvantages:**

1. Not suitable for searching for an element other than maximum/minimum (O(n) in worst case). </br>
2. Extra memory overhead to maintain heap structure. </br>
3. Can be efficiently implemented as an array. </br>
4. Slower than other data structures like arrays and linked lists for non-priority queue operations. </br>




<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/README.md"> 🔙 Back</a></h2>