class Vector2d:
    typecode = 'd'
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __iter__(self):
        return (i for i in(self.x,self.y))
    @property
    def x(self):
        return self.x
    @property
    def y(self):
        return self.y

    