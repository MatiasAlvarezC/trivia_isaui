import tkinter as tk
import mysql.connector
import time
import tkinter as tk
from PIL import Image, ImageTk

# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="trivia"
)
puntaje = 0
tiempo = 0
cursor = db.cursor()

tiempo_inicio_global = 0
tiempo_final_global = 0
puntaje_final = 0


def guardar_puntaje_tiempo_en_BD(nombre, instagram, puntaje, tiempo):
    # Llamar a la función para guardar los datos del jugador
    guardar_datos_jugador(nombre, instagram, puntaje, tiempo)

# Función para guardar los datos del jugador en la base de datos
def guardar_datos_jugador(nombre, instagram, puntaje, tiempo):
    try:
        # Convierte los segundos y centésimas a un formato compatible con TIME en MySQL
        tiempo_formato = time.strftime('%H:%M:%S', time.gmtime(tiempo))
        
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="trivia"
        )
        cursor = db.cursor()

        query = "INSERT INTO usuarios (nombre_de_usuario, instagram, puntaje, tiempo) VALUES (%s, %s, %s, %s)"
        values = (nombre, instagram, puntaje, tiempo_formato)  # Guarda el tiempo formateado

        cursor.execute(query, values)
        db.commit()

        cursor.close()
        db.close()

        print("Datos del jugador guardados en la base de datos correctamente.")

    except mysql.connector.Error as error:
        print(f"Error al insertar datos del jugador en la base de datos: {error}")



# Función para guardar los datos del jugador en la base de datos
def guardar_datos_jugador(nombre, instagram, puntaje, tiempo):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="trivia"
        )
        cursor = db.cursor()

        # Convertir el tiempo a una cadena con 2 decimales
        tiempo_formateado = "{:.2f}".format(tiempo)  # Formatear el tiempo a 2 decimales
        
        query = "INSERT INTO usuarios (nombre_de_usuario, instagram, puntaje, tiempo) VALUES (%s, %s, %s, %s)"
        values = (nombre, instagram, puntaje, tiempo_formateado)  # Usar el tiempo formateado

        cursor.execute(query, values)
        db.commit()

        cursor.close()
        db.close()

        print("Datos del jugador guardados en la base de datos correctamente.")

    except mysql.connector.Error as error:
        print(f"Error al insertar datos del jugador en la base de datos: {error}")


    

def iniciar_juego():
    global nombre, instagram
    nombre = nombre_entry.get()
    instagram = instagram_entry.get()
    
    # Realizar operaciones con los datos ingresados, como guardar en la base de datos, etc.

    # Cerrar la ventana de inicio y abrir la ventana del juego
    inicio.destroy()
    mostrar_ventana_juego()


# Ventana para ingresar nombre e Instagram
def mostrar_ventana_inicio():
    global inicio, nombre_entry, instagram_entry
    
    inicio = tk.Tk()
    inicio.attributes('-fullscreen', True)

    nombre_label = tk.Label(inicio, text="Nombre", font=('Arial', 20))
    nombre_label.pack()
    nombre_label.pack(pady=25)
    nombre_entry = tk.Entry(inicio, font=('Arial', 16), width=30)  # Aumentar el tamaño de fuente y ancho
    nombre_entry.pack()

    instagram_label = tk.Label(inicio, text="Instagram", font=('Arial', 20))
    instagram_label.pack()
    instagram_label.pack(pady=25)
    instagram_entry = tk.Entry(inicio, font=('Arial', 16), width=30)  # Aumentar el tamaño de fuente y ancho
    instagram_entry.pack()

        # Cargar la imagen
    image_path = "C:\\Users\\Matias\\Desktop\\isaui_40.jpg" # Reemplaza con la ruta de tu imagen
    img = Image.open(image_path)
    img = img.resize((500, 300))  # Ajusta el tamaño de la imagen según sea necesario
    img = ImageTk.PhotoImage(img)

    # Mostrar la imagen debajo del campo de Instagram
    image_label = tk.Label(inicio, image=img)
    image_label.pack()  

    # Botón para iniciar el juego, inicialmente deshabilitado
    jugar_button = tk.Button(inicio, text="Jugar!", command=iniciar_juego, state=tk.DISABLED, font=('Arial', 20))
    jugar_button.pack(pady=25)
    jugar_button.pack()

    # Función para habilitar el botón al ingresar datos
    def habilitar_boton():
        if nombre_entry.get() and instagram_entry.get():
            jugar_button.config(state=tk.NORMAL)

    # Revisar continuamente si hay entrada en los campos para habilitar el botón
    nombre_entry.bind('<KeyRelease>', lambda event: habilitar_boton())
    instagram_entry.bind('<KeyRelease>', lambda event: habilitar_boton())

    inicio.mainloop()

