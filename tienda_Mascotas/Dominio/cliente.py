import uuid
from tienda_Mascotas.Dominio.persona import Persona


class Cliente(Persona):
    def __init__(self, codigoCliente, nombre, apellido, cedula, genero, direccion, correo, edad, tiempoCliente):
        super().__init__(nombre, apellido, cedula, genero, direccion, correo, edad)
        self.codigoCliente = codigoCliente
        self.tiempoCliente = tiempoCliente

    def __repr__(self):
        representacion = "Cliente:" + " " + str(self.nombre) + " " + str(
            self.apellido) + " " + "Identificado con cedula:" + " " + str(self.cedula)
        return representacion

    def cumple(self, especificacion):
        dict_cliente = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_cliente or dict_cliente[k] != especificacion.get_value(k):
                return False
        return True

    def modificarTiempoCliente(self, nuevoTiempo):
        self.tiempoCliente = nuevoTiempo
