"""movies = []
mov1 = input("enter 1st mmovie: ")
mov2 = input("enter 2nd mmovie: ")
mov3 = input("enter 3rd mmovie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)"""

#------------------

"""movies = []
mov = input("enter 1st mmovie: ")
movies.append(mov)
mov = input("enter 2nd mmovie: ")
movies.append(mov)
mov = input("enter 3rd mmovie: ")
movies.append(mov)

print(movies)"""
#----------------------

list1 = ["m", "a", "a", "m"]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("notPalindrome")


#------------------------

# Example: Using count() method on a tuple
grade = ("C", "D", "A", "A", "B", "B", "A")

# count() returns the number of times the given value appears
print(grade.count("A"))

#------------------------------

# Example: Using sort() method on a list

grade = ["C", "D", "A", "A", "B", "B", "A"]

# sort() arranges elements in ascending (alphabetical) order
grade.sort()

print(grade)
