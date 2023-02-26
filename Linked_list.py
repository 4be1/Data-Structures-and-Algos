 #Link list Big O
#
# Method 1:  append new node to the end of list
#       It doesn't matter how many nodes we have in the list, the number of operations to add new value to the end is exactly the same
#  BIG O = O(1)


# Method 2:  Remove an item from the end of a linked list
#       Due to pointers in a linked list, we have to iterate through the list until we get to the pointer (pointer for value 7), then we can set tail equal to that pointer
#       Becuase we had to iterate through the whole list BIG O = O(n) 
#  BIG O = O(n)

# Method 3:  Add an item to the front of the Linked list
#      Same number of operations to add an item on to the front of the list (doesn't matter how many items we have in the list)
#  BIG O = O(1)

# Method 4:  Remove an item from the front of the Linked list
#      Same number of operations to remove an item on to the front of the list (doesn't matter how many items we have in the list) 
#  BIG O = O(1)

# Method 5:  Add an item to the middle of a Linked list
#      Start at the head and iterate through the list until we find middle value (23)
#       Becuase we had to iterate through the whole list BIG O = O(n) 
#  BIG O = O(n)

# Method 5:  Remove an item to the middle of a Linked list
#      Start at the head and iterate through the list until we find middle value (23). Set pointer of middle value to next pointer and drop value we are wanting to remove from list
#       Becuase we had to iterate through the whole list BIG O = O(n) 
#  BIG O = O(n)

# Method 6: Looking up by index or looking up by value is BIG O = n



############ What is a Node?##################
# A 'Node' is the value and the pointer. Together these make up the Node
#       
# A Node is essentually a dictionary: **** Below is NOT proper syntax *****
#       e.g. 
#               {
#               "Value": 4,
#               "next": None
#                   }
#
#
# A Linked list is essentually a group of nested dictionaries 
"""    e.g. 
            head = {
            
               "Value": 11,
               "next": {
                        "Value": 3,
                        "next": {
                                "Value": 23,
                                "next":
                        }
                   
                  } 
                   
              }

"""

# print(head['next']['next']['value'])

# This will only run with a Linked List
#print(my_linked_list.head.next.next.value)



########################################################################################################################



# Constructor - Linked List


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)


