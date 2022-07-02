"""
"""


class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        """Alternative constructor.
        Describe at end of file
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    """
    Lets say we wanted a simple function that would take in a date and
    return whether or not that was a work day.
    That has a logical connection to our employee class but it doesn't
    depend on any particular instance or class variable so we'll make
    it a staticmethodA
    A method should be static if you don't access the instance or the class
    anywhere between the function
    """
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

if __name__== '__main__':
    emp_1 = Employee("Mark", "Jumba", 90000)
    emp_2 = Employee("Jumba", "Mark", 91000)

    #Employee.set_raise_amt(1.08)
    emp_1.set_raise_amt(1.07)

    print(Employee.raise_amt)
    print(emp_1.raise_amt)
    print(emp_2.raise_amt)

    # class methods as alternative constructors
    emp_str_1 = "John-Doe-7000"
    emp_str_2 = "Steve-Jobs-3000"
    emp_str_3 = "Jane-Doe-5000"

    first, last, pay = emp_str_1.split('-')
    new_emp_1 = Employee(first, last, pay)
    
    print()
    print(new_emp_1.email)
    print(new_emp_1.pay)

    """
    If the above is a common use case for how someone is using our class
    we dont want them to always have to parse the strings every time they want
    to create a new employee
    Let's create an alternative constructor that allows them to parse the
    string and create the employee for them.
    """
    print('----------')
    new_emp_2 = Employee.from_string(emp_str_2)
    print(new_emp_2.email)
    print(new_emp_2.pay)

    print('-----------')
    import datetime
    my_date = datetime.date(2016, 7, 10)
    print(Employee.is_workday(my_date))
