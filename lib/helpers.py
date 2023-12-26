# lib/helpers.py
from models.artist import Artist
from models.favorites import Favorited_Song

def exit_program():
    print("Exiting menu.. Goodbye!")
    exit()

#functions for artist class
def add_artist():
    print("Adding artist")

    artist_name = input("Artist Name: ")
    artist_id = input("Artist ID: ")

    new_artist = Artist(name=artist_name, artist_id=artist_id)

    print("Nice! Successfully added: ")
    if new_artist:
        print(f"{new_artist}")

def find_artist_by_id():
    print("Finding artist by ID")

    needed_artist_id = input("Enter the artist's ID: ")

    searched_artist = None

    for artist in Artist.all_artists:
        if artist.artist_id == needed_artist_id:
            searched_artist = artist
            break
    if searched_artist:
        print(f"Artist found! --> {searched_artist}")
    else:
        print(f"Oh no! No artist found with the ID of {needed_artist_id}.")

def remove_artist():
    print("Removing artist...")
    
    deleted_artist_id = input ("Please enter the artist's id to remove: ")

    removed_artist = None

    for artist in Artist.all_artists:
        if artist.artist_id == deleted_artist_id:
            removed_artist = artist
            Artist.all_artists.remove(artist)
            break

    if removed_artist:
        print(f"{removed_artist} has now been removed.")
    else:
        print("Uh oh. It seems there is no artist by that ID.")

def list_all_artists():
    print("Listing all artists: ")

    list_of_artists = None
    artists_found = False

    for artist in Artist.all_artists:
        if artist:
            list_of_artists = artist
            print(f"{artist.name} (ID: {artist.artist_id})")
            artists_found = True
    if not artists_found:
        print("Oh no! There are currently no existing artists.. :(")
#functions for artist class

#functions for song class
def add_song():
    print("Adding song! Please provide the requred information..")

    song_title = input('Song Title: ')
    song_id = input("Song ID: ")
    songs_artist_id = input("Artist ID for song assignment: ")

    artist = find_artist_helper(songs_artist_id)

    if artist:
        #If the artist was found with the provided ID, create a new instance of a Song
        newly_added_song = Song(song_id=song_id, title=song_title, artist=artist)
        #Add the song to the matching artist
        artist.add_song(newly_added_song)
        print(f"Song added: {newly_added_song}")
    else:
        print(f"Uh oh! No artist found with the provided ID of {songs_artist_id}")

#This method will find the artist with the specific ID
def find_artist_helper(needed_artist_id):
    for artist in Artist.all_artists:
        if artist.artist_id == needed_artist_id:
            return artist
    return None
#This method will find the artist with the specific ID

def find_song_by_id():
    print("Finding song by ID")

    desired_song_id = input("Enter the desired song's ID ")

    found_song = None

    for song in Song.all_songs:
        if song.song_id == desired_song_id:
            found_song = song
            break
    if found_song:
        print(f"Song found! --> {found_song}")
    else:
        print(f"Oops! There is no song with the ID of {desired_song_id}")

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
            print(song.title)
            songs_found = True
    if not songs_found:
        print("Oh no! There are currently no existing songs.. :(")

def add_song_to_favorites():
    print("Adding song to your favorites!...")

    needed_song_id = input("Enter your desired song's ID: ")

    song_to_be_favorited = find_song_by_id(needed_song_id)

    if song_to_be_favorited:
        favorited_song_instance = Favorited_Song(song=song_to_be_favorited)
        print(f"Success! Song now favorited: {song_to_be_favorited.title}")
    else:
        print(f"Hmmm.. It looks like there is no song with the ID of {needed_song_id}")
#This method will find the song with the inputted song ID
def find_song_by_id(song_id):
    from models.song import Song
    for song in Song.all_songs:
        if song.song_id == song_id:
            return song
    return None
#This method will find the song with the inputted song ID


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