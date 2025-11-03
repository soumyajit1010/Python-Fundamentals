# 📘 Understanding Python File Modes

# ------------------------------
# 1️⃣  "r+" → Read and Write (No Truncate)
# ------------------------------
# Opens the file for reading and writing.
# File must already exist.
# The file pointer starts at the beginning.
# It does NOT erase existing content.
f = open("demo.txt", "r+")
f.write("abc")           # Overwrites from the beginning
print(f.read())          # Reads remaining content after "abc"
f.close()


# ------------------------------
# 2️⃣  "w+" → Write and Read (Truncate)
# ------------------------------
# Opens the file for reading and writing.
# If file exists, its content is ERASED.
# If file doesn’t exist, it’s created.
f = open("demo.txt", "w+")
# f.write("abc")         # You can write before reading
print(f.read())          # Empty because file is truncated
f.close()


# ------------------------------
# 3️⃣  "a+" → Append and Read (No Truncate)
# ------------------------------
# Opens file for reading and appending.
# File pointer is at END of file.
# If file doesn’t exist, it’s created.
f = open("demo.txt", "a+")
# f.write("abc")         # Appends at the end
print(f.read())          # Nothing prints (pointer at end)
f.write("abc")           # Appends new text
f.close()


# ------------------------------
# 🔍 Summary of File Modes
# ------------------------------
# 'r'   → open for reading (default)
# 'w'   → open for writing, truncate (erase) file first
# 'x'   → create new file, fail if already exists
# 'a'   → open for writing, append to end if file exists
# 'b'   → binary mode (e.g., 'rb' or 'wb')
# 't'   → text mode (default)
# '+'   → update mode (read + write)

# Examples:
# "r+" → read + write (no truncate)
# "w+" → write + read (truncates)
# "a+" → append + read (no truncate)
# "rb" → read binary
# "wt" → write text (same as 'w')

print("✅ File mode demonstration complete!")



'''
| Mode | Read | Write | Truncate | Pointer | Create if not exist |
| ---- | ---- | ----- | -------- | ------- | ------------------- |
| `r`  | ✅   | ❌   | ❌      | Start    | ❌                 |
| `r+` | ✅   | ✅   | ❌      | Start    | ❌                 |
| `w`  | ❌   | ✅   | ✅      | Start    | ✅                 |
| `w+` | ✅   | ✅   | ✅      | Start    | ✅                 |
| `a`  | ❌   | ✅   | ❌      | End      | ✅                 |
| `a+` | ✅   | ✅   | ❌      | End      | ✅                 |


'''