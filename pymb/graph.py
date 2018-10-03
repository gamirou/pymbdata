from .linkedlist import LinkedList
from .basetypes.node import Node
from .matrix import Matrix


class Graph:
    """An object that represents a graph with nodes (vertices) and edges
    
    * To insert a node to a graph do:  graph['vertex', key] = data or 
                                       graph['edge', key] = (from, to, distance=optional)
                                       graph['edge', key] = {"from":from, "to":to, "distance":distance},
    * To return a node do: graph['vertex', key] or graph['edge', key],
    * To remove a node do: del graph['vertex', key] or del graph['edge', key],
    * To get all of the vertices, use graph.vertices (list),
    * To get all of the edges, use graph.edges (dictionary),
    * To get the neighbours of a vertex, use graph['vertex', key].neighbours (list of dictionaries with 
    keys: "edge_key" and "vertex_key"),
    """
    
    def __init__(self, type_, size):
        self.size = size
        self.vertices = []

        for i in range(self.size):
            self.vertices.append(Node(key=i, data=None, neighbours=[]))

        self.edges = {}
        self._TYPE = type_

        self.adjacencyList = [None] * self.size
        self.adjacencyMatrix = Matrix(size, size)

    @property
    def TYPE():
        return self._TYPE

    def __len__(self):
        return self.size

    def __setitem__(self, inputs, value):
        """Set an edge or a vertex. 
        from and to need to be the vertices' id
        It should be used as this graph['vertex', key] = data or 
                                  graph['edge', key] = (from, to, distance=optional)
                                  graph['edge', key] = {"from":from, "to":to, "distance":distance}"""
        kind, key = inputs

        # Checks if the input is right
        if kind not in ("edge", "vertex") and key is not None:
            raise ValueError("You need to insert an edge or a vertex.")

        if not isinstance(key, (int, float, str)):
            raise ValueError("Your key needs to be a number or a string.")

        if not isinstance(key, int) and kind == "vertex":
            raise ValueError("Your vertex key needs to be an integer.")

        if kind == "vertex":
            # Insert a vertex
            self.vertices[key].data = value
        elif kind == "edge":
            # First checks for the value arguments
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

            # It is only storing the key to reduce memory waste
            # Neighbours -> {edge_key: edgekey, vertex_key: vertexkey}
            self.vertices[origin].neighbours.append({"edge_key": key, "vertex_key": destination})
            self.vertices[destination].neighbours.append({"edge_key": key, "vertex_key": origin})

            self.edges[key] = Node(key=key, origin=origin, destination=destination, distance=distance)

    def __getitem__(self, args):
        """Returns the whole instance of a node, not just the value"""
        kind, key = args
        if kind not in ("edge", "vertex") and not isinstance(key):
            raise ValueError("The correct format is graph['edge' or 'vertex', id]")

        return self.vertices[key] if kind == "vertex" else self.edges[key]

    def __delitem__(self, args):
        """Deletes a node or an edge"""
        kind, key = args
        if kind not in ("edge", "vertex") and not isinstance(key, (str, int, float)):
            raise ValueError("The correct format is graph['edge' or 'vertex', id]")

        if kind == "edge":
            if key not in self.edges.keys():
                raise ValueError("This edge is not existent")
            
            edge = self.edges[key]

            self.adjacencyMatrix[edge.origin.key][edge.destination.key] = 0
            
            if self._TYPE == "UNDIRECTED":
                self.adjacencyMatrix[edge.destination.key][edge.origin.key] = 0

            # TODO: Delete references inside neighbours lists
            
            for i in range(len(edge.origin.neighbours)):
                if edge.origin.neighbours[i]["edge_key"] == key:
                    del edge.origin.neighbours[i]
                    break
            
            for i in range(len(edge.destination.neighbours)):
                if edge.destination.neighbours[i]["edge_key"] == key:
                    del edge.destination.neighbours[i]
                    break

            del self.edges[key]

        elif kind == "vertex":
            vertex = self.vertices[key]

            if vertex.data is None:
                raise ValueError("This vertex is not existent")

            # Deleting its reference inside neighbours
            for neighbour_key in vertex.neighbours:
                del self.edges[neighbour_key["edge_key"]]
                
                neighbour = self.vertices[neighbour_key["vertex_key"]]
                self.adjacencyMatrix[key][neighbour.key] = 0

                if self._TYPE == "UNDIRECTED":
                    self.adjacencyMatrix[neighbour.key][key] = 0

                for i in range(len(neighbour.neighbours)):
                    if neighbour.neighbours[i]["vertex_key"] == key:
                        del neighbour.neighbours[i]
                        break

            self.vertices[key].data = None
            self.vertices[key].neighbours = []

            if self.adjacencyList[key] is not None:
                self.adjacencyList[key].clear()

    def adjacent(self, origin_key, destination_key):
        """Returns True if there is an edge between origin and destination"""
        neighbours = self.vertices[origin_key].neighbours

        for neighbour in neighbours:
            if neighbours["vertex_key"] == destination_key:
                return True

        return False

    def printList(self):
        """Returns the adjacency list of the graph"""
        string = ""
        for i in range(self.size):
            string += "Adjacency list for vertex {} => {}\n".format(i, self.adjacencyList[i])
        
        return string[:-1]

    def printMatrix(self):
        """Returns the adjacency matrix of the graph"""
        return str(self.adjacencyMatrix)