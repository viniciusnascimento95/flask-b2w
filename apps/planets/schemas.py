from marshmallow import Schema, post_load
from marshmallow.fields import Str, Field, Int
from marshmallow import fields
from apps.messages import MSG_FIELD_REQUIRED


class PlanetRegistrationSchema(Schema):
    name = Str(required=True, error_messages={"required": MSG_FIELD_REQUIRED})
    climate = Str()
    terrain = Str()

    @post_load
    def lowerstrip(self, item, **kwargs):
        item["name"] = item["name"].lower().strip()

        if "climate" in item:
            item["climate"] = item["climate"].lower().strip()

        if "terrain" in item:
            item["terrain"] = item["terrain"].lower().strip()
        return item


class PlanetSchema(Schema):
    id = Str()
    name = Str(required=True, error_messages={"required": MSG_FIELD_REQUIRED})
    climate = Str()
    terrain = Str()
    films = fields.Str(dump_only=True)
    films_appearances = fields.Int(dump_only=True)
    created_at = Str()


class PlanetUpdateSchema(Schema):
    name = Str()
    climate = Str()
    terrain = Str()
