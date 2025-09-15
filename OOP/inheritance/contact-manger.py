"""
Module with a simple contact manager that tracks the name
and email address of several people.
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


# What if our contacts are also suppliers that we need to order from?
# We could add an order "method" but that would allow people to
# accidentally order things from contacts who are customers or family
# friends

"""Supplier class that acts like a Contact but has
but has an additional order method.
"""
class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send "
              "{} order to {}".format(order, self.name))


if __name__ == "__main__":
    c = Contact("Some Body", "somebody@example.net")
    s = Supplier("Sup Plier", "supplier@example.net")
    print(c.name, c.email, s.name, s.email)
    print()
    print(c.all_contacts)
    print("--------")
    try:
        print(c.order("I need pliers"))
    except:
        print("'Contact' object has no attribute 'order'")
    print()
    print(s.order("I need pliers"))

# Our Supplier class can do everything a Contact can do including adding itself to the list of all_contacts

# Extending built-ins
# What if we wanted to search the contact list by name
# We could add a methos on the Contact class to search it but it
# feels like this method belongs on the list itself
