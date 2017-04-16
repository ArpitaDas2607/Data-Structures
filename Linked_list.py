# Node Construction

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
        new_node = Node(node_data, self.root)# here the root-which
        #only contains a pointer is being used as a pointer argument
        self.root = new_node#.get_next_node() #doesn't this part eradicate the root
        #entirely, because i am assigning the new node to it?
        self.size += 1

    def remove(self, node_data): #we must always have a true/false in remove function
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == node_data:
                if prev_node:
                    prev_node.set_next_node(this_node.get_next_node())
                else:
                    self.root = this_node
                self.size -=1
                return True #data removed

            else:
                 prev_node = this_node
                 this_node = this_node.get_next_node()
        return False #not found in LinkedList

    def find(self, node_data):
        this_node = self.root
        while this_node:
            if this_node.get_data == node_data:
                return node_data
            else:
                this_node = this_node.get_next_node()
        return node_data



myList = LinkedList()
myList.add(4)
myList.add(7)
myList.add(5)
myList.add(8)
myList.remove(8)
myList.remove(12)
print myList.remove(5)
print myList.find(7)
