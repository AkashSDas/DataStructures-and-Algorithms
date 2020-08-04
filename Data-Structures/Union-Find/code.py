""" Union Find """


class UnionFind:

    def __init__(self, N):
        assert N >= 0, "Length should be >= 0"
        self.N = N
        self.num_of_components = N

        # Using `comp_size` to keep track of sizes of each of
        # the component.
        self.comp_size = [1] * N

        # _id[i] points to the parent of i,
        # if _id[i] = i then i is a root not node.
        self._id = list(range(N))

    def size(self):
        return self.N

    # Find which component/set `value` belongs to.
    # It takes amortized constant time.
    def find(self, value):
        # Find the root of the node
        root = value
        while root != self._id[root]:
            # Path compression
            root = self._id[root] = self._id[self._id[root]]

        # Compress the path leading back to root (path compression) and this will
        # give amortized constant time complexity.
        # while value != root:
        #     next_value = self._id[value]
        #     self._id[value] = root
        #     value = next_value

        return root

    # Return whether or not "value1" and "value2" are in same component/set
    def connected(self, value1, value2):
        return self.find(value1) == self.find(value2)

    # Return the size of the component/set "value" belongs to
    def component_size(self, value):
        return self.comp_size[self.find(value)]

    # Returns the number of remaining components/sets
    def components(self):
        return self.num_of_components

    # Unify the components/sets containing elements "value1" and "value2"
    def unify(self, value1, value2):
        root1 = self.find(value1)
        root2 = self.find(value2)

        # Check if they are of same group
        if root1 == root2:
            return

        # Merging two components/sets togther
        # Merge smaller component/set into larger one
        if self.comp_size[root1] < self.comp_size[root2]:
            self.comp_size[root2] += self.comp_size[root1]
            self._id[root1] = root2
        else:
            self.comp_size[root1] += self.comp_size[root2]
            self._id[root2] = root1

        # Since the roots found are different we know that number of
        # components/sets has decreased by one.
        self.num_of_components -= 1

    def __len__(self):
        return self.size()

    def __str__(self):
        return f"UF({self._id})"

    def __repr__(self):
        return f"UF({self._id})"


union_find = UnionFind(10)

print(union_find)
print(union_find.size)
print(union_find.num_of_components)
print(union_find.comp_size)
print(union_find._id)

print(union_find.find(4))

print(union_find.unify(3, 4))
print(union_find._id)

print(union_find.connected(3, 4))
print(union_find.connected(2, 4))

print(union_find.size())
print(union_find.num_of_components)

print(union_find.comp_size)
print(union_find._id)

print(union_find.find(4))


# How finding the root component works
# def find(p, _id):
#     # Find the root of the node
#     while p != _id[p]:
#         p = _id[p]
#         print(p)
#     return p

# nodes = [1, 2, 3, 4, 5, 6, 7,  8, 9, 10]
# _id = [8, 1, 2, 3, 4, 0, 6, 7, 8, 9]

# print(find(5, _id))
