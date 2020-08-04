""" Basic Dynamic Array Without Typechecking"""


class Array:

    def __init__(self, *args):
        if args:
            self.array = list(args)
        else:
            self.array = list()
        self.index = 0

    def __str__(self):
        return f"{self.array}"

    def size(self):
        return len(self.array)

    def get(self, index):
        return self.array[index]

    def set(self, index, value):
        self.array[index] = value

    def is_empty(self):
        return self.size() == 0

    def exist(self, value):
        for i in range(len(self.array)):
            return True
        return False

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.array):
            raise StopIteration
        current_value = self.array[self.index]
        self.index += 1
        return current_value


a = Array(1, 2, 3)
print(a)

print(a.size())

print(a.get(0))
a.set(0, 99)
print(a)

print(a.is_empty())

print(a.exist(99))

iter_a = iter(a)
print(next(iter_a))
print(next(iter_a))

for ele in a:
    print(ele)

for ele in a:
    print(ele)
