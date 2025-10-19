# 🎓 Dictionary Example in Python

student = {
    "name": "Soumyajit Rout",
    "Subjects": {
        "Python": 92,
        "C": 87,
        "Java": 98
    },
    "Age": 20,
    "Gender": "M"
}

# 🖨️ Display the entire dictionary
print("Full Student Dictionary:")
print(student)
print()

# 🎯 Access nested dictionary value
print("Marks in C:", student["Subjects"]["C"])
print()

# 🔑 Display all keys
print("Dictionary Keys:", student.keys())

# Convert keys to list
print("Keys as List:", list(student.keys()))

# Count total key-value pairs
print("Total Keys:", len(student))
print("Total Keys (via list):", len(list(student.keys())))
print()

# 🔢 Display values and items
print("Dictionary Values:", student.values())
print("Dictionary Items:", student.items())
print()

# ⚠️ Difference between direct access & get()
print('Accessing "name" directly →', student["name"])        # Works fine
print('Accessing "name" using get() →', student.get("name"))  # Also works
# print(student["city"])   # Would raise KeyError if key doesn't exist
print(student.get("city"))  # Returns None (no error)
print()

# ➕ Add new key-value pair using update()
student.update({"City": "Bhubaneswar"})

print("After Adding City:")
print(student)
