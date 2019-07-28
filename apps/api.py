# Importamos as classes API e Resource
# from flask_restful import Api, Resource
# from flask_restful import Api, Resource
from flask_restplus import Api, Resource, fields


from apps.planets.resources import PlanetsResource, PlanetsFindId


# Criamos uma classe que extende de Resource

# class Index(Resource):

#     # Definimos a operação get do protocolo http
#     def get(self):

#         # retornamos um simples dicionário que será automáticamente
#         # retornado em json pelo flask
#         return {'API B2W': 'Api flask-restfull - localhost:5000/planets'}


# Instânciamos a API do FlaskRestful
api = Api()


def configure_api(app):

    # adicionamos na rota '/' a sua classe correspondente Index

    # api.add_resource(Index, '/')
    api.add_resource(PlanetsResource, '/planets')
    api.add_resource(PlanetsFindId, '/planets/<string:planet_id>')

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)
