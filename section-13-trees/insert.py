# Binary Search Tree (BST) Insertion

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value) # Create a new node

        if self.root is None: # Check if the root if None
            self.root = new_node # If root is None make root new node
            return True # Return True bool as a success and stop running
        
        temp = self.root # Make temp variable to get the current value

        while (True): # Make while loop to search the whole tree
            # Compare the values
            if new_node.value == temp.value: # check if the new node's value is the same as the current value
                return False # Stop the while loop
            
            if new_node.value < temp.value: # Go left if new node value is smaller the the root/temp
                if temp.left is None: # If the left side is empty
                    temp.left = new_node # Insert the new node to the left
                    return True # Return True and stop
                temp = temp.left # Continue to the the left, get temp's left value
            else:
                if temp.right is None: # If right side is empty
                    temp.right = new_node # Set right side to new node
                    return True # Success and Stop
                temp = temp.right # Continue to go right

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value) # Get the middle / root
print(my_tree.root.left.value) # Left side value
print(my_tree.root.right.value) # Right side value
