from mongoengine.errors import FieldDoesNotExist, DoesNotExist
from apps.responses import resp_exception, resp_does_not_exist
from .models import Planet


def get_planet_by_id(planet_id: str):
    try:
        # buscamos todos os usuários da base utilizando o paginate
        return Planet.objects.get(id=planet_id)

    except DoesNotExist as e:
        return resp_does_not_exist('Planets', 'Planet')

    except FieldDoesNotExist as e:
        return resp_exception('Planets', description=e.__str__())

    except Exception as e:
        return resp_exception('Planets', description=e.__str__())
