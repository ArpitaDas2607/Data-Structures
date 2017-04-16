# Doubly Linked LinkedList

class Node(object):

    def __init__(self, node_data=None, next_node=None, prev_node=None):
        self.data = node_data
        self.next_node = next_node
        self.prev_node = prev_node


    def get_data(self):
        return self.data
    def set_data(self, node_data):
        self.data = node_data
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, next_node):
        self.next_node = next_node
    def get_prev_node(self):
        return self.prev_node
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

class Doubly_linked_list(object):

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, node_data):
        new_node = Node(node_data, self.root)
        if self.root:#this part checks if there were nodes already before
            self.root.set_prev_node(new_node)
        self.root = new_node
        self.size += 1

    def remove(self, node_data):
        this_node = self.root

        while this_node:
            if this_node.get_data() == node_data:
                next_n = this_node.get_next_node()
                prev_n = this_node.get_prev_node()

                if next_n:
                    next_n.set_prev_node(prev_n)
                if prev_n:
                    prev_n.set_next_node(next_n)
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                this_node = this_node.get_next_node()
        return False

    def find(self, node_data):
        this_node = self.root
        while this_node:
            if this_node.get_data == node_data:
                return node_data
            else:
                this_node = this_node.get_next_node()
        return node_data


myList = Doubly_linked_list()
myList.add(4)
myList.add(7)
myList.add(5)
myList.add(8)
myList.remove(8)
myList.remove(12)
print myList.remove(5)
print myList.find(7)
