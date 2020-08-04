""" ****** Hash Table - Linear Probing ****** """


class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.keys = [None for _ in range(self.size)]
        self.values = [None for _ in range(self.size)]

    """ Deterministic Hash Function """

    def hash_function(self, key):
        _hash = 0
        for char in key:
            _hash += ord(char)
        return _hash % self.size

    # To get new hash values using the old_hash values
    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def __setitem__(self, key, value):
        _hash = self.hash_function(key)

        # If slot for (key, value) pair is avialable
        if self.keys[_hash] == None:
            self.keys[_hash] = key
            self.values[_hash] = value
        else:
            # To update value
            if self.keys[_hash] == key:
                self.values[_hash] = value
            else:
                next_slot = self.rehash(_hash)
                while self.keys[next_slot] == None:
                    next_slot = self.rehash(next_slot)

                # We got an empty slot that means we are adding new
                # (key, value) pair.
                if self.keys[next_slot] == None:
                    self.keys[next_slot] = key
                    self.values[next_slot] = value
                else:
                    # We got an pre-filled slot that means we are updating
                    # (key, value) pair.
                    self.values[next_slot] = value

    def __getitem__(self, key):
        start_slot = self.hash_function(key)

        value = None
        stop = False  # To stop if we reach the postion from where we started
        found = False
        position = start_slot
        while self.keys[position] != None and not found and not stop:
            if self.keys[position] == key:
                found = True
                value = self.values[position]
            else:
                position = self.rehash(position)
                if position == start_slot:
                    # We reach the position where we started from
                    stop = True
        return value


t = HashTable()
t['James'] = 9
t['Ethan'] = 31
t['Tony'] = 36
t['Tony'] = 7
t['Jame Bond'] = 43
t['Venom'] = 89

print(t['James'])
print(t['Tony'])
print(t['Venom'])

print(t.keys)
print(t.values)
