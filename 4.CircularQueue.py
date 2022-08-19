import numpy as np

class CircularQueue:
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.queue_array = np.zeros([queue_size, ], dtype=np.int32)
        self.front = 0
        self.rear = 0
        self.size = 0
    def isFull(self):
        return self.size==self.queue_size
    def enqueue(self, value):
        if self.isFull():
            print("Queue FULL!")
        else:
            self.queue_array[self.rear] = value
            self.size += 1
            self.rear += 1
            self.rear = self.rear%self.queue_size

    def dequeue(self):
        if self.size==0:
            print("No Elements in Queue!")
        else:
            value = self.queue_array[self.front]
            self.size -= 1
            self.front += 1
            self.front = self.front%self.queue_size
            return value
    def display(self):
        if self.size==0:
            print("Nothing to print!")
        else:
            if self.rear>self.front:
                print("The Values are : ", ",".join([str(ev) for ev in self.queue_array[self.front:self.rear]]))
            else:
                print( "The Values are : ", ",".join([str(ev) for ev in self.queue_array[self.front:]]), ",".join([str(ev) for ev in self.queue_array[:self.rear]]) )
queue_size = 3
circular_queue = CircularQueue(queue_size=queue_size)
print("1 : Push(Value req), 2 : Pop, 3 : Display")
while True:
    ipt = int(input("Enter your choice : "))
    if ipt not in range(1, 4):
        print("Enter VALID Values between 1-3 !")
        continue
    else:
        if ipt==1:
            value = int(input("Enter Value to be inserted : "))
            circular_queue.enqueue(value)
        if ipt==2:
            print(circular_queue.dequeue())
        if ipt==3:
            circular_queue.display()


