class Matrix():

    def __init__ (self, matrix: list = [[0,0], [0,0]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix

    def __repr__(self) -> str:
        return f'Matrix({self.matrix})'

    def __add__(self, otro: 'Matrix') -> 'Matrix':
        if self.m == otro.m and self.n == otro.n:
            new = self.matrix
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
        new = self.matrix
        i, j = 0,0
        while i < self.m:
            while j < self.n:
                new[i][j] *= c
                j += 1
            i += 1
            j = 0
    
a = Matrix([[0]])
b = Matrix([[1]])
print(a + b)