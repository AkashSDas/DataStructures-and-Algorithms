""" PQueue implementation using binary heap """

""" Binary heap is implemented in array """


class PQueue:

    # To compare if element is of right or left subtree
    LEFT = -1
    RIGHT = 1

    def __init__(self):
        self.heap = list()

    def __len__(self):
        return len(self.heap)

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.size() == 0

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        return f"PQ({self.heap})"

    def error_if_empty(self):
        assert self.size() > 0, "PQ is empty"

    def contains_index(self, index):
        assert index < self.size(), "Index is out of bound"

    def root(self):
        self.error_if_empty()
        return self.heap[0]

    def index_of(self, value):
        self.error_if_empty()
        indexes = [i for i in range(len(self.heap)) if self.heap[i] == value]
        if indexes:
            return indexes
        return None

    def left_or_rigth(self, index):
        self.error_if_empty()
        self.contains_index(index)
        if index % 2 == 0:
            return PQueue.RIGHT  # Right
        return PQueue.LEFT  # Left

    def parent_index(self, child_index):
        side = self.left_or_rigth(child_index)
        if side == 1:
            par_idx = int((child_index - 2) / 2)
        else:
            par_idx = int((child_index - 1) / 2)
        return par_idx

    def bubble_up(self, value):
        while True:
            idx = self.index_of(value)
            if idx:
                idx = idx[-1]
                par_idx = self.parent_index(idx)
                if self.heap[par_idx] < value:
                    break
                tmp = self.heap[par_idx]
                self.heap[par_idx] = value
                self.heap[idx] = tmp

    def insert(self, value):
        self.heap.append(value)
        if self.size() > 1:
            self.bubble_up(value)

    def child_indexes(self, parent_index):
        right_child_idx = (2 * parent_index) + 2
        left_child_idx = (2 * parent_index) + 1

        if left_child_idx >= len(self.heap):
            left_child_idx = None
        if right_child_idx >= len(self.heap):
            right_child_idx = None
        return (left_child_idx, right_child_idx)

    def compare_childs(self, parent_index):
        child_idxs = self.child_indexes(parent_index)
        left_child_idx = child_idxs[0]
        right_child_idx = child_idxs[1]

        # To give which child is smaller to do bubbling, we
        # are comparing values
        if left_child_idx == None and right_child_idx == None:
            return (None, None)
        if left_child_idx == None and right_child_idx != None:
            return (RIGHT, right_child_idx)
        if right_child_idx == None and left_child_idx != None:
            return (PQueue.LEFT, left_child_idx)
        if self.heap[left_child_idx] < self.heap[right_child_idx]:
            return (PQueue.LEFT, left_child_idx)
        return (RIGHT, right_child_idx)

    def bubble_down(self, parent_index):
        while True:
            child_to_swap = self.compare_childs(parent_index)
            child_side = child_to_swap[0]
            child_idx = child_to_swap[1]
            if child_idx == None:
                break
            else:
                # Swapping the child if heap invariant is not satisfied
                # child_idx == PQueue.LEFT or child_idx == PQueue.RIGHT
                if self.heap[parent_index] < self.heap[child_idx]:
                    break
                tmp = self.heap[parent_index]
                self.heap[parent_index] = self.heap[child_idx]
                self.heap[child_idx] = tmp
                parent_index = child_idx

    def poll(self):
        root_node = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap[-1] = root_node
        del self.heap[-1]
        index_of_root = 0
        self.bubble_down(index_of_root)
        return root_node

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.heap):
            raise StopIteration
        current_node = self.heap[self.index]
        self.index += 1
        return current_node


heap = PQueue()
print(heap)

print(len(heap))
print(heap.size())

print(heap.is_empty())

heap.insert(0)
print(heap.root())

heap.insert(1)
heap.insert(2)
heap.insert(4)
heap.insert(5)
heap.insert(6)

print(heap)

heap.insert(3)
print(heap)
heap.insert(3)
print(heap)

print(heap.poll())
print(heap)

print(iter(heap))
print(next(heap))

items = iter(heap)
for item in items:
    print(item)

print(heap.root())
