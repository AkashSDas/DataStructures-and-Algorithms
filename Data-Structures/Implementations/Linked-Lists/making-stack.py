# This is Stack build using Singly Linked List


class StackNode:
    def __init__(self, value):
        self.value = value
        self._next = None


class Stack:

    def __init__(self):
        self.head = None,  # bottom
        self.tail = None,  # top
        self.size = 0

    def __len__(self):
        return self.size

    def _size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        linked_list = ""
        current_node = self.head
        while current_node is not None:
            linked_list += f"{current_node.value} -> "
            current_node = current_node._next
        linked_list += "None"
        return linked_list

    def __repr__(self):
        return str(self)

    def push(self, value):
        node = StackNode(value)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail._next = node
            self.tail = node
        self.size += 1

    def pop(self):
        assert self.size != 0, 'Stack is empty'
        tmp = self.head
        self.size -= 1
        if self.is_empty():
            self.head = self.tail = None
        else:
            self.head = self.head._next
        return tmp


s = Stack()

print(s.is_empty())
# print(s)

s.push(1)
print(s, s.head.value, s.tail.value)
s.push(2)
print(s, s.head.value, s.tail.value)
s.push(3)
print(s, s.head.value, s.tail.value)
s.push(4)
print(s, s.head.value, s.tail.value)

print(s.pop().value)
print(s, s.head.value, s.tail.value)
print(s.pop().value)
print(s, s.head.value, s.tail.value)
print(s.pop().value)
print(s, s.head.value, s.tail.value)
print(s.pop().value)
print(s)
