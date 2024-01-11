import sqlite3
from lib.models import CURSOR, CONN

class Favorited_Song:
    my_favorited_songs = []

    def __init__(self, song):
        self.song = song

        Favorited_Song.my_favorited_songs.append(self)

    def __str__(self):
        if self.song and self.song.artist:
            return f"{self.song.title}(ID: {self.song.song_id}) by {self.song.artist.name}"
        elif self.song:
            return f"{self.song.title}(ID: {self.song.song_id})"
        else:
            return "Invalid Favorited Song"
    
    @staticmethod
    def add_favorited_song_to_db(song_id):
        CURSOR.execute("INSERT INTO favorites WHERE song_id = ?", (song_id,))
        CONN.commit()

    @staticmethod
    def remove_favorited_song_from_db(song_id):
        CURSOR.execute("DELETE FROM favorites WHERE song_id = ?", (song_id,))
        CONN.commit()