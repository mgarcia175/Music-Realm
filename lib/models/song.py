from lib import CURSOR, CONN

class Song:
    all_songs = []

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.artist = artist
        self.title = title
        Song.all_songs.append(self)

    def __str__(self):
        return f"{self.title} by {self.artist.name}"
    
    def save_to_db(self):
        CURSOR.execute("""
            INSERT INTO songs (song_id, title, artist_id)
            VALUES (?, ?, ?)
        """, (self.song_id, self.title, self.artist.artist_id))
        #settings values to the desired then making sure to commit changes
        CONN.commit()

    @classmethod
    def load_songs(cls):
        CURSOR.execute("SELECT * FROM songs")
        rows = CURSOR.fetchall()

        for row in rows:
            song_id, title, artist_id = row

            artist = find_artist_by_id(artist_id)
            song = cls(song_id, title, artist)
            cls.all_songs.append(song)