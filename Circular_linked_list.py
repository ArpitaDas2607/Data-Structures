#Circular linked list
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
    def has_next_node(self):
        return self.next_node != None

class Circular_linked_list():

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add_beginning(self, node_data):
        new_node = Node(node_data, self.root)
        new_node.set_next_node(new_node)
        if self.root == None:
            self.root = new_node
            new_node.set_next_node(self.root)
        else:
            new_node.set_next_node(self.root)
            self.root = new_node
        self.size += 1

    def find(self, node_data):
        this_node = self.root
        if this_node == None:
            return "List is empty"
        this_node = this_node.get_next_node()
        count = 1
        while count < self.size:
            if this_node.get_data() == node_data:
                return node_data
            else:
                this_node = this_node.get_next_node()
                count += 1
                if count == self.size:
                    return "Data not in List"


    def get_Nth(self, index):
        this_node = self.root
        i = 0
        #self.index = index
        while i < index and this_node.get_next_node():
                this_node = this_node.get_next_node()
                i += 1
        return this_node.get_data()

    def get_last_node(self):
        this_node = self.root
        i = 0
        while i < (self.size-1):
                this_node = this_node.get_next_node()
                i += 1
        return this_node.get_data()

    def remove(self, node_data):
        if self.size == 0:
            return "List is empty"
        else:
            current_node = self.root
            this_node = self.root
            count = 0
            while count <= self.size:

                if current_node.get_data() == node_data:
                    this_node.set_next_node(current_node.get_next_node())
                    return "Number %d removed from the list"%(node_data)

                else:
                    this_node = current_node
                    current_node = current_node.get_next_node()
                    count += 1
                    if count == self.size:
                        return "Number %d not in List"%(node_data)














myList = Circular_linked_list()
myList.add_beginning(4)
myList.add_beginning(7)
myList.add_beginning(5)
#myList.remove(4)
print (myList.get_last_node())
print (myList.remove(67))
print (myList.find(7))
print (myList.get_Nth(0))
print (myList.get_size())
