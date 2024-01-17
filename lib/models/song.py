from __init__ import CURSOR, CONN
from artist import Artist

class Song:

    def __init__(self, title, artist_id, id=None):
        self.id = id
        self.title = title
        self.artist_id = artist_id

    def __repr__(self):
        return(
            f"<Song {self.id}: {self.title}" +
            f"Artist ID: {self.artist_id}>"
        )

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            title TEXT,
            artist_id INTEGER, FOREIGN KEY (artist_id REFERENCES artists(id))
            )"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO songs (title, artist_id)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.title, self.artist.id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self