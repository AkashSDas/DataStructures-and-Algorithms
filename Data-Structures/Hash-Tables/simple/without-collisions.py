""" ****** Hash Table ****** """

# This class doesn't handel collisions


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    """ Deterministic Hash Function """

    def hash_function(self, key):
        _hash = 0
        for char in key:
            _hash += ord(char)
        return _hash % self.size

    def __setitem__(self, key, value):
        _hash = self.hash_function(key)
        self.table[_hash] = value

    def __getitem__(self, key):
        _hash = self.hash_function(key)
        return self.table[_hash]

    def __delitem__(self, key):
        _hash = self.hash_function(key)
        self.table[_hash] = None


t = HashTable()
t['James'] = 9
t['Ethan'] = 31
t['Tony'] = 36

print(t['James'])

print(t.table)
