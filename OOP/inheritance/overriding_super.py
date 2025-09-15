"""Overriding and super
We can add a phone number for our closest friends by setting a phone
attribute on the contact after its constructed
We have to override __init__

Overriding is altering or replacing a method of the suoerclass with 
a new method(with the same name) in the subclass
The subclass's newly created method is automatically called instead
of the superclass's method

Any method can be overriden, not just nit
"""

class Contact:
    """Represents a Contact class with name and email.
    Responsible for maintaining a list of all contacts in a class
    variable
    """
    all_contacts = []

    def __init__(self, name, email):
        """Method to initialize the Contact instance
        """
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# our Contact and Friend classes have duplicate code to set up the
# name and email properties, this can make maintenance complicated
# as we have to update the code in two or more places
# our Friend class is also neglecting to add itself to the
# all_contacts list we have created on the Contact class

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

# the example gets the instance of the parent object using super
# and calls __init__ on that object
# It then does its own initialization,setting the phone attribute
# super can be called inside any method not just __init__
# call to super can also be made at any point in the method, not 
# necessarily the first line (i.e manipulating the incoming
# parameters before forwarding them to superclass
