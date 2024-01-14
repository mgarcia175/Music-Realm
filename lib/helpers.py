import sqlite3
from .models.artist import Artist
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
    
    existing_artist= next((artist for artist in Artist.all_artists if artist.name.lower() == artist_name.lower()), None)

    if existing_artist:
        print(f"🛑Wait a gosh darn second! {existing_artist} already exists!🛑")
    
    else:
        Artist(name=artist_name)
        print(f"✅Nice! 🎤'{artist_name}'🎤 has been successfully added!✅")

def find_artist_by_id(artist_id):
    try:
        artist_id = int(artist_id)
        artist = next((artist for artist in Artist.all_artists if artist.artist_id == artist_id), None)

        if artist:
            print(f"Nice! Found them! 🌟{artist.name} (ID: {artist.artist_id})🌟")
            return artist
        else:
                print(f"Uh oh.. Looks like we don't have an artist with that ID 😢")
                return None
    except ValueError:
        print("🛑Err! Stop right there! The inputed ID is not valid.🛑")

def list_all_artists():
    try:
        Artist.load_all_artists()

        print(f"---------🌟Available Artists🌟---------")

        artists_found = False

        for artist in Artist.all_artists:
            print(f"🥁🎹🎸{artist.name} (ID: {artist.artist_id})🎸🎹🥁")
            artists_found = True

        if not artists_found:
            print("Oh no! There are currently no existing artists.. 😢")

    except ValueError as ve:
        print(f"Error: {ve}")
#functions for artist ^^^

#functions for song class     
def add_song():
    print("---------🎶Adding song🎶---------")

    # Ask the user for the ID of the artist
    list_all_artists()
    artist_id = input('Enter the ID of the artist to attach the song to (Enter 0 to go back): ')

    if artist_id == "0":
        return

    # Check if the provided artist ID is valid
    artist = find_artist_by_id(artist_id)

    if not artist:
        print("Hmm.. It doesn't seem like there exists an artist with that ID. Sorry.🙁 ")
        return

    # Ask the user for the song title
    song_title = input('Enter the song title: ')

    # Create a new instance of a Song
    newly_added_song = Song(song_id=song_title.lower().replace(" ", "_"), title=song_title, artist=artist)

    print(f"Song Title: {newly_added_song.title} | Assigned Artist: {newly_added_song.artist.name if newly_added_song.artist else None}")

    # Add the song to the matching artist
    artist.songs.append(newly_added_song)
    
    # Save the song to the database
    newly_added_song.save_to_db()
    
    print(f"✅Nicely done! Song added: 🎶{newly_added_song}🎶 and assigned to 🎤{artist}🎤!✅")

def remove_song():
    print("---------❌Removing Song❌---------")

    list_all_songs()

    deleted_song_id = input("Please enter the song's ID to remove (Or enter 0 to go back): ")

    try:
        deleted_song_id = int(deleted_song_id)
    except ValueError:
        print("🛑Invalid input. Valid Song ID required.🛑")
        return

    if deleted_song_id == 0:
        return

    # Find the song by ID
    removed_song = find_song_by_id(deleted_song_id)

    if removed_song:
        try:
            # Remove the song from the list of songs in memory
            Song.all_songs.remove(removed_song)

            # Remove the song from the database
            Song.remove_song_from_db(removed_song.song_id)

            artist_name = removed_song.artist.name if removed_song.artist else 'Not Assigned'
            print(f"Done. ❌{removed_song.title} (ID: {removed_song.song_id})❌ has now been removed. Artist: {artist_name}")
        except Exception as ex:
            print(f"🛑Uh oh! Error occurred while removing!🛑: {ex}")
    else:
        print(f"Uh oh. It seems there is no song with ID {deleted_song_id}. 🙁")

def list_all_songs():
    try:
        Song.load_all_songs()
        print("---------🎹Available Songs🎹---------")

        found_songs = False
        
        for song in Song.all_songs:
            print(f"🎶{song.title} | ID: {song.song_id}🎶")
            found_songs = True

        if not Song.all_songs:
            print("Oh no! There are currently no existing songs.. 😢")
            return
    except ValueError as ve:
        print(f"Error: {ve}")

def find_song_by_id(song_id):
    try:
        song = next((song for song in Song.all_songs if song.song_id == song_id), None)

        if song:
            print(f"Nice! Found it! 🎶{song.title} (ID: {song.song_id})🎶")
            return song
        else:
            print(f"Uh oh.. Looks like we don't have a song with that ID 😢")
            return None
    except ValueError:
        print("🛑Err! Stop right there! The inputed ID is not valid.🛑")
        return None

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

