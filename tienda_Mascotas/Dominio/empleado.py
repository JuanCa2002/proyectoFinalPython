import uuid
from tienda_Mascotas.Dominio.persona import Persona


class Empleado(Persona):
    def __init__(self, codigo, nombre, cedula, apellido, cargo, salario, genero, edad, direccion, correo,
                 horario):

        super().__init__(nombre, apellido, cedula, genero, direccion, correo, edad)
        self.codigo = codigo
        self.cargo = cargo
        self.horario = horario
        self.salario = salario

    def __repr__(self):
        representacion = "Empleado:" + str(self.nombre) + " " + str(self.apellido) + " " + "Con cargo de:" + str(
            self.cargo)
        return representacion

    def ascenso(self, nuevoCargo):
        self.cargo = nuevoCargo

    def aumento(self, nuevoSalario):
        self.salario = nuevoSalario

    def cambioHorarioLaboral(self, nuevoHorario):
        self.horario = nuevoHorario

    def cumple(self, especificacion):
        dict_empleado = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_empleado or dict_empleado[k] != especificacion.get_value(k):
                return False
        return True
