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
    
    def __repr__(self):
        return f"Artist: {self.name} (ID: {self.artist_id})"
    
    def add_artist_to_db(self):
        CURSOR.execute("INSERT INTO artists (name) VALUES (?)", (self.name,))
        self.artist_id = CURSOR.lastrowid
        CONN.commit()
    
    def load_all_artists(cls):
        CURSOR.execute("SELECT * FROM artists")
        rows = CURSOR.fetchall()

        for row in rows:
            artist_id, name = row

            artist = cls(name, artist_id)
            cls.all_artists.append(artist)

    @staticmethod
    def remove_artist_from_db(artist_id):
        CURSOR.execute("EXECUTE FROM artists where ID = ?", (artist_id,))
        CONN.commit()