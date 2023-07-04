class sam_class:
    def __init__(self,age,name):
        self.age = age
        self.name = name

class sam_new(sam_class):
    pass
MAS = sam_class(53, "Captain Zaharie Ahemad Shah")
MAS1 = sam_new(27, "First Officer Fariq Hammid")
print(MAS.name)
print(MAS1.name)

