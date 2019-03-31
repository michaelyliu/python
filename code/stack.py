class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    def print_better(self):
        print (self.stack)        
AStack = Stack()
AStack.add("Mon")
AStack.print_better()
