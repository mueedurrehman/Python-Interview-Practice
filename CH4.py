#Chapter 4: Trees and Graphs
class t_node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
#Learning: Calling function in the same class, need to use self.function()
#Learning: Order traversals require a separate tree parameter to check for not None OBJECT condition
#Note you may have an object with None properties but still created object
def in_order_traversal(tree, func):
    res = []
    if tree is not None:
        res = in_order_traversal(tree.left, func)
        res.append(func(tree.data))
        res = res + in_order_traversal(tree.right, func)
    return res

def post_order_traversal(tree, func):
    res = []
    if tree is not None:
        res = post_order_traversal(tree.left, func)
        res = res + post_order_traversal(tree.right, func)
        res.append(tree.data)
    return res

def pre_order_traversal(tree, func):
    res = []
    if tree is not None:
        res.append(func(tree.data))
        res = pre_order_traversal(tree.left, func)
        res = res + pre_order_traversal(tree.right, func)
    return res
#Learning on implementing tree order traversal for classes
#ToDo: Revise how to construct a minHeap and a maxHeap
#Used the Java implementation taught in 2110
class min_heap:
    def __init__(self, items = []):
        self.heap = items
        for item in items:
            self.heap.append(item)
            self.__bubble_up(len(self.heap) - 1)

    def size(self):
        return len (self.heap)
    def parent(index):
        return (index - 1) // 2

    def left_child(index):
        return index * 2 + 1

    def right_child(index):
        return index * 2 +2

    def push(self, data):
        self.heap.append(data)
        self.__bubble_up(len(self.heap) - 1)

    def peek (self):
        if len(self.heap) >= 1:
            return self.heap[0]
        else:
            return False

    def pop(self):
        items = len(self.heap)
        if items > 1:
            self.__swap(0, len(self.heap) - 1)
            min = self.heap.pop()
            self.__bubbleDown()
        elif items == 1:
            min = self.heap.pop()
        else:
            min = False
        return min

    def __float_up(self, index):
        parent = self.parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            index = parent
            parent = self.parent(index)

    # def __float_up(self, index):
    #     parent = (index - 1) // 2
    #     if index <= 0:
    #         return
    #     elif self.heap[index] > self.heap[parent]:
    #         self.__swap(index, parent)
    #         self.__float_up(parent)

    def __swap(self, i, j):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def biggerChild(self, index):
        largest = 2 * index + 2
        if largest >= self.size() or self.heap[largest - 1] > self.heap[largest]: #taking advantage of short circuit
            largest -= 1
        return largest

    def __bubbleDown(self, index):
        parent = 0
        child = self.biggerChild(parent)
        size = self.size()
        while child < size and self.heap[parent] > self.heap[child]:
            self.swap(child, parent)
            parent = child
            child = self.biggerChild(parent)

#Efficient space, acceptable time complexity
#Hash Table has high space usage, low time usage
class trie:

    def __init__(self):
        self.head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True

class graphNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.visited = False

    def insert(self, node):
        self.children.append(node)

class graph:
    def __init__(self, vertices):
        self.vertices = vertices

    def insert(self, node):
        self.vertices.append(node)

#ToDo: Practice implementing this again
def find_route(tar_graph, nodea, nodeb):
    assert nodea != nodeb, "Nodes must be different"
    target = None
    destination = None
    for node in tar_graph.vertices:
        if node.name == nodea:
            target = node
        if node.name == nodeb:
            destination = node
        if target is not None and destination is not None:
            break
    route_exists(target, destination)
    if destination.visited:
        print("A route exists")
    else:
        print("There is no route")
    graph_reset(tar_graph)

def graph_reset(graph):
    for node in graph.vertices:
        node.visited = False

def route_exists(tar, dest):
    tar.visited = True
    if dest.visited:
        return
    for node in tar.children:
        if not node.visited:
            route_exists(node, dest)
#Learning. Python functions return None by default
#Whether there is just return or no return, in both cases
#Using isinstance(obj, class)

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
# test_1 = graph([node1, node2, node3, node4, node5, node6, node7])
# find_route(test_1, "4", "2")
#Learning: Default mutable arguments
#Passing in a list means the same list reference is given to each object
#So that same list kept on getting incremented

#Terminating DFS early. Monitor for visited property change, return on that
#Then in the main loop, check the visited property
#Reset the visited properties for the graphs when you are done

# class vertex:
#     def __init__(self, name):
#         self.name = name
#         self.neighbors = []
#
#     def add_neighbor(self, v):

#Implement DFS and BFS
# https://www.youtube.com/watch?v=QVcsSaGeSH0

#ToDo: practice building a tree again. Super hard
#Learning: Need to carry out the operation by instantiating new leaves
#Make sure to slice the arrays correctly
#Should only instantiate new tree objects if the array for them is non empty
def min_tree(array, tree):
    items = len(array)
    if array == []:
        return
    midpoint = items // 2
    tree.data = array[midpoint]
    left_array = array[:midpoint]
    right_array = array[midpoint + 1:] #important for slicing
    if left_array != []:
        tree.left = t_node()
        min_tree(left_array, tree.left)
    if right_array != []:
        tree.right = t_node()
        min_tree(right_array, tree.right)

tree = t_node()
array = [1,2,3,4,5,6,7]
min_tree(array, tree)
in_order_traversal(tree, print)

