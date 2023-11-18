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
        print("1 - Clasica")
        print("2 - Fina")
        print("3 - Con queso")
        opcion = input("Opcion: ")
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
        opcion = input("Opcion: ")
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
        opcion = input("Opcion: ")
        if opcion == '1':
            self.salsa = "Barbacoa"
        elif opcion == '2':
            self.salsa = "Picante"
        elif opcion == '3':
            self.salsa = "Carbonara"

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
        print("Elige la tecnica de coccion:")
        print("1 - Horno")
        print("2 - Microondas")
        opcion = input("Opcion: ")
        if opcion == '1':
            self.tecnica = "Horno"
        elif opcion == '2':
            self.tecnica = "Microondas"
    
    def crear_presentacion(self):
        print("Elige la presentacion:")
        print("1 - Para tomar aqui")
        print("2 - Para llevar")
        opcion = input("Opcion: ")
        if opcion == '1':
            self.presentacion = "Para tomar aqui"
        elif opcion == '2':
            self.presentacion = "Para llevar"

class PedidoPizzaCSVBuilder:
    def crear_csv(self):
        with open('pedidos_pizza.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Cliente", "Masa", "Salsa", "Ingredientes", "Tecnica de cocción", "Presentacion", "Tamano"])
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

    pedido_builder = PedidoPizzaCSVBuilder()

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

    if not os.path.isfile('pedidos_pizza.csv'):
        pedido_builder.crear_csv()

    pedido_builder.añadir_pedido("Cliente1", pizza)
