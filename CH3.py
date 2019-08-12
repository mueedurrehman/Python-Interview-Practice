
class stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Empty Stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def size(self):
        return len (self.items)

    def print_stack(self):
        for item in self.items:
            print (item, end = ", ")

    def push_multiple(self, item_list):
        self.items = self.items + item_list

    def pop_multiple(self, number):
        required_items = self.items[-number:]
        required_items.reverse() #So we are returning in stack order
        self.items = self.items[:len(self.items) - number]
        return required_items

    def print_stack(self):
        for item in self.items:
            print(item, end = ", ")
#Learning: Getting the last k items from a list and indexing for that
#Getting the len - k items from a list
class queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(item)

    def dequeue(self, item):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Empty Queue")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def print_queue(self):
        for item in self.items:
            print (item, end = ", ")

#Learning. Improved printing function by using end =", "
def balanced_parentheses(string):
    bracket_stack = stack()
    for paren in string:
            if paren == "(" or paren == "[" or paren == "{":
                bracket_stack.push(paren)
            else:
                if paren == "]" or paren == ")" or paren == "}":
                    try:
                        paren_f = bracket_stack.pop()
                        if paren == "]" and paren_f != "[":
                            return False
                        elif paren == ")" and paren_f != "(":
                            return False
                        elif paren == "}" and paren_f != "{":
                            return False
                    except:
                        return False
    if bracket_stack.size() != 0:
        return False
    else:
        return True

#Learning: For your own classes, you need your own size as len() will not work
# print (balanced_parentheses("(()()(()"))

#Learning:
#import collections
# dQueue = collections.deque([1,2,3])
# pop, popleft, append, appendleft, reverse, efficient both sided operation

#3.1: Single Array, 3 Stacks: Keep 3 pointers along the array. If pointer pushes against another,
#move everything in the array 10 steps down and continue
#3.2 Stack Min: Keep another stack pointer for the minimum. When an item is added
# compare it to the element at the current minimum and move the pointer if needed
#3.3: Stack of Plates

#ToDo: Test
#ToDo: + see if popat requires the next push to happen at that stack that you popped from

class set_of_stacks:

    def __init__(self):
        init_stack = stack()
        self.stacks = [init_stack]
        self.threshold = 3
        self.cur = 0

    def push(self, item):
        cur_stack = self.stacks[self.cur]
        if cur_stack.size() < self.threshold:
            cur_stack.push(item)
        else:
            new_stack = stack()
            new_stack.push(item)
            self.stacks.append(new_stack)
            self.cur +=1

    def pop(self):
        cur_stack = self.stacks[self.cur]
        item = cur_stack.pop()
        if cur_stack.size() == 0:
            self.stacks.remove(cur_stack)
            self.cur -=1
        return item

    def pop_at(self, index):
        assert index >=0,"Index must be non-negative"
        if index > len(self.stacks):
            raise Exception("Invalid index")
        else:
            cur_stack = self.stacks[index]
            cur_stack.pop()
#Learning: When deleting a stack from the list
#Make sure to decrement the cur_stack pointer
#Also, make sure function definitions have the proper parameters
#pop does not need any additional parameters (other than self)
# test_set = set_of_stacks()
# test_set.push(1)
# test_set.push(2)
# test_set.push(3)
# test_set.push(4)
# test_set.push(5)
# test_set.push(6)
# test_set.push(7)
# check_removal_1 = test_set.pop()
# check_removal_2 = test_set.pop()
# check_removal_3 = test_set.pop()
# print('done testing')

#ToDo: Test regular and multipop optimization
class my_queue_two_stacks:
    def __init__(self):
        self.stack_store = stack()
        self.stack_temp = stack()

    def enqueue(self, item):
        self.stack_store.push(item)

    def dequeue(self):
        while not self.stack_store.is_empty():
            self.stack_temp.push(self.stack_store.pop())
        target = self.stack_temp.pop()
        while not self.stack_temp.is_empty():
            self.stack_store.push(self.stack_temp.pop())
        return target

    def size(self):
        return self.stack_store.size()

    def dequeue_eff(self):
        total_items = self.size()
        self.stack_temp.push_multiple(self.stack_store.pop_multiple(total_items))
        target = self.stack_temp.pop()
        total_items -=1
        self.stack_store.push_multiple(self.stack_temp.pop_multiple(total_items))
        return target

    def is_empty(self):
        return self.stack_store.is_empty()

    def peek(self):
        while not self.stack_store.is_empty():
            self.stack_temp.push(self.stack_store.pop())
        target = self.stack_temp.peek()
        while not self.stack_temp.is_empty():
            self.stack_store.push(self.stack_temp.pop())
        return target
#Learning: Stacks with efficient multiple push and pop
#Note that internal list returned by pop_mmultiple_eff must be reversed
#To respect pop properly
# test_queue = my_queue_two_stacks()
# test_queue.enqueue('a')
# test_queue.enqueue('b')
# test_queue.enqueue('c')
# test_queue.enqueue('d')
# test_queue.enqueue('e')
# remove_1 = test_queue.dequeue()
# remove_2 = test_queue.dequeue()
# remove_3 = test_queue.dequeue_eff()
# print ('done testing')
#I will not return the original stack
def sort_stack(input):
    items_sorted = 0
    total_items = input.size()
    if input.is_empty():
        return None
    else:
        while items_sorted != total_items:
            depth = items_sorted
            buffer = stack()
            cur_max = input.pop()
            while input.size() >= depth + 1: #iterate through to find cur_max. + 1 as so we do not pop on an empty stack
                test_value = input.pop() #depth ensures we find a new cur_max each time
                if test_value > cur_max: #Could have just started with a depth of 1 instead
                    cur_max = test_value
                buffer.push(test_value)
            input.push(cur_max) #Maximum value is at the bottom now
            while buffer.size() >= 1: #so we do not pop on empty
                item = buffer.pop()
                if item != cur_max: #As all values were pushed so need to avoid pushing twice
                    input.push(item)
            items_sorted +=1
    return input

