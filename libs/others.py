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

class BinaryNode:
    """A node similar to the linked list, but it has left and right attributes"""

    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=" -- ")
        if self.right:
            self.right.printTree()

class BST:
    """A simple class that represents a binary search tree"""

    def __init__(self, dataType=None):
        self.root = None
        self.size = 0
        self.dataType = dataType

    def insert(self, value):
        if not isinstance(value, self.dataType):
            print("Value inserted is not the accepted data type. it should be {}".format(self.dataType))
            return

        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self._insert(value, self.root)
        
        self.size += 1

    def _insert(self, value, node):
        if node.data < value:
            if node.right is None:
                node.right = BinaryNode(value, node)
            else:
                self._insert(value, node.right)
        else:
            if node.left is None:
                node.left = BinaryNode(value, node)
            else:
                self._insert(value, node.left)

    def showSorted(self):
        print("Binary Tree's nodes in order:")
        print("-- ", end="")
        self.root.printTree()