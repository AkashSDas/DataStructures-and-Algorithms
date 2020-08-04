""" Doubly Linked List """


class Node:
    def __init__(self, value):
        self.value = value
        self._prev = None
        self._next = None


class DoublyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.index = self.head

    def __len__(self):
        return self.size

    def _size(self):
        return self.size

    def _head(self):
        return self.head

    def _tail(self):
        return self.tail

    def __str__(self):
        linked_list = ""
        current_node = self.head
        while current_node is not None:
            linked_list += f"{current_node.value} <-> "
            current_node = current_node._next
        linked_list += "None"
        return linked_list

    def __repr__(self):
        return str(self)

    def get_node_object(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node._next
        return None

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node._next
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
            prev_head._prev = self.head
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
            prev_tail._next = self.tail
        self.size += 1

    def insert_after(self, after, value):
        assert len(self) > 0, "Doubly Linked List is empty"
        if after == self.tail:
            return self.insert_at_end(value)
        else:
            node = Node(value)
            next_node = after._next
            after._next = node
            next_node._prev = node
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

    def remove_head(self):
        assert len(self) > 0, "Doubly Linked List is empty"
        node = self.head
        next_node = self.head._next
        self.head = next_node
        self.head._prev = None
        self.size -= 1
        if len(self) == 0:
            self.tail = None
        return node

    def remove_tail(self):
        assert len(self) > 0, "Doubly Linked List is empty"
        node = self.tail
        prev_node = self.tail._prev
        self.tail = prev_node
        self.tail._next = None
        self.size -= 1
        if len(self) == 0:
            self.head = None
        return node

    def remove_node(self, node):
        assert len(self) > 0, "Doubly Linked List is empty"
        if node == self.head:
            return self.remove_head()
        elif node == self.tail:
            return self.remove_tail()
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
        while current_node is not None:
            prev_node = current_node._prev
            next_node = current_node._next
            current_node._next = prev_node
            current_node._prev = next_node
            current_node = next_node
        self.head = tail_node
        self.tail = head_node

    def __iter__(self):
        self.index = self.head
        return self

    def __next__(self):
        if self.index == None:
            raise StopIteration
        current_node = self.index
        self.index = self.index._next
        return current_node


d = DoublyLinkedList()

d.insert_at_start(4)
d.insert_at_start(3)
d.insert_at_start(2)
d.insert_at_start(1)
d.insert_at_end(100)

print(d)

d.reverse_linked_list()

print(d)

for i in d:
    print(i.value)

print(d.contains(1))
