""" Object Oriented Programming System - programming paradigm -procedure oriented programming"""
# Classes and Objects
#Creating a class with a class name
class Car:
    pass

# Creating objects of the class
honda = Car()  # specifying to which class it belongs
benz = Car()

# Assigning values to the objects/instances
honda.model_name = "City"
honda.yearM = 2017
honda.price = 100000

benz.model_name = "GLA"
benz.yearM = 2020
benz.price = 500000

print(honda.price)

# when we have common values that needs to be created for all of this;
class Car:
    def __init__(self,model_name,yearM,price):      # creating a constructor which initializes values of the objects
        self.model_name = model_name           # referencing the objects
        self.yearM = yearM
        self.price = price


honda  = Car("City",2017,100000)
benz = Car("GLA",2020,500000)

# adding any specific value
honda.cc = 1500
print(honda.price)
# checking the complete values associated to an objeect using dict function
print(honda.__dict__)
print(benz.__dict__)

# performing operations in a class - creating a function of price increase
class Car():
    def __init__(self,model_name,yearM,price):      # creating a constructor which initializes values of the objects
        self.model_name = model_name           # referencing the objects
        self.yearM = yearM
        self.price = price

    def price_inc(self):
        self.price=int(self.price*1.15)


honda  = Car("City",2017,1000000)
benz = Car("GLA",2020,5000000)

# adding any specific value
honda.cc = 1500

print(honda.price)
honda.price_inc()  # calling the function with respect to class
print(honda.price)


# Example 2
class Employee:
    """Common base class for all employees"""
    EmpCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.EmpCount += 1

    def display_count(self):
        print("Total Employees: %d" %Employee.EmpCount)

    def display_employee(self):
        print("Name: ",self.name, ", Salary: ",self.salary)

# creating object instances
""" This would be the first object of Employee class"""
emp1 = Employee("Evans", 9000)
""" This would create second object of Employee class"""
emp2 = Employee("Dan",9000)
""" This would create third object of Employee class"""
emp3 = Employee("Mesh",11000)

# accessing attributes
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()
emp1.display_count()


""" Object Oriented Objects in Python  - inheritance,encapsulation,abstraction """
# inheritance - ability for any  class to inherit the attributes and behaviours from the super class
class SuperCar(Car):  # specify car to enable inheritance
    pass


honda  = SuperCar("City",2017,1000000)  # making honda an instance of the supercar class
benz = Car("GLA",2020,5000000)

honda.cc = 150
print(honda.yearM)  # yearM is defined in the superclass but not explicitly defined in the subclass
print(honda.__dict__)  # printing the name space for honda
print(help(honda))
honda.price_inc()
print(honda.price)

# when defining an init method as part of the subclass
class SuperCar(Car):
    def __init__(self,model_name,yearM,price,cc):
        super.__init__(model_name,yearM,price)
        self.cc= cc    # when including cc as part of the super class


""" Encapsulation - binding the data and code together as a single unit """
""" abstraction - hides implementation details and only provides the functionality to the user """
# abstract class can not have an object of itself-need to inherit and create an object

from abc import ABC, AbstractMethod

class Car(ABC):
    @AbstractMethod
    def price_inc(self): # in my abstract class - defining the method to increase the price based on my requirement
        pass     # not defining any logic

class SuperCar(Car):
    def __init__(self,model_name,yearM,price,cc):
        super.__init__(model_name,yearM,price)
        self.cc= cc    # when including cc as part of the super class
    def price_inc(self):       # creating the same function
        self.price=int(self.price*2)
