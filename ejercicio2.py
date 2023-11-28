from datetime import datetime

class Elemento: 
    def __init__(self, tipo, nombre, tamaño):
        self.tipo = tipo
        self.nombre = nombre
        self.tamaño = tamaño
        
    def get_nombre(self):
        return self.nombre
    
    def get_tipo(self):
        return self.tipo
    
    def get_tamaño(self):
        return self.tamaño
    
    def aceptar(self, usuario, accion, proxy):
        pass

class Documento(Elemento):
    def __init__(self, nombre, tipo, tamaño, contenido):
        super().__init__(tipo, nombre, tamaño)
        self.contenido=contenido

    def get_contenido(self):
        return self.contenido
    
    def modificar_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido
    
    def aceptar(self, usuario, accion, proxy):
        proxy.permitir_acceso(usuario, self, accion)

class Enlace(Elemento):
    def aceptar(self, usuario, accion, proxy):
        proxy.permitir_acceso(usuario, self, accion)

class Carpeta(Elemento):
    def __init__(self, nombre):
        super().__init__(nombre, "carpeta", 0)
        self.elementos = []

    def agregar_elementos(self, elemento):
        self.elementos.append(elemento)

    def eliminar_elementos(self, elemento):
        self.elementos.remove(elemento)

    def get_elementos(self, nombre):
        for elemento in self.elementos:
            if elemento.nombre() == nombre:
                return elemento
    
    def get_tamaño():
        return sum(elemento.tamaño for elemento in self.elementos)
    
    def aceptar(self, usuario, accion, proxy):
        proxy.permitir_acceso(usuario, self, accion)
        for elemento in self.elementos:
            elemento.aceptar(usuario, accion, proxy)

class InterfazUsuario:
    def permitir_acceso(self, usuario, elemento, accion):
        pass

    def get_registros_acceso(self, elemento):
        pass

    def agregar_usuario_autorizado(self, usuario):
        pass

    def registrar_acceso(self, elemento, accion):
        pass

  
