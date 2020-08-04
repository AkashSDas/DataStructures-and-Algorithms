""" Singly Linked List """


class Node:
    def __init__(self, value):
        self.value = value
        self._next = None


class SinglyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.index = self.head

    def __len__(self):
        return self.size

    def _size(self):
        return self.size

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

    def _head(self):
        return self.head

    def _tail(self):
        return self.tail

    def is_empty(self):
        return self.size == 0

    def get_node_object(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node._next
        return None

    def contain(self, value):
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
        self.size += 1

    def insert_after(self, after, value):
        assert len(self) > 0, "Singly Linked List is empty"
        if self.tail == after:
            return self.insert_at_end(value)
        else:
            tmp_next = after._next
            node = Node(value)
            after._next = node
            node._next = node
            node._next = tmp_next
            self.size += 1

    def insert_before(self, before, value):
        assert len(self) > 0, "Singly Linked List is empty"
        if self.head == before:
            return self.insert_at_start(value)
        else:
            # To get previous node of `before` node
            current_node = self.head
            while current_node._next != before:
                current_node = current_node._next
            node = Node(value)
            current_node._next = node
            node._next = before
            self.size += 1

    def remove_head(self):
        assert len(self) > 0, "Singly Linked List is empty"
        node = self.head
        self.head = self.head._next
        self.size -= 1
        if len(self) == 0:
            self._tail = None
        return node

    def remove_tail(self):
        assert len(self) > 0, "Singly Linked List is empty"
        node = self.tail
        current_node = self.head
        while current_node._next != self.tail:
            current_node = current_node._next
        self.tail = current_node
        self.tail._next = None
        self.size -= 1
        if len(self) == 0:
            self.head = None
        return node

    def remove_node(self, node):
        assert len(self) > 0, "Singly Linked List is empty"
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
            self.size -= 1
            return node

    def __iter__(self):
        self.index = self.head
        return self

    def __next__(self):
        if self.index == None:
            raise StopIteration
        current_node = self.index
        self.index = self.index._next
        return current_node

    def reverse_linked_list(self):
        current_node = self.head
        head_node = self.head
        next_node = self.head._next
        while next_node is not None:
            tmp_next_node = next_node._next
            next_node._next = current_node
            current_node = next_node
            next_node = tmp_next_node
        self.head = current_node
        self.tail = head_node
        self.tail._next = None
        return self


s = SinglyLinkedList()

s.insert_at_start(3)
s.insert_at_start(2)
s.insert_at_start(1)
s.insert_at_start(0)

print(s)

n = s.get_node_object(2)
s.insert_after(n, 19)

print(s)

for i in s:
    print(i.value)

print(s.reverse_linked_list())

print(s._head())
