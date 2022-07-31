from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers


class ForeignKeyField(serializers.IntegerField):
    def __init__(self, model, **kwargs):
        self.model = model
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        if not data:
            return None

        try:
            instance = self.model.objects.get(pk=data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError("Id does not exist")
        except (TypeError, ValueError):
            raise serializers.ValidationError("Id type is incorrect")

        return instance.id
