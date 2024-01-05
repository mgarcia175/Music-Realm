--artist table creation
CREATE TABLE IF NOT EXISTS artists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

--song table creation
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id TEXT,
    title TEXT,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artists(id)
);

--favorites table creation
CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER,
    artist_id INTEGER,
    FOREIGN KEY (song_id) REFERENCES songs(id),
    FOREIGN KEY (artist_id) REFERENCES artists(id)
);