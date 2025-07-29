class priNode:
    def __init__(self, data, next=None , sec=None):
        self.data = data
        self.next = next
        self.sec = sec

class secNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Two_D_LinkedList:
    def __init__(self):
        self.head = None
        
    def Append_primary(self, pri_data):
        p = priNode(pri_data)
        if self.head == None:
            self.head = p
            return p
        else:
            p = priNode(pri_data)
            current = self.head
            while current.next != None:
                current = current.next
            current.next = p
            return p
    
    def Delete_primary(self, pri_data):
        current = self.head
        bf = None # before
        while current.data != pri_data:
            if current.next == None:
                return -1
            bf = current
            current = current.next
        if current.data != pri_data:
            return -1
        
        #delete sec_data of pri_data
        current_sec = current.sec
        while current_sec != None:
            now = current_sec
            current_sec = current_sec.next
            #print('del',now.data)
            del(now)
        
        #delete pri_data
        if bf != None:
            bf.next = current.next
            del(current)
        else:
            self.head = current.next
            del(current)
        return 1
    
    def Append_secondary(self, pri_data , sec_data):
        current = self.head
        while current.data != pri_data:
            if current.next == None:
                return -1
            current = current.next
        if current.data != pri_data:
            return -1
        if current.sec != None:
            sec_now = current.sec
            while sec_now.next != None:
                if sec_now.next == None:
                    return -1
                sec_now = sec_now.next
            sec_now.next = secNode(sec_data)
            return 1
        current.sec = secNode(sec_data)
        return 1
        
    def Delete_secondary(self, pri_data, sec_data):
        #loop for pri
        current = self.head
        while current.data != pri_data:
            if current.next == None:
                return -1
            bf = current
            current = current.next
        if current.data != pri_data:
            return -1
        
        #loop for sec
        current_sec = current.sec
        bf = None # before
        while current_sec.data != sec_data:
            if current_sec.next == None:
                return -1
            bf = current_sec
            current_sec = current_sec.next
        if current_sec.data != sec_data:
            return -1
        if bf != None:
            bf.next = current_sec.next
            del(current_sec)
        else:
            current.sec = current_sec.next
            del(current_sec)
        
        return 1
        
    def Print_List(self):
        p = self.head
        while p != None:
            print(p.data ,end=' : ')
            sec = p.sec
            while sec != None:
                print(sec.data, end='')
                if sec.next == None:
                    break
                print(',',end='')
                sec = sec.next
            p = p.next
            print()
        


twoDlink = Two_D_LinkedList()

twoDlink.Append_primary('A')
twoDlink.Append_primary('B')
twoDlink.Append_primary('C')

twoDlink.Append_secondary('A','A1')
twoDlink.Append_secondary('A','A2')
twoDlink.Append_secondary('B','B1')
twoDlink.Append_secondary('B','B2')
twoDlink.Append_secondary('C','C1')
twoDlink.Append_secondary('C','C2')
print('Result')
twoDlink.Print_List()

print()
print('Delete_primary : B')
twoDlink.Delete_primary('B')
twoDlink.Print_List()

print()
print('Delete_secondary : C , C1')
twoDlink.Delete_secondary('C','C1')

twoDlink.Print_List()