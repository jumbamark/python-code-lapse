# Exception-event that disrupts the normal flow of a program's instructions during execution
# exception handling - process of responding to the occurrence of an exception
""" Raising an exception - we can use raise to throw an exception if a condition exists """
x = 10
if x > 5:
    raise Exception('x should not exceed 5.The value of was: {}'.format(x))

""" Assertion Error Exception """
import sys
assert("windows" in sys.platform), "This code runs on Windows only."

""" Exception Handling - Try and except block """
""" Assertion Error Exception """

# The try and except block in python is used to catch and handle exceptions
def windows_interaction():
    assert("windows" in sys.platform), "Function can only run on Windows."
    print("Doing something")


try:
    windows_interaction()
except:
    print("Windows function was not executed")

# Example where you capture the AssertionError and output message
try:
    windows_interaction()
except AssertionError as error:
    print(error)
    print("The windows_interaction() function was not executed")

# Another example where you open a file and use a built-in exception
try :
    with open("file.log") as file:
        read_data = file.read()
except:
    print("Could not open file.log")      # this will be the output if the file.log does not exist

# Exception FileNotFoundError is raised when a file or directory is requested but does not exist
# catching this exception and printing it on the screen
try:
    with open("file.log") as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

# Another Example Case
# try:
#     windows_interaction()
#     with open("file.log") as file:
#         read_data = file.read






""" Geeks for Geeks"""
# Exception - error that occur after passing the syntax test
# Error Handling
# Handling exceptions with try/except/finally

# put unsafe operations in try block
try:
    print("code start")

    # unsafe operation perform
    print(1/0)

    # if error occurs then it goes in except block
except:
    print("an error occurs")

    # final code in finally block
finally:
    print("Geeks for geeks")

# Raising exceptions for a predefined condition
# try for unsafe code
try:
    amount = 19999
    if amount < 2999:
        # raise the ValueError
        raise ValueError("please add money in your account")
    else:
        print("You're eligible to purchase DSA self paced course")
# if false then raise the value error
except ValueError as e:
    print(e)

# The try block does not raise any errors,so the else block is executed
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# the finally block gets executed no matter if the try block raises any errors or not
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")

#  print one message if the Try block raises a NameError and another for other errors
# the try bloc will generate NameError bec x is not defined
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


""" More examples - catching exceptions in python """
# import module sys to get the type of exception
import sys
randomList = ["a", 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        pass
    except:
        print("OOps!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

""" Raising exceptions in python"""
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is a not a positive integer!")
except ValueError as ve:
    print(ve)

# program to print the reciprocal of even numbers
try:
    num =int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number")
else:
    reciprocal = 1/num
    print(reciprocal)

