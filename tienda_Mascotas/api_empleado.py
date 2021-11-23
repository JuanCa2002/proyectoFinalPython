import falcon
from falcon import App

from tienda_Mascotas.Dominio.empleado import Empleado
from tienda_Mascotas.Infraestructura.persistencia_empleado import PersistenciaEmpleado


class Api_empleado():

    def on_get(self, req, resp):
        db = PersistenciaEmpleado()
        empleados = db.consultar_tabla_empleado()
        template = """<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
                    <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link href="css/bootstrap.css" rel="stylesheet" media="screen">
                    <script src="js/bootstrap.js"></script>
                    <script>
                    </head>
                    <h1 style="color: #5e9ca0;">La tienda del CAMI</h1>
                    <h2 style="color: #2e6c80;">Empleados:</h2>
                    <h2 style="color: #2e6c80;">Cleaning options:</h2>
                    <table class="table-info" style="height: 362px;">
                    <thead>
                    <tr style="height: 18px;">
                    <td style="height: 18px; width: 263.172px;">Codigo Empleado</td>
                    <td style="height: 18px; width: 263.172px;">Nombre</td>
                    <td style="height: 18px; width: 348.625px;">Cedula</td>
                    </tr>
                    </thead>
                    <tbody>
                """
        for empleado in empleados:
            empleado_template = f"""<tr style="height: 22px;">
                                <td style="height: 22px; width: 263.172px;">{empleado.codigo}</td>
                                <td style="height: 22px; width: 263.172px;">{empleado.nombre}</td>
                                <td style="height: 22px; width: 348.625px;">{empleado.cedula}</td>                                
                                </tr>
                                """
            template += empleado_template
        template += """</tbody>
        </table>"""
        resp.body = template
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        empleado = Empleado(**req.media)
        empleado.guardar(empleado)
        resp.status = falcon.HTTP_CREATED

    def on_put(self, req, resp, codigoEmpleado):
        empleado_repositorio = PersistenciaEmpleado()
        empleado = empleado_repositorio.cargar_empleado(codigoEmpleado)
        empleado.update(req.media)
        empleado.codigo = codigoEmpleado
        empleado.guardar_actualizar()
        resp.body = empleado.__dict__

    def on_delete(self, req, resp, codigoEmpleado):
        empleado_repositorio = PersistenciaEmpleado()
        empleado = empleado_repositorio.cargar_empleado(codigoEmpleado)
        empleado.eliminar(empleado.codigo)
        resp.body = codigoEmpleado
        resp.status = falcon.HTTP_OK


def iniciar(api) -> App:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api.add_route("/empleado/", Api_empleado())
    api.add_route("/empleado_guardar/", Api_empleado())
    api.add_route("/empleado_actualizar/{codigoEmpleado}", Api_empleado())
    api.add_route("/empleado_eliminar/{codigoEmpleado}", Api_empleado())
    return api

