class Node(object):

    def __init__(self, node_data=None, next_node=None):
        self.data = node_data
        self.next_node = next_node

    def get_data(self):
        return self.data
    def set_data(self, node_data):
        self.data = node_data
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size
    def add(self, node_data):
        new_node = Node(node_data, self.root)# here the node created is pointing to where the root was previously pointing to
        self.root = new_node#the root is now pointing to the new_node
        self.size += 1

    def pop(self): #we must always have a true/false in remove function

        if self.size == 0:
            print "Stack Underflow"
        else:
            popped_data = self.root.get_data()
            self.root = self.root.get_next_node()
            print "popped: ", popped_data
    def get_Nth(self, index):
        this_node = self.root
        i = 0
        self.index = index
        while i < self.index:
                this_node = this_node.get_next_node()
                i += 1
        return this_node.get_data()


myList = LinkedList()
myList.add(446)
myList.add(7)
myList.add(5)
myList.add(8)
myList.add(56)
myList.add(77)
myList.add(55)
myList.add(89)
myList.pop()
#myList.remove(12)
print myList.get_Nth(4)
print myList.get_size()
print myList.pop()
#print myList.find(7)
#print myList.get_last_node()
