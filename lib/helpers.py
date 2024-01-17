import sqlite3
from .models.artist import Artist
# from models.song import Song

def exit_program():
    print("Exiting menu.. Goodbye!")
    exit()

def add_an_artists():
    try:

        artist_name = input("Enter the name of your Artist: ")

        new_artist = Artist.create(artist_name)

        print(f"Nice! '{new_artist.name}' has been successfully added!")
    
    except ValueError as ve:
        print(f"Error: {ve}")

    except Exception as ex:
        print(f"Error adding artist: {ex}")


def list_all_artists():
    print()







    

def remove_an_artist():
    try:
        # Get all artists
        artists = Artist.get_all()

        # Print the list of available artists
        print("Select an artist to remove:")
        for i, artist in enumerate(artists, start=1):
            print(f"{i}. {artist.name}")

        # Prompt the user to enter the name of the artist to remove
        artist_name = input("Enter the name of the artist: ")
        selected_artist = Artist.find_by_name(artist_name)

        if selected_artist:
            # Attempt to delete the selected artist
            try:
                Artist.delete(selected_artist)
                print(f"Artist '{selected_artist.name}' removed successfully!")
            except Exception as exc:
                print(f"Error removing artist: {exc}")
        else:
            print("Artist not found.")

    except Exception as ex:
        print(f"Error: {ex}")






















def add_a_song():
    print()



def list_all_songs():
    print()



def remove_a_song():
    print()



def find_artist_by_name():
    print()



def find_song_by_title():
    print()







































# def list_all_artists():
#     try:
#         Artist.load_all_artists()

#         print("---------🌟Available Artists🌟---------")

#         artists_found = False

#         for artist in Artist.all_artists:
#             print(f"🥁🎹🎸{artist.name} (ID: {artist.artist_id})🎸🎹🥁")
#             artists_found = True

#         if not artists_found:
#             print("Oh no! There are currently no existing artists.. 😢")

#     except ValueError as ve:
#         print(f"Error: {ve}")


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
