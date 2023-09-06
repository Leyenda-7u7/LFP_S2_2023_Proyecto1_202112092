from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Instrucciones.errores import *
from Abstract.lexema import *
from Abstract.numero import *
import os

#Este es un listado de palabras reservadas como lo son multiplicacion y asi, RTEXTO es un token
reserved = { 
    'CREARBD'           : 'CrearBD',
    'ELIMINARBD'        : 'EliminarBD',
    'CREARCOLECION'     : 'EliminarColeccion',
    'INSERTARUNICO'     : 'InsertarUnico',
    'ACTUALIZARUNICO'   : 'ActualizarUnico', 
    'ELIMINARUNICO'     : 'EliminarUnico',
    'BUSCARTODO'        : 'BuscarTodo',
    'BUSCARUNICO'       : 'BuscarUnico',    
    'COMA'              : ',',
    'PUNTO'             : '.',
    'DPUNTO'            : ':',
    'CORI'              : '(',
    'CORD'              : ')',
    'LLAVEI'            : '{',
    'LLAVED'            : '}',
}

#Convertimos el diccionario de arriba en una lista con el nombre lexemas

lexemas = list(reserved.values())

#Llevamos la lsita de lineas, columnas, instrucciones y lista_lexemas
global n_lineas
global n_columnas   
global instrucciones
global lista_lexemas
global lista_errores
global lista_auxiliar

n_lineas = 1
n_columnas = 1
lista_lexemas = []
instrucciones = []
lista_auxiliar = []
lista_errores = []

#Metodo que recibe una cadea donde mando a llamar a mi linea y columna

def instruccion(cadena):
    global n_lineas
    global n_columnas
    global lista_lexemas
    
#Aqui armamos el lexema donde se ejecuta caracter por caracter donde se va eliminado y se haga mas pequeña eso es posible con el puntero
    lexema = ''
    puntero = 0
    
    while cadena:       #Mientras alla algo nos enciclamos 
        char = cadena[puntero]     #El char sera la posicion cero en la cadena
        puntero += 1
        
        if char == '\"':            #Si el char es igual a las comillas vamos a empezar armar nuestro lexema 
            lexema, cadena = armar_lexema(cadena[puntero:])    #Colocamos cadena aqui para que se actualice la cadena que esta en el while y no se me encicle
            if lexema and cadena:   #Esto quiere decir que si cadena no me retorno nulo se sumara uno a la cadena
                n_columnas +=1
                
                l = Lexema(lexema, n_lineas, n_columnas) 
                
                lista_lexemas.append(l)    #Aqui armamos lexema como clase
                n_columnas += len(lexema) +1  
                puntero = 0        #Reiniciamos porque la cadena recibida fue actualizada
        elif char.isdigit():        #Si es un numero mandaremos a traer la cadena
            token, cadena = armar_numero(cadena) #Mandamos la cedena como tal para no cortar nada
            if token and cadena:
                n_columnas +=1
                
                n = Numero(token, n_lineas, n_columnas)
                
                lista_lexemas.append(n)
                n_columnas += len(str(n)) +1    #El toquen lo convertimos en un string y despues a cadena
                puntero = 0
                
        elif char == '[' or char == ']':        #Si el char es igual a un corchete que cierra o abre 
            
            c = Lexema(char, n_lineas, n_columnas)
            
            lista_lexemas.append(c)
            cadena = cadena[1:]
            n_columnas +=1
            puntero = 0
        elif char == '\t':        #En este if ingnoramos los saltos de linea
            n_columnas +=4
            cadena = cadena[4:]       #Cortamos la cadena con esos espacions
            puntero = 0              #Reiniciamos el puntero
        elif char == '\n':        #Este if es por si el char es un salto de linea       
            cadena = cadena[1:]
            puntero = 0
            n_lineas += 1
            n_columnas = 1
        elif char == ':' or char == ',' or char == '.' or char == '}' or char == '{' or char == '\r' or char == ' ': #Esto nos ayuda por si en dado caso viene uno de esos signos y reconocerlos 
            n_columnas += 1
            cadena = cadena[1:]
            puntero = 0
        else: 
            lista_errores.append(Errores(char, n_lineas, n_columnas)) #Estos crea la lista de errores en dado caso la letras no es renocible y asi genera los errores
            cadena = cadena[1:]
            puntero = 0
            n_columnas += 1

    return lista_lexemas

