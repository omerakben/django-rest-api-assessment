from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from tunaapi.models import Artist
from tunaapi.serializers import ArtistDetailSerializer, ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_serializer_class(self) -> type:
        if hasattr(self, "action") and self.action == "retrieve":
            return ArtistDetailSerializer
        return ArtistSerializer