# Función que muestra la ventana del juego
def mostrar_ventana_juego():
    global tiempo_inicio_global
    tiempo_inicio_global = time.time()  # Registra el tiempo de inicio del juego
    # Resto del código de tu función 'mostrar_ventana_juego()'
    pass
    
# Llamar a la función para mostrar la ventana de inicio
mostrar_ventana_inicio()


# Función para iniciar el juego después de ingresar nombre e Instagram
def iniciar_juego():
    nombre = nombre_entry.get()
    instagram = instagram_entry.get()
    
    # Realizar operaciones con los datos ingresados, como guardar en la base de datos, etc.

    # Cerrar la ventana de inicio y abrir la ventana del juego
    inicio.destroy()
    mostrar_ventana_juego()




# Variable para llevar un registro del ID de la última pregunta obtenida
ultima_pregunta_id = 0

# Función para obtener la siguiente pregunta desde la base de datos
def obtener_siguiente_pregunta_desde_bd():
    global ultima_pregunta_id
    cursor.execute("SELECT pregunta, opcion_1, opcion_2, opcion_3, opcion_4, respuesta_correcta, id FROM preguntas_respuestas WHERE id > %s LIMIT 1", (ultima_pregunta_id,))
    pregunta = cursor.fetchone()
    if pregunta:
        ultima_pregunta_id = pregunta[6]  # Actualiza el ID de la última pregunta obtenida
    return pregunta



# Inicializar la ventana
ventana = tk.Tk()
ventana.title('Trivia 40 años ISAUI')

# Obtén el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Establece el tamaño de la ventana para que ocupe toda la pantalla
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")





# Variables
puntaje_actual = 0
pregunta_actual = None
start_time = 0
cronometro = tk.StringVar()
tiempo_inicio_global = 0

def actualizar_cronometro():
    global tiempo_inicio_global
    if tiempo_inicio_global == 0:
        tiempo_inicio_global = time.time()
    
    if tiempo_inicio_global:
        elapsed_time = time.time() - tiempo_inicio_global
        segundos = int(elapsed_time)
        centesimas = int((elapsed_time - segundos) * 100)
        cronometro.set(f'Tiempo transcurrido: {segundos}.{centesimas:02} segundos')
        ventana.after(10, actualizar_cronometro)  # Actualizar cada 10 milisegundos para las centésimas



# Obtener la primera pregunta desde la base de datos
pregunta_actual = obtener_siguiente_pregunta_desde_bd()

# Función para mostrar la pregunta
def mostrar_pregunta():
    global start_time
    start_time = time.time()  # Iniciar el cronómetro
    actualizar_cronometro()
    global pregunta_actual
    pregunta_texto.set(pregunta_actual[0])
    for i in range(4):
        botones_opciones[i].config(text=pregunta_actual[i + 1])
    siguiente_boton.config(state=tk.DISABLED)

# Función para actualizar el puntaje en pantalla   
def actualizar_puntaje():
    puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")

# Función para deshabilitar todos los botones de opciones
def deshabilitar_botones_opciones():
    for boton in botones_opciones:
        boton.config(state=tk.DISABLED)

# Función para verificar la respuesta seleccionada por el usuario
def verificar_respuesta(opcion):
    global puntaje_actual, pregunta_actual
    if opcion == pregunta_actual[5]:
        resultado_texto.set('¡Respuesta Correcta!')
        resultado_label.config(foreground='green')  # Establece el color a verde
        puntaje_actual += 100
        actualizar_puntaje()  # Actualiza el puntaje en pantalla
    else:
        resultado_texto.set('Respuesta Incorrecta')
        resultado_label.config(foreground='red')  # Establece el color a verde
    deshabilitar_botones_opciones()
    # Habilita el botón "Siguiente" para pasar a la siguiente pregunta
    siguiente_boton.config(state=tk.NORMAL)
# Función para habilitar todos los botones de opciones
def habilitar_botones_opciones():
    for boton in botones_opciones:
        boton.config(state=tk.NORMAL)


def mostrar_siguiente_pregunta():
    global nombre, instagram
    global pregunta_actual
    pregunta_actual = obtener_siguiente_pregunta_desde_bd()
    if pregunta_actual is None:
        
        pregunta_texto.set('No hay más preguntas disponibles.')
        tiempo_final_global = time.time()  # Registra el tiempo al responder la última pregunta
        tiempo_final = time.time()  # Registra el tiempo al responder la última pregunta
        # Llamar a la función para guardar el tiempo y puntaje en la base de datos
        guardar_puntaje_tiempo_en_BD(nombre, instagram, puntaje_actual, int(tiempo_final - tiempo_inicio_global))
        ventana.destroy()  # Cierra la ventana actual al finalizar el juego
        mostrar_resultados_usuarios()
        for boton in botones_opciones:
            boton.config(state=tk.DISABLED)
        resultado_texto.set('')  # Restablece el mensaje en blanco
        siguiente_boton.config(state=tk.DISABLED)
        cronometro.set("Fin del juego")
    else:
        mostrar_pregunta()
        habilitar_botones_opciones()
        resultado_texto.set('')
        actualizar_cronometro()

