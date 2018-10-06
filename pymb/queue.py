class Queue:
    """An object that with basic functionality of a queue (FIFO)
    
    It is very basic, needs improved and increased functionality in the future.

    Methods:
    * To push values, use queue.enqueue(*values),
    * To remove a value, use queue.dequeue(),
    * To get length, use len(queue),
    * To check if it is empty, use queue.is_empty() -> True/False
    """

    def __init__(self):
        self._items = []

    @property
    def items(self):
        raise AttributeError("Queue' object has no attribute 'items'")

    @items.setter
    def items(self, val):
        raise AttributeError("Queue' object has no attribute 'items'")

    def enqueue(self, *values):
        """Pushes items to the queue"""
        for val in values:
            self._items.append(val)

    def dequeue(self):
        """Removes item from the queue"""
        if len(self._items) != 0:
            return self._items.pop(0)
        else:
            print("Your have popped all of the items!")
                
    def __len__(self):
        """Returns the length of the queue"""
        return len(self._items)

    def is_empty(self):
        return self.__len__() == 0

    def __str__(self):
        """Returns the string representation of a queue"""
        strQueue = ""
        for i in self._items:
            strQueue += "{} <= ".format(i)
        
        return (strQueue[:-4] if strQueue != "" else "Empty queue")
