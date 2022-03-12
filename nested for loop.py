# pythagoras numbers between 1 and 20
from math import sqrt
n = int(input("Enter a number: "))
for a in range(1, n + 1):
    for b in range(a, n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if (a**2 + b**2) == c**2:
            print(a, b, c)


# pyramid using nested for loops
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# using a for loop inside a while loop
travelling = input("Yes or No: ")

while travelling == "Yes":

    num = int(input("Enter number of people travelling: "))

    for num in range(1, num + 1):
        name = input("Name: ")
        sex = input("Male or Female: ")
        age = input("Age: ")
        print(name)
        print(age)
        print(sex)
    travelling = input("oops, forgot someone")

