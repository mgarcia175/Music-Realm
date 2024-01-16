from __init__ import CURSOR, CONN

class Artist:

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