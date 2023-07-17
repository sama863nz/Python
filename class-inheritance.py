class sam:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class sam1(sam):
    pass

x = sam("samarth",12)
print(x.name)

y = sam1("Sanjeev",41)
print(y.age)



    