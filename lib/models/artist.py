import sqlite3
from lib.models.__init__ import CURSOR, CONN

class Artist:
    all_artists = []

    def __init__(self, name, artist_id=None):
        self.artist_id = artist_id
        self.name = name
        self.songs = []

        if artist_id is None:
            self.add_artist_to_db()

    def __repr__(self):
        return f'<Artist {self.artist_id}: {self.name}>'
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS artists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def __str__(self):
        return f"{self.name} (ID: {self.artist_id})"

    def add_song(self, song):
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
        sql = """
            SELECT *
            FROM artists
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (artist_id,)).fetchone()
        if row:
            return cls(name=row[1], artist_id=row[0])
        else:
            return None

Artist.create_table()