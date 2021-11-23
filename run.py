import waitress
from falcon import App

from apiVenta import iniciar as venta_routes
from apiAlimento import iniciar as alimento_routes
from apiCliente import iniciar as cliente_routes
from apiMascota import iniciar as cliente_mascota
from apiEmpleado import iniciar as cliente_empleado
from apiAccesorio import iniciar as cliente_accesorio


def iniciar() -> App:
    app = App()
    app = venta_routes(app)
    app = alimento_routes(app)
    app = cliente_routes(app)
    app = cliente_mascota(app)
    app = cliente_empleado(app)
    app = cliente_accesorio(app)
    return app


app = iniciar()
if __name__ == '__main__':
    waitress.serve(app, port=2020, url_scheme='http')
