import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import Tk
from analizadorlexico import *
import tkinter.messagebox as messagebox
import subprocess

def abrir_archivo():
    x = ""
    Tk().withdraw()
    try:
        filename = askopenfilename(title='Selecciona un archivo', filetypes=[('Archivos', f'*.json')])
        with open(filename, encoding='utf-8') as infile:
            x = infile.read()
                                        
    except: 
        print("Error, no se ha seleccionado ningún archivo")
        return
    
    texto.delete("1.0", tk.END)  # Limpia el contenido actual del widget de texto
    texto.insert('1.0', x)

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, 'w') as file:
            file.write(texto.get(1.0, tk.END))

def analizar():
    instruccion(texto.get("1.0", tk.END))  # Obtener el texto del widget de texto
    respuestas = operar2()
    resultado = ""
    for respuesta in respuestas:
        resultado += str(respuesta.operar(None)) + "\n"
    texto.delete("1.0", tk.END)  # Limpia el contenido actual del widget de resultado_text
    texto.insert('1.0', format(resultado))
    
def analizar():
    data = texto.get("1.0", tk.END)  # Obtener el contenido del widget de texto
    instrucciones = instruccion(data)
    respuestas_Operaciones = operar2()

    Resultados = ''
    Operacion = 1

    configuracion = 1
    salto = "\n"

    for respuesta in respuestas_Operaciones:
        if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
            Resultados += str(f"Operacion {Operacion} --> {respuesta.tipo.operar(None)} = {respuesta.operar(None)}\n")
            Operacion += 1

    texto.delete("1.0", tk.END)  # Limpia el contenido actual del widget de resultado_text
    texto.insert('1.0', format(Resultados))


def buscar_errores():
    lista_errores = getErrores()
    w = 1
    resultado = "{\n"
    while lista_errores:
        error = lista_errores.pop(0)
        resultado += error.operar(w) + "\n"
        w += 1
    resultado += "}"
    texto.delete("1.0", tk.END)  # Limpia el contenido actual del widget de texto
    texto.insert(tk.END, resultado)
    messagebox.showinfo("Éxito", "El archivo se generó correctamente.")


def gh():
    try:
        operar2().clear()

        data = texto.get("1.0", tk.END)  # Obtener el contenido del widget de texto
        instrucciones = instruccion(data)
        respuestas_Operaciones = operar2()

        contenido = "digraph G {\n\n"  # CREAMOS NUESTRO ARCHIVO CON COMANDOS
        r = open("Operaciones.dot", "w", encoding="utf-8")
        contenido += str(Graphviz(respuestas_Operaciones))
        contenido += '\n}'

        r.write(contenido)
        r.close()

        # Generar la imagen PNG desde el archivo DOT
        subprocess.run(["dot", "-Tpng", "Operaciones.dot", "-o", "Imagen Operaciones.png"])

        print("...............................................................")
        print("            ** COMANDOS DE GRAPHVIZ **               ")
        print("")
        print(contenido)
        print("...............................................................")
        print("")
        print("Imagen generada como Operaciones.png")

    except Exception as e:
        messagebox.showinfo("Se produjo un error: ", str(e))
        messagebox.showinfo("Mensaje", f"Error al generar el archivo de salida, Verificar el Archivo de entrada.")
    else:
        messagebox.showinfo("Mensaje", "Grafica generada con éxito")
        respuestas_Operaciones.clear()
        instrucciones.clear()
    
