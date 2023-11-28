from abc import ABC, abstractmethod
import csv
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

# ... (las clases Bebida, Postre, Entrante se mantienen igual)

def mostrar_opciones(opciones: Dict[str, str]) -> None:
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

try:
    bebidas = {
        "Aguita refrescante": "Aguita refrescante",
        "Flameado de Moe": "Flameado de Moe",
        "Cerveza": "Cerveza",
        "Nada": "Nada"
    }

    print("Elige tu bebida:")
    mostrar_opciones(bebidas)
    opcion_bebida = int(input("Ingresa el número correspondiente: "))
    opcion_seleccionada_bebida = list(bebidas.values())[opcion_bebida - 1]

    postres = {
        "Banana split": "Banana split",
        "Dorayaki": "Dorayaki",
        "Batipasas": "Batipasas",
        "Nada": "Nada"
    }

    print("Elige tu postre:")
    mostrar_opciones(postres)
    opcion_postre = int(input("Ingresa el número correspondiente: "))
    opcion_seleccionada_postre = list(postres.values())[opcion_postre - 1]

    entrantes = {
        "Nachos guerrero": "Nachos guerrero",
        "Enchilada": "Enchilada",
        "Taco": "Taco",
        "Nada": "Nada"
    }

    print("Elige tu entrante:")
    mostrar_opciones(entrantes)
    opcion_entrante = int(input("Ingresa el número correspondiente: "))
    opcion_seleccionada_entrante = list(entrantes.values())[opcion_entrante - 1]

    # Guardar las selecciones en un archivo CSV
    with open('complementos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Bebida', 'Postre', 'Entrante'])
        writer.writerow([opcion_seleccionada_bebida, opcion_seleccionada_postre, opcion_seleccionada_entrante])

    print("Selecciones guardadas en 'complementos.csv'")
except (ValueError, IndexError) as e:
    print("Error: Ingresa un número válido.")