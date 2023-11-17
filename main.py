import pizzeria
import comensal
import os
def main():
    print("Haga un usuario para hacer su pedido")
    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese su direccion: ")
    usuario = comensal.Usuario(nombre, direccion)
    print("Bienvenido, " + usuario.nombre)
    builder = pizzeria.Pizza()
    director = pizzeria.PizzaDirector(builder)
    director.crear_pizza()
    pizza = builder.pizza
    print("Su pizza es: ", pizza)
    respuesta = input("Desea hacer otro pedido? (si/no): ")
    csv_builder= pizzeria.CSV_Builder()
    while respuesta == "si":
        director.crear_pizza()
        pizza = builder.pizza
        print("Su pizza es: ", pizza)
        respuesta = input("Desea hacer otro pedido? (si/no): ")
        if not os.path.isfile('pizza.csv'):
            csv_builder.crear_csv()
        csv_builder.añadir_pizza(pizza)
    print("Gracias por su compra")

if __name__ == "__main__":
    main()
    