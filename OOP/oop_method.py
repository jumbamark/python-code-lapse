class Person:
    def say_hi(self):
        print("Hello, how are you?")

p = Person()
p.say_hi()

"""
We see "self" in action. The "say_hi" method takes no parameters but still has the "self" in the function definition
"""
