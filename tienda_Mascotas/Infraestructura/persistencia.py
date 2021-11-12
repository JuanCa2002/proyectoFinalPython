import sqlite3
import jsonpickle

from tienda_Mascotas.Dominio.especificacion import Especificacion
from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Dominio.mascota import Mascota
from tienda_Mascotas.Dominio.empleado import Empleado
from tienda_Mascotas.Dominio.cliente import Cliente
from tienda_Mascotas.Dominio.alimento import Alimento
from tienda_Mascotas.Dominio.accesorio import Accesorio
from tienda_Mascotas.Dominio.venta import Venta
from tienda_Mascotas.Infraestructura.configuracion import Configuracion


class Persistencia:
    def __init__(self):
        self.con = sqlite3.connect("la_tienda_de_mascotas.sqlite")

    def connect(self):
        self.__crear_tabla_mascota()
        self.__crear_tabla_empleado()
        self.__crear_tabla_cliente()
        self.__crear_tabla_alimento()
        self.__crear_tabla_accesorio()
        self.__crear_tabla_venta()

    def __crear_tabla_mascota(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE MASCOTA(codigoMascota text primary key, tipoMascota text," \
                    " raza text, nombre text,edad int," \
                    " precio float,cantidad int) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_mascota(self, mascota: Mascota):
        cursor = self.con.cursor()
        query = "insert into MASCOTA(codigoMascota , tipoMascota ," \
                " raza , nombre ,edad ," \
                " precio,cantidad) values(" \
                f" ?,?,?,?,?,?,?)"
        cursor.execute(query, (str(mascota.codigoMascota), mascota.tipoMascota, mascota.raza, mascota.nombre,
                               mascota.edad, mascota.precio, mascota.cantidad))
        self.con.commit()

    def consultar_tabla_mascota(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM MASCOTA"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Mascota(*row) for row in rows]

    def __crear_tabla_empleado(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE EMPLEADO(codigo text primary key, nombre text,cedula text," \
                    " apellido text, cargo text,salario float," \
                    " genero text,edad int,direccion text,correo text,horario text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_empleado(self, empleado: Empleado):
        cursor = self.con.cursor()
        query = "insert into EMPLEADO(codigo ," \
                " nombre , cedula, apellido ,cargo , salario, genero, edad, direccion, correo," \
                " horario ) values(" \
                f" ?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(query, (str(empleado.codigo), empleado.nombre, str(empleado.cedula), empleado.apellido,
                               empleado.cargo, empleado.salario, empleado.genero, empleado.edad, empleado.direccion,
                               empleado.correo, empleado.horario))
        self.con.commit()

    def consultar_tabla_empleado(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM EMPLEADO"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Empleado(*row) for row in rows]

    def __crear_tabla_cliente(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE CLIENTE(codigoCliente text primary key, nombre text," \
                    " apellido text,cedula text," \
                    " genero text,direccion text,correo text,edad int,tiempoCliente) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_cliente(self, cliente: Cliente):
        cursor = self.con.cursor()
        query = "insert into CLIENTE(codigoCliente ," \
                " nombre , apellido, cedula ,genero, direccion, correo," \
                " edad,tiempoCliente) values(" \
                f" ?,?,?,?,?,?,?,?,?)"
        cursor.execute(query, (str(cliente.codigoCliente), cliente.nombre, cliente.apellido, str(cliente.cedula),
                               cliente.genero, cliente.direccion, cliente.correo, cliente.edad, cliente.tiempoCliente))
        self.con.commit()

    def consultar_tabla_cliente(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM CLIENTE"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Cliente(*row) for row in rows]

    def __crear_tabla_alimento(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE ALIMENTO(codigoAlimento text primary key,tipoAlimento text, nombreProducto text," \
                    " cantidadAlimento int," \
                    " cantidadContenido text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_alimento(self, alimento: Alimento):
        cursor = self.con.cursor()
        query = "insert into ALIMENTO(codigoAlimento , tipoAlimento ," \
                " nombreProducto , cantidadAlimento ,cantidadContenido," \
                " precio) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query, (str(alimento.codigoAlimento), alimento.tipoAlimento, alimento.nombreProducto,
                               alimento.cantidadAlimento, alimento.cantidadContenido, alimento.precio))
        self.con.commit()

    def consultar_tabla_alimento(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM ALIMENTO"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Alimento(*row) for row in rows]

    def __crear_tabla_accesorio(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE ACCESORIO(codigoAccesorio text primary key,nombreAccesorio text, precioAccesorio float," \
                    " cantidadAccesorio int,descripcionAccesorio text," \
                    " usoAccesorio text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_accesorio(self, accesorio: Accesorio):
        cursor = self.con.cursor()
        query = "insert into ACCESORIO(codigoAccesorio , nombreAccesorio ," \
                " precioAccesorio , cantidadAccesorio ,descripcionAccesorio," \
                " usoAccesorio) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query, (str(accesorio.codigoAccesorio), accesorio.nombreAccesorio, accesorio.precio,
                               accesorio.cantidad, accesorio.descripcionAccesorio, accesorio.usoAccesorio))
        self.con.commit()

    def __crear_tabla_venta(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE VENTA(codigoVenta Integer PRIMARY KEY Autoincrement , cantidadVenta Integer," \
                    " precioUnidad float, precioTotal float,nombreProducto text, codigoCliente text," \
                    " codigo text,FOREIGN KEY(codigoCliente) references CLIENTE(codigoCliente)," \
                    "FOREIGN KEY(codigo) references EMPLEADO(codigo)) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_venta(self, venta: Venta):
        cursor = self.con.cursor()
        query = "insert into VENTA( cantidadVenta ," \
                " precioUnidad , precioTotal ,nombreProducto ," \
                " codigoCliente,codigo) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query, (venta.cantidadVenta, venta.precioUnidad, venta.precioTotal,
                               venta.nombreProducto, str(venta.cliente.codigoCliente), str(venta.empleado.codigo)))
        self.con.commit()

    def consultar_tabla_venta(self,inventario:Inventario):
        cursor = self.con.cursor()
        venta = cursor.execute(
            "select codigoVenta,cantidadVenta,precioUnidad,precioTotal,"
            "nombreProducto, codigoCliente,codigo"
            " from VENTA")
        ventas = []
        for codigoVenta,cantidadVenta,precioUnidad,precioTotal,\
            nombreProducto, codigoCliente,codigo in venta:
            espcCliente= Especificacion()
            espcCliente.agregar_parametro("codigoCliente",codigoCliente)
            espcEmpleado= Especificacion()
            espcEmpleado.agregar_parametro("codigo",codigo)
            clientes=list(inventario.buscar_cliente(espcCliente))
            empleados=list(inventario.buscar_empleado(espcEmpleado))
            venta_cargada = Venta(clientes[0],empleados[0],nombreProducto,cantidadVenta,precioUnidad,precioTotal)
            venta_cargada.codigoVenta=codigoVenta
            ventas.append(venta_cargada)
        return ventas

    def consultar_tabla_accesorio(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM ACCESORIO"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Accesorio(*row) for row in rows]

    @classmethod
    def save_json_mascota(cls, mascota):
        text_open = open("files/" + str(mascota.codigoMascota) + '.jsonMascota', mode='w')
        json_gui = jsonpickle.encode(mascota)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_mascota(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        mascota = jsonpickle.decode(json_gui)
        text_open.close()
        return mascota

    @classmethod
    def save_json_empleado(cls, empleado):
        text_open = open("files/" + str(empleado.codigo) + '.jsonEmpleado', mode='w')
        json_gui = jsonpickle.encode(empleado)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_empleado(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        empleado = jsonpickle.decode(json_gui)
        text_open.close()
        return empleado

    @classmethod
    def save_json_cliente(cls, cliente):
        text_open = open("files/" + str(cliente.codigoCliente) + '.jsonCliente', mode='w')
        json_gui = jsonpickle.encode(cliente)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_cliente(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        cliente = jsonpickle.decode(json_gui)
        text_open.close()
        return cliente

    @classmethod
    def save_json_alimento(cls, alimento):
        text_open = open("files/" + str(alimento.codigoAlimento) + '.jsonAlimento', mode='w')
        json_gui = jsonpickle.encode(alimento)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_alimento(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        alimento = jsonpickle.decode(json_gui)
        text_open.close()
        return alimento

    @classmethod
    def save_json_accesorio(cls, accesorio):
        text_open = open("files/" + str(accesorio.codigoAccesorio) + '.jsonAccesorio', mode='w')
        json_gui = jsonpickle.encode(accesorio)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_accesorio(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        accesorio = jsonpickle.decode(json_gui)
        text_open.close()
        return accesorio

    @classmethod
    def save_json_configuracion(cls, configuracion:Configuracion):
        text_open = open("files/" + str(configuracion.codigoUnico) + '.json', mode='w')
        json_gui = jsonpickle.encode(configuracion)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_configuracion(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        configuracion = jsonpickle.decode(json_gui)
        text_open.close()
        return configuracion
