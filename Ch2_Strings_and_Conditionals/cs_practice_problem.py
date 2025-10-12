"""
Let‘s Practice

WAP to check if a number entered by the user is odd or even.

WAP to find the greatest of 3 numbers entered by the user.

WAP to check if a number is a multiple of 7 or not.
"""
num = int(input("enter a number: "))
if(num%2==0):
    print("number is even!!!")
else:
    print("nnumber is odd!!!")


a = int(input("enter number: "))
b = int(input("enter number: "))
c = int(input("enter number: "))
if(a>=b and a>=c):
    print("largest number", a)
elif(b>=c):
    print("largest number", b)
else:
    print("largest number", c)



x = int(input("enter a number: "))
if(x%7==0):
    print("multiple of 7!")
else:
    print("not multiple of 7!")