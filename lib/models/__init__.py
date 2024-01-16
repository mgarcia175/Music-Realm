import sqlite3

CONN = sqlite3.connect('my_music_libr.db')
CURSOR = CONN.cursor()