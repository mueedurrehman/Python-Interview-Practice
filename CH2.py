
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

test_remove = LinkedList()
test_remove.insert(5)
test_remove.insert(6)
test_remove.remove(5)
test_remove.print_list()

#ToDo: Test this method
def remove_dups_buffer(slist):
    buffer = {}
    current = slist.head
    previous = None
    while current is not None:
        data = current.get_data()
        if data not in buffer:
            buffer[data] = 1
            previous = current
        else:
            previous.set_next(current.get_next())
        current = current.get_next()
    return slist
#Learning. The previous pointer if moved ahead means that we are deleting from the next node onwards. Previous
# should not be moved till you find new data
#Learning: When you need to check for an element's presence, always USE A HASHTABLE!!!
#Do not use lists for this purpose.
#TODO UNDERSTAND THIS. NEED 3 POINTERS TO WORK
def remove_dups_no_buffer(slist):
    searchAhead = slist.head
    current = slist.head
    previous = None
    while current is not None:
        previous = current
        searchAhead = current.get_next()
        data_to_check = current.get_data()
        while searchAhead is not None:
            if searchAhead.get_data() == data_to_check:
                previous.set_next(searchAhead.get_next())
            else:
                previous = searchAhead
            searchAhead = searchAhead.get_next()
        current = current.get_next()
    return slist

#Learning: Removing duplicates is hard. Basically, previous pointer does not move till new data is found as we are skipping
# over all of the repeated data
testList = LinkedList()

testList.insertT(4)
testList.insertT(5)
testList.insertT(4)
testList.insertT(8)
testList.insertT(5)
testList.insertT(6)
testList.insertT(7)

# testList.print_list()
# newList = remove_dups_buffer(testList)
# print("After Remove")
# newList.print_list()


def kth_to_last(slist, k):
    data = []
    current = slist.head
    while current is not None:
        data.append(current.get_data())
        current = current.get_next()
    return data[-k]

#Very Intelligent.
#The issue is that the second last node always points to the last node
#In python, you cannot delete an object that has another reference pointing to it
#The solution is to create new nodes and populate those instead
#Or to simply not let this progress to the last node
#You are setting data, not changing the next pointer
#So the idea is that you continue with this process till you get to the second
#last element to add where you do not move the pointer so you can use the set_next
#method for the last element as the pointer is on the previous node to add in the
#new tail node
def delete_middle_node(node):
    data_left = []
    undeleted_node = node.get_next()
    while undeleted_node is not None:
        data_left.append(undeleted_node.get_data())
        undeleted_node = undeleted_node.get_next()
    total_data = len(data_left)
    for i, data in enumerate(data_left):
        if i < total_data - 2:
            node.set_data(data)
            node = node.get_next()
        elif i == total_data - 2:
            node.set_data(data)
        else:
            tail_node = Node(data)
            node.set_next(tail_node)


#Learning. You often do not pass parameters to methods
#For example, it is node.set_data(data)
#Use setters properly or just use dot notation
#Also see how to use enumerate to go over indices and have the data too
# node1 = Node(6)
# node2 = Node(5)
# node3 = Node(4)
# node4 = Node(3)
# node5 = Node(2)
# node6 = Node(1)
# node7 = Node(0)
# testList2 = LinkedList()
# testList2.insert_node(node1)
# testList2.insert_node(node2)
# testList2.insert_node(node3)
# testList2.insert_node(node4)
# testList2.insert_node(node5)
# testList2.insert_node(node6)
# testList2.insert_node(node7)
# testList2.print_list()
#
# delete_middle_node(node5)
# testList2.print_list()

def partition(slist, x):
    left_partition = []
    right_partition = []
    current = slist.head
    while current is not None:
        data = current.get_data()
        if data < x:
            left_partition.append(data)
        else:
            right_partition.append(data)
        current = current.get_next()
    current = slist.head
    for element in left_partition:
        current.set_data(element)
        current = current.get_next()
    for element in right_partition:
        current.set_data(element)
        current = current.get_next()
    return slist

# partition(testList, 5)
# testList.print_list()

#make sure to account for the leading_zeros case
def list_to_int(l1):
    digits = []
    current = l1.head
    while current is not None:
        digits.append(current.get_data())
        current = current.get_next()
    digits.reverse()
    sum = 0
    multiplier = 1
    leading_zeros = True
    for element in digits:
        if element == 0 and leading_zeros:
            continue
        else:
            sum = sum + (element * multiplier)
            multiplier *= 10
            leading_zeros = False
    return sum

#ToDo test this out with leading zeros
def sum_lists(l1,l2):
    num1 = list_to_int(l1)
    num2 = list_to_int(l2)
    sum = num1 + num2
    sum_string = str(sum)
    digits = [int(x) for x in sum_string]
    out_list = LinkedList()
    for element in digits:
        out_list.insert(element)
    return out_list

# summed = sum_lists(testList,testList)
# summed.print_list()
#Learning: learn the syntax for join. It is used to create a string from a list of strings.
#the itertools one is a list comprehension. You used that again.
#Look at the list comprehensions
#Also note the python map function

def palindrome(l1):
    data = []
    current = l1.head
    even = False
    while current is not None:
        data.append(current.get_data())
        current = current.get_next()
    middle = int(len(data) / 2)
    for index, element in enumerate(data):
        reverse_index = -(index+1)
        if index > middle:
            break
        if element != data[reverse_index]:
            return False
    return True
#Learning: Negative indices in Python Lists are useful
# palL = LinkedList()
# palL.insertT(1)
# palL.insertT(2)
# palL.insertT(3)
# palL.insertT(3)
# palL.insertT(2)
# palL.insertT(1)
# print(palindrome(palL))

def intersection (l1,l2):
    references = {}
    current_2 = l2.head
    while current_2 is not None:
        references[current_2] = 1
        current_2 = current_2.get_next()
    current_1 = l1.head
    while current_1 is not None:
        if current_1 in references:
            return current_1
        current_1 = current_1.get_next()
    return False

# list1 = LinkedList()
# list2 = LinkedList()
# list1.insert(1)
# list1.insert(2)
# nodeInterSect = Node(3)
# list1.insert_node(nodeInterSect)
# list1.insert(4)
# list1.insert(5)
# list2.insert(10)
# list2.insert(11)
# list2.insert_node(nodeInterSect)
# list2.insert(6)
# list2.insert(7)
# list1.print_list()
# list2.print_list()
# i_node =intersection(list1,list2)
# print(i_node.get_data())

#HASHTABLES FOR REFERENCES IS OP!!!
def loop_detection(clist):
    current = clist.head
    references = {}
    while current is not None:
        if current not in references:
            references[current] = 1
            current = current.get_next()
        else:
            return current
    return None

testList = LinkedList()

nodea = Node(3)
nodeb = Node(4)
nodec = Node(5)
testList.insert_node(nodec)
testList.insert_node(nodeb)
testList.insert_node(nodea)
testList.insert(2)
testList.insert(1)
nodec.set_next(nodea)
repeat = loop_detection(testList)
print(repeat.get_data())

