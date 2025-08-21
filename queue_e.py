class Queue:
    # """ class Queue
    # default : empty Queue/
    # Queue([list])
    # """
    def __init__(self, list = None):
        if list == None:
            self.items = [] 
        else:
            self.items = list   

    def isEmtry(self):
        return self.items == []
    
    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        if self.isEmtry != True:
            return self.items.pop(0)
        
    def print(self):
        print(self.items)
        
    def size(self):
        return len(self.items)
lst = 'A,B,C,D,E,F'.split(',')
print('lst :',lst)

q = Queue()
for i in lst:
    q.enQueue(i)
    q.print()

print(q.size())
