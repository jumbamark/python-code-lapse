class Parent:
    def __init__(self, f_name, f_age):
        self.name = f_name
        self.age = f_age

    def view(self):
        print(self.name, self.age)


class Child(Parent):
    def __init__(self,f_name,f_age):
        Parent.__init__(self,f_name,f_age)   # specify the parent function with the init function
        self.name = f_name
        self.age = f_age
        self.lastname = "Jumba"

    def view(self):
        print(self.age, self.lastname, self.name)


ob = Child(21 ,"Mark")
ob.view()    # calling the function

""" types of inheritance"""
# single inheritance - one child class and one parent class
class Parent:
    def func1(self):
        print("this is function 1")


class Child(Parent):
    def func2(self):
        print("this is function 2")

ob = Child()
ob.func1()

  #multiple - more than one parent class
class Parent:
    def func1(self):
        print("this is function 1")

class Parent2():
    def func3(self):
        print("this is function 3")

class Child(Parent, Parent2):
    def func2(self):
        print("this is function 2")


ob = Child()
ob.func1()
ob.func3()

# multilevel - child class acts as a parent class for another child class
class Parent:
    def func1(self):
        print("this is function 1")


class Parent2(Parent):
    def func3(self):
        print("this is function 3")


class Child(Parent2):
    def func2(self):
        print("this is function 2")


ob = Child()
ob.func1()
ob.func3()

# hierarchical - multiple inheritance from the same parent class
class Parent:
    def func1(self):
        print("this is function 1")


class Parent2(Parent):
    def func3(self):
        print("this is function 3")


class Child(Parent):
    def func2(self):
        print("this is function 2")


ob = Child()
ob1= Parent2()
ob.func1()
ob1.func1()
ob.func3()

# hybrid inheritance - i.e single and multiple inheritance going on simultaneously
class Parent:
    def func1(self):
        print("this is function 1")

# single inheritance
class Parent2(Parent):
    def func3(self):
        print("this is function 3")

class Parent3:
    def func4(self):
        print("this is function 4")

# multiple inheritance
class Child(Parent,Parent3):
    def func2(self):
        print("this is function 2")


ob = Child()

ob.func1()
ob.func4()

""" Super function - calls the parent class method """
class Parent:
    def func1(self):
        print("this is function 1")


class Child(Parent):
    def func2(self):
        super().func1()     # instead of calling the parent function from the object
        print("this is function 2")

ob = Child()
ob.func2()

""" Method overriding - can be achieved to change the functionality of the parent class function"""
class Parent:
    def func1(self):
        print("this is function 1")


class Child(Parent):
    def func1(self):
        print("this is function 2")


ob = Child()
ob.func1()






""" Geeks for Geeks """
""" Example 2 """
class Person():
    # init method or constructor
    def __init__(self, name):
        self.name = name

    # to get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False

    # Inherited or subclass
class Employee(Person):

    # Here we return True
    def isEmployee(self):
        return True


    # Driver code
ob = Person("Tom")  # An object of a person
print(ob.getName(), ob.isEmployee())

ob = Employee("Keen")  #An object of employee
print(ob.getName(), ob.isEmployee())

""" Example 3 """
# Parent Class
class Person( object ) :

    # __init__ is known as the constructor
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def view(self):
        print(self.name)
        print(self.id_number)


        # Child class
class Employee( Person )  :
    def __init__(self,name,id_number,salary,post):
        Person. __init__(self,name,id_number)     # invoking the constructor of the parent class
        self.salary = salary
        self.post = post

    def show(self):
        print(self.salary)
        print(self.id_number)

# creation of an object variable on an instance
a = Employee( "Liz", 9801536, 82000, "Intern")

# calling a function of the class object
a.view()
a.show()

""" Example 3 """
# Error if we forget to invoke the constructor of the parent class
class A:
    def __init__(self, n= "Ray"):
        self.name = n

class B(A):
    def __init__(self, roll):
        self.roll = roll

ob = B(23)
print(object.n)


""" Types of inheritance """
# single inheritance - when a child class inherits from only one parent class- examples above
# Multiple inheritance - when a child class inherits from multiple parent classes
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")


class Derived(Base1, Base2):
    def __int__(self,str1,str2):


        # calling constructors of base 1 and Base 2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def view(self):
        print(self.str1, self.str2)

ob = Derived()
ob.view()

""" Multilevel inheritance - when we have a chi(ld and grandchild relationship"""
# Base or Super class. Note in object in bracket
class Base( object ):

    # constructor
    def __init__(self ,name):
        self.name = name

    # TO get name
    def getName(self):
        return self.name

        # Inherited or subclass. Note Person in bracket
class Child (Base):

    # constructor
    def __init__(self,name,age):
        Base.__init__(self, name)
        self.age = age

        # To get age
    def getAge(self):
        return self.age

    # Inherited or sub class . Note person in bracket
class Grandchild(Child):

    # constructor
    def __init__(self,name,age,address):
        Child.__init__(self,name,age)
        self.address = address

    # to get address
    def getAdress(self):
        return self.address

    # Driver code
g = Grandchild( "Euro", 10, "Umoja" )
print(g.getName(), g.getAge(), g.getAddress())

""" Private members of parent class"""
# We don't always want the instance variables of the parent class to be inherited  by the child class
class C(object):
    def __init__(self):
        self.c = 21

        # d is a private instance
        self.__d = 42

class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)

ob1 = D()
# Produces an error as d is a private instance variable
print(ob1.d)




