# creating a linked list with four nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node

            for elem in nodes:
                nodes.next = Node(data = elem)
                node = node.next
                return elem

l_list = LinkedList()
print(LinkedList())

first_node = Node("200")
LinkedList().head = first_node

second_node = Node("Lynne")
third_node = Node("611")
fourth_node = Node("Mercy")
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
print(l_list)