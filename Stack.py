# Stacks

class Stack(object):
    def __init__(self, limit = 10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        stack_temp = self.stk
        if len(stack_temp) == 0:
            print "Stack is empty"

    def push(self,item):
        stack_temp = self.stk
        limit = self.limit
        if len(stack_temp) >= limit:
            return "Stack Overflow"
        else:
            stk = stack_temp.append(item)
        print self.stk

    def pop(self):
        if len(self.stk) == 0:
            "Stack iInderflow"
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) == 0:
            print "Stack underflow"
            return 0
        else:
            return self.stk[-1]

    def sizeOf(self):
        print len(self.stk)



myStack = Stack()
myStack.isEmpty()
myStack.push(4)
myStack.push(6)
myStack.push(8)
myStack.pop()
myStack.push(11)
print myStack.peek()
myStack.push(13)
myStack.sizeOf()
