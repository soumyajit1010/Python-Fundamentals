# Creating a set
collection = {1, 2, 3, 4, 5}

print(collection)
print(type(collection))

# Sets automatically remove duplicate elements
anotherSet = {1, 2, 2, 2, 2, "Hello", "World", "Hello", 4}
print(anotherSet)
print(len(anotherSet))  # Total number of unique items

# Empty set vs empty dictionary
newSet = {}          # Empty dictionary
emptySet = set()     # Empty set

# Set is mutable, but its elements must be immutable
emptySet.add(34)
emptySet.add(34)
emptySet.add(4)
emptySet.add("Soumyajit Rout")

print(emptySet)

# Removing an element
emptySet.remove(34)

# Lists cannot be added to a set (unhashable type)
# emptySet.add([1, 2, 3, 4])  # ❌ TypeError

# Clear all elements from the set
emptySet.clear()
print(emptySet)

# Set operations
col = {"Soumya", "Jit", "Rout", "Coding", "Python"}
# print(col.pop())
# print(col.pop())

dol = {"Jit", "jit", "abc", 4, True, "11", 'c', True, 4}
print(dol)

print("Union:", col.union(dol))
print("Intersection:", col.intersection(dol))
