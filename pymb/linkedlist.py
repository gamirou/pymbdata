from node import Node

class LinkedList:
    """An object that behaves like a linked list"""

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def is_empty(self):
        """Returns true if list is empty"""
        return self.head == None

    def find(self, key):
        """Finds a value based on the key"""
        current = self.head

        # Iterates over the list
        while current is not None:
            if current.data[0] == key:
                return current.data[1]

            current = current.next

        return None

    def insert(self, value):
        """Adds a node to the linked list in its corresponding place"""
        if self.find(value) != None:
            print("Your value is already in the list! Use replace() instead!")

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

    def remove(self, value):
        """Removes a value if it is present by the key"""
        current = self.head

        while current != None:
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
            
        
        print("Your item is not present in the list")     

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

    def count(self):
        """Returns the number of elements"""
        # It could be replaced with __len__ as it is more pythonic, but I want to meet the requirements
        length = 0
        current = self.head

        while current is not None:
            length += 1
            current = current.next

        return length

    def __str__(self):
        """Returns a string representation to visualize the linked list"""
        linkedNode = self.head
        sList = ""

        while linkedNode != None:
            sList += "{} => ".format(linkedNode.data)
            linkedNode = linkedNode.next
        
        # sList[:-4] so the last arrow is removed
        return (sList[:-4] if sList != "" else "The linked list is empty")