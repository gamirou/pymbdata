import pymb

graph = pymb.graph("UNDIRECTED", 5)

graph["vertex", 1] = 45
graph["vertex", 0] = 32

graph["edge", "myedge"] = (0, 1)
print(graph["edge", "myedge"])

print(graph.printMatrix())
print(graph.printList())