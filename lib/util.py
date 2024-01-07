import sqlite3

CONN = sqlite3.connect('music_libr.db')
CURSOR = CONN.cursor()

def execute_query(query, params=None, return_id=False):
    if params is not None:
        CURSOR.execute(query, params)
    else:
        CURSOR.execute(query)

    if return_id:
        return CURSOR.lastrowid
    
    CONN.commit()