""" Testing Bubble Sort Algorithm to its limits """

from random import randint
from time import time


def generate_array(size=1000, start=0, end=10):
    arr = [randint(start, end) for _ in range(size)]
    return arr


def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


arr = generate_array(size=5000)
start = time()
sorted_arr = bubble_sort(arr)
end = time()

print(f"Execution time: {end - start}")
