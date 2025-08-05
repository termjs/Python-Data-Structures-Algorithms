# O(n) approach

def item_in_common(list1, list2):
    # Create a dictionary to store elements from list1
    my_dict = {}
    for i in list1:
        my_dict[i] = True  # Mark each element as present

    # Check if any element in list2 exists in the dictionary
    for j in list2:
        if j in my_dict:
            return True  # Found a common item

    return False  # No common items found

list1 = [1,3,5]
list2 = [2,4,6]

# Print whether the two lists have any items in common
print(item_in_common(list1, list2))
