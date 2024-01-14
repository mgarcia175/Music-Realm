import sqlite3
from lib.models.__init__ import CURSOR, CONN
from models.artist import Artist

class Song:
    all_songs = []

    def __init__(self, title, artist, song_id=None):
        self.song_id = song_id
        self.title = title
        self.artist = artist

        if song_id is None:
            self.add_song_to_db()

    def __repr__(self):
        return f'<Song {self.song_id}: {self.title} | Artist: {self.artist.name if self.artist else "Not Assigned"}>'
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                artist_id INTEGER,
                FOREIGN KEY (artist_id) REFERENCES artists (id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def __str__(self):
        return f"{self.title} by {self.artist.name} (ID: {self.song_id})"

    def save_to_db(self):
        CURSOR.execute("INSERT INTO songs (title, artist_id) VALUES (?, ?)", (self.title, self.artist.artist_id))
        self.song_id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def load_all_songs(cls):
        try:
            # CURSOR.execute("SELECT * FROM songs")
            CURSOR.execute("SELECT songs.id, songs.title, artists.id, artists.name FROM songs LEFT JOIN artists ON songs.artist_id = artists.id")
            rows = CURSOR.fetchall()

            cls.all_songs.clear()

            for row in rows:
                song_id, title, artist_id = row[0], row[1], row[2]
                artist = Artist.find_artist_by_id(artist_id)
                song = cls(title, artist, song_id)
                cls.all_songs.append(song)

        except Exception as e:
            raise e

    @classmethod
    def remove_song_from_db(cls, song_id):
        CURSOR.execute("DELETE FROM songs where ID = ?", (song_id,))
        CONN.commit()

    @classmethod
    def find_song_by_id(cls, song_id):
        existing_song = next((song for song in cls.all_songs if song.song_id == song_id), None)
        return existing_song