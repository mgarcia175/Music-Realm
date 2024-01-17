from __init__ import CURSOR, CONN
from models.artist import Artist

class Song:

    all = {}

    def __init__(self, title, artist, id=None):
        self.id = id
        self.title = title
        self.artist = artist

    def __repr__(self):
        return f"<Song {self.id}: {self.title} by {self.artist.name}>"

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError(
                "Title must be a non-empty string"
            )

    def save(self):
        sql = """
            INSERT INTO songs (title, artist_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.title, self.artist.id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE songs
            SET title = ?, artist_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.artist.id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM songs
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, title, artist):
        new_song = cls(title, artist)
        new_song.save()
        return new_song

    @classmethod
    def create_table(cls):
        try:
            sql = """
                CREATE TABLE IF NOT EXISTS songs (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    artist_id INTEGER,
                    FOREIGN KEY (artist_id) REFERENCES artists(id)
                )
            """
            CURSOR.execute(sql)
            CONN.commit()
            print("Table 'songs' created successfully.")
        except Exception as e:
            print(f"Error creating table: {e}")

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS songs;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        song = cls.all.get(row[0])
        if song:
            song.title = row[1]
            song.artist = Artist.find_by_id(row[2])
            song.id = row[0]
        else:
            artist = Artist.find_by_id(row[2])
            song = cls(row[1], artist, row[0])
            cls.all[song.id] = song
        return song

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM songs
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT *
            FROM songs
            WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
