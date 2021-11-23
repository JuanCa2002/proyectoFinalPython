import waitress
from falcon import App

from tienda_Mascotas.apiVenta import iniciar as venta_routes
from tienda_Mascotas.apiAlimento import iniciar as alimento_routes
from tienda_Mascotas.apiCliente import iniciar as cliente_routes
from tienda_Mascotas.apiMascota import iniciar as cliente_mascota
from tienda_Mascotas.apiEmpleado import iniciar as cliente_empleado
from tienda_Mascotas.apiAccesorio import iniciar as cliente_accesorio


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
    waitress.serve(app, url_scheme='http')
