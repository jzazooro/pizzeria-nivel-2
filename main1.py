from ejercicio1_1 import *
from ejercicio1_2 import *
import csv
import os.path
from abc import ABC, abstractmethod



def main():

    iniciar_sesion_o_registrar() 
    
    director = PizzaDirector(Pizza())
    builder = director.builder
    pedido_builder = PedidoPizzaCSVBuilder()
    director.crear_pizza()
    pizza = builder.pizza
    print("¡Tu pizza está lista!")
    print("Detalles de la pizza:")
    print("Tamano:", pizza[0])
    print("Masa:", pizza[1])
    print("Ingredientes:", pizza[2])
    print("Salsa:", pizza[3])
    print("Tecnica de coccion:", pizza[4])
    print("Presentacion:", pizza[5])
    if not os.path.isfile('pedidos_pizza.csv'):
        pedido_builder.crear_csv()
    pedido_builder.añadir_pedido("cliente1", pizza)
    
    try:
        bebidas = {
            "Aguita refrescante": "Aguita refrescante",
            "Flameado de Moe": "Flameado de Moe",
            "Cerveza": "Cerveza",
            "Nada": "Nada"
        }
        
        print("Elige tu bebida:")
        seleccion_bebida = obtener_seleccion(bebidas)
        
        postres = {
            "Banana split": "Banana split",
            "Dorayaki": "Dorayaki",
            "Batipasas": "Batipasas",
            "Nada": "Nada"
        }
        
        print("Elige tu postre:")
        seleccion_postre = obtener_seleccion(postres)
        
        entrantes = {
            "Nachos guerrero": "Nachos guerrero",
            "Enchilada": "Enchilada",
            "Taco": "Taco",
            "Nada": "Nada"
        }
        
        print("Elige tu entrante:")
        seleccion_entrante = obtener_seleccion(entrantes)
        
        nueva_fila = ['elemento1', 'elemento2', 'elemento3', 'elemento4']


        nombre_archivo = 'complementos.csv'
        with open(nombre_archivo, mode='a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(nueva_fila)

    except ValueError as e:
        print("Error: Ingresa un número válido.")
    
    lista_selecciones = [seleccion_bebida, seleccion_postre, seleccion_entrante]
    cantidad_nada = lista_selecciones.count('Nada')
    preciocomplementos= (3-cantidad_nada)*4
    print("El precio de los complementos es: ", preciocomplementos, "€")
    print("El precio de la pizza es de: ", 8, "€")
    preciototal=preciocomplementos+8
    if preciototal == 20:
        print("Al haber pedidO entrante, pizza, bebida y postre forma un menu individual de tarifa reducida, el nuevo precio es de 15 euros")
        preciototal=15
    print("El precio total es de: ", preciototal, "€")



if __name__ == "__main__":
    main()
