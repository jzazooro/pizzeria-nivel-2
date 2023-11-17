from abc import ABC, abstractmethod
import csv
import os.path

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
        self.masa = ""
        self.salsa = ""
        self.tamano = ""
        self.ingredientes = []
        self.tecnica = ""
        self.presentacion = ""
    
    @property
    def pizza(self):
        pizza = [self.masa, self.salsa, ', '.join(self.ingredientes), self.tecnica, self.presentacion, self.tamano]
        self.reset()
        return pizza
    
    def crear_masa(self):
        print("Elige el tipo de masa:")
        print("1 - Clásica")
        print("2 - Fina")
        print("3 - Con queso")
        opcion = input("Opción: ")
        if opcion == '1':
            self.masa = "Clasica"
        elif opcion == '2':
            self.masa = "Fina"
        elif opcion == '3':
            self.masa = "Con queso"

    def crear_tamano(self):
        print("Elige el tamaño:")
        print("1 - Familiar")
        print("2 - Normal")
        print("3 - Pequeña")
        opcion = input("Opción: ")
        if opcion == '1':
            self.tamano = "Familiar"
        elif opcion == '2':
            self.tamano = "Normal"
        elif opcion == '3':
            self.tamano = "Pequeña"

    def crear_salsa(self):
        print("Elige el tipo de salsa:")
        print("1 - Barbacoa")
        print("2 - Picante")
        print("3 - Carbonara")
        opcion = input("Opción: ")
        if opcion == '1':
            self.salsa = "Barbacoa"
        elif opcion == '2':
            self.salsa = "Picante"
        elif opcion == '3':
            self.salsa = "Carbonara"

    def crear_ingredientes(self):
        print("Elige los ingredientes para tu pizza (ingresa 'listo' cuando hayas terminado):")
        ingredientes_disponibles = ["Queso", "Pepperoni", "Champiñones", "Jamon", "Pimientos", "Cebolla", "Aceitunas"]
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
        print("Elige la técnica de cocción:")
        print("1 - Horno")
        print("2 - Microondas")
        opcion = input("Opción: ")
        if opcion == '1':
            self.tecnica = "Horno"
        elif opcion == '2':
            self.tecnica = "Microondas"
    
    def crear_presentacion(self):
        print("Elige la presentación:")
        print("1 - Para tomar aqui")
        print("2 - Para llevar")
        opcion = input("Opción: ")
        if opcion == '1':
            self.presentacion = "Para tomar aqui"
        elif opcion == '2':
            self.presentacion = "Para llevar"

class CSVBuilder:
    def crear_csv(self):
        with open('pizza.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Masa", "Salsa", "Ingredientes", "Técnica de cocción", "Presentación", "Tamaño"])
        file.close()

    def añadir_pizza(self, pizza):
        with open('pizza.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(pizza)
        file.close()

class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder
    
    def crear_pizza(self):
        self._builder.crear_masa()
        self._builder.crear_salsa()
        self._builder.crear_ingredientes()
        self._builder.crear_tecnica()
        self._builder.crear_presentacion()
        self._builder.crear_tamano()

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        self._builder = builder

class PedidoCSVBuilder:
    def crear_csv(self):
        with open('pedidos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Cliente", "Pedido"])
        file.close()

    def añadir_pedido(self, cliente, pedido):
        with open('pedidos.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([cliente, pedido])
        file.close()

# ... (código anterior)

if __name__ == "__main__":
    director = PizzaDirector(Pizza())
    builder = director.builder

    csv_builder = CSVBuilder()
    pedido_builder = PedidoCSVBuilder()

    director.crear_pizza()

    pizza = builder.pizza

    print("¡Tu pizza está lista!")
    print("Detalles de la pizza:")
    print("Masa:", pizza[0])
    print("Salsa:", pizza[1])
    print("Ingredientes:", pizza[2])
    print("Técnica de cocción:", pizza[3])
    print("Presentación:", pizza[4])
    print("Tamaño:", pizza[5])

    if not os.path.isfile('pedidos.csv'):
        pedido_builder.crear_csv()

    csv_builder.añadir_pizza(pizza)
    pedido_builder.añadir_pedido("Cliente1", ', '.join(pizza))

    # borrar el csv pizza.csv
