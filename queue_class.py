class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,x):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items==[]
