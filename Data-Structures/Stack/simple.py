""" Simple Stack """


class Stack:

    def __init__(self):
        self.stack = []
        self.index = 0

    def __str__(self):
        return f"{self.stack}"

    def __repr__(self):
        return f"Stack({self.stack})"

    def __len__(self):
        return len(self.stack)

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        assert not self.is_empty(), "Stack is empty"
        tmp = self.stack[-1]
        del self.stack[-1]
        return tmp

    def push(self, value):
        self.stack.append(value)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.stack):
            raise StopIteration
        current_value = self.stack[self.index]
        self.index += 1
        return current_value


s = Stack()
print(s)

s.push(10)
s.push(1231)
s.push(23)
s.push(11)
s.push(37)
print(s)

print(s.pop())
print(s)

print(s.is_empty())

print(s.size())

iter_s = iter(s)
print(iter_s)

print(next(iter_s))
print(next(iter_s))

for i in s:
    print(i)

for i in s:
    print(i)
