from rest_framework import serializers


class BaseMasterListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)


class BaseMasterListReqParams(serializers.Serializer):
    parent_id = serializers.IntegerField(required=False)


class BaseMasterCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class BaseMasterDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
