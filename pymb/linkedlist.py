from node import Node


class BaseLinkedList:
    """There will be two types of linked lists, sorted and unsorted"""
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def isEmpty(self):
        return self.head == None   
    
    def find(self, value):
        """Finds a value based on the value"""
        current = self.head

        # Iterates over the list
        while current is not None:
            if current.data == value:
                return True

            current = current.next

        return False 

    def remove(self, value):
        """Removes a value if it is present by the key"""
        current = self.head

        while current is not None:
            # If key is found
            if current.data == value:
                # If it is not the head
                if current.prev != None:
                    # Previous node gets its next attribute replaced
                    current.prev.next = current.next
                    
                    # Replaces next previous attribute with the previous node of the key removed
                    if current.next == None:
                        self.tail = current.prev
                    else:
                        current.next.prev = current.prev
                else:
                    # otherwise we have no prev, head is the next one, and prev becomes None
                    self.head = current.next
                    if current.next != None:
                        current.next.prev = None
                
                return
                
            current = current.next
            
        raise KeyError("Your item is not present in the list")
        
    def count(self):
        """Returns the number of elements"""
        # It could be replaced with __len__ as it is more pythonic, but I want to meet the requirements
        length = 0
        current = self.head

        while current is not None:
            length += 1
            current = current.next

        return length

class LinkedList(BaseLinkedList):
    """An object that behaves like a linked list. It is sorted, unlike normal linked lists"""

    def __init__(self, head = None, tail = None):
        super().__init__(head, tail)

    def append(self, value):
        """Adds a node to the linked list at the end"""
        self.value

    def prepend(self, value):
        """Adds a node to the linked list at the start"""
        pass

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