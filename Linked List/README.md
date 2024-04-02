Linked List is a linear data structure, in which elements are not stored at a contiguous location, rather they are linked using pointers. Linked List forms a series of connected nodes, where each node stores the data and the address of the next node.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220712172013/Singlelinkedlist.png" alt="not found">

**Node Structure:** A node in a linked list typically consists of two components: </br>
**Data:** It holds the actual value or data associated with the node. </br>
**Next Pointer:** It stores the memory address (reference) of the next node in the sequence. </br>
**Head and Tail:** The linked list is accessed through the head node, which points to the first node in the list. The last node in the list points to NULL or nullptr, indicating the end of the list. This node is known as the tail node.

**Why linked list data structure needed?**

Here are a few advantages of a linked list that is listed below, it will help you understand why it is necessary to know.</br>
**1. Dynamic Data structure:** The size of memory can be allocated or de-allocated at run time based on the operation insertion or deletion.</br>
**2. Ease of Insertion/Deletion:** The insertion and deletion of elements are simpler than arrays since no elements need to be shifted after insertion and deletion, Just the address needed to be updated.</br>
**3. Efficient Memory Utilization:** As we know Linked List is a dynamic data structure the size increases or decreases as per the requirement so this avoids the wastage of memory. </br>
**4. Implementation:** Various advanced data structures can be implemented using a linked list like a stack, queue, graph, hash maps, etc.

**Types of Linked List:**

**<a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Linked%20List/singlyLinkedList.md">1. Singly Linked List:</a>**
In a singly linked list, each node contains a reference to the next node in the sequence. Traversing a singly linked list is done in a forward direction.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220712172013/Singlelinkedlist.png" alt="not found">

**<a href="">2. Doubly Linked List:</a>**
In a doubly linked list, each node contains references to both the next and previous nodes. This allows for traversal in both forward and backward directions, but it requires additional memory for the backward reference.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220712180755/Doublylinkedlist.png" alt="not found">

**<a href="">3. Circular linked list:</a>**
A circular doubly linked list is defined as a circular linked list in which each node has two links connecting it to the previous node and the next node.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220712181336/Circularlinkedlist.png" alt="not found">

**<a href="">4. Circular Doubly Linked List:</a>**
In a circular linked list, the last node points back to the head node, creating a circular structure. It can be either singly or doubly linked.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220830114920/doubly-660x177.jpg" alt="not found">

**<a href="">5. Header Linked List:</a>**
A header node is a special node that is found at the beginning of the list. A list that contains this type of node, is called the header-linked list. This type of list is useful when information other than that found in each node is needed.

**Advantages of Linked Lists**

**1. Dynamic Size:** Linked lists can grow or shrink dynamically, as memory allocation is done at runtime. </br>
**2. Insertion and Deletion:** Adding or removing elements from a linked list is efficient, especially for large lists. </br>
**3. Flexibility:** Linked lists can be easily reorganized and modified without requiring a contiguous block of memory. </br>

**Disadvantages of Linked Lists**

**1. Random Access:** Unlike arrays, linked lists do not allow direct access to elements by index. Traversal is required to reach a specific node. </br>
**2. Extra Memory:** Linked lists require additional memory for storing the pointers, compared to arrays. </br>

**Conclusion:**

Linked lists are versatile data structures that provide dynamic memory allocation and efficient insertion and deletion operations. Understanding the basics of linked lists is essential for any programmer or computer science enthusiast. With this knowledge, you can implement linked lists to solve various problems and expand your understanding of data structures and algorithms.


<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/README.md"> 🔙 Back</a></h2>