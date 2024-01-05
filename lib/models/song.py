from lib.models.__init__ import CURSOR, CONN

class Song:
    all_songs = []

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.artist = artist
        self.title = title
        Song.all_songs.append(self)

    def __str__(self):
        return f"{self.title}"
    
    def save_to_db(self, artist_id):
        CURSOR.execute("""
            INSERT INTO songs (song_id, title, artist_id)
            VALUES (?, ?, ?)
        """, (self.song_id, self.title, artist_id))
        #settings values to the desired then making sure to commit changes
        CONN.commit()

    @classmethod
    def load_all_songs(cls):
        CURSOR.execute("SELECT * FROM songs")
        rows = CURSOR.fetchall()

        for row in rows:
            song_id, title, artist_id = row

            song = cls(song_id, title)
            cls.all_songs.append(song)