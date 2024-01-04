--artist table creation
CREATE TABLE IF NOT EXISTS artists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    artist_id TEXT
);

--song table creation
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id TEXT,
    artist_id TEXT,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

--favorites table creation
CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id TEXT,
    artist_id TEXT,
    FOREIGN KEY (song_id) REFERENCES songs(song_id),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);