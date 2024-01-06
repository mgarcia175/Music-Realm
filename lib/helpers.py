# lib/helpers.py
import sqlite3
from .models import CURSOR, CONN
from .models.artist import Artist
from .models.favorites import Favorited_Song
from models.song import Song

def execute_query(query, params=None, return_id=False):
    if params is not None:
        CURSOR.execute(query, params)
    else:
        CURSOR.execute(query)

    if return_id:
        return CURSOR.lastrowid
    
    CONN.commit()

def exit_program():
    print("Exiting menu.. Goodbye!")
    exit()


#functions for artist vvvvv
def add_artist():
    print("Adding artist")

    artist_name = input("Artist Name: ")

    query = "INSERT INTO artists (name) VALUES (?)"
    new_artist_id = execute_query(query, params=(artist_name,), return_id=True)

    new_artist = Artist(name=artist_name, artist_id=new_artist_id)

    print(f"Nice! 🎤'{artist_name}'🎤 has been successfully added!")

def find_artist_by_id(artist_id):
    query = f"SELECT * FROM artists WHERE id = {artist_id}"
    CURSOR.execute(query)
    result = CURSOR.fetchone()

    if result:
        return Artist(name=result[1], artist_id=result[0])
    else:
        return None

def remove_artist():
    print("Removing artist...")

    list_all_artists()

    deleted_artist_id = input ("Please enter the artist's id to remove: ")

    artist_to_delete = find_artist_by_id(deleted_artist_id)

    if artist_to_delete:
        Artist.all_artists.remove(artist_to_delete)
        print(f"Done. ❌{artist_to_delete.name}❌ successfully removed.")

        query = "DELETE FROM artists WHERE id = ?"
        execute_query(query, params=(artist_to_delete.artist_id,))

        print("Remaining artists in the database:")
        execute_query("SELECT * FROM artists")

    else:
        print("Hmm.. There doesn't seem to be an artist with that ID.")

def list_all_artists():
    print(f"🎸🎹🧑‍🎤Available Artists🧑‍🎤🎹🎸")

    list_of_artists = None
    artists_found = False

    for artist in Artist.all_artists:
        if artist:
            list_of_artists = artist
            print(f"🧑‍🎤🎹🎸{artist.name} (ID: {artist.artist_id})🎸🎹🧑‍🎤")
            artists_found = True
    if not artists_found:
        print("Oh no! There are currently no existing artists.. :(")
#functions for artist ^^^


#functions for song class
def add_song():
    print("Adding song! Please provide the requred information..")

    song_title = input('Song Title: ')

    list_all_artists()

    songs_artist_id = input('Enter the ID of the artist to assign your song!(`NA` if not assigning): ')

    #In case NA is entered
    artist = find_artist_by_id(songs_artist_id) if songs_artist_id.lower() != 'na' else None

    #If the artist was found with the provided ID, create a new instance of a Song
    newly_added_song = Song(song_id=song_title.lower().replace(" ", "_"), title=song_title, artist=artist)

    if artist:

        #Add the song to the matching artist
        artist.add_song(newly_added_song)
        print(f"Nicely done! Song added: 🎶{newly_added_song}🎶")
    else:
        print(f"Nicely done! 🎶🎶{newly_added_song}🎶🎶 successfully added!")

def remove_song():
    print("Removing Song...")

    list_all_songs()

    deleted_song_id = input("Please enter the song's ID to remove: ")

    removed_song = find_song_by_id(deleted_song_id)
    
    if removed_song:
        Song.all_songs.remove(removed_song)
        print(f"Done. ❌{removed_song}❌ has now been removed.")

        query = "DELETE FROM songs WHERE song_id = ?"
        execute_query(query, params=(removed_song.song_id,))
    else:
        print("Uh oh. It seems there is no song by that ID.")

def list_all_songs():

    print("🎸🎹🧑‍🎤Songs Available🧑‍🎤🎹🎸")

    song_list = None
    found_songs = False

    for song in Song.all_songs:
        if song:
            song_list = song
            print(f"🎶{song.title} ID:{song.song_id}🎶")
            found_songs = True
    if not found_songs:
        print("Oh no! There are currently no existing songs.. :(")

def find_song_by_id(song_id):
    for song in Song.all_songs:
        if song.song_id == song_id:
            return song
    return None







def add_song_to_favorites():
    print("Adding song to your favorites!...")

    # needed_song_id = input("Enter your desired song's ID: ")

    # song_to_be_favorited = find_song_by_id(needed_song_id)

    # if song_to_be_favorited:
    #     favorited_song_instance = Favorited_Song(song=song_to_be_favorited)
    #     print(f"Success! Song now favorited: {song_to_be_favorited.title}")
    # else:
    #     print(f"Hmmm.. It looks like there is no song with the ID of {needed_song_id}")

def remove_favorited_song():
    print("Removing Favorited song...")

    removed_favorited_song_id = input("Enter the faovorited song's ID: ")

    removed_song = None

    for favorited_song in Favorited_Song.my_favorited_songs:
        if favorited_song.song.song_id == removed_favorited_song_id:
            removed_song = favorited_song
            break
    
    if removed_song:
        Favorited_Song.my_favorited_songs.remove(removed_song)
        print(f"{removed_song} has now been removed from your Favorites.")
    else:
        print(f"Hmm... It seems there is no song with the ID of {removed_favorited_song_id} in your Favorites.")

def list_favorited_songs():
    
    print("Listing all of your favorited songs!..")

    favorited_song_list = None
    favorite_songs_found = False

    for song in Favorited_Song.my_favorited_songs:
        if song:
            favorited_song_list = song
            print(song)
            favorite_songs_found = True
        if not favorite_songs_found:
            print("Hmm... There doesn't seem to be any songs in your Favorites at the moment. Sorry!")
#functions for song class