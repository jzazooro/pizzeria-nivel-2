import ejercicio2 as es

def main():
    documento1 = es.Documento("Informe1", "Texto", "Contenido confidencial...")
    enlace1 = es.Enlace("Enlace1", "Enlace", 0)
    carpeta1 = es.Carpeta("Carpeta1")
    carpeta1.agregar_elementos(documento1)
    carpeta1.agregar_elementos(enlace1)
    print("Elementos de la carpeta: ")
    for i in range(len(carpeta1.elementos)):
        print(carpeta1.elementos[i].nombre)

    proxy_acceso = es.Proxy()
    proxy_acceso.agregar_usuario_autorizado("usuario1")

    print("Intentando acceder al documento con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", documento1, "lectura") 
    print("Intentando acceder al enlace con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", enlace1, "lectura")

    print("Intentando acceder a la carpeta con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", carpeta1, "lectura")
    print("Intentando acceder a la carpeta con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", carpeta1, "escritura")

    print("Intentando acceder a la carpeta con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", carpeta1, "lectura")
    print("Intentando acceder a la carpeta con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", carpeta1, "escritura")

    print("Elementos restantes de la carpeta: ")
    carpeta1.eliminar_elementos(enlace1)
    for i in range(len(carpeta1.elementos)):
        print(carpeta1.elementos[i].nombre)