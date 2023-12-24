import sqlite3

CONN = sqlite3.connect('music_libr.db')
CURSOR = CONN.cursor()

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS artists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        artist_id TEXT
    )
""")

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
        Artist.all_artists.append(self)

    def add_song(self, song):
        self.songs.append(song)

    def __repr__(self):
        return f"{self.name} (ID: {self.artist_id})"