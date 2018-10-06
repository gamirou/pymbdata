class Stack:
    """An object that with basic functionality of a stack (LIFO)
    
    It is very basic, needs improved and increased functionality in the future.

    Methods:
    * To push values, use stack.push(*values),
    * To remove a value, use stack.pop(),
    * To get length, use len(stack),
    * To check if it is empty, use stack.is_empty() -> True/False
    """

    def __init__(self):
        self._items = []

    @property
    def items(self):
        raise AttributeError("Stack' object has no attribute 'items'")

    @items.setter
    def items(self, val):
        raise AttributeError("Stack' object has no attribute 'items'")

    def push(self, *values):
        """Pushes items to the stack"""
        for val in values:
            self._items.append(val)

    def pop(self):
        """Removes last item from the stack"""
        if len(self._items) != 0:
            return self._items.pop(-1)
        else:
            print("Your have popped all of the items!")

    def __len__(self):
        """Returns the length of the stack"""
        return len(self._items)

    def is_empty(self):
        """Returns True or False if it is empty or not"""
        return self.__len__() == 0

    def __str__(self):
        """Returns the string representation of a stack"""
        strStack = ""
        for i in self._items:
            strStack += "{} => ".format(i)
        
        return (strStack[:-4] if strStack != "" else "Empty stack")