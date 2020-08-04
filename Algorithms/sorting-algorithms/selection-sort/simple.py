# ###### Selection Sort Algorithm version 1 ######

from time import time


def selection_sort(arr):
    for i in range(1, len(arr)):
        smallest_value_index = i
        for j in range(i+1, len(arr)):
            if arr[smallest_value_index] > arr[j]:
                smallest_value_index = j
        arr[i], arr[smallest_value_index] = arr[smallest_value_index], arr[i]
    return arr


arr = [5, 4, 3, 2, 1]

start = time()
sorted_arr = selection_sort(arr)
end = time()

print(f"Sorted List: {arr}")
print(f"Execution time: {end-start}")
