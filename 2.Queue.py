class queue:
    def __init__(self):
        self.queue_list = []
    def push(self, value):
        self.queue_list.append(value)
    def pop(self):
        if self.queue_list==[]:
            print("The Queue is empty!")
        else:
            return self.queue_list.pop(0)
    def display(self):
        if self.queue_list==[]:
            print("Empty Queue!")
        else:
            print("The values are : "+",".join([str(qv) for qv in self.queue_list]))
    def peek(self):
        print("The Top Most Value Is : ", self.queue_list[0])


my_queue = queue()
print("1 : Push(Value req), 2 : Pop, 3 : Display, 4 : Peek")
while True:
    ipt = int(input("Enter your choice : "))
    if ipt not in range(1, 5):
        print("Enter VALID Values between 1-4 !")
        continue
    else:
        if ipt==1:
            value = int(input("Enter Value to be inserted : "))
            my_queue.push(value)
        if ipt==2:
            my_queue.pop()
        if ipt==3:
            my_queue.display()
        if ipt==4:
            my_queue.peek()

