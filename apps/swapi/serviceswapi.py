import json
import requests

SWAPI_URL = 'https://swapi.co/api'
SWAPI_PLANETS_URL = "%s/planets/" % SWAPI_URL


class Swapi:

    @classmethod
    def search_planet_by_name(cls, name):

        url = "%s?search=%s" % (SWAPI_PLANETS_URL, name)
        response = requests.get(url)
        if response.ok:
            return next(
                filter(
                    lambda r: r['name'].lower() == name.lower(),
                    json.loads(response.text)['results']),
                {})

        raise "swapi communication error"

    @classmethod
    def get_films_from_planet(cls, planet_name):

        planet = cls.search_planet_by_name(planet_name)
        return planet.get('films', [])
