""" Dynamic Array """


class Array:

    def __init__(self, *args):
        if args:
            self.array = list(args)
        else:
            self.array = list()
        self.index = 0

    def __str__(self):
        return f"{self.array}"

    def __repr__(self):
        return f"Array({self.array})"

    def __len__(self):
        return len(self.array)

    def size(self):
        return len(self.array)

    def is_indexing_correct(self, index):
        assert index >= 0, "Negative indexing is not allowed"
        assert index < len(self.array), "Index is out of range"

    def __getitem__(self, index):
        self.is_indexing_correct(index)
        return self.array[index]

    def get(self, index):
        self.is_indexing_correct(index)
        return self.array[index]

    def __setitem__(self, index, value):
        self.is_indexing_correct(index)
        self.array[index] = value

    def set(self, index, value):
        self.is_indexing_correct(index)
        self.array[index] = value

    def clear(self, value=None):
        assert len(self.array) != 0, "Array is empty"
        for i in range(len(self.array)):
            self.array[i] = value
        return self.array

    def insert(self, value, index=None):
        if index == None:
            self.array.append(value)
            return None
        assert index < len(self.array) + 1, "Index is out of range"
        self.array.append(None)
        idx = len(self.array) - 1
        while idx >= index:
            self.array[idx] = self.array[idx - 1]
            idx -= 1
        self.array[index] = value

    def is_empty(self):
        return len(self) == 0

    def exist(self, value):
        for i in range(len(self.array)):
            if self.array[i] == value:
                return True
        return False

    def slice(self, start_index=0, end_index=None):
        slice_part = Array()
        if end_index == None:
            end_index = len(self.array)
        for i in range(start_index, end_index):
            slice_part.insert(value=self.array[i])
        return slice_part

    def __reversed__(self):
        return reversed(self.array)

    def reverse(self):
        reverse_items = [self.array[i]
                         for i in range(len(self.array) - 1, -1, -1)]
        for i in range(len(self.array)):
            self.array[i] = reverse_items[i]
        return self.array

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
print(str(a))
print(repr(a))

print(len(a))
print(a.size())

print(a[0])
print(a[1])
print(a.__getitem__(index=0))
print(a.get(index=0))

a.set(index=0, value=19)
print(a)
a.set(2, 79)
print(a)

a.__setitem__(index=0, value=13)
a.__setitem__(2, 17)
print(a)

print(a.is_empty())

a.insert(99)
print(a)
a.insert(value=111, index=0)
print(a)
a.insert(77, 3)
print(a)

print(a.exist(77))
print(a.exist(821398))

print(a.slice())
print(a.slice(1, 3))

print(list(reversed(a)))
print(a.reverse())

iter_a = iter(a)
print(iter_a)
print(next(iter_a))
print(next(iter_a))

print()

for ele in a:
    print(ele)

print()

for ele in a:
    print(ele)

a.clear()
print(a)
