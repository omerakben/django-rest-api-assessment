from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from tunaapi.models import Song
from tunaapi.serializers import SongDetailSerializer, SongSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_serializer_class(self):
        if hasattr(self, "action") and self.action == "retrieve":
            return SongDetailSerializer
        return SongSerializer

    def list(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            song = serializer.save()
            return Response(SongSerializer(song).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        song = get_object_or_404(Song, pk=pk)
        serializer = SongDetailSerializer(song)
        return Response(serializer.data)

    def update(self, request, pk=None):
        song = get_object_or_404(Song, pk=pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            song = serializer.save()
            return Response(SongSerializer(song).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        song = get_object_or_404(Song, pk=pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
