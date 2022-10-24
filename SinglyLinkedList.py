class Node:
    def __init__(self,data):
        self.data = data
        self.nextRef = None
#node class to represent and creation of the node
#it has data as .data and reference to next node as .nextRef
#linkedlist class will initiate the linked list as it stores the head node in its self.head instance
#it is the starting point of the linked list
class LinkedList:
    def __init__(self):
        self.head = None
        
#printlist method will traverse through the linked list and print the data values until the last node
#it will terminate at last node as the node has next node reference as "None"
    def printlist(self):
        val = self.head
        while val:
            print(val.data)
            val = val.nextRef
            

#AddatBegining method is used to a node at begining of the linked list
#when added at begining the node will automatically becomes the head node
#with this method , a node can be added by passing the data or a node
    def AddatBegining(self,node=None,data=None):
        if data is None:
            if node is None:
                print("Node is empty")
                return
            node.nextRef = self.head
            self.head = node
            return
        newnode = Node(data)
        newnode.nextRef = self.head
        self.head = newnode
        

#AddatMiddle method will have same functionality as AddatBegining but we can add at middle of the list
#this will insert the node in the middle by interchanging the next node reference between the previous node and insertion node
    def AddatMiddle(self,preNode=None,newnode=None,data = None):
        if data is None:
            if preNode is None:
                print("must give a previous node")
                return
            elif newnode is None:
                print("must give a inserting node")
                return
            newnode.nextRef = preNode.nextRef
            preNode.nextRef = newnode
            return
        newnode = Node(data)
        newnode.nextRef = preNode.nextRef
        preNode.nextRef = newnode


#this method will add the required node at the end of the linked list
    def AddatEnd(self,newnode=None):
        if newnode is None:
            print("must give a inserting node")
            return
        if self.head == Node:
            self.head = newnode
            return
        last = self.head
        while last.nextRef:
            last = last.nextRef
        last.nextRef = newnode        
        
#this node will delete the required node by unlinking the node from chain
    def remove(self,key):
        if key is None:
            print("Data must be given")
            return    
        n = self.head
        if n.data==key:
            self.head = n.nextRef
        while n:
            prenode = n
            keynode = n.nextRef
            if keynode.data == key:
                prenode.nextRef = keynode.nextRef
                del keynode
                n = None
            else:
                n = n.nextRef
                
                
#this method will find the length of the linked list or number of the nodes in it
    def length(self):
        n = self.head
        l = 0
        while n:
            l += 1
            n = n.nextRef
        return l
    
#this method will find the node with the helf of the given node data and returns its position
    def find(self,key):
        keynode = self.head
        c = 0
        while keynode:
            c += 1
            if keynode.data == key:
                return c
            keynode = keynode.nextRef
            
#this will return the node data of a node at a given position
    def getNode(self,nod_pos):
        keynode = self.head
        c = 0
        while keynode:
            c+=1
            if c == nod_pos:
                return keynode.data
            keynode = keynode.nextRef   

#this method has the same functionality as previous one but will return the node data of repective node position from end.
    def getNodeFormEnd(self,key):
        l = self.length()
        node_pos = l - key +1
        return self.getNode(node_pos)