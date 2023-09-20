UNIVESIDAD DE SAN CARLOS DE GUATEMALA

FACULTAD DE INGENIERIA

ESCUELA DE CIENCAS Y SISTEMAS

LANGUAJES FORMALES Y DE PROGRAMACION

SECCIÓN B+

SEGUNDO SEMESTRE 2023

AUX. FRANCISCO MAGDIEL ASICONA MATEO




<p align="center"> MANUAL TECNICO </p>



BRANDON EDUARDO PABLO GARCIA

202112092

Guatemala, septiembre del 2023









# Introduccion

Este manual describe los pasos necesarios para cualquier persona que tenga ciertas bases de sistemas pueda realizar el código implementado en Python donde se crea un código para un sistema de muestras de películas utilizando POO (Programación Orientada a Objetos) de la misma manera Tkinter y así poder implementarlo de la mejor manera. El siguiente código se explicó de la manera más detalla posible para la mejor compresión de la persona.



# Objetivos

* Brindar la información necesaria para poder  representar la funcionalidad técnica de la estructura, diseño y definición del aplicativo.

* Describir las herramientas utilizadas para el diseño y desarrollo del prototipo


# Requerimientos de funcion


|          Requerimientos      |     Descripcion |                                      
|----------------|-------------------------------|
|Visual Studio Code            |Se recomienda el uso de Visual Studio Code que fue la versión donde se programó el sistema de información. |       
|Tkinter         |Conocimiento sobre el uso de las librerias tkinter para el uso de la interfaz grafica |            |            |


##	Desarrollo

[![Crono.jpg](https://i.postimg.cc/0jqCq0fW/Crono.jpg)](https://postimg.cc/0McSYmhD)

 



#	Contenido tecnico

El código presenta la definición de una clase en Python llamada `LToken`. La clase tiene cuatro atributos: `nombre`, `lexema`, `fila` y `columna`, todos de tipo `str` o `int`. El método constructor `__init__` toma como argumentos cuatro parámetros, `nombre`, `lexema`, `fila` y `columna`, que son asignados a los respectivos atributos de la instancia creada.

El método `__str__` devuelve una representación en forma de cadena de la instancia de la clase, en la que se muestra el valor de cada uno de sus atributos.

La variable `Instrucciones` es una lista de cadenas que contiene los nombres de varios tipos de funciones.

		
    def instruccion(cadena):
        global n_lineas
        global n_columnas
        global lista_lexemas

Para el analixar lexico se implemento la clase que contiene métodos para identificar y generar tokens a partir de una cadena de entrada dada llamada `AnalizadorLexico`. La clase tiene un `analizar` método que toma una cadena de entrada y la analiza carácter por carácter para identificar y generar tokens.



Se definido un método llamado `instrucciones` y recibe una cada dónde se manda a llamar a la línea y columna, por lo mismo en esta parte se va leyendo partes del archivo JSON donde se usaron condicionales para ir viendo que cuando entra una palabra reservada e ir armando cada lexema. Esto fue posible por un “while” para tener ciclos y así seguir dentro de la función mientras se cumplan ciertas condiciones, como notan se usa un puntero el cual se iguala a cero para no acumular demasiada información.

Junto con esto se crearon la clase llamada un diccionario de palabras reservadas las cuales son:


    'OPERACION'         : 'Operacion',
    'RVALOR1'            : 'Valor1',
    'RVALOR2'           : 'Valor2',
    'RSUMA'             : 'Suma',
    'RMULTIPLICACION'   : 'Multiplicacion', 
    'RDIVISION'         : 'Division',
    'RPOTENCIA'         : 'Potencia',
    'RRAIZ'             : 'Raiz',   
    'RINVERSO'          : 'Inverso',
    'RSENO'             : 'Seno',
    'RCOSENO'           : 'Coseno',
    'RTANGENTE'         : 'Tangente',
    'RMODULO'           : 'Modulo',
    'RTEXTO'            : 'Texto',
    'RCOLORFONDONODO'   : 'Color-Fondo-Nodo',
    'RCOLORFUENTENODO'  : 'Color-Fuente-Nodo',
    'RFORMANODO'        : 'Forma-Nodo',  
    'COMA'              : ',',
    'PUNTO'             : '.',
    'DPUNTO'            : ':',
    'CORI'              : '[',
    'CORD'              : ']',
    'LLAVEI'            : '{',
    'LLAVED'            : '}',



La clase tiene varios métodos, pero el principal es `Analizadorlexico`. Es método es el encargado de leer una lista de tokens que se le pasan como argumento, y de acuerdo a los comandos definidos en la lista "comandos", ejecuta distintas acciones dependiendo del comando reconocido en el token actual.

Cada comando está definido como un método dentro de la clase cada una con su funcion las cuales son `CrearBD`, `EliminarBD`. Estos métodos ejecutan distintas acciones según el comando reconocido.

Se creo un método llamado `armar_lexema` aquí recorremos nuestra cadena y si leímos unas comillas se arma el lexema, para que no falle se retorna un None.

    def armar_lexema(cadena):
        global n_lineas
        global n_columnas
        global lista_lexemas
        lexema = ''
        puntero = ''
        for char in cadena:    
                puntero += char
                if char == '\"':        
                    return lexema, cadena[len(puntero):]
                else:
                    lexema += char
        return None, None

Aquí en operaciones se define las operaciones a realizar todo esto fue posible con el métodos abstractos.

 # Interfaz
 
En la interfaz se llamaron las funciones del archivo analizarolexico para que asi crear otras funciones que se usaran en los botones como lo fueron las funciones de `abrir_archivo`, `guardar_archivo`, `analizar`, `buscar_errores`, `gh`, este ultimo para generar la parte grafica a travez de Graphiz. Se coloco el nombre y el tamaño de la pantalla

Para los Frames se necesitaron botones donde cada uno cuenta con un comando que les ayuda a realizar dichas operaciones y mostrar de manera mas cómoda al usuario como usar la interfaz gráfica en cuestión. Con el método `Button` se crearon los botones y se les dio color junto con su forma.

[![Captura-de-pantalla-2023-09-18-174914.png](https://i.postimg.cc/2jFLKLTp/Captura-de-pantalla-2023-09-18-174914.png)](https://postimg.cc/xq8dkCWg)

La interfaz seria la siguiente:

[![cap-7.png](https://i.postimg.cc/W1cKbKgq/cap-7.png)](https://postimg.cc/SJVVggZm)

## AFD del analizar lexico

Este grafo marca de manera teorica como se utilozo los AFD para comprender como poder aplicar la logica de programacion y asi poder llevarla acabo de manera ordenada y funcional.

[![cap-8.png](https://i.postimg.cc/CLh7PgGN/cap-8.png)](https://postimg.cc/QVzcCvn9)
