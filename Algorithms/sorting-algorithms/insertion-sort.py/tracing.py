""" Insertion Sort Algorithm Tracing  """

from time import time


def tracing(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        print(f"{arr} | outerloop: {i} | tmp: {tmp}")
        while j >= 0 and tmp <= arr[j]:
            arr[j+1] = arr[j]
            print(f"{arr} | outerloop: {i} | innerloop: {j} | tmp: {tmp}")
            j -= 1
        arr[j+1] = tmp
        print('=' * 50)
    return arr


arr = [1, 4, 3, 2, 1]
start = time()
tracing(arr)
end = time()

print(f"Execution time: {end - start}")
