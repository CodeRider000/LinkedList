class Node:
    def __init__(self,data):
        self.data = data
        self.rRef = None
        self.lref = None
    
class CircularlyDoublyLinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        val = self.head
        while True:
            print(val.data)
            val = val.rRef
            if val==self.head:
                return

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
cdll = CircularlyDoublyLinkedList()
node1.lref = node3
node1.rRef = node2
node2.lref = node1
node2.rRef = node3
node3.lref = node2
node3.rRef = node1

cdll.head = node1

cdll.printList()