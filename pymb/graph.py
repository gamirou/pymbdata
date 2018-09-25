from .linkedlist import LinkedList
from .matrix import Matrix

class Graph:
    """An object that represents a graph with nodes (vertices) and edges"""
    
    def __init__(self, type_, size):
        self.size = size
        self.vertices = {}
        self.edges = {}
        self._TYPE = type_

        self.adjacencyList = LinkedList()
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
            self.vertices[key] = value
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

            self.edges[key] = {"from": origin, "to": destination, "distance": distance}

    def __getitem__(self, args):
        kind, key = args
        if kind not in ("edge", "vertex") and not isinstance(key):
            raise ValueError("The correct format is graph['edge' or 'vertex', id]")

        return self.vertices[key] if kind == "vertex" else self.edges[key]
        