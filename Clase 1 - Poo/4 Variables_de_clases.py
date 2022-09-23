class Class:
    def __init__(self, val=1):
        if val % 2 !=0:
            self.a = 1
        else:
            self.b = 1
object = Class(1)
print(object.a)
print(object.b) 
