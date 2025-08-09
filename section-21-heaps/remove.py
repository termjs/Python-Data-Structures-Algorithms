# Heap: Remove

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    # Helper method to move a node down the heap to restore heap property
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # Check if left child exists and is greater than current max
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            # Check if right child exists and is greater than current max
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            # If a child is greater, swap and continue sinking down
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                # Heap property is restored
                return

    # Remove and return the maximum value from the heap
    def remove(self):
        if len(self.heap) == 0:
            # Heap is empty
            return None

        if len(self.heap) == 1:
            # Only one element, just pop and return it
            return self.heap.pop()
        
        # Store the max value to return later
        max_value = self.heap[0]
        # Move the last element to the root
        self.heap[0] = self.heap.pop()
        # Restore heap property by sinking down
        self._sink_down(0)

        return max_value

# Example usage
myheap = MaxHeap()
myheap.insert(95)   # Insert elements into the heap
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(55)
myheap.insert(55)
myheap.insert(65)

print(myheap.heap)  # Print heap after insertions

myheap.remove()     # Remove the max element

print(myheap.heap)  # Print heap after removal

myheap.remove()     # Remove the next max element

print(myheap.heap)  # Print heap after second removal
