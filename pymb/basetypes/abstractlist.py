from .node import Node


class BaseLinkedList:
    """There will be two types of linked lists, sorted and unsorted"""
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def clear(self):
        self.head = Node(data=None, next=None, prev=None)
        self.tail = self.head.copy()

    def is_empty(self):
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

    def replace(self, old, new):
        """Replaces a node with a new one"""
        current=self.head

        while current is not None:
            if current.data == old:
                current.data = new
            
            current=current.next

        raise ValueError("{} is not present".format(old))