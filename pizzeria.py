from abc import ABC, abstractmethod
import csv
import os.path

class PizzaBuilder(ABC):
    @property
    @abstractmethod
    def crear_pizza(self):
        pass

    @abstractmethod
    def crear_masa(self):
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

    @abstractmethod
    def crear_extras(self):
        pass

    @abstractmethod
    def crear_bebidas(self):
        pass

class Pizza:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.masa = ""
        self.salsa = ""
        self.ingrediente = []
        self.tecnica = ""
        self.presentacion = ""
        self.extras = ""
        self.bebidas = ""
    
    @property
    def pizza(self):
        pizza = [self.masa, self.salsa, self.ingrediente, self.tecnica, self.presentacion, self.extras, self.bebidas]
        self.reset()
        return pizza
    def crear_masa(self):
        masa= input("Ingrese el tipo de masa: ")
        self.masa = masa

    def crear_salsa(self):
        salsa = input("Ingrese el tipo de salsa: ")
        self.salsa = salsa

    def crear_ingrediente(self):
        respuesta = "si"
        while respuesta == "si":
            ingrediente = input("Ingrese un ingrediente: ")
            self.ingrediente.append(ingrediente)
            respuesta = input("Desea agregar otro ingrediente? si/no: ")

    def crear_tecnica(self):
        tecnica = input("Ingrese la tecnica de coccion: ")
        self.tecnica = tecnica
    
    def crear_presentacion(self):
        presentacion = input("Ingrese la presentacion: ")
        self.presentacion = presentacion

    def crear_extras(self):
        extras = input("Ingrese los extras: ")
        self.extras = extras
    
    def crear_bebidas(self):
        bebidas = input("Ingrese las bebidas: ")
        self.bebidas = bebidas
class Producto():
    def __init__(self):
        self.pizza = []

    def add(self, parte):
        self.pizza.append(parte)
    
    def __str__(self):
        return f"Partes de la pizza: {','.join(self.pizza)}"
    
class CSV_Builder():
    def crear_csv(self):
        with open('pizza.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["masa", "salsa", "ingrediente", "tecnica", "presentacion", "extras", "bebidas"])
        file.close()
    def añadir_pizza(self, pizza):
        with open('pizza.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([pizza[0], pizza[1], pizza[2], pizza[3], pizza[4], pizza[5], pizza[6]])
        file.close()

class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder
    
    def crear_pizza(self):
        self._builder.crear_masa()
        self._builder.crear_salsa()
        self._builder.crear_ingrediente()
        self._builder.crear_tecnica()
        self._builder.crear_presentacion()
        self._builder.crear_extras()
        self._builder.crear_bebidas()

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        self._builder = builder
        