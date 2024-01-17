from __init__ import CURSOR, CONN

class Artist:

    #Dict of objects saved to database
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Artist {self.id}: {self.name}"

    def save(self):
        sql = """
            INSERT INTO artists (name)
            VALUES (?)
            """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        #This adds artist instance to dict
        type(self).all[self.id] = self

    def update(self):
        #UPDATES table row
        sql = """
            UPDATE artists
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    #Is, by default, the getter method
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    def delete(self):
        #DELETES table ROW
        sql = """
            DELETE FROM artists
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name):
        new_artist = cls(name)
        new_artist.save()
        return new_artist

    @classmethod
    def create_table(cls):
        try:
            sql = """
                CREATE TABLE IF NOT EXISTS artists (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )
            """
            CURSOR.execute(sql)
            CONN.commit()
            print("Table 'artists' created successfully.")
        except Exception as e:
            print(f"Error creating table: {e}")

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS artists;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        artist = cls.all.get(row[0])
        if artist:
            artist.name = row[1]
            artist.id = row[0]
        else:
            artist = cls(row[1], row[0])
            artist.id = row[0]
            cls.all[artist.id] = artist
        return artist
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM artists
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    #Might not actually use this method? Maybe searching by name is more user friendly
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM artists
            WHERE id = ?
        """

        #.fetchone() will give you the 1 row of the found element
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    #Might not actually use this method? Maybe searching by name is more user friendly   

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM artists
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    #Handles the artist's songs
    @classmethod
    def artists_songs(cls, artist):
        from models.song import Song

        sql = """
            SELECT * FROM songs
            WHERE artist_id = ?
        """
        CURSOR.execute(sql, (artist.id,))

        rows = CURSOR.fetchall()
        return [
            Song.instance_from_db(row) for row in rows
        ]
    #Handles the artist's songs