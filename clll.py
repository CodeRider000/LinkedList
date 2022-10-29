class Node:
    def __init__(self,data):
        self.data = data
        self.nextRef = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printlist(self):
        val = self.head
        while True:
            print(val.data)
            val = val.nextRef
            if val == self.head:
                return
    def AddNode(self,prenode,data):
        if prenode == None:
            print("previous node must be given")
            return
        if data == None:
            print("node data must be given")
            return
        newnode = Node(data)
        newnode.nextRef = prenode.nextRef
        prenode.nextRef = newnode
    def AddNodeHead(self,data):
        if data == None:
            print("node data must be given")
            return
        head = self.head
        newnode = Node(data)
        newnode.nextRef = self.head
        while head.nextRef != self.head:
            head = head.nextRef
        head.nextRef = newnode
        self.head = newnode
    def RemoveNode(self,key):
        if key == None:
            print("data must be given")
            return
        if True:
            val = self.head
            while val.nextRef != self.head:
                val = val.nextRef
                if key == val.data:
                    t = True 
                    break
            else: 
                t= False
        if t:        
            n = self.head
            if n.data==key:
                self.head = n.nextRef
                head = self.head
                while head.nextRef != self.head:
                    head = head.nextRef
                head.nextRef = n.nextRef
                return
            while n:
                prenode = n
                keynode = n.nextRef
                if keynode.data == key:
                    prenode.nextRef = keynode.nextRef
                    n = None
                else:
                    n = n.nextRef
        else:
            print("node is not in the list")
            
    def length(self):
        c = 1
        val = self.head
        while val.nextRef != self.head:
            c += 1
            val = val.nextRef
        return c
        
        
cll = LinkedList()
node1 = Node(1)
cll.head = node1
node2 = Node(2)
node3 = Node(3)

node1.nextRef = node2
node2.nextRef = node3
node3.nextRef = node1

cll.AddNode(prenode = node2,data = 2.5)
cll.AddNodeHead(0)
cll.AddNode(node3,4)
cll.RemoveNode(2.5)
cll.printlist()
cll.RemoveNode(2.5)
print(cll.length())