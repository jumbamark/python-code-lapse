# Linked lists are ordered collections of objects, what's different is how data is stored in memory
# With a list pointers to the objects are stored sequentially in a contiguous block of memory
# Because the pointers that make up the underlying array in a list are all stored sequentially in a contiguous block of memory we don't need to traverse or step past previous elements to access the one we want; if we want to get the element at list index 2 we can just jump right there and follow the pointer to access the data (we don't have to step past index 0 and 1 first)
# The ability to jump to any random memory is called random access


# Linked lists work differently, they are made up of nodes
# Every node stores not only some data but also a pointer to the next node in the linked list
# A special head pointer stores a reference to the first node in the list, the last pointer points to None since there are no more nodes
# Nodes in a list don't have to be stored sequentially in a contiguous block of memory they can be scattered

# Big O Notation
# used to describe the performance of an algorithm in the worst case scenario (scenario where the algorithm runs the slowest)
# Allows us to compare different algorithms or operations on different data structures, so we can decide what data structure best fits our need
# i.e some operations like inserting an element or searching for one might be faster with an array than a linked list
# Big O Notation gives us a way to describe roughly how long an operation will take

# There are many time complexities but in this context we use O(1) and O(n)
# O(1) - constant time (will take the same amount of time to complete regardless of the number of elements in the collection)
#      - considered the fastest time complexity but it is not always achievable  
# O(N) - linear time (the time the algorithm takes to complete scales with how many elements are in the collection, the more elements the slower)
#      - If your algorithm involves iterating through an entire collection once such as with a for loop that's a good sign that its an O(N) algo

# Lists vs Linked Lists
# In the default implementation of python called CPython, lists are represented as an array of objects in memory
# Bec arrays are stored in sequential contiguous blocks of memory they support random access this means we can access any element by its index in O(1) or constant time
# C arrays have some fundamental differences from python lists, the important one in this context is that arrays cannot grow or shrink like a list can
# You cannot simply add a new object to the end of an array that is already full instead you have to recreate the entire array allocating more or less space as needed. This happens behind the scenes so that your python list can grow or shrink without the python developer having t worry about memory management. You don't have to think about allocating new space to the array that represents your list
# CPython automatically resizes underlying arrays that make up python lists when it determines it needs to. It typically allocates more space than needed when this happens so that the next few append operations don't require further resizing. In fact resizing happens so infrequently that we say the time complexity of an append operation on a list is O(1). Explains why accessing elements in a list and appending new ones is a constant time operation.
# Where things fall a part is when trying to insert new items into the list anywhere else, inserting at the end(appending is an O(1) operation)
# Inserting anywhere in the middle or at the beginning is an O(N) operation where N is the number of elements in the list. The amount of time the operation takes depends on how many elements are in the list bec every element after the desired new location for the new item must be pushed down by one addres to make space for the new one then the new element can be added (the slowest scenario therefore will be inserting at the beginning of a list)
# Lists are therefore great when we quickly need to obtain items at a specific index or when we need to append new items to the end but they start to slow down when inserting somewhere in the middle or at the beginning

# Linked lists are not represented by C arrays under the hood, Nodes are simply stored in sections of random memory with that section of random memory containing a pointer to the data stored in that node and a pointer to the next node in the linked list
# Nodes are just objects in memory with an instance attribute for the data and an instance attribute that acts as a pointer to the next node
# These nodes are often created from a class or a data class, bec no arrays are involved lists don't suffer from the same limitations as arrays such as needing to be resized. they really just a series of random objects in memory pointing to one another
# Where linked lists shine is inserting elements at the beginning or the end

# If you wanna insert a new node at the beginning all I have to do is create the new node, redirect the "Next" attribute to the previous head and change the head to point to the new node (no resizing or touching most of the other nodes)
# Adding at the end however requires traversing through the entire linked list until I reach the entire end node and the create a new Node and then point the previous end node to it and make the new node point to None
# The time it takes to traverse the linked list grows with the number of elements so accessing elements is an O(N) operation
# The reason why its quick to insert new nodes at the end is because it's common to store a separate pointer to the end node of a linked list so you don't have to keep traversing the whole thing every time
# The processing of creating a new node and redirecting pointers is always an O(1) operation
# Linked list dont require resizing so we dont suffer the performance penalty associated with resizing