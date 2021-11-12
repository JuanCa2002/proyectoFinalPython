import json
import waitress

import falcon
from falcon import API

from tienda_Mascotas.Infraestructura.persistencia import Persistencia


class mascota():

    def on_get(self, req, resp, codigo):
        db = Persistencia()
        mascotas = db.consultar_tabla_mascota()
        template = """<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
                    <h1 style="color: #5e9ca0;">La tienda del CAMI</h1>
                    <h2 style="color: #2e6c80;">Mascotas:</h2>
                    <h2 style="color: #2e6c80;">Cleaning options:</h2>
                    <table class="editorDemoTable" style="height: 362px;">
                    <thead>
                    <tr style="height: 18px;">
                    <td style="height: 18px; width: 263.172px;">Nombre</td>
                    <td style="height: 18px; width: 348.625px;">Tipo Mascota</td>
                    <td style="height: 18px; width: 55.2031px;">Raza</td>
                    </tr>
                    </thead>
                    <tbody>
                """
        for mascota in mascotas:
            mascota_template  = f"""<tr style="height: 22px;">
                                <td style="height: 22px; width: 263.172px;">{mascota.nombre}</td>
                                <td style="height: 22px; width: 348.625px;">{mascota.tipoMascota}</td>
                                <td style="height: 22px; width: 55.2031px;">{mascota.raza}</td>
                                </tr>
                                """
            template+=mascota_template
        template+="""</tbody>
        </table>"""
        resp.body = template
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_OK


def iniciar() -> API:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api = API()
    api.add_route("/mascota/{codigo}", mascota())

    return api


app = iniciar()
if __name__ == '__main__':
    waitress.serve(app, port=2020, url_scheme='http')
