# Binary Search Tree (BST) Contains

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    # Define contains method
    def contains(self, value):
        if self.root is None:  # If root doesn't exist
            return False
        temp = self.root

        while temp:  # While temp is not None
            if value < temp.value:  # If value is less than temp.value
                temp = temp.left  # Move to the left
            elif value > temp.value:  # If value is greater than temp.value
                temp = temp.right  # Move to the right
            else:  # If value equals temp.value
                return True
        return False  # If not found, return False

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(92)) # Returns False

print(my_tree.contains(27)) # Returns True
