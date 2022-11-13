import pydot
import os

# os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz2.38\\bin'

graph = pydot.Dot(graph_type="graph", rankdir="UD")

root = "Pydot"
edge = pydot.Edge(root, "How to install it")
graph.add_edge(edge)

graph.write_png("Hello.png")
os.startfile("Hello.png")