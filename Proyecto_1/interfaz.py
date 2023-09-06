import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import Tk
from analizadorlexico import instruccion, operar2, getErrores

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
boton_reporte = tk.Button(banda_superior, font=("Century Gothic", 12),  bg="#ACA8F0", text="REPORTE", command=buscar_errores)
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
