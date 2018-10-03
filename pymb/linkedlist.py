from .basetypes.node import Node
from .basetypes.abstractlist import BaseLinkedList


class LinkedList(BaseLinkedList):
    """An object that behaves like a linked list. It is sorted, unlike normal linked lists"""

    def __init__(self, head = None, tail = None):
        super().__init__(head, tail)

    def prepend(self, value):
        """Adds a node to the linked list at the start"""
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
        list1 = self.copy()
        list2 = other.copy()

        while list1.head != None or list2.head != None:
            # If one list is empty, insert the remaining items from the other list
            if list1.head == None:
                merged.insert(list2.head.data)
                list2.remove(list2.head.data)
                continue
            elif list2.head == None:
                merged.insert(list1.head.data)
                list1.remove(list1.head.data)
                continue

            # Otherwise checks if the keys are the same
            if list1.head.data == list2.head.data:
                # Overwrites second list's value because it is the argument, not the instance
                merged.insert(list1.head.data)

                list1.remove(list1.head.data)
                list2.remove(list2.head.data)
            else:
                # Minimum value inserted
                if list1.head.data < list2.head.data:
                    merged.insert(list1.head.data)
                    list1.remove(list1.head.data)
                else:
                    merged.insert(list2.head.data)
                    list2.remove(list2.head.data)

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
        sList = ""

        while linkedNode != None:
            sList += "{} => ".format(linkedNode.data)
            linkedNode = linkedNode.next
        
        # sList[:-4] so the last arrow is removed
        return (sList[:-4] if sList != "" else "The linked list is empty")