class Stack:
    """An object that with basic functionality of a stack (LIFO)"""

    def __init__(self):
        self.items = []

    def push(self, *values):
        """Pushes items to the stack"""
        for val in values:
            self.items.append(val)

    def pop(self):
        """Removes last item from the stack"""
        if len(self.items) != 0:
            return self.items.pop(-1)
        else:
            print("Your have popped all of the items!")

    def __len__(self):
        """Returns the length of the stack"""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of a stack"""
        strStack = ""
        for i in self.items:
            strStack += "{} => ".format(i)
        
        return (strStack[:-4] if strStack != "" else "Empty stack")