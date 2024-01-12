import sqlite3
from .models.artist import Artist
from .models.favorites import Favorited_Song
from models.song import Song

def exit_program():
    print("Exiting menu.. Goodbye!")
    exit()

#functions for artist vvv
def add_artist():
    print("---------🌟Adding artist🌟---------")

    artist_name = input("Artist Name (Or enter 0 to go back): ")

    if artist_name == '0':
        return

    new_artist = Artist(name=artist_name)
    Artist.all_artists.append(new_artist)

    print(f"✅Nice! 🎤'{artist_name}'🎤 has been successfully added!✅")

def find_artist_by_id(artist_id):
    try:
        artist_id = input("Enter the Artist's ID: ")
        artist = Artist.find_artist_by_id(artist_id)

        if artist:
            print(f"Nice! Found them! 🌟{artist.name} (ID: {artist.artist_id})🌟")
        else:
            print(f"Uh oh.. Looks like we don't have an artist with that ID 😢")
    except ValueError:
        print("🛑Err! Stop right there! The inputed ID is not valid.🛑")

def list_all_artists():
    try:
        print(f"---------🌟Available Artists🌟---------")

        list_of_artists = None
        artists_found = False

        for artist in Artist.all_artists:
            if artist:
                list_of_artists = artist
                print(f"🥁🎹🎸{artist.name} (ID: {artist.artist_id})🎸🎹🥁")
                artists_found = True
        if not artists_found:
            print("Oh no! There are currently no existing artists.. 😢")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
#functions for artist ^^^

#functions for song class
def add_song():
    print("---------🎶Adding song🎶---------")

    song_title = input('Enter song title (Or enter 0 to go back): ')

    if song_title == "0":
        return
    
    if not Artist.all_artists:
        print("Oh no! There are currently no existing artists..😢")


    list_all_artists()

    songs_artist_id = input('Enter the ID of the artist to assign your song!(`NA` if not assigning): ')

    try:
        songs_artist_id = int(songs_artist_id)
    except ValueError:
        print ("🛑Invalid input. Valid Song ID required.🛑")
        return
    #In case NA is entered
    artist = find_artist_by_id(songs_artist_id) if songs_artist_id.lower() != 'na' else None

    #If the artist was found with the provided ID, create a new instance of a Song
    newly_added_song = Song(song_id=song_title.lower().replace(" ", "_"), title=song_title, artist=artist)

    print(f"Song Title:{newly_added_song.title}, Assigned Artist: {newly_added_song.artist.name if newly_added_song.artist else None}")

    if artist:
        #Add the song to the matching artist
        artist.add_song(newly_added_song)
        newly_added_song.save_to_db()
        print(f"✅Nicely done! Song added: 🎶{newly_added_song}🎶 and assigned to 🎤{artist}🎤!✅")
    else:
        print(f"Hmm.. It doesn't seem like there exists an artist with that ID. Sorry.🙁 ")

def remove_song():
    print("---------❌Removing Song❌---------")

    list_all_songs()

    deleted_song_id = input("Please enter the song's ID to remove (Or enter 0 to go back): ")

    try:
        deleted_song_id = int(deleted_song_id)
    except ValueError:
        print("🛑Invalid input. Valid Song ID required.🛑")

    removed_song = find_song_by_id(deleted_song_id)

    if deleted_song_id == '0':
        return
    
    if removed_song:
        try:
            Song.remove_song_from_db(remove_song.song_id)
            Song.all_songs.remove(removed_song)
            print(f"Done. ❌{removed_song}❌ has now been removed.")
        except Exception as ex:
            print(f"🛑Uh oh! Error occurred while removing!🛑: {ex}")

        else:
            print("Uh oh. It seems there is no song by that ID. 🙁")

def list_all_songs():

    print("---------🎹Available Songs🎹---------")

    song_list = None
    found_songs = False

    for song in Song.all_songs:
        if song:
            song_list = song
            print(f"🎶{song.title} (ID:{song.song_id}🎶)")
            found_songs = True
    if not found_songs:
        print("Oh no! There are currently no existing songs.. 😢")

def find_song_by_id():
    try:
        song_id = input("Please enter the Song's ID: ")
        song = find_artist_by_id(song_id)

        if song:
            print(f"Nice! Found it! 🎶{song.title} (ID: {song.song_id})🎶")
        else:
            print(f"Uh oh.. Looks like we don't have an song with that ID 😢")
    except ValueError:
        print("🛑Err! Stop right there! The inputed ID is not valid.🛑")

def list_artists_songs():
    print("---------🌟🌟Listing songs for an artist🌟🌟---------")

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
    print("---------❤️Adding song to your favorites❤️---------")

    list_all_songs()

    needed_song_id = input("Enter your desired song's ID (Or enter 0 to go back): ")

    song_to_be_favorited = find_song_by_id(needed_song_id)

    if needed_song_id == '0':
        return

    if song_to_be_favorited:
        favorited_song_instance = Favorited_Song(song_to_be_favorited)
        Favorited_Song.add_favorited_song_to_db(song_to_be_favorited)
        print(f"✅Success! 🎶{song_to_be_favorited.title}🎶 now favorited:✅")

    else:
        print(f"Hmmm.. It looks like there is no song with the ID of {needed_song_id}.🙁")

def remove_favorited_song():
    print("---------❌Removing Favorited song❌---------")

    list_favorited_songs()

    try:
        removed_favorited_song_id = input("Enter the favorited song's ID (Or enter 0 to go back): ")

        removed_song = None

        if removed_favorited_song_id == '0':
            return

        for favorited_song in Favorited_Song.my_favorited_songs:
            if favorited_song.song.song_id == removed_favorited_song_id:
                removed_song = favorited_song
                break
        
        if removed_song:
            Favorited_Song.my_favorited_songs.remove(removed_song)
            Favorited_Song.remove_favorited_song_from_db(removed_favorited_song_id)
            print(f"Done! ❌{removed_song}❌ has now been removed from your Favorites.")
        else:
            print(f"Hmm... It seems there is no song with the ID of {removed_favorited_song_id} in your Favorites. 🙁")

    except ValueError:
        print("🛑Invalid input. Valid Song ID required.🛑")
    except Exception as ex:
        print(f"🛑Error! {ex}🛑")

def list_favorited_songs():
    
    print("---------❤️Your Favorited Songs❤️---------")

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
        
def find_favorited_song_by_id():

    try:
        favorited_song_id = input("Enter the favorited Song's ID: ")
        favorited_song = Favorited_Song.find_favorited_song_by_id(favorited_song_id)
                              
        if favorited_song:
            print(f"Nice! Found it! 🎶{favorited_song.song.title} (ID: {favorited_song.song.song_id})🎶")
        else:
            print(f"Uh oh.. Looks like you don't have a favorited song with that ID 😢")
    except ValueError:
        print("🛑Err! Stop right there! The inputed ID is not valid.🛑")

