<h2>Heap</h2>

A Heap is a complete binary tree data structure that satisfies the heap property: for every node, the value of its children is less than or equal to its own value. Heaps are often used to implement priority queues, where the smallest (or largest) element is always at the root of the tree.

**Types of Heap Data Structure:**

**Max heap:** In this heap, the value of the root node must be the greatest among all its child nodes and the same thing must be done for its left and right sub-tree also.

The total number of comparisons required in the max heap is according to the height of the tree. The height of the complete binary tree is always logn; therefore, the time complexity would also be O(logn).

**Min heap:** In this heap, the value of the root node must be the smallest among all its child nodes and the same thing must be done for its left and right sub-tree also.

The total number of comparisons required in the min heap is according to the height of the tree. The height of the complete binary tree is always logn; therefore, the time complexity would also be O(logn).

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221220165711/MinHeapAndMaxHeap1.png" alt="not found">

**Properties of Heap:**

**1. Complete Binary Tree:** A heap tree is a complete binary tree, meaning all levels of the tree are fully filled except possibly the last level, which is filled from left to right. This property ensures that the tree is efficiently represented using an array.

**2. Heap Property:** This property ensures that the minimum (or maximum) element is always at the root of the tree according to the heap type.

**3. Parent-Child Relationship:** The relationship between a parent node at index ‘i’ and its children is given by the formulas: left child at index 2i+1 and right child at index 2i+2 for 0-based indexing of node numbers.

**4. Efficient Insertion and Removal:** Insertion and removal operations in heap trees are efficient. New elements are inserted at the next available position in the bottom-rightmost level, and the heap property is restored by comparing the element with its parent and swapping if necessary. Removal of the root element involves replacing it with the last element and heapifying down.

**5. Efficient Access to Extremal Elements:** The minimum or maximum element is always at the root of the heap, allowing constant-time access





<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/README.md"> 🔙 Back</a></h2>