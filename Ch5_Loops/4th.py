# ---------------------------------------------
# 🧩 Understanding range() in Python
# ---------------------------------------------

# range(stop) → generates numbers from 0 to stop-1
seq = range(10)  # same as range(0, 10)

# Accessing individual elements
print("Accessing elements individually:")
print(seq[0])  # 0
print(seq[1])  # 1
print(seq[2])  # 2
print(seq[3])  # 3

print("---------------------------------------------")

# Using range() in a for loop
print("Using range(10) in a loop:")
for i in seq:
    print(i)

print("---------------------------------------------")

# range(stop)
print("range(22): Numbers from 0 to 21")
for j in range(22):
    print(j)

print("---------------------------------------------")

# range(start, stop)
print("range(90, 100): Numbers from 90 to 99")
for m in range(90, 100):
    print(m)

print("---------------------------------------------")

# range(start, stop, step)
print("range(2, 10, 2): Numbers from 2 to 8 with step of 2")
for k in range(2, 10, 2):
    print(k)

print("---------------------------------------------")
