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
        super().__init__("Documento", nombre, tamaño)
        self.tipo = tipo
        self.contenido = contenido

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
        super().__init__("Carpeta", nombre, 0)
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def eliminar_elemento(self, elemento):
        self.elementos.remove(elemento)

    def get_elemento(self, nombre):
        for elemento in self.elementos:
            if elemento.nombre == nombre:
                return elemento

    def get_tamaño(self):
        return sum(elemento.tamaño for elemento in self.elementos)

    def aceptar(self, usuario, accion, proxy):
        proxy.permitir_acceso(usuario, self, accion)
        for elemento in self.elementos:
            elemento.aceptar(usuario, accion, proxy)

class InterfazServicio:
    def permitir_acceso(self, usuario, elemento, accion):
        pass

    def get_registros_acceso(self, elemento):
        pass

    def agregar_usuario_autorizado(self, usuario):
        pass

    def registrar_acceso(self, elemento, accion):
        pass

class Proxy(InterfazServicio):
    def __init__(self):
        self.usuarios_autorizados = []
        self.registros_acceso = {}

    def agregar_usuario_autorizado(self, usuario):
        self.usuarios_autorizados.append(usuario)

    def registrar_acceso(self, elemento, accion):
        ahora = datetime.now()
        nombre_elemento = elemento.nombre
        if nombre_elemento not in self.registros_acceso:
            self.registros_acceso[nombre_elemento] = []
        self.registros_acceso[nombre_elemento].append((accion, ahora))

    def get_registros_acceso(self, elemento):
        nombre_elemento = elemento.nombre
        return self.registros_acceso.get(nombre_elemento, [])

    def permitir_acceso(self, usuario, elemento, accion):
        if usuario in self.usuarios_autorizados:
            self.registrar_acceso(elemento, accion)
            print("Pasa a: ", elemento.nombre, "Registros: ", self.get_registros_acceso(elemento))
            return True
        else:
            print("Por aqui no pasas...")
            return False
