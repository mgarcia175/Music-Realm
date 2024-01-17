from __init__ import CURSOR, CONN

class Artist:

    #Dict of objects saved to database
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Artist {self.id}: {self.name}>"

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

    def delete(self):
        #DELETES table ROW
        sql = """
            DELETE FROM artists
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

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
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM artists
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None