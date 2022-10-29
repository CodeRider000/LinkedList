from ast import Not


class Node:
    def __init__(self,data):
        self.data = data
        self.rRef = None
        self.lref = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        val = self.head
        while val:
            print(val.data)
            val = val.rRef
    def printListRev(self):
        val = self.head
        while val.rRef:
            val = val.rRef
        while val:
            print(val.data)
            val = val.lref
            
    def addAtBegining(self,data):
        if data is None:
            print("data must be given")
            return
        head = self.head
        newnode = Node(data)
        newnode.rRef = head
        head.lref = newnode
        self.head = newnode
        
    def addAtMiddle(self,data,lnode=None,rnode=None):
        if data is None:
            print("data must be given")
            return
        if lnode == None and rnode == None:
            print("any one node must be given")
            return
        elif rnode is None:
            newnode = Node(data)
            rnode = lnode.rRef
            newnode.rRef = rnode
            newnode.lref = lnode
            rnode.lref = newnode
            lnode.rRef = newnode
        elif lnode is None:            
            newnode = Node(data)
            lnode = rnode.lref
            newnode.rRef = rnode
            newnode.lref = lnode
            rnode.lref = newnode
            lnode.rRef = newnode
        else :
            newnode = Node(data)
            newnode.rRef = rnode
            newnode.lref = lnode
            rnode.lref = newnode
            lnode.rRef = newnode
    def addAtEnd(self,data):
        newnode = Node(data)
        last = self.head
        while last.rRef:
            last = last.rRef
        last.rRef = newnode
        newnode.lref = last
    def RemoveNode(self,key):
        #if key value is present in the head node
        if self.head.data == key:
            self.head = self.head.rRef
            self.head.lref = None
        val = self.head
        keynode = None
        #collecting the keynode where key data is presented
        while val.rRef:
            if val.rRef.data == key:
                keynode = val.rRef
            val = val.rRef
        if keynode:        
            lnode = keynode.lref
            #if key value is present in the last node
            if keynode.rRef == None:
                lnode.rRef = None
            #if key value is in the middle nodes
            else:
                rnode = keynode.rRef
                lnode.rRef = rnode
                rnode.lref = lnode
        else:
            print("node is not in the list")
    def find(self,key):
        val = self.head
        c = 1
        while val.rRef:
            if val.rRef.data == key:
                return c
            c += 1
            val = val.rRef
        print("node not in the list")
        
    def length(self,key):
        val = self.head
        c = 1
        while val.rRef:
            c += 1
            val = val.rRef
        return c

    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
dll = DoublyLinkedList()
dll.head = node1
node1.rRef = node2
node2.lref = node1
node2.rRef= node3
node3.lref = node2
dll.addAtBegining(0)
dll.addAtMiddle(2.5,lnode=node2)
dll.addAtEnd(4)
dll.printList()
dll.RemoveNode(4)
dll.printList()