import tkinter as tk
from tkinter import ttk
import mysql.connector


def mostrar_resultados_usuarios():
    resultados_ventana = tk.Tk()
    resultados_ventana.title('Grilla de Usuarios')

    ancho_pantalla = resultados_ventana.winfo_screenwidth()
    alto_pantalla = resultados_ventana.winfo_screenheight()

    resultados_ventana.attributes('-fullscreen', True)

    # Tamaño del Treeview
    tree_ancho = ancho_pantalla // 2
    tree_alto = alto_pantalla // 2

    # Crear un Frame para contener el Treeview
    tree_frame = tk.Frame(resultados_ventana, width=tree_ancho, height=tree_alto)
    tree_frame.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)

    # Crear el Treeview dentro del Frame
    tree = ttk.Treeview(tree_frame)
    tree['columns'] = ('nombre', 'instagram', 'puntaje', 'tiempo')
    tree.column('#0', width=0, stretch=tk.NO)  # Ocultar la columna de ID

    tree.heading('nombre', text='Nombre')
    tree.column('nombre', anchor='center', width=100)
    tree.heading('instagram', text='Instagram')
    tree.column('instagram', anchor='center', width=100)
    tree.heading('puntaje', text='Puntaje')
    tree.column('puntaje', anchor='center', width=75)
    tree.heading('tiempo', text='Tiempo')
    tree.column('tiempo', anchor='center', width=100)

    # Aumentar el tamaño de la fuente
    tree.tag_configure('big_font', font=('Arial', 14))  # Ajustar la fuente aquí (Arial, tamaño 14)

    # Crear Scrollbars para el Treeview
    y_scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
    y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=y_scrollbar.set)

    x_scrollbar = ttk.Scrollbar(tree_frame, orient='horizontal', command=tree.xview)
    x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    tree.configure(xscrollcommand=x_scrollbar.set)

    # Establecer el estilo con el tamaño de fuente grande para los encabezados
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 16, 'bold'))  
    tree.pack(fill=tk.BOTH, expand=True)

  # Configurar el tamaño de fuente para las filas
    tree.tag_configure('big_font', font=('Arial', 12))  # Tamaño de fuente 12
    
    # Conexión a la base de datos y datos del Treeview
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="trivia"
    )
    cursor = db.cursor()

    cursor.execute("SELECT nombre_de_usuario, instagram, puntaje, tiempo FROM usuarios ORDER BY puntaje DESC")
    users = cursor.fetchall()

    for user in users:
        tree.insert('', 'end', values=(user[0], user[1], user[2], user[3]), tags=('big_font'))  # Aplicar el tamaño de fuente
    
    def salir_del_juego():
        resultados_ventana.destroy()
        
    tree.pack(fill=tk.BOTH, expand=True)
    salir_button = tk.Button(resultados_ventana, text="Salir", command=salir_del_juego, font=('Arial', 20))
    salir_button.pack(pady=50, padx=100)  # Ajusta el relleno según lo que necesites
    
    resultados_ventana.mainloop()







# Variables de la interfaz
cronometro_label = tk.Label(ventana, textvariable=cronometro, font=('Arial', 16))
cronometro_label.pack()

pregunta_texto = tk.StringVar()
pregunta_label = tk.Label(ventana, textvariable=pregunta_texto, font=('Arial', 24))
pregunta_label.pack(pady=70)

botones_opciones = []
for i in range(4):
    boton = tk.Button(ventana, text='', font=('Arial', 16), command=lambda i=i: verificar_respuesta(i + 1))
    botones_opciones.append(boton)
    boton.pack(pady=10)

resultado_texto = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_texto, font=('Arial', 16))
resultado_label.pack(pady=10)

siguiente_boton = tk.Button(ventana, text='Siguiente', font=('Arial', 16), command=mostrar_siguiente_pregunta)
siguiente_boton.pack(pady=10)
siguiente_boton.config(state=tk.DISABLED)

puntaje_label = tk.Label(ventana, text=f"Puntaje actual: {puntaje_actual}", font=('Arial', 16))
puntaje_label.pack(pady=10)

# Mostrar la primera pregunta
mostrar_pregunta()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

