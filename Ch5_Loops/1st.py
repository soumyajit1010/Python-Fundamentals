# ---------------------------------------------
# 🧩 Let's Practice (Loops)
# ---------------------------------------------

# ---------------------------------------------
# Q1. Print numbers from 1 to 100.
# ---------------------------------------------

print("Q1. Numbers from 1 to 100:")
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1

print("\n---------------------------------------------\n")


# ---------------------------------------------
# Q2. Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ---------------------------------------------

print("Q2. Elements of the list:")
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for num in numbers:
    print(num, end=" ")

print("\n---------------------------------------------\n")


# ---------------------------------------------
# Q3. Print numbers from 100 to 1.
# ---------------------------------------------

print("Q3. Numbers from 100 to 1:")
j = 100
while j >= 1:
    print(j, end=" ")
    j -= 1

print("\n---------------------------------------------\n")


# ---------------------------------------------
# Q4. Print the multiplication table of a number n.
# ---------------------------------------------

print("Q4. Multiplication Table of n:")
n = int(input("Enter the number: "))
k = 1
while k <= 10:
    print(f"{n} × {k} = {n * k}")
    k += 1

print("---------------------------------------------\n")


# ---------------------------------------------
# Q5. Search for a number x in this list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ---------------------------------------------

print("Q5. Search for a number in the list:")
numbers_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter number to search: "))

found = False
for num in numbers_list:
    if num == x:
        found = True
        break

if found:
    print(f"{x} is found in the list ✅")
else:
    print(f"{x} is not found in the list ❌")

print("---------------------------------------------")
