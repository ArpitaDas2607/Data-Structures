#Queues

class Queue(object):
    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size <= 0

    def EnQueue(self, data):
        if self.size >= self.limit:
            self.resize()
        self.que.append(data)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
            #self.front = 0
        self.size += 1
        print "Que after enQueue:", self.que


    def DeQueue(self):
         if self.size <= 0:
             print "Queue Underflow!!"
             return 0
         else:
             self.que.pop()
             self.size -= 1
             if self.size == 0:
                 self.rear = self.front = None
             else:
                 self.rear = self.size -1
             print "Queue after Deque: ", self.que


    def queueRear(self):
        if self.rear is None:
            print "Sorry, the queue is empty"
            raise Exception("My error!!")
        return self.que[self.rear]

    def queueFront(self):
        if self.front is None:
            print "Sorry, the queue is empty"
            raise IndexError
        return self.que[self.front]

    def queueSize(self):
        return self.size

    def resize(self):
        NewQueue = list(self.que)
        self.limit = 2*self.limit
        self.que = NewQueue



que = Queue()
que.EnQueue("first")
print "Front: ", que.queueFront()
print "Rear: ", que.queueRear()
que.EnQueue("second")
print "Front: "+que.queueFront()
print "Rear: "+que.queueRear()
que.EnQueue("third")
print "Front: "+que.queueFront()
print "Rear: "+que.queueRear()
que.EnQueue("fourth")
print "Front: "+que.queueFront()
print "Rear: "+que.queueRear()
que.EnQueue("fifth")
print "Front: "+que.queueFront()
print "Rear: "+que.queueRear()
que.EnQueue("sixth")
print "Front: "+que.queueFront()
print "Rear: "+que.queueRear()
que.DeQueue()
print "Front: "+que.queueFront()
print "Rear: "+que.queueRear()
