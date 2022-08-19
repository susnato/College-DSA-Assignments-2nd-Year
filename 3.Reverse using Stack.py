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
ipt_str = input("Enter the String : ")
reversed_str = []
for c in ipt_str:
    my_stack.push(c)

for _ in range(len(ipt_str)):
    rv = my_stack.pop()
    reversed_str.append(rv)

reversed_str = "".join(reversed_str)
print(reversed_str)