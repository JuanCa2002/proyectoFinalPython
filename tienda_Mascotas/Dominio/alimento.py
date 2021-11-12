import uuid
from tienda_Mascotas.Dominio.elementoCompra import ElementoCompra


class Alimento(ElementoCompra):
    def __init__(self, codigoAlimento, tipoAlimento, nombre, cantidadAlimento,
                 cantidadContenido, precio):

        super().__init__(cantidadAlimento, precio)
        self.codigoAlimento = codigoAlimento
        self.tipoAlimento = tipoAlimento
        self.nombreProducto = nombre
        self.cantidadAlimento = cantidadAlimento
        self.cantidadContenido = cantidadContenido
        self.precio = precio

    def __repr__(self):
        representacion = "Codigo:" + " " + str(self.codigoAlimento) + " " + "Nombre:" + str(
            self.nombreProducto) + " " + "Alimento para:" + str(self.tipoAlimento) + "" \
                                                                                     "Con un precio de:" + " " + str(
            self.precio)
        return representacion

    def cumple(self, especificacion):
        dict_alimento = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_alimento or dict_alimento[k] != especificacion.get_value(k):
                return False
        return True
