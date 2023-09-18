from Abstract.abstract import Expression

class Errores(Expression):
    
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)
        
#Este metodo realiza la operacion donde entra al lado derecho e ingresa despues vuelva y devuelve el valor izquiero
#Recursivdad
    def operar(self , no):
        no1 = f'\t\t"No.": {no}\n'
        descripcion = '\t\t"Descripcion-Token": {\n'
        lexema = f'\t\t\t"Lexema": {self.lexema}\n'
        tipo = '\t\t\t"Tipo:": Error Lexico\n'
        fila = f'\t\t\t"Fila": {self.fila}\n'
        columna= f'\t\t\t"Columna": {self.columna}\n'
        fin = '\t\t}\n'

        return '\t{\n' + no1 + descripcion + lexema + tipo + fila + columna + fin + '\t}'
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()