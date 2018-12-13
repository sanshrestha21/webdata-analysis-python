class calculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y

cal=calculator()
print cal.add(2,4)
print cal.sub(2,4 )


class simpleinterest:
    def __init__(self):
        self.p=0.0
        self.t=0.0
        self.r=0.0 
    def interest(self):
        return (self.p * self.t * self.r)/100
