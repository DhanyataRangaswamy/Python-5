class AP:

    def __init__(self,r):
        self.r=r

    def area(self):
        return self.r**2*3.14
    def peri(self):
        return self.r*2*3.14
    
c=AP(8)
print(c.area())
print(c.peri())
        