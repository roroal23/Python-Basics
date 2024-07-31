import numpy as np
class Matrix():

    def __init__ (self, matrix: list = [[0,0], [0,0]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix

    def __repr__(self) -> str:
        return f'Matrix({self.matrix})'

    def __add__(self, otro: 'Matrix') -> 'Matrix':
        if self.m == otro.m and self.n == otro.n:
            new = [row[:] for row in self.matrix]
            i, j = 0, 0
            while i < self.m:
                while j < self.n:
                    new[i][j] += otro.matrix[i][j]
                    j += 1
                i += 1
                j = 0    
            return Matrix(new)
        else:
            return None
        
    def __mul__(self, c: 'float') -> 'Matrix':
        print(self.matrix, 'a')
        new = [row[:] for row in self.matrix] #new = self.matrix[:][:] doesnt make a deep copy of the og matrix
        print(new, 'b')
        i, j = 0,0
        while i < self.m:
            while j < self.n:
                new[i][j] *= c
                j += 1
            i += 1
            j = 0
        return 3
    
    __rmul__ = __mul__

    def __matmul__ (self, otro: 'Matrix') -> 'Matrix':
        if self.n == otro.m:
            new = [[0] * self.m for n in range(otro.n)]
            i, j, k = 0,0,0
            for i in range(self.m):
                for j in range(otro.n):
                    for k in range(otro.m):
                        new[i][j] += self.matrix[i][k] * otro.matrix[k][j]
            return Matrix(new)
        else:
            return None

    
a = Matrix([[1,0],
            [0,1]])
b = Matrix([[3,3],
            [2,4]])
print(a @ b)
