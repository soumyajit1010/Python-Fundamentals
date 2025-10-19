# ---------------------------------------------
# 🧩 Let's Practice (Using for & range())
# ---------------------------------------------

# Q1. Print numbers from 1 to 100
print("Q1. Numbers from 1 to 100:")
for i in range(1, 101):   # starts at 1, ends at 100
    print(i, end=" ")
print("\n---------------------------------------------\n")


# Q2. Print numbers from 100 to 1
print("Q2. Numbers from 100 to 1:")
for j in range(100, 0, -1):   # starts at 100, ends at 1, step -1
    print(j, end=" ")
print("\n---------------------------------------------\n")


# Q3. Print the multiplication table of a number n
print("Q3. Multiplication table of n:")
n = int(input("Enter the number: "))

for k in range(1, 11):   # 1 to 10
    print(f"{n} × {k} = {n * k}")

print("---------------------------------------------")
