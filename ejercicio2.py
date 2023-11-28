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

class Carpeta(Elemento):
    