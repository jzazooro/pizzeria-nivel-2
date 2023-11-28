import csv
from abc import ABC, abstractmethod
import os.path
from typing import Dict

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








class PizzaBuilder(ABC):
    @abstractmethod
    def crear_masa(self):
        pass
    
    @abstractmethod
    def crear_tamano(self):
        pass
    
    @abstractmethod
    def crear_salsa(self):
        pass
    
    @abstractmethod
    def crear_ingredientes(self):
        pass
    
    @abstractmethod
    def crear_tecnica(self):
        pass
    
    @abstractmethod
    def crear_presentacion(self):
        pass

class Pizza(PizzaBuilder):
    def __init__(self):
        self.reset()
        
    def reset(self):    
        self.tamano = ""
        self.masa = ""
        self.ingredientes = []
        self.salsa = ""
        self.tecnica = ""
        self.presentacion = ""
    
    @property
    def pizza(self):
        pizza = [self.tamano, self.masa, ', '.join(self.ingredientes), self.salsa, self.tecnica, self.presentacion]
        self.reset()
        return pizza

    def crear_masa(self):
        while True:
            print("Elige el tipo de masa:")
            print("1 - Clasica")
            print("2 - Fina")
            print("3 - Con queso")
            opcion = input("Opcion: ")
            if opcion == '1':
                self.masa = "Clasica"
                break
            elif opcion == '2':
                self.masa = "Fina"
                break
            elif opcion == '3':
                self.masa = "Con queso"
                break
            else:
                print("Por favor, elige una opcion valida (1, 2, o 3)")


    def crear_tamano(self):
        while True:
            print("Elige el tamano:")
            print("1 - Familiar")
            print("2 - Normal")
            print("3 - Pequena")
            opcion = input("Opcion: ")
            if opcion == '1':
                self.tamano = "Familiar"
                break
            elif opcion == '2':
                self.tamano = "Normal"
                break
            elif opcion == '3':
                self.tamano = "Pequena"
                break
            else:
                print("Por favor, elige una opción valida (1, 2, o 3)")

    def crear_salsa(self):
        while True:
            print("Elige el tipo de salsa:")
            print("1 - Barbacoa")
            print("2 - Picante")
            print("3 - Carbonara")
            opcion = input("Opcion: ")
            if opcion == '1':
                self.salsa = "Barbacoa"
                break
            elif opcion == '2':
                self.salsa = "Picante"
                break
            elif opcion == '3':
                self.salsa = "Carbonara"
                break
            else:
                print("Por favor, elige una opcion valida (1, 2, o 3)")


    def crear_ingredientes(self):
        print("Elige los ingredientes para tu pizza (ingresa 'listo' cuando hayas terminado):")
        ingredientes_disponibles = ["Queso", "Pepperoni", "Champinones", "Jamon", "Pimientos", "Cebolla", "Aceitunas"]
        while True:
            print(f"Ingredientes disponibles: {', '.join(ingredientes_disponibles)}")
            ingrediente = input("Ingrediente: ")
            if ingrediente.lower() == 'listo':
                break
            if ingrediente in ingredientes_disponibles:
                self.ingredientes.append(ingrediente)
                ingredientes_disponibles.remove(ingrediente)
            else:
                print("Ingrediente no disponible. Elige otro.")

    def crear_tecnica(self):
        while True:
            print("Elige la tecnica de coccion:")
            print("1 - Horno")
            print("2 - Microondas")
            opcion = input("Opcion: ")
            if opcion == '1':
                self.tecnica = "Horno"
                break
            elif opcion == '2':
                self.tecnica = "Microondas"
                break
            else:
                print("Por favor, elige una opción valida (1 o 2)")

    def crear_presentacion(self):
        while True:
            print("Elige la presentacion:")
            print("1 - Para tomar aqui")
            print("2 - Para llevar")
            opcion = input("Opcion: ")
            if opcion == '1':
                self.presentacion = "Para tomar aqui"
                break
            elif opcion == '2':
                self.presentacion = "Para llevar"
                break
            else:
                print("Por favor, elige una opción valida (1 o 2)")


class PedidoPizzaCSVBuilder:
    def crear_csv(self):
        with open('pedidos_pizza.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Cliente", "Tamano", "Masa", "Ingredientes", "Salsa", "Tecnica de coccion", "Presentacion"])
        file.close()

    def añadir_pedido(self, cliente, pizza):
        with open('pedidos_pizza.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([cliente] + pizza)
        file.close()

class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder
    
    def crear_pizza(self):
        self._builder.crear_tamano()
        self._builder.crear_masa()
        self._builder.crear_ingredientes()
        self._builder.crear_salsa()
        self._builder.crear_tecnica()
        self._builder.crear_presentacion()

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        self._builder = builder

class Producto(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def descripcion(self):
        pass

class Bebida(Producto):
    opciones_bebidas = ["Aguita refrescante", "Flameado de Moe", "Cerveza", "Nada"]

    def __init__(self, nombre, seleccion):
        super().__init__(nombre)
        if seleccion in self.opciones_bebidas:
            self.seleccion = seleccion
        else:
            raise ValueError("Opción de bebida no válida")

    def descripcion(self):
        return f"{self.nombre}: {self.seleccion}"

class Postre(Producto):
    opciones_postres = ["Banana split", "Dorayaki", "Batipasas", "Nada"]

    def __init__(self, nombre, seleccion):
        super().__init__(nombre)
        if seleccion in self.opciones_postres:
            self.seleccion = seleccion
        else:
            raise ValueError("Opción de postre no válida")

    def descripcion(self):
        return f"{self.nombre}: {self.seleccion}"

class Entrante(Producto):
    opciones_entrantes = ["Nachos guerrero", "Enchilada", "Taco", "Nada"]

    def __init__(self, nombre, seleccion):
        super().__init__(nombre)
        if seleccion in self.opciones_entrantes:
            self.seleccion = seleccion
        else:
            raise ValueError("Opción de entrante no válida")

    def descripcion(self):
        return f"{self.nombre}: {self.seleccion}"


def mostrar_opciones(opciones: Dict[str, str]) -> None:
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

def mostrar_opciones(opciones: Dict[str, str]) -> None:
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

def seleccion_valida(opcion: int, opciones: Dict[str, str]) -> bool:
    return 1 <= opcion <= len(opciones)

def obtener_seleccion(opciones: Dict[str, str]) -> str:
    while True:
        mostrar_opciones(opciones)
        opcion = input("Ingresa el número correspondiente: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if seleccion_valida(opcion, opciones):
                return list(opciones.values())[opcion - 1]
        print("Error: Ingresa un número válido.")
