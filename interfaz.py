import csv
import tkinter as tk
from PIL import Image, ImageTk
# Funciones de manipulación de usuarios

def usuario_existe(correo):
    with open('usuarios.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == correo:
                return True
    # Código para verificar si el usuario ya existe

def registrar_nuevo_usuario():
    while True:
        print("¡Vamos a crear una cuenta!")
        nombre = input("Ingresa tu nombre: ")
        correo = input("Ingresa tu correo electrónico: ")
        contraseña = input("Ingresa una contraseña: ")

        if nombre.strip() != "" and correo.strip() != "" and contraseña.strip() != "":
            if not usuario_existe(correo):
                with open('usuarios.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([nombre, correo, contraseña])
                    print("Usuario registrado exitosamente. Ahora inicia sesión.")
                    break
            else:
                print("Ya existe un usuario con este correo. Por favor, inicia sesión.")
                break
        else:
            print("Debes completar todos los campos.")

    # Código para registrar un nuevo usuario

def verificar_usuario(correo, contraseña):
    with open('usuarios.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == correo and row[2] == contraseña:
                return True
    return False
    # Código para verificar las credenciales del usuario

# Crear la interfaz gráfica con Tkinter

def crear_interfaz():
    def registrar():
        nombre = nombre_entry.get()
        correo = correo_entry.get()
        contraseña = contraseña_entry.get()

        if nombre.strip() != "" and correo.strip() != "" and contraseña.strip() != "":
            if not usuario_existe(correo):
                with open('usuarios.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([nombre, correo, contraseña])
                    status_label.config(text="Usuario registrado exitosamente. Ahora inicia sesión.")
            else:
                status_label.config(text="Ya existe un usuario con este correo. Por favor, inicia sesión.")
        else:
            status_label.config(text="Debes completar todos los campos.")

    def iniciar_sesion():
        correo = correo_entry.get()
        contraseña = contraseña_entry.get()

        if verificar_usuario(correo, contraseña):
            status_label.config(text="Inicio de sesión exitoso. ¡Disfruta tu estadía!")
            # Aquí podrías redirigir al usuario a la página principal de la pizzería
        else:
            status_label.config(text="Credenciales incorrectas. Inténtalo de nuevo.")

    root = tk.Tk()
    root.title("Registro e Inicio de Sesión")

    image = Image.open("foto1.jpg")  # Cambia "nombre_de_la_imagen.jpg" por tu ruta de imagen
    image = image.resize((1600, 800), Image.ANTIALIAS)  # Ajusta el tamaño según tus preferencias
    photo = ImageTk.PhotoImage(image)

    # Mostrar la imagen como fondo en un label
    background_label = tk.Label(root, image=photo)
    background_label.image = photo  # Conservar una referencia para evitar la recolección de basura
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    nombre_label = tk.Label(root, text="Nombre:")
    nombre_label.pack()
    nombre_entry = tk.Entry(root)
    nombre_entry.pack()

    correo_label = tk.Label(root, text="Correo electrónico:")
    correo_label.pack()
    correo_entry = tk.Entry(root)
    correo_entry.pack()

    contraseña_label = tk.Label(root, text="Contraseña:")
    contraseña_label.pack()
    contraseña_entry = tk.Entry(root, show="*")
    contraseña_entry.pack()

    registro_button = tk.Button(root, text="Registrarse", command=registrar)
    registro_button.pack()

    inicio_sesion_button = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion)
    inicio_sesion_button.pack()

    status_label = tk.Label(root, text="")
    status_label.pack()

    root.mainloop()

# Llama a la función para crear la interfaz
crear_interfaz()
