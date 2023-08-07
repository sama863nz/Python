class sam:
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname

    def MH(self, age, pet_name):
        self.age = age
        self.pet_name = pet_name
        print("My name is "+ self.fname)
        print("My age is " + str(self.age))

z = sam("Optimus", "Prime")
print(z.fname)
z.MH(4444, "boss")