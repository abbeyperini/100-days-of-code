class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            return print("Queue is empty.")

        return print(self.items.pop(0))

queue = Queue() 
queue.enqueue(3) 
queue.enqueue(10)
queue.enqueue(2) 

queue.dequeue() # returns 2 
queue.dequeue() # returns 10 
queue.dequeue() # returns 3 
queue.dequeue() # what should happen when there are no items in the queue