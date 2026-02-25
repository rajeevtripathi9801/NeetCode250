# 🧠 Lists and Arrays in Python — Notes

# 🧮 1. Lists in Python
# A list is an ordered, mutable (changeable) collection that can hold elements of any data type.

# numbers = [1, 2, 3, 4]
# mixed = [1, "Raj", 3.5, True]

# 🔹 List Characteristics
# Property	Description
# Ordered	Elements have a fixed order (index-based)
# Mutable	You can change, add, or remove elements
# Allow Duplicates	[1, 2, 2, 3] is valid
# Heterogeneous	Can contain multiple data types

# 🔹 Indexing & Slicing
a = [10, 20, 30, 40, 50]

print(a[0])      # 10 (first element)
print(a[-1])     # 50 (last element)
print(a[1:4])    # [20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10] (reverse)


# 🔹 Common List Operations
list_1 = [10,20,30,40]
print("Original List is", list)

length_list = len(list_1)
print("Length of the list is:", length_list)       # For finding the length of the list

list_1.append(50)     # Insert element at the end of the array
print("The list after appening at end of array is", list_1)

list_1.insert(2, 25)          # Insert at a position
print("The list after  inserting at an index is", list_1)

list_1.extend([30, 60])
print("The list after extending the list is", list_1)

list_1.remove(30)
print("The list after removing an element from list", list_1)

del list_1[2]
print("The list after deleting an element from particular index 2 is", list_1)

list_1.pop()                            # Pop last element	a.pop()	Removes and returns last element
list_1.index(40)                        # Returns the index at which the given element is present

list_1.count(10)                          # Count occurrences like a frequency mao	a.count(10)	Returns 1
a.sort()	                              # Sorts in place in O(logN) where N is size of array
a.reverse()	                              # Reverses in place

# 🔹 List Comprehension -> Used only there is relation that can established in between elements of the list

# Compact syntax to create lists.
squares = [x**2 for x in range(5)]
print(squares)                                              # Output: [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)                                                # Output: [0, 2, 4, 6, 8]


# 🔹 Nested Lists (Matrix-like)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix[1][2])   # 6

# ⚙️ 3. Arrays in Python (array module)
# An array in Python (from the array module) is a sequence of elements of the same data type, more memory-efficient than a list.

import array
arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' means signed integer
print(arr)

# 🔹 Type Codes
# Type Code	C Type	Python Type	Size (bytes)
# 'b'	signed char	int	1
# 'B'	unsigned char	int	1
# 'i'	signed int	int	2
# 'I'	unsigned int	int	2
# 'f'	float	float	4
# 'd'	double	float	8

# 🔹 Basic Operations on Array in Python
from array import array
arr = array('i', [1, 2, 3])
arr.append(4)
arr.insert(1, 5)
arr.remove(3)
print(arr[2])      # 2
print(arr.tolist())  # Convert to normal list