#Learning. With these, you always need to look out for cases where pop returns empty
#Monitoring size is good. The depth that you check for thus needed to be depth + 1 to get around
#the empty stack issue.
#Good to have good exceptions. Help you debug later.
# stack_test = stack()
# stack_test.push(5)
# stack_test.push(8)
# stack_test.push(3)
# stack_test.push(11)
# stack_test.push(15)
# stack_test.push(16)
# sorted = sort_stack(stack_test)
# sorted.print_stack()


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
#Lazy size implementation
    def size (self):
        current = self.head
        size = 0
        while current:
            size +=1
            current = current.get_next()
        return size

    def remove_last(self):
        current = self.head
        previous = None
        found = False
        while current and not found:  # Search till not found AND list not empty
            if current.get_next() is None: #current is the last Node
                found = True
            else:
                previous = current
                current = current.get_next()
        if found and previous is not None:  # data is not in head
            previous.set_next(current.get_next())
            return current
        elif found:  # must be head. Delete one Node only
            self.head = current.get_next()
            return current
        else:
            return False  # empty List


    def remove_node(self,node):
        current = self.head
        previous = None
        found = False
        while current and not found:  # Search till not found AND list not empty
            if current is node: #current is the last Node
                found = True
            else:
                previous = current
                current = current.get_next()
        if found and previous is not None:  # data is not in head
            previous.set_next(current.get_next())
            return current
        elif found:  # must be head. Delete one Node only
            self.head = current.get_next()
            return current
        else:
            return False  # empty List

#Naive Implementation.
#Note removing node does not work as different data structures will
#have different nodes in them
class animal_shelter():
    def __init__(self):
        self.all = LinkedList()
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def enqueue(self,type,name):
        if type.lower() == "c":
            self.cats.insert((type,name))
            self.all.insert((type,name))
        elif type.lower() == "d":
            self.dogs.insert((type,name))
            self.all.insert((type,name))
        else:
            raise Exception("Invalid type")

    def size_cats(self):
        return self.cats.size()

    def size_dogs(self):
        return self.dogs.size()

    def size_all(self):
        return self.all.size()

    def dequeue_all(self):
        pet = self.all.remove_last()
        data = pet.get_data()
        if data[0] == "c":
            self.cats.remove(data)
        else:
            self.dogs.remove(data)
        return pet

    def dequeue_cat(self):
        pet = self.cats.remove_last()
        self.all.remove(pet.get_data())
        return pet

    def dequeue_dog(self):
        pet = self.dogs.remove_last()
        self.all.remove(pet.get_data())
        return pet

# test = animal_shelter()
# test.enqueue("c","Cat1")
# test.enqueue("c","Cat2")
# test.enqueue("c","Cat3")
# test.enqueue("c","Cat4")
# test.enqueue("c","Cat5")
# test.enqueue("d","Dog1")
# test.enqueue("d","Dog2")
# test.enqueue("d","Dog3")
# test.enqueue("d","Dog4")
# test_cat = test.dequeue_cat()
# test_dog = test.dequeue_dog()
# test_all = test.dequeue_all()
# print("Done Testing")

#Improved Animal Shelter with one custom queue
class animal_shelter_2:
    def __init__(self):
        self.animals = LinkedList()

    def size(self):
        return self.animals.size()

    def is_empty(self):
        return self.animals.size() == 0

    def enqueue(self, type, name):
        self.animals.insert((type, name))

    def dequeue_any(self):
        pet = self.animals.remove_last()
        return pet

    def dequeue_animal(self, type):
        searchable = self.animals
        current = searchable.head
        last_animal = None
        while current is not None:
            if current.get_data()[0] == type:
                last_animal = current
            current = current.get_next()
        self.animals.remove_node(last_animal)
        return last_animal

    def dequeue_cat(self):
        return self.dequeue_animal("c")

    def dequeue_dog(self):
        return self.dequeue_animal("d")
#Learning: when removing, the else is bound to trigger everytime
#as the condition is till you have not found and current is not None
#Here, you have to keep on continuing till the list is null so
#current must be going to next every single time and this should not be in the else.
#Note that you must remove a node in LinkedList when dequeueing the animals
#This is AN ELEGANT SOLUTION.

# test = animal_shelter_2()
# test.enqueue("c","Cat1")
# test.enqueue("c","Cat2")
# test.enqueue("c","Cat3")
# test.enqueue("c","Cat4")
# test.enqueue("c","Cat5")
# test.enqueue("d","Dog1")
# test.enqueue("d","Dog2")
# test.enqueue("d","Dog3")
# test.enqueue("d","Dog4")
# test_cat = test.dequeue_cat()
# test_dog = test.dequeue_dog()
# test_all = test.dequeue_any()
# print("Done Testing")