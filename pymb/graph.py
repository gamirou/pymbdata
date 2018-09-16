from node import *
from linkedlist import *
from matrix import *

class Graph:
    """An object that represents a graph with nodes (vertices) and edges"""
    
    def __init__(self, *nodes):
        self.adjacencyList = []
        self.adjacencyMatrix = Matrix()