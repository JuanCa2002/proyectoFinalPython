import uuid
from tienda_Mascotas.Dominio.elementoCompra import ElementoCompra


class Mascota(ElementoCompra):
    def __init__(self, codigoMascota, tipoMascota, raza, nombre, edad, precio, cantidad):

        super().__init__(cantidad, precio)
        self.tipoMascota = tipoMascota
        self.codigoMascota = codigoMascota
        self.raza = raza
        self.edad = edad
        self.nombre = nombre

    def __repr__(self):
        representacion = "La mascota es un:" + " " + str(self.tipoMascota) + " " + "De raza:" + " " + str(
            self.raza) + " " \
                         "Con edad:" + " " + str(self.edad) + " " + "Y un precio de:" + " " + str(self.precio)
        return representacion

    def cumpleaños(self, nueva_Edad):
        self.edad = nueva_Edad

    def cumple(self, especificacion):
        dict_mascota = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_mascota or dict_mascota[k] != especificacion.get_value(k):
                return False
        return True
