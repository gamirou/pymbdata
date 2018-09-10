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