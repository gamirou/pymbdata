from .basetypes.node import Node
from .basetypes.abstractlist import BaseLinkedList

# Will use for future functionality
# https://www.geeksforgeeks.org/data-structures/linked-list/#doublyLinkedList

class LinkedList(BaseLinkedList):
    """An object that behaves like a linked list"""

    def __init__(self, head = None, tail = None):
        super().__init__(head, tail)

    def prepend(self, value):
        """Adds a node to the linked list at the start"""
        if self.head is None:
            self.head = self.tail = Node(data=value, next=None, prev=None)
            return

        self.head.prev = Node(data=value, next=self.head, prev=None)
        self.head = self.head.prev

    def append(self, value):
        """Adds a node to the linked list at the end"""
        if self.head is None:
            self.head = self.tail = Node(data=value, next=None, prev=None)
            return
        
        self.tail.next = Node(data=value, next=None, prev=self.tail)
        self.tail = self.tail.next

    def merge(self, other):
        """Merges two linked lists together"""
        merged = LinkedList()
        current = self.head

        if self.is_empty():
            return other.copy()
        elif other.is_empty():
            return self.copy()

        while current is not None:
            merged.insert(current.data)
            current = current.next

            if current is None:
                current = other.head

        return merged

    def copy(self):
        """Returns a copy of itself"""
        result = LinkedList(self.head, self.tail)
        oldCurrent = self.head
        resCurrent = result.head

        while oldCurrent is not None:
            resCurrent = oldCurrent.copy()

            oldCurrent = oldCurrent.next
            resCurrent = resCurrent.next

        return result

    def __str__(self):
        """Returns a string representation to visualize the linked list"""
        linkedNode = self.head
        string = ""

        while linkedNode != None:
            string += "{} => ".format(linkedNode.data)
            linkedNode = linkedNode.next
        
        # string[:-4] so the last arrow is removed
        return (string[:-4] if string != "" else "The linked list is empty")