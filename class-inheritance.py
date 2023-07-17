class sam_class:
    def __init__(self,age,name):
        self.name = name
        self.age = age
class Transformers(sam_class):
    pass
Prime = Transformers(41,"Optimus")
print(Prime.age)
print(Prime.name)