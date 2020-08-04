""" Bubble Sort Algorithm version 1 """

# One loop isn't enough for bubble sorting

from time import time


def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


arr = [3, 4, 5, 1, 2]

start = time()
sorted_arr = bubble_sort(arr)
end = time()

print(f"Execution time: {end - start}")
print(sorted_arr)


# 1) Direct Swapping
# arr[j], arr[j-1] = arr[j-1], arr[j]

# 2) Using temporary variable
# tmp = arr[j]
# arr[j] = arr[j-1]
# arr[j-1] = tmp

# 3) Using some operations
# arr[j-1]  = arr[j-1] * arr[j]
# arr[j] = arr[j-1] // arr[j]
# arr[j-1] = arr[j-1] // arr[j]
# The order of operation must be same

# Example:
a = 3
b = 4

a = a * b

b = a // b
# ((a * b) // b) == a therefore value of b is assigned to
# value of a.

a = a // b
# ((a * b) // a) == b above value of a was assigned to b
# therefore resplacing a by b.

print(a, b)
