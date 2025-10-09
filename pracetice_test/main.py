class Node:
    linked_table = {
        1: [2,4,7,15],
        2: [1,3,8,16],
        3: [2,4,7,15],
        4: [1,3,8,16],
        5: [1,6,8,9],
        6: [2,5,7,10],
        7: [3,6,8,11],
        8: [4,5,7,12],
        9: [5,10,12,13],
        10: [6,9,11,14],
        11: [7,10,12,15],
        12: [8,9,11,16],
        13: [1,9,14,16],
        14: [2,10,13,15],
        15: [3,11,14,16],
        16: [4,12,13,15],
    }
    
    def __init__(self, data, idx):
        self.data = data
        self.idx = idx
        self.next = None
        self.link = self.linked_table[self.idx]

class ColorPuzzle:
    match_row_to_index = {
        0: [0,1,2,3],
        1: [4,5,6,7],
        2: [8,9,10,11],
        3: [12,13,14,15],
    }
    match_col_to_index = {
        0: [0,4,8,12],
        1: [1,5,9,13],
        2: [2,6,10,14],
        3: [3,7,11,15],
    }

    def __init__(self):
        # TODO: Implement
        lst = 'RRRRYYYYBBBBGGGG'
        self.head = None
        for idx , color in enumerate(lst):
            if idx == 0:
                self.head = Node(color, idx+1)
                current = self.head
            else:
                new_node = Node(color, idx+1)
                current.next = new_node
                current = new_node
        
    def display(self):
        # TODO: Implement
        current = self.head
        self.nodes = []
        while current:
            self.nodes.append(current)
            current = current.next
        for i in range(4):
            for j in range(4):
                print(self.nodes[i*4 + j].data, end=' ')
            print()

        # row = self.match_row_to_index[3]
        # for i in row:
        #     for j in self.nodes:
        #         if i == j.idx:
        #             print(j.idx, j.data, j.link)
    
    def shift_row_left(self, row_index):
        # TODO: Implement
        row = self.match_row_to_index[row_index]
        first_color = self.nodes[row[0]].data
        for i in range(len(row)-1):
            ins = self.find_instance(row[i])
            ins.data = self.nodes[row[i+1]].data
        self.nodes[row[3]].data = first_color

    
    def shift_row_right(self, row_index):
        # TODO: Implement
        row = self.match_row_to_index[row_index]
        last_instance = self.find_instance(row[3])
        first_color = last_instance.data
        for i in range(len(row)-1, 0, -1):
            ins = self.find_instance(row[i])
            ins.data = self.nodes[row[i-1]].data
        first_instance = self.find_instance(row[0])
        first_instance.data = first_color
    
    def shift_column_down(self, col_index):
        col = self.match_col_to_index[col_index]
        first_color = self.nodes[col[-1]].data  # Get the last color
        for i in range(len(col) - 1, 0, -1):  # Iterate from bottom to top
            ins = self.find_instance(col[i])
            ins.data = self.nodes[col[i - 1]].data
        first_instance = self.find_instance(col[0])
        first_instance.data = first_color  # Set the first color to the top

    def shift_column_up(self, col_index):
        col = self.match_col_to_index[col_index]
        first_instance = self.find_instance(col[0])
        first_color = first_instance.data  # Get the first color
        for i in range(len(col) - 1):  # Iterate from top to bottom
            ins = self.find_instance(col[i])
            ins.data = self.nodes[col[i + 1]].data
        last_instance = self.find_instance(col[-1])
        last_instance.data = first_color  # Set the last color to the bottom

    def find_instance(self, idx):
        current = self.head
        while current:
            if current.idx == idx+1:
                return current
            current = current.next
        return None
    
# Test Code
if __name__ == "__main__":
    puzzle = ColorPuzzle()
    print("=== Initial State ===")
    puzzle.display()
    
    # Run all test steps
    # .....................
    # ลำดับการทดสอบ: เรียก method ตามลำดับดังนี้ แต่ละครั้งมีการ display() เพื่อตรวจคำตอบ
    print("\n=== After shifting column 0 up ===")
    puzzle.shift_column_up(0)  #เลื่อนคอลัมน์ที่ 0 ขึ้นบน
    puzzle.display()

    print("\n=== After shifting column 1 down ===")
    puzzle.shift_column_down(1) #เลื่อนคอลัมน์ที่ 1 ลงล่าง
    puzzle.display()

    print("\n=== After shifting column 2 up ===") 
    puzzle.shift_column_up(2) #เลื่อนคอลัมน์ที่ 2 ขึ้นบน 
    puzzle.display()

    print("\n=== After shifting column 3 down ===")
    puzzle.shift_column_down(3) #เลื่อนคอลัมน์ที่ 3 ลงล่าง
    puzzle.display()

    print("\n=== After shifting row 0 right ===")
    puzzle.shift_row_right(0) #เลื่อนแถวที่ 0 ไปขวา 
    puzzle.display()

    print("\n=== After shifting row 1 left ===")
    puzzle.shift_row_left(1) #เลื่อนแถวที่ 1 ไปซ้าย 
    puzzle.display()

    print("\n=== After shifting row 2 right ===")
    puzzle.shift_row_right(2) #เลื่อนแถวที่ 2 ไปขวา 
    puzzle.display()

    print("\n=== After shifting row 3 left ===")
    puzzle.shift_row_left(3)  #เลื่อนแถวที่ 3 ไปซ้าย 
    puzzle.display()
    
    print(  )
    puzzle.shift_column_up(0)
    puzzle.display()
