class Song:
    all_songs = []

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.artist = artist
        self.title = title
        Song.all_songs.append(self)

    def __str__(self):
        return f"{self.title} by {self.artist.name}"