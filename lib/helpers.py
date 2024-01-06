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


#functions for artist class
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

    print("🧑‍🎤🎹🎸Artists Available🎸🎹🧑‍🎤")
    list_all_artists()

    deleted_artist_id = input ("Please enter the artist's id to remove: ")

    artist_to_delete = find

def list_all_artists():
    print(f"Listing all artists:")

    list_of_artists = None
    artists_found = False

    for artist in Artist.all_artists:
        if artist:
            list_of_artists = artist
            print(f"🧑‍🎤🎹🎸{artist.name} (ID: {artist.artist_id})🎸🎹🧑‍🎤")
            artists_found = True
    if not artists_found:
        print("Oh no! There are currently no existing artists.. :(")
#functions for artist class






#functions for song class
def add_song():
    print("Adding song! Please provide the requred information..")

    song_title = input('Song Title: ')

    print('🎤🎹🎸Available Artists🎤🎹🎸')
    list_all_artists()

    songs_artist_id = input('Enter the ID of the artist to assign your song!(`NA` if not assigning): ')

    #In case NA is entered
    artist = find_artist_helper(songs_artist_id) if songs_artist_id.lower() != 'na' else None

    #If the artist was found with the provided ID, create a new instance of a Song
    newly_added_song = Song(song_id=song_title.lower().replace(" ", "_"), title=song_title, artist=artist)

    if artist:

        #Add the song to the matching artist
        artist.add_song(newly_added_song)
        print(f"Nicely done! Song added: 🎶{newly_added_song}🎶")
    else:
        print(f"Nicely done! 🎶🎶{newly_added_song}🎶🎶 successfully added!")



def remove_song():
    print("Removing song..")

    deleted_song_id = input("Please enter the song's ID ")

    removed_song = None

    for song in Song.all_songs:
        if song.song_id == deleted_song_id:
            removed_song = song
            Song.all_songs.remove(song)
            break
    
    if removed_song:
        print(f"{removed_song} has now been removed.")
    else:
        print("Uh oh. It seems there is no song by that ID.")

def list_all_songs():

    print("Listing all songs...")

    list_of_songs = None
    songs_found = False

    for song in Song.all_songs:
        if song:
            list_of_songs = song
            print(f'🎶🎹🎸{song.title}🎸🎹🎶')
            songs_found = True
    if not songs_found:
        print("Oh no! There are currently no existing songs.. :(")

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