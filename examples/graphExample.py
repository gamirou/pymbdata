import pymb

graph = pymb.graph("UNDIRECTED", 5)

graph["vertex", 2] = 31
graph["vertex", 1] = 45
graph["vertex", 0] = 32

graph["edge", "myedge"] = (0, 1)
graph["edge", "edge2"] = (1, 2)

print(graph["edge", "myedge"])

del graph["vertex", 0]

print(graph.printList())
print(graph.printMatrix())