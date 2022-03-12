# allows execution of statements multiple times
# while loops- are conditional  or indefinite loops
# they keep iterating until a certain condition is met
# while loops are used if the number of iterations are not guaranteed
count = 0
while count < 9:
    count = count + 1
    print("Number:", count)

print("Good bye")

# A little guessing game
import random
n = 20
x = int(n*random.random())
guess = 0   # initializing iterator
while guess != x:
    guess = int(input("Enter a number: "))
    if guess > 0:
        if guess > x:
            print("Number too large")
        elif guess < x:
            print("Number too small")
    else:
        print("sorry that you are giving up")
        pass
else:
    print("Congratulations you made it")

# infinite loop - condition never becomes false
# useful in a client/server programming  where the server needs to run continuously
# so that clients can communicate with it as and when required
var = 1
while var == 1:
    num = int(input("Enter a number: "))
    print("You enterd:", num)

# more examples
a = [1, 2, 3, 4]
while a:
    print(a.pop())

# single statements
count = 0
while count < 5: count += 1; print("Hello Mark")

# Loop control statements
# continue statement - returns the loop to the beginning of the loop
i = 0
a = "geeksforgeeks"
while i < len(a):
    if a[i] == "e" or a[i] == "s":
        i += 1
        continue
    print("Current letter:", a[i])
    i += 1

# continue statement causes termination of that iteration, 2 is not printed and execution returns to top of the loop
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print("Loop ended")

# the break statement terminates a loop entirely
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("Loop ended")


# break/pass  - brings control out of the loop
# breaks the loo as soon as it sees a or e
# prints all letters except e and s
i = 0
a = "geeksforgeeks"
while i < len(a):
    if a[i] == "e" or a[i] == "s":
        i += 1
        pass
    print("Current letter:", a[i])
    i += 1


# Example 5
# initialize offset
offset = 83
while offset != 0:   # true
    print("correcting")
    offset = offset - 1
    print(offset)


# while else loop
# else is only executed when the condition becomes false
i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No break")  # not executed as there is a break

# executed
i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No break")


# example2 on while else loop
# additional statements are executed only if the loop terminates by exhaustion
# if the loop is exited by a break statement the  else wont be executed
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print("Loop done")

# using the pass statement
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print("Loop done")






