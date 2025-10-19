# ---------------------------------------------
# 🧩 Let's Practice
# ---------------------------------------------

# ---------------------------------------------
# Q1. Store the following word meanings in a dictionary:
# table : "a piece of furniture", "list of facts & figures"
# cat   : "a small animal"
# ---------------------------------------------

meaning = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}
print("Q1. Word Meanings Dictionary:")
print(meaning)
print("---------------------------------------------\n")


# ---------------------------------------------
# Q2. You are given a list of subjects for students.
# Assume one classroom is required for 1 subject.
# How many classrooms are needed by all students?
#
# Subjects:
# "python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"
# ---------------------------------------------

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print("Q2. Subjects Set:", subjects)
print("Number of classrooms needed:", len(subjects))
print("---------------------------------------------\n")


# ---------------------------------------------
# Q3. WAP to enter marks of 3 subjects from the user
# and store them in a dictionary.
# Start with an empty dictionary & add one by one.
# Use subject name as key & marks as value.
# ---------------------------------------------

marks = {}

x = int(input("Enter marks in Physics: "))
marks.update({"Physics": x})

y = int(input("Enter marks in Chemistry: "))
marks.update({"Chemistry": y})

z = int(input("Enter marks in Math: "))
marks.update({"Math": z})

print("Q3. Marks Dictionary:", marks)
print("---------------------------------------------\n")


# ---------------------------------------------
# Q4. Figure out a way to store 9 and 9.0 as separate
# values in the set. (Use built-in data types)
# ---------------------------------------------

# Method 1: Use string for differentiation
values = {9, 9.0, 9.25, "9.0"}
print("Q4. Set storing 9 and 9.0 separately (Method 1):")
print(values)

# Method 2: Use tuples with type tagging
values2 = {
    ("int", 9),
    ("float", 9.0)
}
print("\nQ4. Set storing 9 and 9.0 separately (Method 2):")
print(values2)

print("---------------------------------------------")
