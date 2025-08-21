import random
rnddat = [random.randint(1,10) for i in range(0,10000)]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
bubble_sort(rnddat)
print("Sorted array is:", rnddat)
