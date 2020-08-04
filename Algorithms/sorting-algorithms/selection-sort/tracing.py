""" Selection Sort Algorithm Tracing  """

from time import time


def tracing(arr):
    for i in range(1, len(arr)):
        smallest_value_index = i
        print(f"{arr} | outerloop: {i}")
        for j in range(i+1, len(arr)):
            if arr[smallest_value_index] > arr[j]:
                smallest_value_index = j
            print(
                f"{arr} | outerloop: {i} | innerloop: {j} | smallest element index: {smallest_value_index}")
        arr[i], arr[smallest_value_index] = arr[smallest_value_index], arr[i]
        print('=' * 50)


arr = [5, 4, 3, 2, 1]
start = time()
tracing(arr)
end = time()

print(f"Execution time: {end - start}")
