class D_stack:
    def __init__(self):
        self.items = []
        
    def right_push(self, item):
        self.items.append(item)
    
    def right_pop(self):
        return self.items.pop()

    def left_push(self, item):
        self.items.insert(0,item)
    
    def left_pop(self):
        return self.items.pop(0)
    

Dstack1 = D_stack()
Dstack2 = D_stack()
Dstack3 = D_stack()
Dstack4 = D_stack()

lst = list('ABCD')


#Stack test
#left push -> left pop
print("left push -> left pop")
for i in lst:
    print(Dstack1.items)
    Dstack1.left_push(i)
    
for i in range(len(Dstack1.items)):
    print(Dstack1.items)
    Dstack1.left_pop()
print(Dstack1.items)
print()

#right push -> right pop
print("#right push -> right pop")
for i in lst:
    print(Dstack2.items)
    Dstack2.right_push(i)
    
for i in range(len(Dstack2.items)):
    print(Dstack2.items)
    Dstack2.right_pop()
print(Dstack2.items)
print()

#Queue test 
#left push -> right pop
print('left push -> right pop')
for i in lst:
    print(Dstack3.items)
    Dstack3.left_push(i)
    
for i in range(len(Dstack3.items)):
    print(Dstack3.items)
    Dstack3.right_pop()
print(Dstack3.items)
print()

#right push -> left pop
print("right push -> left pop")
for i in lst:
    print(Dstack4.items)
    Dstack4.right_push(i)
    
for i in range(len(Dstack4.items)):
    print(Dstack4.items)
    Dstack4.left_pop()
print(Dstack4.items)
print()