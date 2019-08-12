class graphNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.visited = False

    def insert(self, node):
        self.children.append(node)

class graph:
    def __init__(self, vertices = None):
        if vertices = None:
            vertices = []
        self.vertices = vertices

    def insert(self, node):
        self.vertices.append(node)

# #ToDo: How to solve this using a graph
# def build_order(projects, dependencies):
#     projs_and_dependents = {}
#     projs_and_dependencies = {}
#     for proj in projects:
#         projs_and_dependents[proj] = []
#         projs_and_dependencies[proj] = []
#     for (proj, dependents) in dependencies:
#         projs_and_dependents[proj].append(dependents)
#     build_order = []
#     valid = False
#     for proj, dependencies in nodes.items():
#         if dependencies == []:
#             valid = True
#             starting = proj
#     if not valid:
#         print("No valid build order")
#For graph, find project with no children. Add to Build order
#Remove from lists of all projects, repeat
#For hash tables, use tables to test no dependencies project
#For that project, search its dependents.
#Remove project from hashtable, see if another project with no dependencies
#Repeat

