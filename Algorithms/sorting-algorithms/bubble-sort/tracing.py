""" Bubble Sort Algorithm Tracing """

from time import time


def tracing(arr):
    for i in range(1, len(arr)):
        print(f"{arr} | outerloop: {i}")
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            print(f"{arr} | outerloop: {i} | innerloop: {j}")
        print('=' * 50)


arr = [5, 4, 3, 2, 1]
start = time()
tracing(arr)
end = time()

print(f"Execution time: {end - start}")
