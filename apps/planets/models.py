from datetime import datetime
from mongoengine import (
    BooleanField,
    DateTimeField,
    DictField,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
    URLField
)
# Apps
from apps.db import db
from apps.swapi.serviceswapi import Swapi


class Mixin(db.Document):
    """
    Default implementation for Planet fields
    """
    meta = {
        'abstract': True,
        'ordering': ['created']
    }

    created_at = DateTimeField(default=datetime.now)


class Planet(Mixin):
    """
    Implementation Model for Planet
    """
    meta = {'collection': 'planets'}

    name = StringField(max_length=200, unique=True, required=True)
    terrain = StringField(max_length=200, default='unknown')
    climate = StringField(max_length=200, default='unknown')

    service = Swapi()

    @property
    def films(self):
        return self.service.get_films_from_planet(self.name)

    @property
    def films_appearances(self):
        return len(self.films)
