from .basetypes.node import Node

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
            self.root = Node(data=value, left=None, right=None, parent=None)
        else:
            self._insert(value, self.root)
        
        self.size += 1

    def _insert(self, value, node):
        if node.data < value:
            if node.right is None:
                node.right = Node(data=value, parent=node, left=None, right=None)
            else:
                self._insert(value, node.right)
        else:
            if node.left is None:
                node.left = Node(data=value, parent=node, left=None, right=None)
            else:
                self._insert(value, node.left)