#Queues as Linked List

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

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def getRear(self):
        this_node = self.root
        print "Rear Node: ",  this_node.get_data()
        return this_node

    def getFront(self):
        this_node = self.root
        i = 0
        while i < (self.size-1):
                this_node = this_node.get_next_node()
                i += 1
        print "Front Node: ", this_node.get_data()
        return this_node


    def remove(self):
        if self.root is None:
            print "Stack Underflow!"
            return
        else:
            this_node = self.root
            prev_node = self.root
            i = 0
            while i < (self.size-2):
                    prev_node = prev_node.get_next_node()
                    this_node = prev_node.get_next_node()
                    i += 1
            prev_node.set_next_node(this_node.get_next_node())
            self.size -= 1
            return prev_node




myList = LinkedList()
myList.add(446)
myList.add(7)
myList.add(5)
myList.add(8)
myList.add(56)
myList.add(77)
myList.add(55)
myList.add(89)
myList.getRear()
myList.getFront()
myList.remove()
myList.getRear()
myList.getFront()
