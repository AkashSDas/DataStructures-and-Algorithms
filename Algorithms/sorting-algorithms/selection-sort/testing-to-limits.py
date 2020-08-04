""" Testing Selection Sort Algorithm to its limit """

from random import randint
from time import time


def selection_sort(arr):
    for i in range(1, len(arr)):
        smallest_value_index = i
        for j in range(i+1, len(arr)):
            if arr[smallest_value_index] > arr[j]:
                smallest_value_index = j
        arr[i], arr[smallest_value_index] = arr[smallest_value_index], arr[i]
    return arr


def generate_array(size=1000, start=0, end=10):
    arr = [randint(start, end) for _ in range(size)]
    return arr


arr = generate_array(size=5000)
start = time()
sorted_arr = selection_sort(arr)
end = time()

print(f"Execution time: {end - start}")
