## Object Oriented Programming
- In the preceding programs we have designed them around functions i.e blocks of statements which manipulate data. This is called the __procedure-oriented__ way of programming
- There is another way of organizing programs which is to combine data and functionality and wrap it inside something called an object. This is called the __object oriented programmming__ paradigm
- Most of the time you can use procedural programming but when writing large programs or have a problem that is better suited to this method, you can use object oriented programming techniques.
- Classes and objects are the two main aspects of object oriented programming. A __class__ creates a new type where __objects__ are __instances__ of the class. An analogy is that you can have variables of type `int` which translates to saying that variables that stores integers are variables which are instances(objects) of the `int` class.
- Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as __fields__.
- Objects can also have functionality by using functions that belong to a class. Such functions are called __methods__ of the class.
- This terminology is importatnt because it helps us differentiate between functions and variables which are independent and those which belong to a class or object. Collectively the __fields__ and __methods__ can be reffered to as __attributes__ of that class.
- Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called __instance variables__ and __class variables__ respectively.

- The four major principles of object-orientation:
    1. Encapsulation
    2. Data Abstraction
    3. Polymorphism
    4. Inheritance

- 

## The `self`
- Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it
- This particular variable refers to the object itself and by convention it is given the name __self__
- Say you have a class called `MyClass` and an instance of this class called `myobject`. When you call a method of this object as `myobject.method(arg1, arg2)`, this is automatically converted by Python into `MyClass.method(myobject, arg1, arg2)` - this is all the special __self__ is about


# Class And Object Variables
- We have discussed the functionality part of classes and objects (i.e methods), let's look through the data part
- The data part i.e fields are nothing but ordinary variables that are _bound_ to the __namespaces__ of the classes and objects.This means that these names are valid within the context of these classes and objects only. That's why they are called _name spaces_
- There are two types of fields - class variables and object variables which are classified depending on whether the class or object owns the variables respectively
__Class variables__ are shared - they can be accessed by all instances of that class. There is only one copy of the class variable and when any one object makes a change to a class variable that change will be seen by all the other instances
__Object variables__ are owned by each individual object/instance of the class. In this case each object has its own copy of the field i.e they are not shared and related in any way to the field by the same name in a different instance


## Class Vs Instance Attributes
- Instance attributes are owned by the specific instances of a class. That is, for two different instances, the instance attributes are usually different
- Class attributes are attributes which are owned by the class itself, they will be shared by all the instances of the class. They therefore have the same value for every instance
- They are defined outside all the methods and are usually placed at the top, right below the class header
- If you want to change a class attribute you have to do it with the notation ClassName.AttributeName. Otherwise you will create a new instance variable
    ```python
    class A:
        a = "I am a class attribute!"
    x = A()
    y = A()
    x.a = "This creates a new instance attribute for x"
    A.a = "This is changing the class attribute 'a'!"
    ```

- Python's class attributes and object attributes are stored in separate dictionaries
    ```python
    x.__dict__
    y.__dict__
    A.__dict__
    x.__class__.__dict__
    ```
## Static Methods
- We've used class attributes as public attributes but we can make public attributes private as well
- We can do this by adding double underscore, if we do so we need a possibility to access and change these private class attributes. We could use instance methods for this purpose
    ```python
    class Robot:
        __counter = 0

        def __init__(self):
            type(self).__counter += 1

        def RobotInstances(self):
            return Robot.__counter

    if __name__ == "__main__":
        x = Robot()
        print(x.RobotInstances())
        y = Robot()
        print(y.RobotInstances())
    ```
    __OUTPUT__ : `1`, `2`

- This is not a goot idea though, because:
    1. The number of robots has nothing to do with a single robot instance
    2. We can't inquire the number of robots before we create an instance

- If we try to invoke the method with the class name `Robot.RobotInstances()` we get an error message because it needs an instance as an argument
- The next idea which doesn't solve our problem is omitting the parameter "self"
     ```python
      class Robot:
          __counter = 0
  
          def __init__(self):
              type(self).__counter += 1
  
          def RobotInstances():
              return Robot.__counter
     
      if __name__ == "__main__":
          Robot.RobotInstances()
      ```
      __OUTPUT__ : `0`

