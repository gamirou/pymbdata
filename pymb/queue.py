class Queue:
    """An object that with basic functionality of a queue (FIFO)"""

    def __init__(self):
        self.items = []

    def enqueue(self, *values):
        """Pushes items to the queue"""
        for val in values:
            self.items.append(val)

    def dequeue(self):
        """Removes item from the queue"""
        if len(self.items) != 0:
            return self.items.pop(0)
        else:
            print("Your have popped all of the items!")
                
    def __len__(self):
        """Returns the length of the queue"""
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

    def __str__(self):
        """Returns the string representation of a queue"""
        strQueue = ""
        for i in self.items:
            strQueue += "{} <= ".format(i)
        
        return (strQueue[:-4] if strQueue != "" else "Empty queue")
