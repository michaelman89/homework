class Vector():
    def __init__(self,x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def __abs__(self):
        return(self.x**2+self.y**2+self.z**2)**0.5
    def __radd__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
        if isinstance(other, int):
            return Vector(self.x+other, self.y+other, self.z+other)
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x+other,self.y+other,self.z+other)
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x*other.x + self.y*other.y + self.z*other.z
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x*other, self.y*other, self.z*other)
    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'
n=int(input())   #количество точек
d=Vector(0,0,0)
for i in range(n):
    x,y,z=map(int, input().split())
    d=d+Vector(x,y,z)
print(d*(1/n))
