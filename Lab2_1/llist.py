# Activity 3 : ให้นักศึกษาเขียนโปรแกรม

# สร้าง Link List แล้ว
# เก็บข้อมูล A,B,C,D,E,F แต่ละตัวอักษรอยู่ใน 1 node
# หลังจากนั้นให้แทรกข้อมูล X,Y,Z ระหว่าง C,D

class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class mylist:
    def __init__(self):
        self.head = None

    def append(self, data):
        p = node(data)
        if self.head is None:
            self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p

    def insertAfter(self, data, bf):
        current = self.head
        while current is not None and current.data != bf:
            current = current.next
        if current is None:
            return -1
        p = node(data, current.next)
        current.next = p

    def print_list(self):
        p = self.head
        while p is not None:
            print(p.data, end=' -> ')
            p = p.next
        print('None')

i1 = mylist()
i1.append('A')
i1.append('B')
i1.append('C')
i1.append('D')
i1.append('E')
i1.append('F')
i1.print_list()

print('Insert after :  X Y Z After C')
i1.insertAfter('Z', 'C')
i1.insertAfter('Y', 'C')
i1.insertAfter('X', 'C')

i1.print_list()

print('eiei')