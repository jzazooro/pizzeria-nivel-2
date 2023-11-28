from ejercicio2 import *

def main():
    documento1 = Documento("Informe1", "Texto", 3333, "Informacion privilegiada...")
    enlace1 = Enlace("Enlace1", "Enlace", 0)
    carpeta1 = Carpeta("Carpeta1")
    carpeta1.agregar_elemento(documento1)
    carpeta1.agregar_elemento(enlace1)
    print("Los elementos de la carpeta son los siguientes:")
    for elemento in carpeta1.elementos:
        print(elemento.nombre)
    proxy_acceso = Proxy()
    proxy_acceso.agregar_usuario_autorizado("usuario1")
    print("Accediendo al documento con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", documento1, "lectura")
    print("Accediendo al documento con el proxy...")
    proxy_acceso.permitir_acceso("usuario2", documento1, "lectura")
    print("Accediendo a la carpeta con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", carpeta1, "lectura")
    print("Accediendo a la carpeta con el proxy...")
    proxy_acceso.permitir_acceso("usuario2", carpeta1, "lectura")
    print("Accediendo al enlace con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", enlace1, "lectura")
    print("Accediendo al enlace con el proxy...")
    proxy_acceso.permitir_acceso("usuario2", enlace1, "lectura")
    print("Los elementos restantes de la carpeta son los siguientes:")
    carpeta1.eliminar_elemento(enlace1)
    for elemento in carpeta1.elementos:
        print(elemento.nombre)
if __name__ == "__main__":
    main()