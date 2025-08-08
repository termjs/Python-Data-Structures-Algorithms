# Helper Heap methods + Insert

class MaxHeap:
    def __init__(self):
        self.heap = []  # Initialize an empty list to store heap elements

    def _left_child(self, index):
        # Return the index of the left child
        return 2 * index + 1
    
    def _right_child(self, index):
        # Return the index of the right child
        return 2 * index + 2
    
    def _parent(self, index):
        # Return the index of the parent node
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        # Swap the elements at the given indices
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        # Add the new value to the end of the heap
        self.heap.append(value)
        current = len(self.heap) - 1  # Index of the newly added element

        # Bubble up the new element to maintain max-heap property
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

# Create a MaxHeap instance
myheap = MaxHeap()
myheap.insert(99)   # Insert elements into the heap
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)  # Print heap after initial inserts

myheap.insert(100)  # Insert a new maximum value

print(myheap.heap)  # Print heap after inserting 100

myheap.insert(100)  # Insert another maximum value

print(myheap.heap)  # Print heap after inserting another 100
