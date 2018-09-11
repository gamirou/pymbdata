class MetaAttributeInit(type):
    def __call__(self, *args, **kwargs):
        """ Create a new instance. """

        # First, create the object in the normal default way.
        obj = type.__call__(self, *args)

        # Additionally, set attributes on the new object.
        for name, value in kwargs.items():
            setattr(obj, name, value)

        # Return the new object.
        return obj

class Node(metaclass=MetaAttributeInit):
    """An object that represents nodes in graphs, linked lists and binary trees"""
    def copy(self):
        """Returns a copy of itself"""
        coppied = Node()
        coppied.__dict__ = self.__dict__.copy()
        return coppied

