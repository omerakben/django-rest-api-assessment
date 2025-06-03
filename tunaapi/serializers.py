from rest_framework import serializers

from tunaapi.models import Artist, Genre, Song


class SongSerializer(serializers.ModelSerializer):
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(), source="artist"
    )

    class Meta:
        model = Song
        fields = ["id", "title", "artist_id", "album", "length"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "description"]


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name", "age", "bio"]


class SongDetailSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ["id", "title", "artist", "album", "length", "genres"]

    def get_genres(self, obj):
        # Get actual Genre objects
        genre_ids = obj.song_genres.values_list("genre", flat=True)
        genres = Genre.objects.filter(id__in=genre_ids)
        return GenreSerializer(genres, many=True).data


class ArtistDetailSerializer(serializers.ModelSerializer):
    song_count = serializers.SerializerMethodField()
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ["id", "name", "age", "bio", "song_count", "songs"]

    def get_song_count(self, obj):
        return obj.songs.count()

    def get_songs(self, obj):
        return [
            {
                "id": song.id,
                "title": song.title,
                "album": song.album,
                "length": song.length,
            }
            for song in obj.songs.all()
        ]


class GenreDetailSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ["id", "description", "songs"]

    def get_songs(self, obj):
        return [
            {
                "id": sg.song.id,
                "title": sg.song.title,
                "artist_id": sg.song.artist.id,
                "album": sg.song.album,
                "length": sg.song.length,
            }
            for sg in obj.song_genres.select_related("song")
        ]
