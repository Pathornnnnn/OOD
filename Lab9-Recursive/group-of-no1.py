def group_of_no_1(island_list, point_no):
    if point_no > len(island_list):
        return 0
    
    if island_list[point_no - 1] == 0:
        return 0
    
    if island_list[point_no - 1] == 1:
        return 1 + group_of_no_1(island_list, point_no + 1)
    
    # เผื่อกรณีที่ list มีค่าอื่นนอกจาก 0/1
    return 1


print(group_of_no_1([1,1,1,1,0,0,0,1,1,1,0,0], 1))
print(group_of_no_1([1,1,1,1,0,0,0,1,1,1,0,0], 5))
print(group_of_no_1([1,0,1,1,1,0,0,0,1,1,1,1,1,1], 4))
print(group_of_no_1([1,0,1,1,1,0,0,0,1,1,1,1,1,1], 10))
print(group_of_no_1([1,0,1,1,1,0,0,0,1,1,1,1,1,1], 1))
print(group_of_no_1([0,1,0,1,0,1,0,1,0,1], 7))
