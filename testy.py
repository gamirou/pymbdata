import pymb

graph = pymb.graph(5)

graph["vertex", 1] = 45
graph["vertex", 0] = 32

graph["edge", "myedge"] = (0, 1)
print(graph["edge", "myedge"])

del graph["vertex", 0]

print(graph.print_list())
print(graph.print_matrix())