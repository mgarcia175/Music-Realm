import sqlite3
from lib.util import execute_query
from lib.models.__init__ import CURSOR, CONN

CONN = sqlite3.connect('music_libr.db')
CURSOR = CONN.cursor()

class Artist:

    #List of songs to refer to when needing to manipulate song instances
    all_artists = []

    def __init__(self, name, artist_id=None):
        self.artist_id = artist_id
        self.name = name

        #Will hold songs with the instance of the artist
        self.songs = []

        if artist_id is None:
            self.add_artist_to_db()
    
    def add_artist_to_db(cls, name):
        CURSOR.execute("INSERT INTO artists (name) VALUES (?)", (name,))
        artist_id = CURSOR.lastrowid
        CONN.commit()
        return cls(name, artist_id)
    
    @classmethod
    def load_all_artists(cls):
        CURSOR.execute("SELECT * FROM artists")
        rows = CURSOR.fetchall()

        for row in rows:
            artist_id, name = row

            artist = cls(name, artist_id)
            cls.all_artists.append(artist)

    @staticmethod
    def remove_artist_from_db(artist_id):
        CURSOR.execute("DELETE FROM artists where ID = ?", (artist_id,))
        CONN.commit()

    @staticmethod
    def find_artist_by_id(cls, artist_id):
        for artist in cls.all_artists:
            if artist.artist_id == int(artist_id):
                return artist
        return None