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
    