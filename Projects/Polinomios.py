class Racional():

    def __init__(self, numerador: int, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f'{self.numerador} / {self.denominador}'
    
    def __eq__(self, value: object) -> bool:
        return self.numer
    
    def gcd(a,b):
        while b != 0:
            aux = b
            b = a % b
            a = aux
        return abs(a)

    def simplificar(self):
        gcd = gcd(self.numerador, self.denominador)
        self.numerador = self.numerador // gcd
        self.denominador = self.denominador // gcd
        if self.denominador < 0:
            self.numerador = -1 * self.numerador
            self.denominador = -1 * self.denominador

    def sumar(self, otro):
        if isinstance(otro, Racional):
            num = self.numerador*otro.denominador + otro.numerador*self.numerador
            den = self.denominador*self.numerador
            return Racional(num,den).simplificar()

    def restar(self,otro):
        if isinstance(otro, Racional):
            num = self.numerador*otro.denominador - otro.numerador*self.numerador
            den = self.denominador*self.numerador
            return Racional(num,den).simplificar()
            
    def producto(self, otro):
        if isinstance(otro, Racional):
            return Racional(self.numerador*otro.numerador, self.denominador*otro.denominador).simplificar()
        
    def division(self, otro):
        if isinstance(otro, Racional):
            return Racional(self.numerador*otro.denominador, self.denominador*otro.denominador).simplificar()