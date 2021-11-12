from tienda_Mascotas.Dominio.mascota import Mascota
from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Dominio.alimento import Alimento
from tienda_Mascotas.Dominio.accesorio import Accesorio
from tienda_Mascotas.Dominio.cliente import Cliente
from tienda_Mascotas.Dominio.empleado import Empleado
from tienda_Mascotas.Dominio.venta import Venta
from tienda_Mascotas.Infraestructura.persistencia import Persistencia
from tienda_Mascotas.Dominio.especificacion import Especificacion
from tienda_Mascotas.Infraestructura.configuracion import Configuracion
import os

if __name__ == '__main__':

    """Primero declaramos la persistencia y luego utilizamos el metodo saver.connect cuando iniciamos la aplicacion
    esto genera la base de datos sqlite y las tablas de la entitades que necesitamos con sus atributos"""

    saver = Persistencia()
    saver.connect()



    # Metodo generar configuracion, el cual trae la configuracion que esta guardada en archivo plano json

    def generarConfiguracion():
        for file in os.listdir("./files"):
            if '1.json' in file:
                configuracion = Persistencia.load_json_configuracion(file)
        return configuracion


    """En el metodo generarInventario cargamos los datos que estan guardados tanto en archivos planos json y 
    los que estan guardados en base de datos sqlite para utilizarlos en uno solo, en este caso la clase inventario"""


    def generarInventario():
        inventario = Inventario()
        mascotas = saver.consultar_tabla_mascota()
        alimentos = saver.consultar_tabla_alimento()
        accesorios = saver.consultar_tabla_accesorio()
        clientes = saver.consultar_tabla_cliente()
        empleados = saver.consultar_tabla_empleado()
        for mascota in mascotas:
            inventario.agregar_mascota(mascota)
        for alimento in alimentos:
            inventario.agregar_alimento(alimento)
        for accesorio in accesorios:
            inventario.agregar_accesorio(accesorio)
        for cliente in clientes:
            inventario.agregar_cliente(cliente)
        for empleado in empleados:
            inventario.agregar_empleado(empleado)
        ventas= saver.consultar_tabla_venta(inventario)
        for venta in ventas:
            inventario.agregar_venta(venta)
        for file in os.listdir("./files"):
            if '1.json' in file:
                configuracion = Persistencia.load_json_configuracion(file)
            elif '.jsonMascota' in file:
                inventario.agregar_mascota(Persistencia.load_json_mascota(file))
            elif '.jsonEmpleado' in file:
                inventario.agregar_empleado(Persistencia.load_json_empleado(file))
            elif '.jsonCliente' in file:
                inventario.agregar_cliente(Persistencia.load_json_cliente(file))
            elif '.jsonAlimento' in file:
                inventario.agregar_alimento(Persistencia.load_json_alimento(file))
            elif '.jsonAccesorio' in file:
                inventario.agregar_accesorio(Persistencia.load_json_accesorio(file))
        return inventario


    """En el metodo agregar informacion, le damos al usuario una seria de opciones dadas por un while,
    y dependiendo la que elija, lo lleva a llenar los datos de la clase que escogio.Dependiendo de la configuracion
    esta lo guarda como un archivo plano json o base sqlite"""


    def agregar_informacion(saver, configuracion):
        inventario = generarInventario()
        ans = True
        while ans:
            print("""
        BIENVENIDO A LA TIENDA DE MASCOTAS, ELIGE ENTRE NUESTRAS OPCIONES,
        PARA MANTENER LA TIENDA ORDENADA Y REGISTRAR SUS ELEMENTOS
        
        1.Agregar nueva mascota.
        2.Agregar nuevo alimento de mascotas.
        3.Agregar nuevo accesorio de mascotas.
        4.Agregar nuevo cliente.
        5.Agregar nuevo empleado.
        6.Configuracion.
        7.Regresar al menu principal.
        """)
            ans = input("Cual de las opciones quieres?: ")
            if ans == "1":
                codigoMascota = str(input("Ingrse el codigo de la mascota:"))
                tipo_mascota = str(input("Ingrese el de que tipo de animal que es la mascota:"))
                raza = str(input("Ingrese la raza de la mascota:"))
                nombre = str(input("Ingres el nombre provicional de la mascota:"))
                edad = int(input("Ingrese la edad que tiene la mascota:"))
                precioMascota = float(input("Ingrese el precio de la mascota:"))
                cantidadMascota = int(input("Ingrese la cantidad de mascotas que hay con estas caracteristicas:"))
                mascota = Mascota(codigoMascota, tipo_mascota, raza, nombre, edad, precioMascota, cantidadMascota)
                try:
                    inventario.agregar_mascota(mascota)
                    if configuracion.estado == "archivo plano json":
                        Persistencia.save_json_mascota(mascota)
                        print("\n Se agrego la mascota con exito en js")
                    else:
                        saver.guardar_mascota(mascota)
                        print("\n Se agrego la mascota con exito en bd")
                except Exception as ex:
                    print(ex)


            elif ans == "2":
                codigoAlimento = str(input("Ingrse el codigo del alimento:"))
                tipo_alimento = str(input("Ingrese el tipo de alimento que quiere registrar:"))
                nombreAlimento = str(input("Ingrese el nombre del producto::"))
                cantidadAlimento = int(input("Ingrese numero de existencias del articulo:"))
                cantidadContenido = int(input("Ingrese la cantidad de contenido del producto(en gramos):"))
                precioAlimento = float(input("Ingrese el precio del producto alimenticio:"))
                alimento = Alimento(codigoAlimento, tipo_alimento, nombreAlimento, cantidadAlimento, cantidadContenido,
                                    precioAlimento)
                try:
                    inventario.agregar_alimento(alimento)
                    if configuracion.estado == "archivo plano json":
                        Persistencia.save_json_alimento(alimento)
                        print("\n Se agrego el alimento para mascotas con exito en js")
                    else:
                        saver.guardar_alimento(alimento)
                        print("\n Se agrego el alimento para mascotas con exito en bd")
                except Exception as ex:
                    print(ex)
            elif ans == "3":
                codigoAccesorio = str(input("Ingrse el codigo del accesorio:"))
                nombreAccesorio = str(input("Ingrese el nombre del accesorio:"))
                descripcionAccesorio = str(input("Ingrese una descripcion corta del accesorio:"))
                usoAccesorio = str(input("Ingrese el uso del accesorio:"))
                precioAccesorio = float(input("Ingrese el precio del accesorio:"))
                cantidadAccesorio = int(input("Ingrese la cantidad de existencias del acesorio:"))
                accesorio = Accesorio(codigoAccesorio, nombreAccesorio, cantidadAccesorio, precioAccesorio,
                                      descripcionAccesorio, usoAccesorio)
                try:
                    inventario.agregar_accesorio(accesorio)
                    if configuracion.estado == "archivo plano json":
                        Persistencia.save_json_accesorio(accesorio)
                        print("\n Se agrego el accesorio de mascotas con exito en js")
                    else:
                        saver.guardar_accesorio(accesorio)
                        print("\n Se agrego el accesorio de mascotas con exito en bd")
                except Exception as ex:
                    print(ex)

            elif ans == "4":
                codigoCliente = str(input("Ingrse el codigo del cliente:"))
                nombreCliente = str(input("Ingrese el nombre del cliente:"))
                cedulaEmpleado = str(input("Ingrese la cedula del empleado:"))
                apellidoCliente = str(input("Ingrese el apellido del cliente:"))
                generoCliente = str(input("Ingrese el genero del cliente:"))
                edadCliente = int(input("Ingrese la edad del cliente"))
                direccionCliente = str(input("Ingrese la direccion de residencia del cliente:"))
                correoCliente = str(input("Ingrese el correo de contacto del cliente:"))
                tiempoCliente = str(input("Ingrese el tiempo que lleva la persona siendo su cliente:"))
                cliente = Cliente(codigoCliente, nombreCliente, apellidoCliente, cedulaEmpleado, generoCliente
                                  , direccionCliente, correoCliente, edadCliente, tiempoCliente)
                try:
                    inventario.agregar_cliente(cliente)
                    if configuracion.estado == "archivo plano json":
                        Persistencia.save_json_cliente(cliente)
                        print("\n Se agrego el nuevo cliente con exito en js")
                    else:
                        saver.guardar_cliente(cliente)
                        print("\n Se agrego el nuevo cliente con exito en bd")
                except Exception as ex:
                    print(ex)

            elif ans == "5":
                codigoEmpleado = str(input("Ingrse el codigo del empleado:"))
                nombreEmpleado = str(input("Ingrese el nombre del empleado:"))
                cedulaEmpleado = str(input("Ingrese la cedula del empleado:"))
                apellidoEmpleado = str(input("Ingrese el apellido del empleado:"))
                generoEmpleado = str(input("Ingrese el genero del empleado:"))
                edadEmpleado = int(input("Ingrese la edad del empleado:"))
                direccionEmpleado = str(input("Ingrese la direccion de residencia del empleado:"))
                correoEmpleado = str(input("Ingrese el correo de contacto del empledo:"))
                cargoEmpleado = str(input("Ingrese el cargo que tiene el empleado en la tienda:"))
                horarioEmpleado = str(input("Ingrese el horario que cumple el empleado:"))
                salarioEmpleado = str(input("Ingrese el salario que tiene el empleado:"))
                empleado = Empleado(codigoEmpleado, nombreEmpleado, cedulaEmpleado, apellidoEmpleado, cargoEmpleado,
                                    salarioEmpleado, generoEmpleado,
                                    edadEmpleado, direccionEmpleado, correoEmpleado, horarioEmpleado)
                try:
                    inventario.agregar_empleado(empleado)
                    if configuracion.estado == "archivo plano json":
                        Persistencia.save_json_empleado(empleado)
                        print("\n Se agrego el nuevo empleado con exito en js")
                    else:
                        saver.guardar_empleado(empleado)
                        print("\n Se agrego el nuevo empleado con exito en bd")
                except Exception as ex:
                    print(ex)

            elif ans == "6":
                opcion = True
                while opcion:
                    print("En estos momentos los elemento se guardan por medio de:" + " " + str(configuracion.estado))
                    print("""Elija como quiere guardar sus elementos
                           1.Archivos planos tipo json
                           2.Base de datos sqlite
                           3.Regresar.
                           """)
                    opcion = input("Que opcion elige?:")
                    if opcion == "1":
                        configuracion.cambiarEstadoConfiguracion("archivo plano json")
                        Persistencia.save_json_configuracion(configuracion)
                        print("Se cambio la configuracion a archivos planos de tipo json")
                    elif opcion == "2":
                        configuracion.cambiarEstadoConfiguracion("Base de datos sqlite")
                        Persistencia.save_json_configuracion(configuracion)
                        print("Se cambio la configuracion a Base de datos sqlite")
                    elif opcion == "3":
                        print("Se guardaron los cambios")
                        opcion = False
                    elif opcion != "":
                        print("Opcion invalida")
            elif ans == "7":
                ans = False
            elif ans != "":
                print("\n Opcion no es valida, verifique el numero ingresado")


    """En el metodo buscar informacion el usuario se le da un menu de opciones para buscar la clase que quiera,y por 
    los atributos que quiera. Dependiendo de la clase que elija, se despliegan una serie de caracteristicas. El usuario
    escoje el numero de caracteristicas, el numero de referencia a la caracteristica y por ultimo el valor de esta,
    luego de esto se visualiza la representacion del objeto en caso de que exista"""


    def buscar_informacion():
        opc = True
        inventario = generarInventario()
        while opc:
            especificacion = Especificacion()
            print("""
            BIENVENIDO A LA TIENDA DE MASCOTAS, ELEGI ENTRE NUESTRAS OPCIONES,
            PARA BUSCAR TUS ELEMENTOS Y TENER UN CONTROL SOBRE ESTOS
            
            1.Buscar mascota.
            2.Buscar alimento de mascotas.
            3.Buscar accesorio de mascotas.
            4.Buscar cliente.
            5.Buscar empleado.
            6.Regresar al menu principal.
            """)
            opc = input("Ingrese la opcion que desee:")
            if opc == "1":
                print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                A LA MASCOTA.
                
                1.Codigo mascota.
                2.tipo de mascota.
                3.raza de la mascota.
                4.nombre de la mascota.
                5.precio de la mascota.
                6.edad mascota.
                7.Regresar.
                """)
                resultado = int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
                if resultado > 6:
                    print("No puede buscar por mas de 5 atributos para la mascota")
                else:
                    for i in range(resultado):
                        llave = input("Ingrese el numero al que corresponde la caracteristica:")
                        valor = input("Ingrese el valor de la caracteristica:")
                        if llave == "1":
                            llave = "codigoMascota"
                        elif llave == "2":
                            llave = "tipoMascota"
                        elif llave == "3":
                            llave = "raza"
                        elif llave == "4":
                            llave = "nombre"
                        elif llave == "5":
                            llave = "precio"
                        elif llave == "6":
                            llave == "edad"
                        elif llave == "7":
                            print("No hubo busqueda")
                        elif llave != "":
                            print("Ingreso opciones invalidas")
                        especificacion.agregar_parametro(llave, valor)
                    print(list(inventario.buscar_mascota(especificacion)))
            elif opc == "2":
                print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                EL ALIMENTO PARA MASCOTAS.
                
                1.Codigo alimento de mascotas.
                2.tipo de alimento de mascotas.
                3.cantidad existencias.
                4.nombre del producto.
                5.precio del producto.
                6.cantidad de contenido alimento.
                7.Regresar.
                """)
                resultado = int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
                if resultado > 6:
                    print("No puede buscar por mas de 5 atributos para el alimento")
                else:
                    for i in range(resultado):
                        llave = input("Ingrese el numero al que corresponde la caracteristica:")
                        valor = input("Ingrese el valor de la caracteristica:")
                        if llave == "1":
                            llave = "codigoAlimento"
                        elif llave == "2":
                            llave = "tipoAlimento"
                        elif llave == "3":
                            llave = "cantidadAlimento"
                        elif llave == "4":
                            llave = "nombreProducto"
                        elif llave == "5":
                            llave = "precio"
                        elif llave == "6":
                            llave == "cantidadContenido"
                        elif llave == "7":
                            print("No hubo busqueda")
                        elif llave != "":
                            print("Ingreso opciones invalidas")
                        especificacion.agregar_parametro(llave, valor)
                    print(list(inventario.buscar_alimento(especificacion)))
            elif opc == "3":
                print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                EL ACCESORIO DE MASCOTAS.
                
                1.Codigo accesorio.
                2.Nombre del accesorio.
                3.Cantidad existencias del accesorio.
                4.Precio del accesorio.
                5.Descripcion del accesorio.
                6.Uso del accesorio.
                7.Regresar.
                """)
                resultado = int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
                if resultado > 6:
                    print("No puede buscar por mas de 5 atributos para el accesorio")
                else:
                    for i in range(resultado):
                        llave = input("Ingrese el numero al que corresponde la caracteristica:")
                        valor = input("Ingrese el valor de la caracteristica:")
                        if llave == "1":
                            llave = "codigoAccesorio"
                        elif llave == "2":
                            llave = "nombreAccesorio"
                        elif llave == "3":
                            llave = "cantidadAccesorio"
                        elif llave == "4":
                            llave = "precioAccesorio"
                        elif llave == "5":
                            llave = "descripcionAccesorio"
                        elif llave == "6":
                            llave == "usoAccesorio"
                        elif llave == "7":
                            print("No hubo busqueda")
                        elif llave != "":
                            print("Ingreso opciones invalidas")
                        especificacion.agregar_parametro(llave, valor)
                    print(list(inventario.buscar_accesorio(especificacion)))
            elif opc == "4":
                print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                A EL CLIENTE.
                
                1.Codigo del cliente.
                2.Cedula del cliente.
                3.Genero del cliente.
                4.Nombre del cliente.
                5.apellido del cliente.
                6.Edad el cliente.
                7.Direccion del cliente.
                8.Correo del cliente.
                9.Tiempo como cliente de la tienda.
                10.Regresar.
                """)
                resultado = int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
                if resultado > 8:
                    print("No puede buscar por mas de 8 atributos para el cliente")
                else:
                    for i in range(resultado):
                        llave = input("Ingrese el numero al que corresponde la caracteristica:")
                        valor = input("Ingrese el valor de la caracteristica:")
                        if llave == "1":
                            llave = "codigoCliente"
                        elif llave == "2":
                            llave = "cedula"
                        elif llave == "3":
                            llave = "genero"
                        elif llave == "4":
                            llave = "nombre"
                        elif llave == "5":
                            llave = "apellido"
                        elif llave == "6":
                            llave == "edad"
                        elif llave == "7":
                            llave = "direccion"
                        elif llave == "8":
                            llave = "correo"
                        elif llave == "9":
                            llave = "tiempoCliente"
                        elif llave == "10":
                            print("No hubo busqueda")
                        elif llave != "":
                            print("Ingreso opciones invalidas")
                        especificacion.agregar_parametro(llave, valor)
                    print(list(inventario.buscar_cliente(especificacion)))
            elif opc == "5":
                print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                A EL EMPLEADO.
                
                1.Codigo del empleado.
                2.Cedula del empleado.
                3.Genero del empleado.
                4.Nombre del empleado.
                5.apellido del apellido.
                6.Edad del empleado.
                7.Direccion del empleado.
                8.Correo del empleado.
                9.Cargo del empleado.
                10.Horario del empleado.
                11.Salario del empleado.
                12.Regresar.
                """)
                resultado = int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
                if resultado > 8:
                    print("No puede buscar por mas de 8 atributos para el cliente")
                else:
                    for i in range(resultado):
                        llave = input("Ingrese el numero al que corresponde la caracteristica:")
                        valor = input("Ingrese el valor de la caracteristica:")
                        if llave == "1":
                            llave = "codigo"
                        elif llave == "2":
                            llave = "cedula"
                        elif llave == "3":
                            llave = "genero"
                        elif llave == "4":
                            llave = "nombre"
                        elif llave == "5":
                            llave = "apellido"
                        elif llave == "6":
                            llave = "edad"
                        elif llave == "7":
                            llave = "direccion"
                        elif llave == "8":
                            llave = "correo"
                        elif llave == "9":
                            llave = "cargo"
                        elif llave == "10":
                            llave = "horario"
                        elif llave == "11":
                            llave = "salario"
                        elif llave == "12":
                            print("No hubo busqueda")
                        elif llave != "":
                            print("Ingreso opciones invalidas")
                        especificacion.agregar_parametro(llave, valor)
                    print(list(inventario.buscar_empleado(especificacion)))
            elif opc == "6":
                opc = False
            elif opc != "":
                print("\n Opcion invalida porfavor rectifica")

    def generarVenta():
        inventario= generarInventario()
        respVenta = True
        while respVenta:
            print("""
                ESCOJA EL ELEMENTO QUE QUIERE COMPRAR:
                
                1.Mascota.
                2.Accesorio.
                3.Alimento.
                4.Terminar y salir.
                """)
            respVenta = input("Cual de las opciones quieres?: ")
            if respVenta=="1":
                venderMascota(inventario)
            elif respVenta== "2":
                venderAccesorio(inventario)
            elif respVenta== "3":
                venderAlimento(inventario)
            elif respVenta== "4":
                respVenta=False
            else:
                print("Ingrese una de las opciones maldito fracasado!")


    def venderMascota(inventario):
        for mascota in inventario.mascotas:
                print("codigoMascota: "+str(mascota.codigoMascota)+"\n"
                          +"Nombre: "+mascota.nombre+"\n"
                          +"Tipo de mascota: "+mascota.tipoMascota+"\n"
                          +"Raza: "+mascota.raza+"\n"
                          +"Edad: "+str(mascota.edad)+"\n"
                          +"Cantidad disponible: "+str(mascota.cantidad)+"\n"
                          +"Precio: "+str(mascota.precio))
                    #Actualizar la base de datos
        codigoMascota=input("Ingrese el codigo de la mascota que se quiere comprar: ")
        codigoCliente= input("Ingrese el codigo del cliente que realiza la compra: ")
        codigoEmpleado= input("Ingrese el codigo del empleado que realiza la venta: ")
        cantidad=int(input("Ingrese la cantidad de mascotas que desea comprar: "))
        espc= Especificacion()
        espc.agregar_parametro("codigoMascota",codigoMascota)
        espcEmpleado= Especificacion()
        espcEmpleado.agregar_parametro("codigo",codigoEmpleado)
        espcCliente= Especificacion()
        espcCliente.agregar_parametro("codigoCliente",codigoCliente)
        mascotas=list(inventario.buscar_mascota(espc))
        empleados= list(inventario.buscar_empleado(espcEmpleado))
        clientes= list(inventario.buscar_cliente(espcCliente))
        precioTotal= cantidad*mascotas[0].precio
        venta= Venta(clientes[0],empleados[0],mascotas[0].nombre,cantidad,mascotas[0].precio,precioTotal)
        saver.guardar_venta(venta)

    def venderAccesorio(inventario):
        for accesorio in inventario.accesorios:
                print("codigo accesorio: "+str(accesorio.codigoAccesorio)+"\n"
                          +"Nombre: "+accesorio.nombreAccesorio+"\n"
                          +"Descripcion: "+accesorio.descripcionAccesorio+"\n"
                          +"Uso: "+accesorio.usoAccesorio+"\n"
                          +"Cantidad diponible: "+str(accesorio.cantidad)+"\n"
                          +"Precio: "+str(accesorio.precio))
                    #Actualizar la base de datos
        codigoAccesorio=input("Ingrese el codigo del accesorio que se quiere comprar: ")
        codigoCliente= input("Ingrese el codigo del cliente que realiza la compra: ")
        codigoEmpleado= input("Ingrese el codigo del empleado que realiza la venta: ")
        cantidad=input("Ingrese la cantidad de accesorios que desea comprar: ")
        espc= Especificacion()
        espc.agregar_parametro("codigoAccesorio",codigoAccesorio)
        espcEmpleado= Especificacion()
        espcEmpleado.agregar_parametro("codigo",codigoEmpleado)
        espcCliente= Especificacion()
        espcCliente.agregar_parametro("codigoCliente",codigoCliente)
        accesorios=list(inventario.buscar_accesorio(espc))
        empleados= list(inventario.buscar_empleado(espcEmpleado))
        clientes= list(inventario.buscar_cliente(espcCliente))
        precioTotal= cantidad*accesorios[0].precio
        venta= Venta(clientes[0],empleados[0],accesorios[0].nombreAccesorio,cantidad,accesorios[0].precio,precioTotal)
        saver.guardar_venta(venta)

    def venderAlimento(inventario):
        for alimento in inventario.alimentos:
                print("codigo alimento: "+alimento.codigoAlimento+"\n"
                          +"Nombre: "+alimento.nombreProducto+"\n"
                          +"Tipo de alimento: "+alimento.tipoAlimento+"\n"
                          +"Contenido: "+alimento.cantidadContenido+"\n"
                          +"Cantidad diponible: "+alimento.cantidad+"\n"
                          +"Precio: "+alimento.precio)
                    #Actualizar la base de datos
        codigoAlimento=input("Ingrese el codigo del alimento que se quiere comprar: ")
        codigoCliente= input("Ingrese el codigo del cliente que realiza la compra: ")
        codigoEmpleado= input("Ingrese el codigo del empleado que realiza la venta: ")
        cantidad=input("Ingrese la cantidad de alimentos que desea comprar: ")
        espc= Especificacion()
        espc.agregar_parametro("codigoAlimento",codigoAlimento)
        espcEmpleado= Especificacion()
        espcEmpleado.agregar_parametro("codigo",codigoEmpleado)
        espcCliente= Especificacion()
        espcCliente.agregar_parametro("codigoCliente",codigoCliente)
        alimentos=list(inventario.buscar_alimento(espc))
        empleados= list(inventario.buscar_empleado(espcEmpleado))
        clientes= list(inventario.buscar_cliente(espcCliente))
        precioTotal= cantidad*alimentos[0].precio
        venta= Venta(clientes[0],empleados[0],alimentos[0].nombreProducto,cantidad,alimentos[0].precio,precioTotal)
        saver.guardar_venta(venta)

    """Este es el while principal donde se ejecutan todos los metodos previamente dichos dependiendo de la 
    decision del usuario"""

    ansPrin = True
    while ansPrin:
        print("""
            BIENVENIDO A LA TIENDA DE MASCOTAS, ELEGI ENTRE NUESTRAS OPCIONES,
            PARA AGREGAR, BUSCAR O VENDER UN ELEMENTO DE TU TIENDA:
            
            1.Agregar elemento.
            2.Buscar elemento.
            3.Vender elemento.
            4.Ver ventas.
            5.Terminar y salir.
            """)
        ansPrin = input("Cual de las opciones quieres?: ")
        if ansPrin == "1":
            configuracion = generarConfiguracion()
            agregar_informacion(saver, configuracion)
        elif ansPrin == "2":
            buscar_informacion()
        elif ansPrin == "3":
            generarVenta()
        elif ansPrin != "":
            print("\n Nos vemos hasta la proxima!")
            ansPrin = False
