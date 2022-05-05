# creating a linked list with four nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

l_list = LinkedList()
print(l_list)

first_node = Node("200")
l_list.head = first_node

second_node = Node("Lynne")
third_node = Node("611")
fourth_node = Node("Mercy")
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
print(l_list)