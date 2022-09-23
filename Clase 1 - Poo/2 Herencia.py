class Stack:
    def __init__(self):
        self.__stk = []

    def push(self,val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    def push(self,val):
        self.__sum += val
        Stack.push(self,val)
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    def getSum(self):
        return self.__sum

    

little_stack = AddingStack()
another_stack = AddingStack()
funny_stack = AddingStack()
little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
print(another_stack.getSum())
funny_stack.push(another_stack.pop() - 2)
print(funny_stack.pop())
print(another_stack.getSum())



    
