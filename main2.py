from ejercicio2 import *

def main():
    documento1 = Documento("Informe1", "Texto", 1024, "Contenido confidencial...")
    enlace1 = Enlace("Enlace1", "Enlace", 0)
    carpeta1 = Carpeta("Carpeta1")
    carpeta1.agregar_elemento(documento1)
    carpeta1.agregar_elemento(enlace1)

    print("Elementos de la carpeta:")
    for elemento in carpeta1.elementos:
        print(elemento.nombre)

    proxy_acceso = Proxy()
    proxy_acceso.agregar_usuario_autorizado("usuario1")

    print("Intentando acceder al documento con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", documento1, "lectura")
    print("Intentando acceder al documento con el proxy...")
    proxy_acceso.permitir_acceso("usuario2", documento1, "lectura")

    print("Intentando acceder a la carpeta con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", carpeta1, "lectura")
    print("Intentando acceder a la carpeta con el proxy...")
    proxy_acceso.permitir_acceso("usuario2", carpeta1, "lectura")

    print("Intentando acceder al enlace con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", enlace1, "lectura")
    print("Intentando acceder al enlace con el proxy...")
    proxy_acceso.permitir_acceso("usuario2", enlace1, "lectura")

    print("Elementos restantes de la carpeta:")
    carpeta1.eliminar_elemento(enlace1)
    for elemento in carpeta1.elementos:
        print(elemento.nombre)

if __name__ == "__main__":
    main()
