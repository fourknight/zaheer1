class dog:
    def __init__(self, name):
        self.name = name

     def bark(self) -> None:
        print("Bark") 
d = dog();
print(d)
print(d.bark)  
