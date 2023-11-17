import csv

# Función para verificar si un usuario ya está registrado
def usuario_existente(correo):
    with open('usuarios.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == correo:
                return True
    return False

# Función para registrar un nuevo usuario si no existe previamente
def registrar_usuario():
    while True:
        print("¡Vamos a crear una cuenta!")
        nombre = input("Ingresa tu nombre: ")
        correo = input("Ingresa tu correo electrónico: ")
        contraseña = input("Ingresa una contraseña: ")

        if nombre.strip() != "" and correo.strip() != "" and contraseña.strip() != "":
            if not usuario_existente(correo):
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

# Función para verificar si el usuario existe en el archivo CSV
def verificar_usuario(correo, contraseña):
    with open('usuarios.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == correo and row[2] == contraseña:
                return True
    return False

# Interacción con el usuario
def iniciar_sesion_o_registrar():
    print("Bienvenido a la pizzería")
    opcion = input("¿Estás registrado? (sí/no): ")

    if opcion.lower() == 'no':
        registrar_usuario()
        iniciar_sesion_o_registrar()
    elif opcion.lower() == 'sí':
        correo = input("Ingresa tu correo electrónico: ")
        contraseña = input("Ingresa tu contraseña: ")
        if verificar_usuario(correo, contraseña):
            print("Inicio de sesión exitoso. ¡Disfruta tu estadía!")
            # Aquí podrías redirigir al usuario a la página principal de la pizzería
        else:
            print("Credenciales incorrectas. Inténtalo de nuevo.")
            iniciar_sesion_o_registrar()
    else:
        print("Opción no válida. Por favor, responde 'sí' o 'no'.")
        iniciar_sesion_o_registrar()

# Iniciar el proceso de inicio de sesión o registro
iniciar_sesion_o_registrar()