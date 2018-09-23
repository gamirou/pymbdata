from .linkedlist import LinkedList
from .matrix import Matrix

class Graph:
    """An object that represents a graph with nodes (vertices) and edges"""
    
    def __init__(self, size):
        self.size = size
        self.vertices = {}
        self.edges = {}

        self.adjacencyList = LinkedList()
        self.adjacencyMatrix = Matrix(size, size)

    def __len__(self):
        return size

    def __setitem__(self, args, value):
        """Set an edge or a vertex. 
        It should be used as this graph['vertex', key] or 
                                  graph['edge', key] = (from, to, distance=optional)"""
        kind, item = args

        if kind not in ("edge", "vertex") and item is not None:
            raise ValueError("You need to insert an edge or a vertex.")

        if kind == "vertex":
            if isinstance(item, tuple) and len(item) == 1:
                #######################
                key = item[0]
                self.vertices[key] = value
            else:
                raise ValueError("The correct format is graph['vertex', key] = value")
        """else:

                self.adjacencyMatrix[origin][destination] = distance
                #TODO: Don't add this in directed graphs
                self.adjacencyMatrix[destination][origin] = distance

                self.edges[key] = {origin: origin, destination: destination, distance: distance}
            else:
                raise ValueError("The correct format is graph['edge', (key, from, to, distance=optional)]")
        """


    def __getitem__(self, args):
        kind, key = args
        if kind not in ("edge", "vertex") and not isinstance(key):
            raise ValueError("The correct format is graph['edge' or 'vertex', id]")

        return self.vertices[key] if kind == "vertex" else self.edges[key]
        