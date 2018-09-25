import pymb

graph = pymb.graph("DIRECTED", 5)

graph["vertex", 1] = 45
graph["vertex", 0] = 32

graph["edge", "myedge"] = (0, 1)
print(graph.vertices)
print(graph.edges)