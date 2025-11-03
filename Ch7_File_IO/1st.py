# 📁 File Handling in Python

# ------------------------------
# 1️⃣ Read from a file
# ------------------------------
# Make sure 'demo.txt' exists before running this part.
# If it doesn’t, Python will give FileNotFoundError.
# f = open("demo.txt", "r")
# data = f.read()        # Reads entire content of the file
# print(data)
# print(type(data))      # Output type: <class 'str'>
# f.close()


# ------------------------------
# 2️⃣ Read line by line
# ------------------------------
# f = open("demo.txt", "r")
# line1 = f.readline()   # Reads first line
# print(line1)
# line2 = f.readline()   # Reads next line
# print(line2)
# f.close()


# ------------------------------
# 3️⃣ Write to a file
# ------------------------------
# "w" mode will overwrite the file if it already exists.
# f = open("demo.txt", "w")
# f.write("iiiiiiiiiiiiiiiiiiiiiiiiiiiii")   # Writes new content
# f.close()


# ------------------------------
# 4️⃣ Append to a file
# ------------------------------
# "a" mode adds new data at the end of file.
# f = open("demo.txt", "a")
# f.write("bbbbbbbbbbbbb")   # Adds this text at end
# f.close()


# ------------------------------
# 5️⃣ Create a new file
# ------------------------------
# "w" will create a new file if it doesn't exist.
f = open("abc.txt", "w")
f.close()

print("✅ File operations executed successfully!")
