class graphNode:
    def __init__(self, name, neighbors = []):
        self.name = name
        self.children = neighbors
        self.visited = False

    def insert(self, node):
        self.children.append(node)

# node1 = graphNode("1")
# node2 = graphNode("2")
# node3 = graphNode("3")
# node4 = graphNode("4")
# node5 = graphNode("5")
# node6 = graphNode("6")
# node7 = graphNode("7")
# node1.insert(node2)
# node1.insert(node3)
# node1.insert(node4)
# node2.insert(node4)
# node2.insert(node5)
# node5.insert(node4)
# node5.insert(node7)
# node7.insert(node6)
# node4.insert(node3)
# node4.insert(node6)
# node4.insert(node7)
# node3.insert(node6)

for i in range(3,3):
    print (i)