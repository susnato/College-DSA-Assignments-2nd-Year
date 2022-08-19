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

my_stack = stack()
print("1 : Push(Value req), 2 : Pop, 3 : Display, 4 : Peek")
while True:
    ipt = int(input("Enter your choice : "))
    if ipt not in range(1, 5):
        print("Enter VALID Values between 1-4 !")
        continue
    else:
        if ipt==1:
            value = int(input("Enter Value to be inserted : "))
            my_stack.push(value)
        if ipt==2:
            my_stack.pop()
        if ipt==3:
            my_stack.display()
        if ipt==4:
            my_stack.peek()

