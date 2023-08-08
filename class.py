class sam():
    def __init__(self, name, age):
        self.age = age
        self.name = name
Heaton = sam("Hello, I am Samarth and I am ", "12 years old!")
print(Heaton.name + Heaton.age)
class new(sam):
    pass
monkey = new("Malaysian 370, Contact Ho Chi Minh 120.9, Good Night.", ", Malaysian 370.")
print(monkey.name)