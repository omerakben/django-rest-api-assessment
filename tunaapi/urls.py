from django.urls import path

from tunaapi.views import ArtistViewSet, GenreViewSet, SongViewSet

song_list = SongViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
song_detail = SongViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)

artist_list = ArtistViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
artist_detail = ArtistViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)

genre_list = GenreViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
genre_detail = GenreViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("songs", song_list, name="song-list"),
    path("songs/<int:pk>", song_detail, name="song-detail"),
    path("artists", artist_list, name="artist-list"),
    path("artists/<int:pk>", artist_detail, name="artist-detail"),
    path("genres", genre_list, name="genre-list"),
    path("genres/<int:pk>", genre_detail, name="genre-detail"),
]
