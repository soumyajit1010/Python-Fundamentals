# ---------------------------------------------
# 🚀 Example: break and continue in Python
# ---------------------------------------------

print("🔹 Example 1: Using break\n")

# Loop from 1 to 10
for i in range(1, 11):
    if i == 5:
        print("Breaking at", i)
        break  # stops the loop completely
    print("i =", i)

print("\nLoop stopped because break was triggered at 5.\n")
print("---------------------------------------------\n")


print("🔹 Example 2: Using continue\n")

# Loop from 1 to 10
for j in range(1, 11):
    if j == 5:
        print("Skipping number", j)
        continue  # skips only this iteration, continues next
    print("j =", j)

print("\nLoop continued after skipping 5.\n")
print("---------------------------------------------")
