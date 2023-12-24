import sqlite3

class Favorited_Song:
    my_favorited_songs = []

    def __init__(self, song):
        self.song = song

        Favorited_Song.my_favorited_songs.append(self)

    def __str__(self):
        return f"{self.song.title}(ID: {self.song.song_id}) by {self.song.artist.name}"