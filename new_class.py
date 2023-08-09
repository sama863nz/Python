class Sam():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def SI(self, P,R,T):
        SI =(P*R*T)/100
        return SI
    
prime = Sam("Malaysian 370", "9")
print(prime.name +": The plane that dissapeared about "+ prime.age + " years ago.")
print(prime.SI(12345,12,2))