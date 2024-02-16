class myclass:
    x=10
    y=20
    def print_x(self):
        print("hello",self.x,self.y)
    def add(self):
        z=self.x+self.u
        print(self.x,'+',self.y,'=',z)
obj=myclass()
obj.print_x()