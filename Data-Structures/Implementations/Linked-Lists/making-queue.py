# This is Queue build using Singly Linked List


class QueueNode:
    def __init__(self, value):
        self.value = value
        self._next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
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

    def enqueue(self, value):
        node = QueueNode(value)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail._next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        node_to_remove = self.head
        if self.head is self.tail:
            self.head = self.tail = None
            self.size -= 1
            return node_to_remove.value
        self.head = self.head._next
        self.size -= 1
        return node_to_remove.value


q = Queue()
print(q)

q.enqueue(1)
print(q, q.head.value, q.tail.value)
q.dequeue()
print(q.size)
print(q)

q.enqueue(2)
print(q, q.head.value, q.tail.value)
q.enqueue(3)
print(q, q.head.value, q.tail.value)
q.enqueue(4)
print(q, q.head.value, q.tail.value)
q.enqueue(5)
print(q, q.head.value, q.tail.value)

print(q)
print(q._size())

q.dequeue()
print(q, q.head.value, q.tail.value)
q.dequeue()
print(q, q.head.value, q.tail.value)
q.dequeue()
print(q, q.head.value, q.tail.value)
q.dequeue()

print(q)
