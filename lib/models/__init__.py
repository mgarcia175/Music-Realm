import sqlite3

CONN = sqlite3.connect('music_libr.db')
CURSOR = CONN.cursor()