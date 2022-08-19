import numpy as np

class stack:
    def __init__(self):
        self.stack_list = []
    def push(self, value):
        self.stack_list.append(value)
    def pop(self):
        return self.stack_list.pop(-1)
    def display(self):
        if self.stack_list==[]:
            print("Stack is Empty!")
        else:
            print("The Stack Values are : "+",".join([str(sl) for sl in self.stack_list]))
    def peek(self):
        if self.stack_list == []:
            print("Stack is Empty!")
        else:
            print("The Top most value is : "+str(self.stack_list[-1]))

class CircularQueue:
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.queue_array = np.zeros([queue_size, ], dtype=object)
        self.front = 0
        self.rear = 0
        self.size = 0
    def isFull(self):
        return self.size == self.queue_size
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

stack1 = stack()
stack2 = stack()

i = 0
n = int(input("Enter the no of boxes : "))
for _ in range(n):
    colors = input("Enter the colors with commas in between : ")
    stack1.push(colors)
    i+=1

eligible, not_eligible = 0, 0
my_queue = CircularQueue(queue_size=i)
for _ in range(n):
    box_colors = stack1.pop()
    box_colors = [str(color).strip() for color in box_colors.strip().split(",")]
    count = 0
    if len(box_colors) != 3:
        my_queue.enqueue(",".join(box_colors))
        not_eligible += 1
    else:
        if set(box_colors) == {"red", "blue", "green"}:
            stack2.push(",".join(box_colors))
            eligible += 1
        else:
            my_queue.enqueue(",".join(box_colors))
            not_eligible += 1

print("ELIGIBLE BOXES : ")
for _ in range(eligible):
    print(stack2.pop())

print("NOT ELIGIBLR BOXES : ")
for _ in range(not_eligible):
    print(my_queue.dequeue())
