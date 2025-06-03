from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from tunaapi.models import Genre
from tunaapi.serializers import GenreDetailSerializer, GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_serializer_class(self) -> type:
        if hasattr(self, "action") and self.action == "retrieve":
            return GenreDetailSerializer
        return GenreSerializer
