# List Slicing in Python

# Example list
marks = [87, 64, 33, 95, 76]

# Slicing examples
print("marks[1:4] =", marks[1:4])          # [64, 33, 95]
print("marks[:4] =", marks[:4])            # [87, 64, 33, 95]
print("marks[1:] =", marks[1:])            # [64, 33, 95, 76]
print("marks[-3:-1] =", marks[-3:-1])      # [33, 95]


# List Methods in Python

# 1️⃣ append() – adds one element at the end
nums = [2, 1, 3]
nums.append(4)
print("After append:", nums)  # [2, 1, 3, 4]


# 2️⃣ insert() – inserts an element at a specific index
nums.insert(1, 5)
print("After insert:", nums)  # [2, 5, 1, 3, 4]


# 3️⃣ sort() – sorts the list in ascending order
nums.sort()
print("After sort (ascending):", nums)  # [1, 2, 3, 4, 5]


# 4️⃣ reverse() – reverses the list
nums.reverse()
print("After reverse:", nums)  # [5, 4, 3, 2, 1]


# 5️⃣ sort(reverse=True) – sorts the list in descending order
nums.sort(reverse=True)
print("After sort (descending):", nums)  # [5, 4, 3, 2, 1]


# ---------------------------------------------------------

# 6️⃣ remove() – removes the first occurrence of an element
nums2 = [2, 1, 3, 1]
nums2.remove(1)
print("After remove(1):", nums2)  # [2, 3, 1]


# 7️⃣ pop() – removes the element at a specific index
nums2.pop(1)
print("After pop(1):", nums2)  # [2, 1]
