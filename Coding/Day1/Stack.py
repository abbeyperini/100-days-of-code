class Stack():
    def __init__(self):
        self.items = []

    def push_item(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return print(self.items.pop(-1))
        else:
            print("Stack is empty.")

stack = Stack() 
stack.push_item(3) 
stack.push_item(10)
stack.push_item(2) 

stack.pop() # returns 2 
stack.pop() # returns 10 
stack.pop() # returns 3 
stack.pop() # what should happen when there are no items in the stack