#metodo armar lexema
def armar_lexema(cadena):
    global n_lineas
    global n_columnas
    global lista_lexemas
    lexema = ''
    puntero = ''
    for char in cadena:    #Aqui recorremos nuestra cadena 
        puntero += char
        if char == '\"':         #Ya leimos la comilla 
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None #Para que no falle se retorna None None


#Metodo para armar los numeros y sus operaciones
def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal = False      #Numeros decimales
    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True 
        if char == '"' or char == ' ' or char == '\n' or char == '\t' or char== ']' or char== "}]":   #Por si viene una comia, un espacio, una tabulacion o salto de linea
            if is_decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
            
        elif char.isdigit() or char =='.':
            numero += char
        else:
            puntero = puntero[:-1]

    return None, None


def operar():
    global lista_lexemas
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    while lista_lexemas:                            
        lexema = lista_lexemas.pop(0)       
        if lexema.operar(None) == 'Operacion':  
            if lista_lexemas:       
                operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = lista_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()
        #Aqui ya armamos la funcion aritmetica y nos recibe lado dercho e izquierdo osea fila y columna
        if operacion and n1 and n2:
            return Aritmeticas(n1, n2, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}') 

        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):
            return Trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None

#Aqui creamos su metodo recursivo

def operar2():
    global instrucciones
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
        
    #for instruccion in instrucciones:
        #print(instruccion.operar())
    return instrucciones
        

'''def getErrores():
    global lista_errores
    return lista_errores'''
    
def getErrores():
    global lista_errores
    contador = 1
    print('{')
    dataErrores = '{\n'

    while lista_errores:
        error = lista_errores.pop(0)
        print(str(error.operar(contador)), ',')
    
        dataErrores += error.operar(contador)
        dataErrores += ',\n'

        contador += 1

    dataErrores +='}'

    print('}')

    with open('RESULTADOS_202112092.json', 'w') as f:         
        f.write(dataErrores)

    
