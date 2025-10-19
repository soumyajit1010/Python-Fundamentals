for i in range(5):
    pass

print("Some useful work...")



# ---------------------------------------------
# 🧩 Let's Practice
# ---------------------------------------------
# Q1. WAP to find the sum of first n numbers (using while loop)
# Q2. WAP to find the factorial of a number n (using for loop)
# ---------------------------------------------

# Q1. Sum of first n numbers using while loop
print("Q1. Sum of first n numbers (using while loop)")
n = int(input("Enter the value of n: "))

sum_n = 0
i = 1

while i <= n:
    sum_n += i
    i += 1

print(f"Sum of first {n} numbers = {sum_n}")
print("---------------------------------------------\n")


# Q2. Factorial of n using for loop
print("Q2. Factorial of a number (using for loop)")
num = int(input("Enter the number: "))

fact = 1
for i in range(1, num + 1):
    fact *= i

print(f"Factorial of {num} = {fact}")
print("---------------------------------------------")
