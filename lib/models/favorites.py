import sqlite3
from lib.models.__init__ import CURSOR, CONN

class Favorited_Song:
    all_favorites = []

    def __init__(self, user_id, song_id):
        self.user_id = user_id
        self.song_id = song_id

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS favorites (
                user_id INTEGER,
                song_id INTEGER,
                PRIMARY KEY (user_id, song_id),
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (song_id) REFERENCES songs (id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def add_favorite(cls, user_id, song_id):
        CURSOR.execute("INSERT INTO favorites (user_id, song_id) VALUES (?, ?)", (user_id, song_id))
        CONN.commit()

    @classmethod
    def remove_favorite(cls, user_id, song_id):
        CURSOR.execute("DELETE FROM favorites WHERE user_id = ? AND song_id = ?", (user_id, song_id))
        CONN.commit()

    @classmethod
    def load_all_favorites(cls):
        try:
            CURSOR.execute("SELECT * FROM favorites")
            rows = CURSOR.fetchall()

            cls.all_favorites.clear()

            for row in rows:
                user_id, song_id = row[0], row[1]
                favorite = cls(user_id, song_id)
                cls.all_favorites.append(favorite)

        except Exception as e:
            raise e

    @classmethod
    def find_favorite(cls, user_id, song_id):
        existing_favorite = next((fav for fav in cls.all_favorites if fav.user_id == user_id and fav.song_id == song_id), None)
        return existing_favorite


Favorited_Song.create_table()