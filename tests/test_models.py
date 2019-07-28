from mongoengine import (
    BooleanField,
    StringField,
)
# Apps

from apps.planets.models import Planet


class TestPlanet:
    def setup_method(self):
        self.data = {
            'name': 'teste', 'climate': 'abc123',
            'terrain': 'bca321'

        }
        # create instance object planet
        self.model = Planet(**self.data)
    
    # test field name

    def test_name_field_exists(self):
        """
        Field Name Verification Exists
        """
        assert 'name' in self.model._fields

    def test_name_field_is_required(self):
        """
        Field Name Verification is required
        """
        assert self.model._fields['name'].required is True

    def test_name_field_is_unique(self):
        """
        Field Name Verification is unique
        """
        assert self.model._fields['name'].required is True

    def test_name_field_is_str(self):
        """
        Field Name Verification type is string
        """
        assert isinstance(self.model._fields['name'], StringField)

    # test field climate

    def test_climate_field_exists(self):
        """
        Field Climate Verification Exists
        """
        assert 'climate' in self.model._fields

    def test_climate_field_not_required(self):
        """
        Field climate Verification is required
        """
        assert self.model._fields['climate'].required is False

    def test_climate_field_not_unique(self):
        """
        Field climate Verification is unique
        """
        assert self.model._fields['climate'].required is False

    def test_climate_field_is_str(self):
        """
        Field climate Verification type is string
        """
        assert isinstance(self.model._fields['climate'], StringField)

    # teste field terrain
    def test_terrain_field_exists(self):
        """
        Field terrain Verification Exists
        """
        assert 'terrain' in self.model._fields

    def test_terrain_field_not_required(self):
        """
        Field terrain Verification is required
        """
        assert self.model._fields['terrain'].required is False

    def test_terrain_field_not_unique(self):
        """
        Field terrain Verification is unique
        """
        assert self.model._fields['terrain'].required is False

    def test_terrain_field_is_str(self):
        """
        Field terrain Verification type is string
        """
        assert isinstance(self.model._fields['terrain'], StringField)

    def test_all_fields_in_model(self):
        """
        I check if all fields are actually in my model
        """
        fields = [
            'name', 'climate', 'terrain', 'created_at'
        ]

        model_keys = [i for i in self.model._fields.keys()]

        fields.sort()
        model_keys.sort()

        assert fields == model_keys
