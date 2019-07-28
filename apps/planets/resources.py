from flask import request
from flask_restful import Resource
from mongoengine.errors import NotUniqueError, ValidationError, FieldDoesNotExist
from apps.responses import (
    resp_already_exists,
    resp_exception,
    resp_data_invalid,
    resp_ok
)
from apps.messages import MSG_INVALID_DATA, MSG_RESOURCE_CREATED, MSG_RESOURCE_FETCHED_PAGINATED, MSG_RESOURCE_FETCHED, MSG_RESOURCE_UPDATED, MSG_RESOURCE_DELETED

from .models import Planet
from .schemas import PlanetRegistrationSchema, PlanetSchema, PlanetUpdateSchema
from .utils import get_planet_by_id


class PlanetsResource(Resource):
    def post(self, *args, **kwargs):
        # Inicializo todas as variaveis utilizadas
        req_data = request.get_json() or None
        data, errors, result = None, None, None
        schema = PlanetRegistrationSchema()

        # Se meus dados postados forem Nulos retorno uma respota inválida
        if req_data is None:
            return resp_data_invalid('Planets', [], msg=MSG_INVALID_DATA)

        # Desserialização os dados postados ou melhor meu payload
        data, errors = schema.load(req_data)

        # Se houver erros retorno uma resposta inválida
        if errors:
            return resp_data_invalid('Planets', errors)

        try:
            model = Planet(**data)
            model.save()

        except NotUniqueError:
            return resp_already_exists('Planets', 'local')

        except ValidationError as e:
            return resp_exception('Planets', msg=MSG_INVALID_DATA, description=e.__str__())

        except Exception as e:
            return resp_exception('Planets', description=e.__str__())

        # Realizo um dump dos dados de acordo com o modelo salvo
        schema = PlanetSchema()
        result = schema.dump(model)

        # Retorno 200 o meu endpoint
        return resp_ok(
            'Planets', MSG_RESOURCE_CREATED.format('Planet'),  data=result.data
        )

    def get(self, page_id=1):
        sc = PlanetSchema(many=True)
        # paginate definid
        page_size = 3

        if 'page_size' in request.args:
            if int(request.args.get('page_size')) < 1:
                page_size = 3
            else:
                page_size = int(request.args.get('page_size'))

        try:
            # buscamos todos os planetas da base utilizando o paginate
            planets = Planet.objects().paginate(page_id, page_size)

        except FieldDoesNotExist as e:
            return resp_exception('Planets', description=e.__str__())

        except Exception as e:
            return resp_exception('Planets', description=e.__str__())

        # criamos dados extras a serem respondidos
        extra = {
            'page': planets.page, 'pages': planets.pages, 'total': planets.total,
            'params': {'page_size': page_size}
        }

        # fazemos um dump dos objetos pesquisados
        result = sc.dump(planets.items)

        return resp_ok(
            'Planets', MSG_RESOURCE_FETCHED_PAGINATED.format('planets'),  data=result.data,
            **extra
        )


class PlanetsFindId(Resource):

    def get(self, planet_id):
        result = None
        schema = PlanetSchema()

        planet = get_planet_by_id(planet_id)

        result = schema.dump(planet)

        return resp_ok(
            'Planets', MSG_RESOURCE_FETCHED.format('Planets'),  data=result.data
        )

    def put(self, planet_id):
        result = None

        schema = PlanetSchema()

        update_schema = PlanetUpdateSchema()

        req_data = request.get_json() or None

        planet = get_planet_by_id(planet_id)

        data, errors = update_schema.load(req_data)

        if errors:
            return resp_data_invalid('Planets', errors)

        try:
            for i in data.keys():
                planet[i] = data[i]
            planet.save()

        except NotUniqueError:
            return resp_already_exists('Planets', 'usuário')

        except ValidationError as e:
            return resp_exception('Planets', msg=MSG_INVALID_DATA, description=e.__str__())

        except Exception as e:
            return resp_exception('Planets', description=e.__str__())

        result = schema.dump(planet)

        return resp_ok(
            'Planets', MSG_RESOURCE_UPDATED.format('Planet'),  data=result.data
        )

    def delete(self, planet_id):

        planet = get_planet_by_id(planet_id)

        try:

            planet.delete()

        except NotUniqueError:
            return resp_already_exists('Planets', 'planet')

        except ValidationError as e:
            return resp_exception('Planets', msg=MSG_INVALID_DATA, description=e.__str__())

        except Exception as e:
            return resp_exception('Planets', description=e.__str__())

        return resp_ok('Planets', MSG_RESOURCE_DELETED.format('Planet'))
