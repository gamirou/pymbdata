class Node:
    """An object that represents nodes in graphs, linked lists and binary trees"""
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def copy(self):
        """Returns a copy of itself"""
        coppied = Node()
        coppied.__dict__ = self.__dict__.copy()
        return coppied

    def __str__(self):
        string = ""

        for i in self.__dict__:
            string += "Attribute {0} is {1};\n".format(i, self.__dict__[i])

        return string[:-1]