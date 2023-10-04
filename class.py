class sam():
    def __init__(self):
        pass
    
    def CI(self, P, R, T):
        A = P*(1 + R/100)**T
        return A
    
prime = sam()
print(prime.CI(55555,96,6))