- Its now possible to access the method via a classname but we can't call it via an instance
    ```python
    x = Robot()
    x.RobotInstances()
    ```
    __OUTPUT__: `TypeError: RobotInstances() takes 0 positional arguments but 1 was given`

- The call `x.RobotInstances()` is treated as an instance method call and an instance method needs a reference to the instance as the first parameter
- What do we want? We want a method which we can call via the class name or via the instance name without necessity of passing a reference to an instance to it
The solution lies in __static methods__, refer to `instance-count_staticmethods.py`

## Class Methods
- Static methods shouldn't be confused with class methods
- Like static methods class methods aren't bound to instances, but unlike static methods class methods are bound to a class
- The first parameter of a class method is a reference to a class, i.e a class object
- They can be called via an instance or class name, refer to `instance-count_classmethods.py`

### Uses of classmethods
1. Used in the definition of the so-called factory methods
2. Often used where we have static methods which have to call other static methods.To do this we have to hard code the class name, if we had to use static methods. This is a problem, if we are in a use case, where we have inherited classes
`fraction-methods.py`

## Class Methods vs. Static Methods and Instance Methods
-  Third example will demonstrate the usefulness of classmethods in inheritance

#### Example 1
- Define a class `Pet` with a method `about`, gives some general class information
- The class `Pet` will be inherited both in the subclass `Dog` and `Cat`, the method `about` will be inherited as well
- __End goal__: Demonstrate that we encounter problems if we define the method `about` as a normal instance method or as a static method

- __Defining `about` as an instance method:__

    ```python
    class Pet:
        _class_info = "pet animals"

        def about(self):
            print("This class is about" + self._class_info + "!")

    class Dog(Pet):
        _class_info = "man's best friends"

    class Cat(Pet):
        _class_info = "all kinds of cats"

    ```
    ```python
    p = Pet()
    p.about()

    d = Dog()
    d.about()

    c = Cat()
    c.about()
    ```
    __OUTPUT:__
    ```
    This class is about pet animals!
    This class is about man's best friends!
    This class is about all kinds of cats!
    ```
- Looks okay at first glance, on second thought we recognize the awful design
- We had to create instances of the `Pet`, `Dog` and `Cat` classes to be able to ask what the class is about
- It would be better if we could write `Pet.about()`, `Dog.about()` and `Cat.about()` to get the previous result
- We cannot do this, we will have to write `Pet.about(p)`, `Dog.about(d)` and `Cat.about(c)` instead

- __Defining `about` as a static method__
- Defining `about` as a static method to show the disadvantage of this approach
- A static method does not have a parameter with a reference to an object, so about will have no parameters at all
- Due to this we are capable of calling "about" without the necessity of passing an instance  as a parameter, i.e `Pet.about()`, `Dog.about()` and `Cat.about()`
- A problem lurks in the definition of `about`. The only way to access the class info `_class_info` is putting a class name in front
- Arbitrarily put in `Pet`, we could put in `Cat` or `Dog` as well. No matter what we do the solution will not be what we want.

    ```python
    class Pet:
        _class_info = "pet animals"

        @staticmethod
        def about():
            print("This class is about" + Pet.__class_info + "!")

    class Dog(Pet):
        _class_info = "man's best friends"

    class Cat(Pet):
    _class_info = "all kinds of cats"
    ```
    ```python
    Pet.about()
    Dog.about()
    Cat.about()
    ```

    __OUTPUT:__
    ```
    This class is about pet animals!
    This class is about pet animals!
    This class is about pet animals!
    ```
- We have no way of differentiating between the Class `Pet` and its subclasses `Dog` and `Cat`
- classmethod is the solution

- __Defining `about` as a class method__

    ```python
    class Pet:
        _class_info = "pet animals"

        @classmethod
        def about(cls):
            print("This class is about" + cls._class_info + "!")

    class Dog(Pet):
        _class_info = "man's best friends"

    class Cat(Pet):
        _class_info = "all kinds of cats"
    ```
    ```python
    Pet.about()
    Dog.about()
    Cat.about()
    ```

    __OUTPUT:__
    ```
    This class is about pet animals!
    This class is about man's best friends!
    This class is about all kinds of cats!
    ```