def grafica(sumatoriaData):
    global lista_auxiliar
    global lista_errores
    
    lista_errores = []

    while lista_auxiliar:

        lexema =lista_auxiliar.pop(0)

        if lexema.operar(None) == 'Texto':
            textoTitulo = lista_auxiliar.pop(0)
            print(textoTitulo.operar(None))
        
        elif lexema.operar(None) == 'Color-Fondo-Nodo':
            colorNodo = lista_auxiliar.pop(0)
            print(colorNodo.operar(None))

        elif lexema.operar(None) == 'Color-Fuente-Nodo':
            fuenteNodo = lista_auxiliar.pop(0)
            print(fuenteNodo.operar(None))

        elif lexema.operar(None) == 'Forma-Nodo':
            formaNodo = lista_auxiliar.pop(0)
            print(formaNodo.operar(None))
    
    

    data = '''
    digraph {\n
    '''


    #COLOR DEL NODO

    color = colorNodo.operar(None).lower()

    if color == "amarillo" or color == "#ffff00":
        data += f'node[fillcolor = "yellow"'
    
    elif color == "rojo" or color == "#ff0000":
        data += f'node[fillcolor = "red"'
    
    elif color == "verde" or color == "#008000":
        data += f'node[fillcolor = "green"'
    
    elif color == "azul" or color == "0000ff":
        data += f'node[fillcolor = "blue"'
    
    elif color == "celeste" or color == "#87ceeb":
        data += f'node[fillcolor = "skyblue"'
    
    elif color == "negro" or color == "#000000":
        data += f'node[fillcolor = "black"'
    
    elif color == "cafe" or color == "#a52a2a":
        data += f'node[fillcolor = "brown"'
    
    elif color == "gris" or color == "#808080":
        data += f'node[fillcolor = "gray"'
    
    elif color == "rosado" or color == "rosa" or color == "#ff0c0cb":
        data += f'node[fillcolor = "pink"'
    
    elif color == "purpura" or color == "morado" or color == "#800080":
        data += f'node[fillcolor = "purple"'
    
    elif color == "blanco" or color == "#ffffff":
        data += f'node[fillcolor = "white"'
    
    elif color == "naranja" or color == "anaranjado" or color == "#ffa500":
        data += f'node[fillcolor = "orange"'

    #FUENTE COLOR NODO

    fuente = fuenteNodo.operar(None).lower()

    if fuente == "amarillo"  or fuente == "#ffff00":
        data += f' fontcolor = "yellow"'
    
    elif fuente == "rojo" or fuente == "#ff0000":
        data += f' fontcolor = "red"'
    
    elif fuente == "verde" or fuente == "#008000":
        data += f' fontcolor = "green"'

    elif fuente == "azul" or fuente == "0000ff":
        data += f' fontcolor = "blue"'
    
    elif fuente == "celeste" or fuente == "#87ceeb":
        data += f' fontcolor = "skyblue"'
    
    elif fuente == "negro" or fuente == "#000000":
        data += f' fontcolor = "black"'
    
    elif fuente == "cafe" or fuente == "#a52a2a":
        data += f' fontcolor = "brow"'
    
    elif fuente == "gris" or fuente == "#808080":
        data += f' fontcolor = "gray"'
    
    elif fuente == "rosado" or fuente == "rosa" or fuente == "#ff0c0cb":
        data += f' fontocolor = "pink"'
    
    elif fuente == "purpura" or fuente == "morado" or fuente == "#800080":
        data += f' fontcolor = "purple"'
    
    elif fuente == "blanco" or fuente == "#ffffff":
        data += f' fontcolor = "white"'
    
    elif fuente == "naranja" or fuente == "anaranjado" or fuente == "#ffa500":
        data += f' fontcolor = "orange"'
    

    #FORMA NODO

    if (formaNodo.operar(None)).lower() == "cuadrado":
        data += f' shape = "square"'
    
    elif (formaNodo.operar(None)).lower() == "circulo":
        data += f' shape = "circle"'
    
    elif (formaNodo.operar(None)).lower() == "triangulo":
        data += f' shape = "triangle"'
    
    elif (formaNodo.operar(None)).lower() == "elipse":
        data += f' shape = "ellipse"'
    
    elif (formaNodo.operar(None)).lower() == "ovalo":
        data += f' shape = "oval"'
    
    elif (formaNodo.operar(None)).lower() == "rombo":
        data += f' shape = "diamond"'
    
    elif (formaNodo.operar(None)).lower() == "pentagono":
        data += f' shape = "pentagon"'
    
    elif (formaNodo.operar(None)).lower() == "hexagono":
        data += f' shape = "hexagon"'
    
    elif (formaNodo.operar(None)).lower() == "hexagono":
        data += f' shape = "hexagon"'
    
    elif (formaNodo.operar(None)).lower() == "heptagono":
        data += f' shape = "septagon"'
    
    elif (formaNodo.operar(None)).lower() == "octagono":
        data += f' shape = "octagon"'
    
    elif (formaNodo.operar(None)).lower() == "paralelogramo":
        data += f' shape = "parallelogram"'
    
    elif (formaNodo.operar(None)).lower() == "estrella":
        data += f' shape = "star"'
    
    data += ' style = filled]\n'


    data += f'label = "{textoTitulo.operar(None)}"\n'

    data += sumatoriaData

    data += '\n}'

    with open('Myejemplo_graphviz.dot', 'w') as f:         
        f.write(data)

    os.system('dot -Tpng Myejemplo_graphviz.dot -o Operaciones.png')

    print(data)