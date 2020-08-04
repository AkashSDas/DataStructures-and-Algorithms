""" Static array with type-checking """


class Array:

    def multiple_typechecking(self, dtype, iterable):
        for ele in iterable:
            if type(ele) != dtype:
                assert False, f"Wrong data-type, it should be of type {dtype}"

    def __init__(self, size, dtype, elements=None):
        assert size > 0, "Array size should be greater than 0"
        if not elements:
            self.array = [None for _ in range(size)]
        else:
            self.multiple_typechecking(dtype, elements)
            self.array = list(elements)
        self.size = size
        self.dtype = dtype
        self.index = 0

    def __str__(self):
        return f"{self.array}"

    def __repr__(self):
        return f"Array({self.array})"

    def __len__(self):
        return len(self.array)

    def _size(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def is_indexing_correct(self, index):
        assert index >= 0, "Negative indexing is not allowed"
        assert index < len(self.array), "Index is out of range"

    def __getitem__(self, index):
        self.is_indexing_correct(index)
        return self.array[index]

    def get(self, index):
        self.is_indexing_correct(index)
        return self.array[index]

    def single_typecheck(self, value):
        assert type(
            value) == self.dtype, f"Wrong data-type, it should be of type {self.dtype}"

    def __setitem__(self, index, value):
        self.is_indexing_correct(index)
        self.single_typecheck(value)
        self.array[index] = value

    def set(self, index, value):
        self.is_indexing_correct(index)
        self.single_typecheck(value)
        self.array[index] = value

    def clear(self, value=None):
        assert len(self.array) != 0, "Array is empty"
        for i in range(len(self.array)):
            self.array[i] = value
        return self.array

    def insert(self, value, index=None):
        self.single_typecheck(value)
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

    def exist(self, value):
        for i in range(len(self.array)):
            if self.array[i] == value:
                return True
        return False

    def slice(self, start_index=0, end_index=None):
        slice_part = list()
        if end_index == None:
            end_index = len(self.array)
        for i in range(start_index, end_index):
            slice_part.append(self.array[i])
        slice_part = Array(size=len(slice_part),
                           dtype=self.dtype, elements=slice_part)
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


a = Array(size=3, dtype=int, elements=[1, 2, 3])
print(a)
print(str(a))
print(repr(a))

print(len(a))
print(a._size())

print(a[0])
print(a[1])
print(a.__getitem__(index=0))
print(a.get(index=0))

a.set(index=0, value=19)
print(a)
a.set(2, 79)
print(a)

a.__setitem__(index=0, value=1)
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
