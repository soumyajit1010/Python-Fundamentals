tup =  (1, 2, 3, 4, 5,6, 6, 6, 7)
for num in tup:
    print(num)

str = "Soumyajit Rout"
for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("END")


# ---------------------------------------------
# 🧩 Let's Practice (Using for loop)
# ---------------------------------------------

# Q1. Print the elements of the following list using a loop
nums_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("Elements of the list:")
for el in nums_list:
    print(el)

print("---------------------------------------------")


# Q2. Search for a number x in this tuple using a loop
nums_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
found = False

for idx, el in enumerate(nums_tuple):  # enumerate gives both index & value
    if el == x:
        print(f"Number {x} found at index {idx}")
        found = True

if not found:
    print(f"Number {x} not found in the tuple")

print("---------------------------------------------")
