class Venta():
    def __init__(self,cliente,empleado,nombreProducto,cantidadVenta,precioUnidad,precioTotal):
        self.codigoVenta=None
        self.cliente= cliente
        self.nombreProducto= nombreProducto
        self.empleado= empleado
        self.cantidadVenta= cantidadVenta
        self.precioUnidad= precioUnidad
        self.precioTotal= precioTotal

    def __repr__(self):
        representacion= str(self.codigoVenta)+" "+"Venta realizada por el empleado:"+" "+self.empleado.nombre+"\n"\
                        +"venta realiza al cliente:"+" "+self.cliente.nombre+" "+"con cedula: "+str(self.cliente.cedula)+"\n"\
                        +"producto vendido: "+self.nombreProducto+" "+"cantidad: "+str(self.cantidadVenta)+"\n"\
                        +"precio unidad: "+str(self.precioUnidad)+" "+"precio total: "+str(self.precioTotal)
        return representacion

    def cumple(self, especificacion):
        dict_venta = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_venta or dict_venta[k] != especificacion.get_value(k):
                return False
        return True
