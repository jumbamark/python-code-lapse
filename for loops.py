# used when you know the number of iterations required
fruits = ["mango", "grapes", "apples"]
for fruit in fruits:
    print("current fruit", fruit)

print("Good bye")

# calculating the factorial - we know how many iterations are required
num = int(input("Number: "))
factorial = 1
if num < 0:
    print("Number must be positive")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print(factorial)


# the break and continue statements
# break terminates the loop completely and proceeds to the first statement
for i in ["foo", "boo", "baz", "qux"]:
    if "b" in i:
        break
    print(i)

# continue terminates the current situation and proceeds to the next iteration
for i in ["foo", "boo", "baz", "qux"]:
    if "b" in i:
        continue
    print(i)

# The else clause
# the else clause will be executed if the loop terminates through exhaustion of the iterable
for i in ["foo", "boo", "baz", "qux"]:
    print(i)
else:
    print("Done")

# the else clause will not execute if the list is broken out of with a break statement
for i in ["foo", "bar", "baz", "qux"]:
    if i == "bar":
        break
    print(i)
else:
    print("Done")


