class Monomio():
    def __init__(self, base: float = 1, grado: float = 0):
        self.coef = base
        self.grado = grado
        self.variable = 'x'

    def __repr__(self):
        return f'Monomio({self.coef},{self.grado})'
    
    def __add__(self, otro: 'Monomio'):
        if self.grado == otro.grado:
            return Monomio(self.coef + otro.coef, self.grado)
        else:
            return None
    
    def __neg__(self):
        return Monomio(-self.coef, self.grado)
    
    def __sub__(self, otro: 'Monomio'):
        if self.grado == otro.grado:
            return Monomio(self.coef - otro.coef, self.grado)
        else:
            return None
        
    def __mul__(self, c: float):
        return Monomio(self.coef * c, self.grado)
    
    __rmul__ = __mul__
    
    def __matmul__(self, otro: 'Monomio'):
        return Monomio(self.coef * otro.coef, self.grado + otro.grado)
    
class Polinomio():

    def __init__(self, *args):
        self.monomios = []
        self.grado_abs = 0
        for mon in args:
            self.monomios.append(mon)
            if mon.grado > self.grado_abs:
                self.grado_abs = mon.grado

    def __repr__(self):
        return str(self.monomios)

x = Polinomio(Monomio(1,2), Monomio(2,3), Monomio(6,5), Monomio(2,7))
print(x)
print(x.grado_abs)