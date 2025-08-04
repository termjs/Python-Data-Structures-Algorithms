# HT: Set

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        # Get the index in the data_map using the hash function
        index = self.__hash(key)
        # If there is no list at this index, create one
        if self.data_map[index] == None:
            self.data_map[index] = []
        # Add the [key, value] pair to the list at this index
        self.data_map[index].append([key, value])
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 100)
my_hash_table.set_item("lumber", 70)

my_hash_table.print_table()
