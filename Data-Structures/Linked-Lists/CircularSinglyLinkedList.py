""" Circular Singly Linked List """


class Node:
    def __init__(self, value):
        self.value = value
        self._next = None


class CircularSinglyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def _size(self):
        return self.size

    def __str__(self):
        linked_list = ""
        current_node = self.head
        stop_at_node = None
        while current_node is not stop_at_node:
            linked_list += f"{current_node.value} -> "
            current_node = current_node._next
            stop_at_node = self.head
        linked_list += f"{current_node.value}(head)"
        return linked_list

    def __repr__(self):
        return str(self)

    def _head(self):
        return self.head

    def _tail(self):
        return self.tail

    def is_empty(self):
        return len(self) == 0

    def get_node_object(self, value):
        current_node = self.head
        stop_at_node = None
        while current_node is not stop_at_node:
            if current_node.value == value:
                return current_node
            current_node = current_node._next
            stop_at_node = self.head
        return None

    def contains(self, value):
        current_node = self.head
        stop_at_node = None
        while current_node is not stop_at_node:
            if current_node.value == value:
                return True
            current_node = current_node._next
            stop_at_node = self.head
        return False

    def insert_at_start(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            prev_head = self.head
            self.head = node
            self.head._next = prev_head
            self.tail._next = self.head
        self.size += 1

    def insert_at_end(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            prev_tail = self.tail
            self.tail = node
            prev_tail._next = self.tail
            self.tail._next = self.head
        self.size += 1

    def insert_after(self, after, value):
        assert len(self) > 0, "Singly Linked List is empty"
        if self.tail == after:
            return self.insert_at_end(value)
        tmp_next = after._next
        node = Node(value)
        after._next = node
        node._next = tmp_next
        self.size += 1

    def insert_before(self, before, value):
        assert len(self) > 0, "Singly Linked List is empty"
        if self.head == before:
            return self.insert_at_end(value)
        current_node = self.head
        while current_node._next == before:
            current_node = current_node._next
        node = Node(value)
        current_node._next = node
        node._next = before
        self.size += 1

    def remove_first(self):
        assert len(self) > 0, "Singly Linked List is empty"
        node = self.head
        self.head = self.head._next
        self.tail._next = self.head
        self.size -= 1
        if len(self) == 0:
            self.tail = None
        return node

    def remove_last(self):
        assert len(self) > 0, "Singly Linked List is empty"
        node = self.tail
        current_node = self.head
        while current_node._next != self.tail:
            current_node = current_node._next
        self.tail = current_node
        self.tail._next = self.head
        self.size -= 1
        if len(self) == 0:
            self.head = None
        return node

    def remove_node(self, node):
        assert len(self) > 0, "Singly Linked List is empty"
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
            self.size -= 1
            return node

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

    def reverse_linked_list(self):
        current_node = self.head
        head_node = self.head
        next_node = self.head._next
        while next_node is not self.head:
            tmp_next_node = next_node._next
            next_node._next = current_node
            current_node = next_node
            next_node = tmp_next_node
        self.head = current_node
        self.tail = head_node
        self.tail._next = self.head
        return self


s = CircularSinglyLinkedList()

s.insert_at_start(3)
s.insert_at_start(2)
s.insert_at_start(1)
s.insert_at_start(0)

print(s)

print(s.reverse_linked_list())

for i in s:
    print(i.value)
