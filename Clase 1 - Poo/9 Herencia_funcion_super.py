class Super:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Super):
    def __init__(self,name):
        super().__init__(name)
      
o = Sub("Andy")
print(o)
