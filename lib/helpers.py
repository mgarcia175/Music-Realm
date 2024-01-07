# lib/helpers.py
import sqlite3
from .models.artist import Artist
from .models import CURSOR, CONN
from .util import execute_query
from .models.favorites import Favorited_Song
from models.song import Song

def exit_program():
    print("Exiting menu.. Goodbye!")
    exit()

#functions for artist vvvvv
def add_artist():
    print("Adding artist")

    artist_name = input("Artist Name (Or enter 0 to go back): ")

    if artist_name == '0':
        return

    query = "INSERT INTO artists (name) VALUES (?)"
    new_artist_id = execute_query(query, params=(artist_name,), return_id=True)

    new_artist = Artist(name=artist_name, artist_id=new_artist_id)

    if new_artist not in Artist.all_artists:
        new_artist.add_artist_instance()

    print(f"✅Nice! 🎤'{artist_name}'🎤 has been successfully added!✅")









def find_artist_by_id(artist_id):
    # query = f"SELECT * FROM artists WHERE id = {artist_id}"
    # CURSOR.execute(query)
    # result = CURSOR.fetchone()

    # if result:
    #     return Artist(name=result[1], artist_id=result[0])
    # else:
    #     return None
    for artist in Artist.all_artists:
        if artist.artist_id == int(artist_id):
            return artist
    return None

def list_all_artists():
    print(f"🌟Available Artists🌟")

    list_of_artists = None
    artists_found = False

    for artist in Artist.all_artists:
        if artist:
            list_of_artists = artist
            print(f"🥁🎹🎸{artist.name} (ID: {artist.artist_id})🎸🎹🥁")
            artists_found = True
    if not artists_found:
        print("Oh no! There are currently no existing artists.. 😢")
#functions for artist ^^^


#functions for song class
def add_song():
    print("Adding song! Please provide the requred information..")

    song_title = input('Song Title (Or enter 0 to go back): ')

    if song_title == "0":
        return
    
    if not Artist.all_artists:
        print("Oh no! There are currently no existing artists..😢")


    list_all_artists()

    songs_artist_id = input('Enter the ID of the artist to assign your song!(`NA` if not assigning): ')

    #In case NA is entered
    artist = find_artist_by_id(songs_artist_id) if songs_artist_id.lower() != 'na' else None

    #If the artist was found with the provided ID, create a new instance of a Song
    newly_added_song = Song(song_id=song_title.lower().replace(" ", "_"), title=song_title, artist=artist)

    print(f"Song Title:{newly_added_song.title}, Assigned Artist: {newly_added_song.artist.name if newly_added_song.artist else None}")

    if artist:
        #Add the song to the matching artist
        artist.add_song(newly_added_song)
        newly_added_song.assign_to_artist(artist)
        print(f"✅Nicely done! Song added: 🎶{newly_added_song}🎶 and assigned to 🎤{artist}🎤!✅")
    else:
        print(f"Hmm.. It doesn't seem like there exists an artist with that ID. Sorry.🙁 ")







def remove_song():
    print("Removing Song...")

    list_all_songs()

    deleted_song_id = input("Please enter the song's ID to remove (Or enter 0 to go back): ")

    removed_song = find_song_by_id(deleted_song_id)

    if deleted_song_id == '0':
        return
    
    if removed_song:
        Song.all_songs.remove(removed_song)
        print(f"Done. ❌{removed_song}❌ has now been removed.")

        query = "DELETE FROM songs WHERE song_id = ?"
        execute_query(query, params=(removed_song.song_id,))
    else:
        print("Uh oh. It seems there is no song by that ID. 🙁")

def list_all_songs():

    print("🎹Available Songs🎹")

    song_list = None
    found_songs = False

    for song in Song.all_songs:
        if song:
            song_list = song
            print(f"🎶{song.title} (ID:{song.song_id}🎶)")
            found_songs = True
    if not found_songs:
        print("Oh no! There are currently no existing songs.. 😢")

def find_song_by_id(song_id):
    for song in Song.all_songs:
        if song.song_id == song_id:
            return song
    return None

def list_artists_songs():
    print("🌟🌟Listing songs for an artist..🌟🌟.")

    list_all_artists()

    selected_artist_id = input("Enter the artist's ID: ")

    selected_artist = find_artist_by_id(selected_artist_id)

    if selected_artist:
        #Checking for songs under the desired artist
        if selected_artist.songs:
            print(f"Songs by 🌟{selected_artist.name}🌟")
            for song in selected_artist.songs:
                print(f"🎶{song.title} (ID: {song.song_id})🎶")
    else:
        print(f"Uh oh. There doesn't seem to be an artist with that ID🙁")


def add_song_to_favorites():
    print("Adding song to your favorites!...")

    list_all_songs()

    needed_song_id = input("Enter your desired song's ID (Or enter 0 to go back): ")

    song_to_be_favorited = find_song_by_id(needed_song_id)

    if needed_song_id == '0':
        return

    if song_to_be_favorited:
        favorited_song_instance = Favorited_Song(song=song_to_be_favorited)
        print(f"✅Success! 🎶{song_to_be_favorited.title}🎶 now favorited:✅")

        query = "INSERT INTO favorites (song_id) VALUES (?)"
        execute_query(query, params=(song_to_be_favorited.song_id,))
    else:
        print(f"Hmmm.. It looks like there is no song with the ID of {needed_song_id}.🙁")

def remove_favorited_song():
    print("Removing Favorited song...")

    list_favorited_songs()

    removed_favorited_song_id = input("Enter the faovorited song's ID (Or enter 0 to go back): ")

    removed_song = None

    if removed_favorited_song_id == '0':
        return

    for favorited_song in Favorited_Song.my_favorited_songs:
        if favorited_song.song.song_id == removed_favorited_song_id:
            removed_song = favorited_song
            break
    
    if removed_song:
        Favorited_Song.my_favorited_songs.remove(removed_song)
        print(f"Done! ❌{removed_song}❌ has now been removed from your Favorites.")
    else:
        print(f"Hmm... It seems there is no song with the ID of {removed_favorited_song_id} in your Favorites. 🙁")

def list_favorited_songs():
    
    print("❤❤❤Your Favorited Songs❤❤❤")

    favorited_song_list = None
    favorite_songs_found = False

    for song in Favorited_Song.my_favorited_songs:
        if song:
            favorited_song_list = song
            print(f"🎶{song}🎶")
            favorite_songs_found = True
    if not favorite_songs_found:
        print("Hmm... There doesn't seem to be any songs in your Favorites at the moment. Sorry! 😢")
#functions for song class