def Graphviz(respuestas_Operaciones):
        Titulo = "Realizacion de Operaciones"
        colorNodo = "yellow"
        fuenteNodo = "black"
        formaNodo = "circle "
        try:
            print('---------------------------------------------')
            for respuesta in respuestas_Operaciones:
                if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
                    pass
                else:
                    temporal = str(respuesta.texto.operar(None)).lower()
                    print(respuesta.texto.operar(None))
                    print(respuesta.ejecutarT())
                    if respuesta.ejecutarT() == "texto":  # Podemos recibir cualquier texto
                        Titulo = str(respuesta.texto.operar(None))
                    if respuesta.ejecutarT() == "color-fondo-nodo":  # Vericar el color del nodo a asignar
                        if temporal == ("amarillo" or "yellow"):
                            temporal = "yellow"
                            colorNodo = temporal
                        elif temporal == ("verde" or "green"):
                            temporal = "green"
                            colorNodo = temporal
                        elif temporal == ("azul" or "blue"):
                            temporal = "blue"
                            colorNodo = temporal
                        elif temporal == ("rojo" or "red"):
                            temporal = "red"
                            colorNodo = temporal
                        elif temporal == ("morado" or "purple"):
                            temporal = "purple"
                            colorNodo = temporal

                    if respuesta.ejecutarT() == "color-fuente-nodo":  # Vericar la fuente del nodo a asignar

                        if temporal == ("amarillo" or "yellow"):
                            temporal = "yellow"
                            fuenteNodo = temporal
                        elif temporal == ("verde" or "green"):
                            temporal = "green"
                            fuenteNodo = temporal
                        elif temporal == ("azul" or "blue"):
                            temporal = "blue"
                            fuenteNodo = temporal
                        elif temporal == ("rojo" or "red"):
                            temporal = "red"
                            fuenteNodo = temporal
                        elif temporal == ("morado" or "purple"):
                            temporal = "purple"
                            fuenteNodo = temporal
                        elif temporal == ("negro" or "black"):
                            temporal = "black"
                            fuenteNodo = temporal

                    if respuesta.ejecutarT() == "forma-nodo":  # Vericar el formato de nodo a asignar
                        if temporal == ("circulo" or "circle"):
                            temporal = "circle"
                            formaNodo = temporal
                        elif temporal == ("cuadrado" or "square"):
                            temporal = "square"
                            formaNodo = temporal
                        elif temporal == ("triangulo" or "triangle"):
                            temporal = "triangle"
                            formaNodo = temporal
                        elif temporal == ("rectangulo" or "box"):
                            temporal = "box"
                            formaNodo = temporal
                        elif temporal == ("elipse" or "ellipse"):
                            temporal = "ellipse"
                            formaNodo = temporal

            temporal = ''
            CnumIzquierdo = 0
            CnumDerecho = 0
            Crespuesta = 0
            Ctotal = 0

            text = ""
            text += f"\tnode [shape={formaNodo}]\n"

            text += f"\tnodo0 [label = \"{Titulo}\"]\n"
            text += f"\tnodo0" + "[" + f"fontcolor = {fuenteNodo}" + "]\n"

            for respuesta in respuestas_Operaciones:
                CnumIzquierdo += 1
                CnumDerecho += 1
                Crespuesta += 1
                Ctotal += 1

                if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:

                    text += f"\tnodoRespuesta{Crespuesta}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n"
                    text += f"\tnodoIzqu{CnumIzquierdo}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n"
                    text += f"\tnodoDere{CnumDerecho}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n"
                    text += f"\tnodoT{Ctotal}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n"

                    text += f"\tnodoRespuesta{Crespuesta}" + f"[label = \"{str(respuesta.tipo.operar(None))}: " + "\"]\n"
                    text += f"\tnodoIzqu{CnumIzquierdo}" + "[label = \"Valor1: " + f" {str(respuesta.left.operar(None))} " + "\"]\n"
                    text += f"\tnodoDere{CnumDerecho}" + "[label = \"Valor2: " + f" {str(respuesta.right.operar(None))} " + "\"]\n"

                    text += f"\tnodoRespuesta{Crespuesta} -> nodoIzqu{CnumIzquierdo}\n"
                    text += f"\tnodoRespuesta{Crespuesta} -> nodoDere{CnumDerecho}\n"

                    text += f"\tnodoT{Ctotal}" + f"[label = \"{respuesta.operar(None)}" + "\"]\n"
                    text += f"\tnodoT{Ctotal} -> nodoRespuesta{Crespuesta}\n"

                else:
                    pass

            return text
        except Exception as e:
            messagebox.showinfo("Se produjo un error: ",str(e))
            messagebox.showinfo("Mensaje", "Error en los comandos de Graphviz")

    
ventana = tk.Tk()
ventana.title("ANALIZADOR LEXICO")

ancho_ventana = 900
alto_ventana = 700
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")


banda_superior = tk.Frame(ventana, bg="#E69EDB")
banda_superior.pack(fill=tk.X)

menu_archivo = tk.Menu(ventana)
ventana.config(menu=menu_archivo)

submenu_archivo = tk.Menu(menu_archivo, tearoff=0)
menu_archivo.add_cascade(label="Archivo", menu=submenu_archivo)
submenu_archivo.add_command(label="Abrir Archivo", command=abrir_archivo)
submenu_archivo.add_command(label="Guardar", command=guardar_archivo)
submenu_archivo.add_command(label="Guardar Como", command=guardar_archivo)

boton_analizar = tk.Button(banda_superior, font=("Century Gothic", 12), bg="#ACA8F0", text="ANALIZAR", command=analizar)
boton_errores = tk.Button(banda_superior, font=("Century Gothic", 12), bg="#ACA8F0", text="ERRORES", command=buscar_errores)
boton_reporte = tk.Button(banda_superior, font=("Century Gothic", 12),  bg="#ACA8F0", text="REPORTE", command=gh)
boton_salir = tk.Button(banda_superior, font=("Century Gothic", 12), bg="#ACA8F0", text="SALIR", command=ventana.quit)

boton_analizar.pack(side=tk.LEFT, padx=10, pady=10)
boton_errores.pack(side=tk.LEFT, padx=10, pady=10)
boton_reporte.pack(side=tk.LEFT, padx=10, pady=10)
boton_salir.pack(side=tk.LEFT, padx=10, pady=10)

texto = tk.Text(ventana, wrap=tk.WORD, height=20, width=50)
scroll_y = tk.Scrollbar(ventana, orient=tk.VERTICAL, command=texto.yview)
texto.pack(fill=tk.BOTH, expand=True, padx=70, pady=100)


ventana.configure(bg='#ECECEC')
texto.configure(bg='#F9F9F9')
ventana.configure(bg='#A1AFE6') #EL color del fondo
ventana.mainloop()


