from Abstract.abstract import Expression

class Aritmeticas(Expression):
    
    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)
        
#Este metodo realiza la operacion donde entra al lado derecho e ingresa despues vuelva y devuelve el valor izquiero
#Recursivdad

    def operar(self, arbol):
        leftValue = ''
        rightValue = ''
        if self.left != None:
            leftValue = self.left.operar(arbol)   #aqui me devuelve el valor de un numero ya sea entero o decimal
        if self.right != None:
            rightValue = self.right.operar(arbol) #aqui me devuelve el valor de un numero ya sea entero o decimal
    
        if self.tipo.operar(arbol) == 'Suma':
            return leftValue + rightValue
        elif self.tipo.operar(arbol)  == 'Resta':
            return leftValue - rightValue
        elif self.tipo.operar(arbol)  == 'Multiplicacion':
            return leftValue * rightValue
        elif self.tipo.operar(arbol)  == 'Division':
            return leftValue / rightValue
        elif self.tipo.operar(arbol)  == 'Modulo':
            return leftValue % rightValue
        elif self.tipo.operar(arbol)  == 'Potencia':
            return leftValue ** rightValue
        elif self.tipo.operar(arbol)  == 'Raiz':
            return leftValue ** (1/rightValue)
        elif self.tipo.operar(arbol)  == 'Inverso':
            return 1/leftValue
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()