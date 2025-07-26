# Activity 2 : ให้นักศึกษาเขียนโปรแกรม

# สร้าง Queue แล้ว
# เก็บข้อมูล ABCDEF
# หลังจากนั้นให้แสดงผล ขนาดของข้อมูลที่เก็บใน Queue
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
    
lst = list('ABCDEF')

print('enQueue')
print('')
q = Queue()
for i in lst:
    print(q.items)
    q.enQueue(i)
print(q.items)

print('----------------------------')
print()
print('deQueue')
for i in range(len(q.items)):
    print(q.items)
    q.deQueue()
print(q.items)