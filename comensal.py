class Usuario():
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pedido = []

    '''def pedido_actual(self, pizza):
        self.ordenes.append(pizza)

    def ultimo_pedido(self):
        if self.ordenes:
            return self.ordenes[-1]
        else:
            return "no hay pedidos""'''