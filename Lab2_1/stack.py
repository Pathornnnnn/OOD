class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        if self.items != []:
            s = f'stack of '+ str(self.size())+' items : '
            for ele in self.items:
                s += str(ele)+' '
            return s
        else:
            return 'stack of '+ str(self.size())+' items : []'

lst = list('ABCDEF')

s = Stack()

# PUSH ABCDEF
print('------------------------ PUSH')
print(s)
for i in lst:
    s.push(i)    
    print(s.items)
print(s)


#POP ABCDEF
print()
print('----------------------- POP')
for i in range(s.size()):
    s.pop()
    print(s.items)
print(s)