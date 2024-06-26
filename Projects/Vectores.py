import math
class Vector():
    '''
    Implementacion de vectores bidimensionales
    '''
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x},{self.y})'
    
    def __eq__(self, otro: 'Vector') -> bool:
        return self.x == otro.x and self.y == otro.y
    
    def __abs__(self) -> float:
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def __neg__(self) -> 'Vector':
        return Vector(-self.x, -self.y)
    
    def __add__(self, otro: 'Vector') -> 'Vector':
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __sub__(self, otro: 'Vector') -> 'Vector':
        return Vector(self.x - otro.y, self.x - self.y)
        
    def __mul__(self, c) -> 'Vector':
        return Vector(self.x * c, self.y * c)
    
    def __rmul__(self, c):
        return Vector(self.x * c, self.y * c)   
    
u = Vector(3,4)
v = Vector(3,4)
w = Vector(6,8)
print(u - v)
print(u + -v )
print(w == (u + v))
print(u * 2)
print(2 * u)
