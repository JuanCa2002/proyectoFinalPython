import json
import waitress

import falcon
from falcon import API

from tienda_Mascotas.Infraestructura.persistencia import Persistencia


class mascota():

    def on_get(self, req, resp, codigo):
        db = Persistencia()
        gui = db.load_json_mascota(codigo + '.jsonMascota')
        resp.body = json.dumps(gui.__dict__)
        resp.status = falcon.HTTP_OK


def iniciar() -> API:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api = API()
    api.add_route("/mascota/{codigo}", mascota())

    return api


app = iniciar()
if __name__ == '__main__':
    waitress.serve(app, port=2020, url_scheme='http')
