import sqlite3
from .models.artist import Artist
# from models.song import Song

def exit_program():
    print("Exiting menu.. Goodbye!")
    exit()

#KEEP
def list_all_artists():
    try:
        Artist.load_all_artists()

        print("---------🌟Available Artists🌟---------")

        artists_found = False

        for artist in Artist.all_artists:
            print(f"🥁🎹🎸{artist.name} (ID: {artist.artist_id})🎸🎹🥁")
            artists_found = True

        if not artists_found:
            print("Oh no! There are currently no existing artists.. 😢")

    except ValueError as ve:
        print(f"Error: {ve}")
#KEEP

#KEEP
# def list_all_songs():
#     try:
#         Song.load_all_songs()
#         print("---------🎹Available Songs🎹---------")

#         for song in Song.all_songs:
#             print(f"🎶{song.title} | ID: {song.song_id}🎶")

#         if not Song.all_songs:
#             print("Oh no! There are currently no existing songs.. 😢")
#             return
#     except ValueError as ve:
#         print(f"Error: {ve}")
#KEEP