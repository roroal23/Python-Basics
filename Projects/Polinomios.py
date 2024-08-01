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
        self.grados = {}
        for mon in args:
            self.agregar(mon)

    def agregar(self, mon: 'Monomio'):
        self.monomios.append(mon)
        self.grados[mon.grado] = len(self.monomios) - 1 #grado : posicion
        if mon.grado > self.grado_abs:
                self.grado_abs = mon.grado

    def __repr__(self):
        return str(self.monomios)
    
    def __len__(self): #Devuelve el numero de monomios
        return len(self.monomios)
    
    def __getitem__(self, i : int):
        return self.monomios[i]
    
    def __neg__(self):
        for i in range(len(self.monomios)):
            self.monomios[i] *= -1

    def sumaMonomio(self, mon :'Monomio'):
        if mon.grado in self.grados:
            pos = self.grados[mon.grado]
            self.monomios[pos] = self.monomios[pos] + mon
        else:
            self.agregar(mon)

    def sumaPolinomio(self, pol: 'Polinomio'):
        for mon in pol.monomios:
            self.sumaMonomio(mon)

    def multEscalar(self, c : float):
        for i in range(len(self.monomios)):
            self.monomios[i] *= c

x = Polinomio(Monomio(1,2), Monomio(2,3), Monomio(6,5), Monomio(2,7))
y = Polinomio(Monomio(3,2), Monomio(6,3), Monomio(8,5), Monomio(-2,7))
mon = Monomio(3,2)
#print(x)
#print(x.grado_abs)
#x.sumaMonomio(mon)
#print(x)
#print(x.grado_abs)
#x.sumaPolinomio(y)
x.multEscalar(3)
print(x)