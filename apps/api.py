from flask_restful import Api, Resource
from apps.planets.resources import PlanetsResource, PlanetsFindId, PlanetsFindName
# from flask_restplus import Api, Resource, fields


class Index(Resource):

    # Definimos a operação get do protocolo http
    def get(self):

        # return documentation with swagger.json
        return {'API B2W': 'Api flask-restfull - localhost:5000/planets'}


api = Api()


def configure_api(app):

    # adicionamos na rota '/' a sua classe correspondente Index

    api.add_resource(Index, '/')
    api.add_resource(PlanetsResource, '/planets')
    api.add_resource(PlanetsFindId, '/planets/<string:planet_id>')
    api.add_resource(PlanetsFindName, '/planets/name/<string:planet_name>')

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)
