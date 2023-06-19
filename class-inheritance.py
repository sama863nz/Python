class sam_class:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname 

    def sam_function(self):
        print(self.lname)

class sam_class_new(sam_class):
    pass

MAS = sam_class_new("Malaysian Airlines", "Flight 370")
print(MAS.fname)
print(MAS.sam_function())
