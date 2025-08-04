# HT: Constructor

class HashTable:
    def __init__(self, size = 7): # Default size 7 if no value was passed
        self.data_map = [None] * size # Call this list and make it None times [*] the size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # Add the ASCII value of each character (multiplied by 23) to my_hash, then take modulo table size to keep it in bounds
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

my_hash_table = HashTable()

my_hash_table.print_table()
