from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class CustomDestroyMixin(GenericViewSet):
    def destroy(self, request, *arg, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
