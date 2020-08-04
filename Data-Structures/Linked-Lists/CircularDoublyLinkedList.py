""" Circular Doubly Linked List """


class Node:
    def __init__(self, value):
        self.value = value
        self._prev = None
        self._next = None


class CircularDoublyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def _size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _head(self):
        return self.head

    def _tail(self):
        return self.tail

    def __str__(self):
        linked_list = ""
        current_node = self.head
        stop_at_node = None
        while current_node is not stop_at_node:
            linked_list += f"{current_node.value} <-> "
            current_node = current_node._next
            stop_at_node = self.head
        linked_list += f"{current_node.value}(head)"
        return linked_list

    def __repr__(self):
        return str(self)

    def contains(self, value):
        current_node = self.head
        stop_at_node = None
        while current_node is not stop_at_node:
            if current_node.value == value:
                return True
            stop_at_node = self.head
            current_node = current_node._next
        return False

    def get_node_object(self, value):
        current_node = self.head
        stop_at_node = None
        while current_node is not stop_at_node:
            if current_node.value == value:
                return current_node
            stop_at_node = self.head
            current_node = current_node._next
        return None

    def insert_at_start(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            prev_node = self.head
            self.head = node
            self.head._next = prev_node
            prev_node._prev = node
            node._prev = self.tail
            self.tail._next = node
        self.size += 1

    def insert_at_end(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            prev_tail = self.tail
            self.tail = node
            self.tail._prev = prev_tail
            node._prev = prev_tail
            prev_tail._next = node
            node._next = self.head
            self.head._prev = node
        self.size += 1

    def insert_after(self, after, value):
        assert len(self) > 0, "Doubly Linked List is empty"
        if after == self.tail:
            return self.insert_at_end(value)
        else:
            node = Node(value)
            next_node = after._next
            after._next = node
            next_node._prev = next_node
            node._next = next_node
            node._prev = after
            self.size += 1

    def insert_before(self, before, value):
        assert len(self) > 0, "Doubly Linked List is empty"
        if before == self.head:
            return self.insert_at_start(value)
        else:
            node = Node(value)
            prev_node = before._prev
            before._prev = node
            prev_node._next = node
            node._next = before
            node._prev = prev_node
            self.size += 1

    def remove_first(self):
        assert len(self) > 0, "Doubly Linked List is empty"
        node = self.head
        next_node = self.head._next
        self.head = next_node
        self.head._prev = self.tail
        self.tail._next = self.head
        self.size -= 1
        if len(self) == 0:
            self.tail = None
        return node

    def remove_last(self):
        assert len(self) > 0, "Doubly Linked List is empty"
        node = self.tail
        prev_node = self.tail._prev
        self.tail = prev_node
        self.tail._next = self.head
        self.head._prev = self.tail
        self.size -= 1
        if len(self) == 0:
            self.tail = None
        return node

    def remove_node(self, node):
        assert len(self) > 0, "Doubly Linked List is empty"
        if node == self.head:
            return self.remove_first()
        elif node == self.tail:
            return self.remove_last()
        else:
            current_node = self.head
            while current_node != node:
                prev_node = current_node
                current_node = current_node._next
            next_node = current_node._next
            prev_node._next = next_node
            next_node._prev = prev_node
            self.size -= 1
        return node

    def reverse_linked_list(self):
        head_node = self.head
        tail_node = self.tail
        current_node = self.head
        stop_at_node = None
        while current_node is not stop_at_node:
            prev_node = current_node._prev
            next_node = current_node._next
            current_node._next = prev_node
            current_node._prev = next_node
            current_node = next_node
            stop_at_node = self.head
        self.head = tail_node
        self.tail = head_node
        self.head._prev = self.tail
        self.tail._next = self.head
        return self

    def __iter__(self):
        self.index = self.head
        self.is_tail_iterated = False
        return self

    def __next__(self):
        if self.is_tail_iterated:
            raise StopIteration
        current_node = self.index
        self.index = self.index._next
        if current_node == self.tail:
            self.is_tail_iterated = True
        return current_node


d = CircularDoublyLinkedList()

d.insert_at_start(4)
d.insert_at_start(3)
d.insert_at_start(2)
d.insert_at_start(1)
d.insert_at_end(100)

print(d)
print(repr(d))

print(d.reverse_linked_list())
