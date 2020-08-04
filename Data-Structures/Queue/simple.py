""" Basic Queue """


class Queue:

    def __init__(self):
        self.queue = []
        self.index = 0

    def __str__(self):
        return f"{self.queue}"

    def __repr__(self):
        return f"Queue({self.queue})"

    def __len__(self):
        return len(self.queue)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        assert len(self.queue) > 0, "Queue is empty"
        tmp = self.queue[0]
        del self.queue[0]
        return tmp

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.queue):
            raise StopIteration
        current_node = self.queue[self.index]
        self.index += 1
        return current_node


q = Queue()
print(q)

print(q.size())

print(q.is_empty())

q.enqueue(21)
q.enqueue(17)
q.enqueue(1)
q.enqueue(99)
q.enqueue(2123)
print(q)

print(q.dequeue())
print(q)
print(q.dequeue())
print(q)

iter_q = iter(q)
print(iter_q)
print(next(iter_q))
print(next(iter_q))

for ele in q:
    print(ele)

for ele in q:
    print(ele)
