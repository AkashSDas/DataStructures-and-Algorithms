""" Insertion Sorting Algorithm version 1 """

from time import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and tmp <= arr[j]:  # tmp <= arr[j] for duplicate values
            arr[j+1] = arr[j]  # Shifting value of j+1 to j
            j -= 1  # moving from right to left
        arr[j+1] = tmp  # updating the value for the smallest value in the subarray
    return arr


arr = [3, 4, 5, 1, 2]

start = time()
sorted_arr = insertion_sort(arr)
end = time()

print(f"Execution time: {end - start}")
print(sorted_arr)
