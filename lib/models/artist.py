import sqlite3
from lib.util import execute_query

CONN = sqlite3.connect('music_libr.db')
CURSOR = CONN.cursor()

class Artist:

    #List of songs to refer to when needing to manipulate song instances
    all_artists = []

    def __init__(self, name, artist_id):
        self.artist_id = artist_id
        self.name = name
        
        #Will hold songs with the instance of the artist
        self.songs = []

        self.add_artist_instance()

    def add_artist_instance(self):
        if self not in Artist.all_artists:
            Artist.all_artists.append(self)

            query = "INSERT INTO artists (name) VALUES (?)"
            new_artist_id = execute_query(query, params=(self.name,), return_id=True)

            self.artist_id = new_artist_id

            CONN.commit()

    def add_song(self, song):
        self.songs.append(song)
        song.assign_to_artist(self)

    def __repr__(self):
        return f"{self.name} (ID: {self.artist_id})"