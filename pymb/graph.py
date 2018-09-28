from .linkedlist import LinkedList
from .basetypes.node import Node
from .matrix import Matrix

# https://en.wikipedia.org/wiki/Graph_%28abstract_data_type%29
# Need to make each vertex a node

class Graph:
    """An object that represents a graph with nodes (vertices) and edges"""
    
    def __init__(self, type_, size):
        self.size = size
        self.vertices = {}
        self.edges = {}
        self._TYPE = type_

        self.adjacencyList = [None] * self.size
        self.adjacencyMatrix = Matrix(size, size)

    @property
    def TYPE():
        return self._TYPE

    def __len__(self):
        return size

    def __setitem__(self, inputs, value):
        """Set an edge or a vertex. 
        from and to need to be the vertices' id
        It should be used as this graph['vertex', key] = data or 
                                  graph['edge', key] = (from, to, distance=optional)
                                  graph['edge', key] = {"from":from, "to":to, "distance":distance}"""
        kind, key = inputs

        if kind not in ("edge", "vertex") and key is not None:
            raise ValueError("You need to insert an edge or a vertex.")

        if not isinstance(key, (int, float, str)):
            raise ValueError("Your key needs to be a number or a string.")

        if not isinstance(key, int) and kind == "vertex":
            raise ValueError("Your vertex key needs to be an integer.")

        if kind == "vertex":
            self.vertices[key] = Node(key=key, data=value, neighbours=[])
        elif kind == "edge":
            if isinstance(value, tuple):
                if len(value) == 2:
                    origin, destination = value
                    distance = 1
                elif len(value) == 3:
                    origin, destination, distance = value
                    if not isinstance(distance, (int, float)):
                        raise ValueError("The distance needs to be a number")
                else:
                    raise ValueError("Your value should be a tuple with from, to and distance(optional); or a dictionary.")
            elif isinstance(value, dict):
                if "from" in value and "to" in value:
                    origin = value["from"]
                    destination = value["to"]
                    distance = value["distance"] if "distance" in value else 1
                else:
                    raise ValueError("Your value should be a tuple with from, to and distance(optional); or a dictionary.")
            else:
                raise ValueError("Your value should be a tuple with from, to and distance(optional); or a dictionary.")

            self.adjacencyMatrix[origin, destination] = distance
                
            if self._TYPE == "UNDIRECTED":
                self.adjacencyMatrix[destination, origin] = distance

            if self.adjacencyList[origin] is None:
                self.adjacencyList[origin] = LinkedList()
            
            self.adjacencyList[origin].append(destination)
            self.edges[key] = Node(origin=origin, destination=destination, distance=distance)

    def __getitem__(self, args):
        kind, key = args
        if kind not in ("edge", "vertex") and not isinstance(key):
            raise ValueError("The correct format is graph['edge' or 'vertex', id]")

        return self.vertices[key] if kind == "vertex" else self.edges[key]
    
    def printList(self):
        string = ""
        for i in range(self.size):
            string += "Adjacency list for vertex {} => {}\n".format(i, self.adjacencyList[i])
        
        return string[:-1]

    def printMatrix(self):
        return str(self.adjacencyMatrix)