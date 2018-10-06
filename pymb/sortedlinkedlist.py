from .basetypes.node import Node
from .basetypes.abstractlist import BaseLinkedList


class SortedLinkedList(BaseLinkedList):
    """An object that behaves like a linked list. It is sorted, unlike normal linked lists"""

    def __init__(self, head = None, tail = None):
        super().__init__(head, tail)

    def getForHash(self, key):
        """Returns the value based on key (only hash tables)"""
        current = self.head

        # Iterates over the list
        while current is not None:
            if current.data[0] == key:
                return True

            current = current.next

        return False

    def insert(self, value):
        """Adds a node to the linked list in its corresponding place"""
        if self.find(value):
            raise ValueError("Your value is already in the list! Use replace() instead!")

        # Checks if list is empty
        current = self.head
        if current is None:
            self.head = self.tail = Node(data=value, next=None, prev=None)
            return
    
        # If the value is smaller than the head
        if current.data > value:
            # If there is a single item
            if self.tail == self.head:
                self.head = Node(data = value, prev = None, next = current)
                self.tail = Node(data = current.data, prev = self.head, next = None)
                current = self.tail
            else:
                current = self.head
                self.head = Node(data = value, prev = None, next = current)
            return

        # If it is in the middle or at the end
        while current.next is not None:
            if current.next.data > value:
                break
            current = current.next

        # Found the correct place
        newNode = Node(data=value, prev=current, next=current.next)
        current.next = newNode
        
        # If it is the tail, don't change previous attribute
        if current.next.next != None:
            current.next.next.prev = newNode     

    def removeByKey(self, key):
        """Removes a node by its key (only hash tables)"""
        current=self.head

        while current != None:
            if current.data[0] == key:
                self.remove(current.data)
                return

            current=current.next
        
        raise KeyError("Value not present")

    def merge(self, other, **kwargs):
        """Merges two linked lists together"""
        merged = SortedLinkedList()
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
            
            if "isHash" in kwargs:
                # Otherwise checks if the keys are the same
                if list1.head.data[0] == list2.head.data[0]:
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
            else:
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
        result = SortedLinkedList(self.head, self.tail)
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
        
        # sList[:-4] so the last arrow is removed
        return (string[:-4] if sList != "" else "The sorted linked list is empty")