import sqlite3
from lib.models.__init__ import CURSOR, CONN

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

    def __str__(self):
        return f"{self.name} (ID: {self.artist_id})"

    def add_song(self, song):
        """
        Add a song to the artist's list of songs.
        """
        self.songs.append(song)

    def add_artist_to_db(self):
        CURSOR.execute("INSERT INTO artists (name) VALUES (?)", (self.name,))
        self.artist_id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def load_all_artists(cls):
        try:
            CURSOR.execute("SELECT * FROM artists")
            rows = CURSOR.fetchall()

            cls.all_artists.clear()
            
            for row in rows:
                artist_id, name = row[0], row[1]
                artist = cls(name, artist_id)
                cls.all_artists.append(artist)

        except Exception as e:
            raise e

    @classmethod
    def remove_artist_from_db(cls, artist_id):
        CURSOR.execute("DELETE FROM artists where ID = ?", (artist_id,))
        CONN.commit()

    @classmethod
    def find_artist_by_id(cls, artist_id):

        existing_artist = next((artist for artist in cls.all_artists if artist.artist_id == artist_id), None)
        return existing_artist
    