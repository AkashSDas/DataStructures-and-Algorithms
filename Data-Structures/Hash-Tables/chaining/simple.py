""" ****** Hash Table - Chaining ****** """

# Instead of linked list the default python list is used


class HashTable:

    def __init__(self, max_length=10):
        self.max_length = max_length
        # max_length of hash table is fixed
        self.size = 0
        self.table = [[] for _ in range(self.max_length)]

    def __len__(self):
        return self.size

    """ Deterministic Hash Function """

    def hash_function(self, key):
        _hash = 0
        for char in key:
            _hash += ord(char)
        return _hash % self.max_length

    def __setitem__(self, key, value):
        _hash = self.hash_function(key)

        # If (key, value) pair exists in the table
        found = False

        # For updating value in the table
        for idx, element in enumerate(self.table[_hash]):
            # len(element) == len((key, value)) == 2
            if len(element) == 2 and element[0] == key:
                # Updating the value
                self.table[_hash][idx][0] = value
                found = True
                break

        # To enter a new value
        if not found:
            self.size += 1
            self.table[_hash].append((key, value))

    def __getitem__(self, key):
        _hash = self.hash_function(key)
        for idx, element in enumerate(self.table[_hash]):
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        _hash = self.hash_function(key)
        for idx, element in enumerate(self.table[_hash]):
            if element[0] == key:
                self.size -= 1
                del self.table[_hash][idx]

    def __str__(self):
        _table = ''
        lines = ['=' for _ in range(70)]
        _table += f"Hash | (key1, value1) -> (key2, value2) -> ... -> (key_n, value_n) \n{''.join(lines)}\n"
        for bucket in self.table:
            if bucket:
                _hash = self.hash_function(bucket[0][0])
                _table += f'{_hash} | '
                for idx, element in enumerate(bucket):
                    key, value = element
                    if idx != len(bucket) - 1:
                        _table += f'({key}, {value}) -> '
                    else:
                        _table += f'({key}, {value})'
                _table += '\n'
            else:
                _table += 'None \n'
        return _table

    def __repr__(self):
        return f"HashTable: \nMax Lengh: {self.max_length} \nSize: {self.size} \n{str(self.table)}"


t = HashTable()
t['James'] = 9
t['Ethan'] = 31
t['Tony'] = 36
t['Jame Bond'] = 43
t['Venom'] = 89

print(t.max_length)
print(t.size)
print(len(t))

print(t['James'])
print(t['Tony'])
print(t['Venom'])

print(t.table)

del t['Tony']

print(len(t))
print(t.table)

print()
print(t)
print()
print(repr(t))
