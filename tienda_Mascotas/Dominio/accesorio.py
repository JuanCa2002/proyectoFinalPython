import uuid
from tienda_Mascotas.Dominio.elementoCompra import ElementoCompra


class Accesorio(ElementoCompra):
    def __init__(self, codigoAccesorio, nombre, cantidadAccesorio, precioAccesorio, descripcionAccesorio,
                 usoAccesorio):
        super().__init__(cantidadAccesorio, precioAccesorio)
        self.codigoAccesorio = codigoAccesorio
        self.nombreAccesorio = nombre
        self.descripcionAccesorio = descripcionAccesorio
        self.usoAccesorio = usoAccesorio

    def __repr__(self):
        representacion = "Accesorio:" + " " + self.nombreAccesorio + " " + "Con precio:" + " " + str(
            self.precio) + " " + "Y uso de:" + " " + str(self.usoAccesorio)
        return representacion

    def cumple(self, especificacion):
        dict_accesorio = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_accesorio or dict_accesorio[k] != especificacion.get_value(k):
                return False
        return True
