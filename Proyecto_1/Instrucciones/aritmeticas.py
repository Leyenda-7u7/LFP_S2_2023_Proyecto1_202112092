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
    
        if self.tipo.operar(arbol) == 'suma':
            return round(leftValue + rightValue, 2)
        elif self.tipo.operar(arbol)  == 'resta':
            return round(leftValue - rightValue, 2)
        elif self.tipo.operar(arbol)  == 'multiplicacion':
            return round(leftValue * rightValue, 2)
        elif self.tipo.operar(arbol)  == 'division':
            return round(leftValue / rightValue, 2)
        elif self.tipo.operar(arbol)  == 'modulo':
            return round(leftValue % rightValue, 2)
        elif self.tipo.operar(arbol)  == 'potencia':
            return round(leftValue ** rightValue, 2)
        elif self.tipo.operar(arbol)  == 'raiz':
            return round(leftValue ** (1/rightValue), 2)
        elif self.tipo.operar(arbol)  == 'inverso':
            return round(1/leftValue, 2)
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()