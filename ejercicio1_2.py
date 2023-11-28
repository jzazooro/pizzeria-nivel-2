import csv
from abc import ABC, abstractmethod
import os.path
from typing import Dict

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
