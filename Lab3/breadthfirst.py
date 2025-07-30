class Queue:
    def __init__(self):
        self.items = []
    
    def enQueue(self,i):
        self.items.append(i)
        
    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print('Error : Queue Underflow')
            return -1
    def size(self):
        return len(self.items)  
    
    def isEmpty(self):
        return self.items == []

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
             self.data = data


    def PrintTree(self):
            if self.left:
                self.left.PrintTree()
            print( self.data),
            if self.right:
                self.right.PrintTree()

    def breadthFirst(self,root ,queue:Queue) :
        q = queue
        q.enQueue(root)
        res = []
        while (not q.isEmpty()):
            n = q.deQueue()
            if n.left != None:
                q.enQueue(n.left)
            if n.right != None:
                q.enQueue(n.right)
            res.append(n.data)
            
        return res
            
          

lst = [3,16,9,23,11,7,5,34,19,2]
root = Node(15)
q = Queue()
for i in lst:
  root.insert(i)

print(root.breadthFirst(root , q))