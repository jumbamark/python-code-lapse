# Implementing your own linked list


# creating a class to represent the linked list (only store where the list starts, the head of the list)
class LinkedList:
    def __init__(self):
        self.head = None

# class to represent each node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None