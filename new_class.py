class sam():
    def __init__(self, name, age):
        self.name = name
        self.age = age

prime = sam("my name is Samarth and my age is ", "12")
print(prime.name + prime.age)

class new(sam):
   pass

Car = new("Malaysian 370", 12)
print(Car.name)


