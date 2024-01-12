import sqlite3
from lib.util import execute_query
from lib.models.__init__ import CURSOR, CONN
from models.song import Song

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
        CURSOR.execute("INSERT INTO favorited_songs (song_id) VALUES (?)", (song_id,))
        CONN.commit()

    @classmethod 
    def load_all_favorited_songs(cls):
        CURSOR.execute("SELECT * FROM favorited_songs")
        rows = CURSOR.fetchall()

        for row in rows:
            song_id = row[0]
            song = Song.find_song_by_id(song_id)

            favorited_song = cls(song)
            cls.my_favorited_songs.append(favorited_song)
    
 
    @staticmethod
    def remove_favorited_song_from_db(song_id):
        CURSOR.execute("DELETE FROM favorites WHERE song_id = ?", (song_id,))
        CONN.commit()

    @staticmethod
    def find_favorited_song_by_id(song_id):
        for favorited_song in Favorited_Song.my_favorited_songs:
            if favorited_song.song.song_id == song_id:
                return favorited_song
        return None