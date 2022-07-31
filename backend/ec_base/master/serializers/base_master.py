from rest_framework import serializers


class BaseMasterListSlz(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)


class BaseMasterCreateSlz(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class BaseMasterRetrieveSlz(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)


# -------------------------------------------- Params
class BaseMasterListReqParams(serializers.Serializer):
    parent_id = serializers.IntegerField(required=False)
