# Data Structures Practice


#linked List

class sNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, nextNode):
        self.next = nextNode

# class LinkedList:
#     def __init__(self, head = None):
#         self.head = head
#
#     def insert(self, data):
#         newNode = SNode(data)
#         newNode.set_next(self.head)
#         self.head = newNode
#
#     def size(self):
#         current = self.head
#         count = 0
#         while (current):
#             count += 1
#             current = self.next
#         return count
#
#     def search(self,data):
#         current = self.head
#         while current:
#             if current.get_data() == data:
#                 return current
#             else:
#                 current = current.get_next()
#         raise ValueError ("Data not in list")
#
#     def delete(self, data):
#         previous = None
#         current = self.head
#         found = False
#         while current and (not found):
#             if current.get_data() == data:
#                 found = True
#             else:
#                 previous = current
#                 current = current.get_next()
#         if current == None:
#             raise ValueError ("Data not in the list")
#         if previous == None:
#             self.head = current.get_next()
#         else:
#             previous.set_next(current.get_next())
#
#     def printList(self):
#         current = self.head
#         while current:
#             print (current.get_data())
#             current = current.get_next()


# node1 = SNode(1)
# node2 = SNode(2)
# node3 = SNode(3)
# LL1 = LinkedList()
# LL1.insert(1)
# LL1.insert(2)
# LL1.insert(3)
# LL1.printList()
# LL1.delete(3)
# LL1.delete(1)
# LL1.delete(2)
# LL1.printList()
#
# print(node3)

class SLinkedList:

    def __init__ (self, head = None):
        self.head = head
        if head == None:
            self.size = 0
        else:
            self.size = 1

    def get_size (self):
        return self.size

    def add (self, data):
        new_node = sNode(data)
        self.head = new_node
        self.head.set_next(new_node)
        self.size += 1

    def add_node (self, new_node):
        new_node.set_next(self.head)
        self.head = new_node
        self.size +=1

    def remove (self, data):
        current = self.head
        previous = None
        while (current):
            if current.get_data() == data:
                if previous:
                    previous.set_next(current.get_next())
                else:
                    self.head = current.get_next()
                    self.size -= 1
                    return True
            else:
                previous = current
                current = current.get_next()
        return False

    def search (self, data):
        current = self.head
        while current:
            if current.get_data() == self.data:
                return current
            else:
                current = current.get_next()
        return None

# add sorting function https://github.com/joeyajames/Python/blob/master/LinkedLists/LinkedList1.py


class dNode:

    def __init__(self, data, next = None, prev = None):
        self.val = data
        self.next = next
        self.prev = prev

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, next_node):
        self.next = next_node

    def set_prev(self, prev_node):
        self.prev = prev_node

    def self_data(self, data):
        self.val = data

    def get_data(self):
        return self.val

    def has_next(self):
        if self.get_next() == None:
            return False
        else:
            return True

class DLinkedList:
    def __init__(self, node = None):
        self.head = node
        self.tail = node
        if node is None:
            self.size = 0
        else:
            self.size = 1

    def get_size(self):
        return self.size

    def add (self, d):
        if self.size == 0:
            node = dNode(d)
            self.head = node
            self.tail = node
        else:
            node = dNode(d, self.head)
            self.head.set_prev(node)
            self.head = node
        self.size +=1

    def remove (self, data):
        current = self.head
        while current is not None:
            if current.get_data() == data:
                if current.get_prev () is not None: #deleting middle node
                    if current.has_next():
                        current.get_prev().set_next(current.get_next())
                        current.get_next.set_prev(current.get_prev())
                    else: #deleting tail
                        current.get_prev.set_next(None)
                        self.tail = current.get_prev()
                else: #deleting head
                    self.head = current.get_next()
                    self.head.set_prev(None) #on github set to head but makes no sense
                self.size -=1
                return True
            else:
                current = current.get_next()
        return False

    def find(self, d):
        current = self.head
        while current is not None:
            if current.get_data() == d:
                return current
            else:
                current = current.get_next()
        return False





