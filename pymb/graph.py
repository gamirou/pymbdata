from .basetypes.node import Node
from .linkedlist import LinkedList
from .matrix import Matrix

class Graph:
    """An object that represents a graph with nodes (vertices) and edges"""
    
    def __init__(self, *nodes):
        self.adjacencyList = LinkedList()
        self.adjacencyMatrix = Matrix()