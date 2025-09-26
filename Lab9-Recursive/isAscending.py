def isAscendding(lst):
    if len(lst) <= 1:
        return True
    if lst[0] > lst[1]:
        return False
    return isAscendding(lst[2:])

print(isAscendding([1,2,3,4,5,6,7]))
print(isAscendding([3,4,2,5,6,1,2]))
print(isAscendding([9,8,7,6,5,4]))
print(isAscendding([0,0,1,1,2,2,3,3,4,4,5,5]))
print(isAscendding([6,7,8,9,10,11,12]))
print(isAscendding([6,3,8,7,9,2,3,1,5]))