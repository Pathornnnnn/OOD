class Stack:
    
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)
    def pop(self):
        return self.items.pop()

    def push(self,item):
        self.items.append(item)
        self.size += 1

    def print(self):
        print(self.items)

    def size(self):
        return self.size


s = Stack()
lst = 'A B C D E F'.split(" ")
print("lst : ",lst)
print()

print('PUSH')
for i in lst:
    s.push(i)
    s.print()
print()

print('POP')
for i in range(s.size):
    s.pop()
    s.print()
