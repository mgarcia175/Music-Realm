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

    for artist in Artist.all_artists:
        if artist.name.lower() == artist_name.lower():
            print(f"🛑Wait a gosh darn second! '{artist_name}' already exists!🛑")
        else:
            Artist(name=artist_name)
            print(f"✅Nice! 🎤'{artist_name}'🎤 has been successfully added!✅")

def find_artist_by_input():
    try:
        artist_id = int(input("Enter the ID of the artist: "))
        artist = Artist.find_artist_by_id(artist_id)

        if artist:
            print("----------🎤Found Artist🎤----------")
            print(f"Details: \nArtist Name: 🌟{artist.name} (ID: {artist.artist_id})🌟")
        
            update_artist_name = input("Would you like to update the artist's name? (Y/N?): ")

            if update_artist_name == 'y':
                new_artist_name = input("Enter the updated artist name: ")
                Artist.update_artist_name(artist_id, new_artist_name)
            elif update_artist_name == 'n':
                return

        else:
            print(f"Uh oh.. Looks like we don't have an artist with that ID 😢")
    except ValueError:
        print("🛑Err! Stop right there! The inputed ID is not valid.🛑")
        return None

def remove_artist():
    print("---------❌Removing Artist❌---------")

    list_all_artists()

    deleted_artist_id = input("Please enter the Artist's song to remove (Or 0 to go back): ")

    try:
        deleted_artist_id = int(deleted_artist_id)
    except ValueError:
        print("🛑Invalid input. Valid Song ID required.🛑")
        return

    if deleted_artist_id == 0:
        return

    removed_artist = Artist.find_artist_by_id(deleted_artist_id)

    if removed_artist:
        try:
            if removed_artist in Artist.all_artists:
                Artist.all_artists.remove(removed_artist)

            Artist.remove_artist_from_db(deleted_artist_id)
            
            removed_artist_name = removed_artist.name
            print(f"Done. ❌{removed_artist_name} has now been removed.❌")
        except ValueError as ex:
            print(f"🛑Uh oh! Error occurred while removing!🛑: {ex}")
    else:
        print(f"Uh oh. It seems there is no Artist with the ID of {deleted_artist_id}")

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
#functions for artist ^^^

#functions for song class     
def add_song():
    print("---------🎶Adding song🎶---------")

    # Ask the user for the ID of the artist
    list_all_artists()
    artist_id = input('Enter the ID of the artist to attach the song to (Enter 0 to go back): ')

    if artist_id == "0":
        return

    artist = Artist.find_artist_by_id(artist_id)

    if not artist:
        print("Hmm.. It doesn't seem like there exists an artist with that ID. Sorry.🙁 ")
        return

    song_title = input('Enter the song title: ')

    newly_added_song = Song(song_id=song_title.lower().replace(" ", "_"), title=song_title, artist=artist)

    print(f"Song Title: {newly_added_song.title} | Assigned Artist: {newly_added_song.artist.name if newly_added_song.artist else None}")

    artist.songs.append(newly_added_song)
    
    newly_added_song.save_to_db()
    
    print(f"✅Nicely done! Successfully added 🎶{newly_added_song}🎶 by 🎤{artist}🎤!✅")

def remove_song():
    print("---------❌Removing Song❌---------")

    list_all_songs()

    deleted_song_id = input("Please enter the song's ID to remove (Or 0 to go back): ")

    try:
        deleted_song_id = int(deleted_song_id)
    except ValueError:
        print("🛑Invalid input. Valid Song ID required.🛑")
        return

    if deleted_song_id == 0:
        return

    # Find song by ID
    removed_song = Song.find_song_by_id(deleted_song_id)

    if removed_song:
        try:
            if removed_song in Song.all_songs:
                Song.all_songs.remove(removed_song)

            Song.remove_song_from_db(removed_song.song_id)

            artist_name = removed_song.artist.name if removed_song.artist else 'Not Assigned'
            print(f"Done. ❌{removed_song.title} (ID: {removed_song.song_id})❌ has now been removed. Artist: {artist_name}")
        except ValueError as ex:
            print(f"🛑Uh oh! Error occurred while removing!🛑: {ex}")
    else:
        print(f"Uh oh. It seems there is no song with ID {deleted_song_id}. 🙁")

def list_all_songs():
    try:
        Song.load_all_songs()
        print("---------🎹Available Songs🎹---------")
        
        for song in Song.all_songs:
            print(f"🎶{song.title} | ID: {song.song_id}🎶")

        if not Song.all_songs:
            print("Oh no! There are currently no existing songs.. 😢")
            return
    except ValueError as ve:
        print(f"Error: {ve}")

def find_song_by_id_helper(song_id):
    try:
        song_id = int(song_id)
        found_song = Song.find_song_by_id(song_id)

        if found_song:
            return {
                "title": found_song.title,
                "song_id": found_song.song_id,
                "artist_name": found_song.artist.name if found_song.artist else 'Not Assigned'
            }
        else:
            return None
    except ValueError:
        return None
    except Exception as e:
        raise e

def find_song_by_id():
    try:
        song_id = input("Enter the ID of the song: ")
        found_song = Song.find_song_by_id(song_id)

        if found_song:
            print("----------🎶Found Song🎶----------")
            print(f"Details: \n- Title: {found_song.title} \n- Song ID: {found_song.song_id}")
            print(f"- Artist: {found_song.artist.name if found_song.artist else 'Not Assigned'}")

            update_title = input("Would you like to udpate the song's title? (Y/N?): ").lower()

            if update_title == 'y':
                new_title = input("Enter the updated Title: ")
                Song.update_song_title(song_id, new_title)
            elif update_title == 'n':
                return

        else:
            print(f"Uh oh. Looks like we don't have a song with that ID.. 😢")

    except ValueError:
        print("Invalid input. Please enter a valid Song ID.")
    except Exception as e:
        print(f"Error occurred: {e}")