#ToDo: Implement Binary Search Tree
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_data(self,data):
        self.data = data

    def add_data(self,data):
        node = Node()
        node.data = data
        self.next = node

    def set_next(self,node):
        self.next = node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

#Learnings
#Use setter methods and not dot notation
class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node

    def insert_node(self, node):
        node.set_next(self.head)
        self.head = node

    def insertT(self, data):
        node = Node(data)
        current = self.head
        if current is not None:
            current = self.head
            next = current.get_next()
            while next is not None:
                current = next
                next = current.get_next()
            current.set_next(node)
        else:
            self.head = node

    def remove(self,data):
        current = self.head
        previous = None
        found = False
        while current and not found: #Search till not found AND list not empty
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found and previous is not None: #data is not in head
            previous.set_next(current.get_next())
            return True
        elif found: #must be head
            self.head = current.get_next()
            return True
        else:
            return False #data not found

    def print_list(self):
        current = self.head
        while current is not None:
            print (current.data)
            current = current.get_next()

def list_of_depths(btree):
    nodes_with_depths = get_all_nodes_with_depths (btree, 0)
    max_depth = max(nodes_with_depths, key = lambda x: x[1]) #Pattern matching basically
    #Note above will still get the max tuple element
    lists = []
    for i in range(max_depth[1] + 1): #Need + 1 as need to index to +2
        lists.append(LinkedList())
    for node, depth in nodes_with_depths:
        lists[depth].insert(node)
    return lists


def get_all_nodes_with_depths(btree, depth):
    nodes = []
    if btree:
        nodes = get_all_nodes_with_depths(btree.left, depth + 1)
        nodes.append((btree, depth))
        nodes = nodes + get_all_nodes_with_depths(btree.right, depth + 1)
    return nodes

# list = list_of_depths(tree)
# print("Done Testing")
#Note condition. Balanced tree must be between 2^h-1<=n<2^h nodes
def check_balanced(tree):
    tree_height = height(tree, 0)
    total_nodes = count_nodes(tree)
    if total_nodes >= 2**(tree_height-1) and total_nodes < 2**tree_height:
        return True
    else:
        return False

def count_nodes(tree):
    return len (in_order_traversal(tree, lambda x: x))

def height(tree, accu):
    if tree is None:
        return accu
    else:
        height_left = height(tree.left, accu + 1)
        height_right = height(tree.right, accu + 1)
        return max(height_left, height_right)

# print(check_balanced(tree))
tree1 = t_node(1)
tree2 = t_node(2)
tree3 = t_node(3)
tree4 = t_node(4)
tree5 = t_node(5)
tree6 = t_node(6)
tree7 = t_node(7)
tree1.left = tree2
tree2.left = tree3
tree1.right = tree4
tree4.right = tree5
tree5.right = tree6
tree6.right = tree7
# print(check_balanced(tree1))

def validate_bst_v1(tree):
    ascending_test = in_order_traversal(tree, lambda x:x)
    ascending = sorted(ascending_test) #.sort() would return None so does not work. Use sorted() for assignment
    if ascending_test == ascending:
        return True
    else:
        return False

def validate_bst(tree):
    if tree is None:
        return True
    data = tree.data
    data_min = tree.data + 1
    data_max = tree.data - 1
    return rec_checker_left(tree.left, data_max) and \
           rec_checker_right (tree.right, data_min)

def rec_checker_left(tree, maximum):
    if tree is None:
        return True
    data = tree.data
    if data <= maximum:
        return rec_checker_left(tree.left, data - 1) and rec_checker_left(tree.left, data + 1)
    else:
        return False

def rec_checker_right(tree, minimum):
    if tree is None:
        return True
    data = tree.data #if and elif cannot be broken. Second if must be separate
    if data >= minimum:
        return rec_checker_left(tree.left, data - 1) and rec_checker_right(tree.right, data + 1)
    else:
        return False
#Learning: Your in order traversal method is very powerful. Remember that
#Recursive algorithms need more practice. Remember that each branching if needs to be a return
print("Testing v1")
print(validate_bst_v1(tree))
print(validate_bst_v1(tree1))
print("Testing rec")
print(validate_bst(tree))
print(validate_bst(tree1))

class tp_node():
    def __init__(self, data = None, left = None, right = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def insert_left(self, tree):
        tree.parent = self
        self.left = tree

    def insert_right (self, tree):
        tree.parent = self
        self.right = tree

#ToDo: Reattempt again. Reasoned properly. Should be able to implement again.
def successor(node):
    if node.right is None:
        parent = node.parent
        while parent.left is not node and parent is not None:
            node = node.parent
            parent = node.parent
        return parent
    else:
        target = node.right
        while target.left is not None:
            target = target.left
        return target
    return None
#Learning, leftmost node of right subtree is successor
#Or if no right tree, travel up to find the node, which is the left child of its parent

# tree_test = tp_node()
# tree_test.data = 2
# tree_test.left = tp_node(1)
# tree_parent = tp_node(3.5)
# tree_parent.left = tp_node(1.8)
# tree_parent.left.parent = tree_parent
# tree_parent.left.right = tp_node(1.9)
# tree_parent.left.right.parent = tree_parent.left
# tree_parent.left.right.right = tree_test
# tree_test.parent = tree_parent.left.right
# print(successor(tree_test).data)

def build_order(projects, dependencies):
    nodes = []
    for item in projects:
        graph_node
