# Extending built-ins
# What if we wanted to search the contact list by name
# We could add a methos on the Contact class to search it but it
# feels like this method belongs on the list itself


class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value
        in their name.
        """
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    """
    instead of instantiating a normal list as our class variable
    we create a new ContactList class that extends the built-in
    list.
    """
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


if __name__ == '__main__':
    c1 = Contact("John A", "john@example.net")
    c2 = Contact("John B", "johnb@example.net")
    c3 = Contact("Jenna C", "jennac@example.net")

    print([c.name for c in Contact.all_contacts.search('John')])
