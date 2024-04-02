**Operations Supported by Singly Linked List:**

| Algorithm          | Best | Average | Worst | Space Complexity |
| ------------------ | ---- | ------- | ----- | ---------------- |
| Insert At Begining | O(1) | O(1)    | O(1)  | O(1)             |
| Insert At End      | O(N) | O(N)    | O(N)  | O(1)             |
| Insert At Index    | O(1) | O(N)    | O(N)  | O(1)             |
| Update At Begining | O(1) | O(1)    | O(1)  | O(1)             |
| Update At End      | O(N) | O(N)    | O(N)  | O(1)             |
| Update At Index    | O(1) | O(N)    | O(N)  | O(1)             |
| Delete At Begining | O(1) | O(1)    | O(1)  | O(1)             |
| Delete At End      | O(N) | O(N)    | O(N)  | O(1)             |
| Delete At Index    | O(1) | O(N)    | O(N)  | O(1)             |
| Get Size           | O(N) | O(N)    | O(N)  | O(1)             |

**Implementation of Singly Linked List:**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        node = Node(data)
        if(not self.head):
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insertAtEnd(self, data):
        node = Node(data)
        if(not self.head):
            self.head = node
            return
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = node

    def insertAtIndex(self, data, index):
        node = Node(data)
        if(index == 0):
            self.insertAtBegin(data)
        else:
            position = 0
            curr = self.head
            while(curr and position + 1 != index):
                position += 1
                curr = curr.next
            if(curr):
                node.next = curr.next
                curr.next = node
            else:
                print("Index not present")

    def updateNode(self, val, index):
        if(index == 0):
            self.head.data = val
        else:
            position = 0
            curr = self.head
            while(curr and position != index):
                position += 1
                curr = curr.next
            if(curr):
                curr.data = val
            else:
                print("Index not present")

    def deleteAtBegin(self):
        if(not self.head):
            return
        self.head = self.head.next

    def deleteAtEnd(self):
        if(not self.head):
            return
        curr = self.head
        while(curr.next.next):
            curr = curr.next
        curr.next = curr.next.next

    def deletAtIndex(self, index):
        if(not self.head):
            return
        if(index == 0):
            self.deleteAtBegin()
        else:
            position = 0
            curr = self.head
            while(curr and position + 1 != index):
                position += 1
                curr = curr.next
            if(curr and curr.next):
                curr.next = curr.next.next
            else:
                print("Index not present")

    def getSize(self):
        if(not self.head):
            return 0
        size = 0
        curr = self.head
        while(curr):
            curr = curr.next
            size += 1
        return size

    def displayList(self):
        if(not self.head):
            return
        curr = self.head
        while(curr):
            print(curr.data, end=",")
            curr = curr.next

list = LinkedList()
list.insertAtBegin(1)
list.insertAtEnd(2)
print("Size of linked list: ", list.getSize())
list.displayList()
```