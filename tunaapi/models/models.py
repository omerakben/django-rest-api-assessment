from django.db import models

"""
This module contains data models for the Tuna API.
"""


class Artist(models.Model):
    """
    Represents an artist in the Tuna API.
    """

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    bio = models.TextField()


class Genre(models.Model):
    """
    Represents a music genre in the Tuna API.
    """

    description = models.CharField(max_length=255)


class Song(models.Model):
    """
    Represents a song in the Tuna API.
    """

    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, related_name="songs", on_delete=models.CASCADE)
    album = models.CharField(max_length=255)
    length = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name="songs", through="SongGenre")


class SongGenre(models.Model):
    """
    Represents a many-to-many relationship between songs and genres in the Tuna API.
    """

    song = models.ForeignKey(Song, related_name="song_genres", on_delete=models.CASCADE)
    genre = models.ForeignKey(
        Genre, related_name="song_genres", on_delete=models.CASCADE
    )
