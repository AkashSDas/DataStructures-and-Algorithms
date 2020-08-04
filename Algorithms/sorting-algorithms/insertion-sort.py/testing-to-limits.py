""" Testing Insertion Sort Algorithm to its limit """

from random import randint
from time import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and tmp <= arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp
    return arr


def generate_array(size=1000, start=0, end=10):
    arr = [randint(start, end) for _ in range(size)]
    return arr


arr = generate_array(size=5000)
start = time()
sorted_arr = insertion_sort(arr)
end = time()

print(f"Execution time: {end - start}")
