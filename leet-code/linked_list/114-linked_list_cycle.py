import unittest

"""Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed 
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
class ListNode:
    """ A node in a singly linked list """
    def __init__(self, x):
        self.val = x
        self.next = None

# My Solution

def has_cycle(head):
    """ Return true if there is a cycle in the linked list. Otherwise, return false """

    # Edge case: If the linked list is empty, then there is no cycle, return False
    if head is None:
        return False
    
    # Otherwise, initialize an empty set to store all the seen nodes
    seen = set()

    # Use variable current to keep track of iteration, initialize it to the head 
    # of the linked list, and add this head node to the seen set
    current = head
    seen.add(head)

    # Keep traversing through the linked list until the end of the list, 
    # if the next node is not seen, add it to the seen set and keep moving
    # otherwise if it is already seen, it means there is cycle, return True
    while current.next:
        if current.next not in seen:
            seen.add(current.next)
            current = current.next
        else:
            return True

    # Get to the end of the linked list and see no cycle -> return False
    return False

#Runtime complexity: O(n)


class MyTestCase(unittest.TestCase):
    """ Unit test """
    def test_llist_cycle(self):
        """ 3 -> 2 -> 0 -> -4 
                 ^          |
                 |----------| """
        
        node1 = ListNode("3")
        node2 = ListNode("2")
        node3 = ListNode("0")
        node4 = ListNode("-4")
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2

        self.assertIs(has_cycle(node1), True)

    def test_empty_llist(self):
        """ Empty linked list """
        node1 = None
        self.assertIs(has_cycle(node1), False)

    def test_one_node(self):
        """ 1 """

        node1 = ListNode("1")

        self.assertIs(has_cycle(node1), False)

    def test_no_cycle(self):
        """ 3 -> 2 -> 0 -> -4 """
        node1 = ListNode("3")
        node2 = ListNode("2")
        node3 = ListNode("0")
        node4 = ListNode("-4")
        node1.next = node2
        node2.next = node3
        node3.next = node4

        self.assertIs(has_cycle(node1), False)

    def test_no_cycle_repeating_value(self):
        """ 3 -> 2 -> 0 -> -4 -> 2 -> 1"""
        node1 = ListNode("3")
        node2 = ListNode("2")
        node3 = ListNode("0")
        node4 = ListNode("-4")
        node5 = ListNode("2")
        node6 = ListNode("1")
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6

        self.assertIs(has_cycle(node1), False)

testclass = unittest.main(exit=False)

if testclass.result.wasSuccessful():
    print("All tests pass -- Nice work!")