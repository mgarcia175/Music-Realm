from lib.models.__init__ import CURSOR, CONN
from models.artist import Artist

class Song:
    all_songs = []

    def __init__(self, song_id, title, artist=None):
        self.song_id = song_id
        self.artist = artist
        self.title = title

    def __str__(self):
        return f"{self.title}"
    
    def save_to_db(self):
        CURSOR.execute("""
            INSERT INTO songs (song_id, title, artist_id)
            VALUES (?, ?, ?)
        """, (self.song_id, self.title, self.artist.artist_id))
        #settings values to the desired then making sure to commit changes
        CONN.commit()

    @classmethod
    def load_all_songs(cls):  
        CURSOR.execute("SELECT song_id, title, artist_id FROM songs")
        rows = CURSOR.fetchall()

        cls.all_songs.clear()

        for row in rows:
            song_id, title, artist_id = row
            artist = Artist.find_artist_by_id(artist_id)
            song = cls(song_id, title, artist)

            if artist:
                song.artist = artist

            cls.all_songs.append(song)
            print(f"Song ID: {song_id}, Title: {title}, Artist ID: {artist_id}")

        return cls.all_songs


    def add_song_instance(self):
        if self not in Song.all_songs:
            Song.all_songs.append(self)
            if self.artist:
                self.artist.add_song(self)
        elif self.artist and self not in self.artist.songs:
            self.artist.add_song(self)

    def assign_to_artist(self, artist):
        self.artist = artist

    @staticmethod
    def remove_song_from_db(song_id):
        CURSOR.execute("DELETE FROM songs WHERE song_id = ?", (song_id,))
        CONN.commit()

    @classmethod
    def find_song_by_id(cls, song_id):
        for song in cls.all_songs:
            if song.song_id == song_id:
                return song
        return None
