import sqlite3
from .models.artist import Artist
from models.song import Song

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
    print("---------🌟Available Artists🌟---------")

    try:
        artists = Artist.get_all()

        if artists:
            for artist in artists:
                print(f"{artist.id}. {artist.name}")
        else:
            print("Oh no! There are currently no existing artists.. 😢")
    except Exception as ex:
        print(f"Error: {ex}")

def remove_an_artist():
    print("---------❌Removing Artist❌---------")
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
                print(f"Done. ❌{selected_artist.name} has now been removed.❌")
            except Exception as exc:
                print(f"Error removing artist: {exc}")
        else:
            print("Artist not found.")

    except Exception as ex:
        print(f"Error: {ex}")

def add_a_song():
    print("---------🎶Adding song🎶---------")

    try:
        # Get all artists
        artists = Artist.get_all()

        if not artists:
            print("Oh no! There are currently no existing artists..😢 Please add an artist first.")
            return

        # Print the list of all artists for the user to choose
        print("---------🌟Available Artists🌟---------")
        for artist in artists:
            print(f"{artist.id}. {artist.name}")

        # Prompt the user to select an artist or create a new one
        print("Select an artist (Or 'new' to create a new artist, or 0 to exit).")
        artist_choice = input("Enter: ")

        if artist_choice == '0':
            return

        if artist_choice.lower() == 'new':
            new_artist_name = input("Enter the name of the new artist: ")

            # Create new artist
            selected_artist = Artist.create(new_artist_name)
            print(f"✅Nicely done! New artist 🥁🎹🎸'{new_artist_name}'🎸🎹🥁 created successfully.✅")

        else:
            artist_id = int(artist_choice)
            selected_artist = Artist.find_by_id(artist_id)

            if not selected_artist:
                print("Invalid artist selection. Please try again.")
                return

        song_title = input("Enter the title of the song: ")

        # Creates song with title and slected artist
        Song.create(song_title, selected_artist)

        print(f"✅Nicely done! Song '{song_title}' by {selected_artist.name} added successfully.✅")

    except Exception as ex:
        print(f"Error: {ex}")

def list_all_songs():
    print("---------🎹Available Songs🎹---------")
    try:
        songs = Song.get_all()

        print("List of all songs:")
        for song in songs:
            if song:
                print(f"🎶{song.title}")
            else:
                print("Song with missing or deleted artist:")
    except Exception as e:
        print(f"Error listing all songs: {e}")

def remove_a_song():
    try:
        # Displaying all songs for user to choose
        songs = Song.get_all()
        print("---------🎹Available Songs🎹---------")
        for song in songs:
            if song:
                print(f"🎶{song}")
            else:
                print("Song with missing or deleted artist")

        title_to_remove = input("Enter the title of the song for removal: ")

        # Finding the song
        song_to_remove = Song.find_by_title(title_to_remove)

        if song_to_remove:
            # Deleting
            song_to_remove.delete()
            print(f"Done. ❌ '{title_to_remove}' has now been removed.❌")
        else:
            print(f"Uh oh. No song found with the title '{title_to_remove}'. 🙁")
    except Exception as e:
        print(f"Error removing the song: {e}")

def find_artist_by_name():
    try:
        name = input("Enter the name of the artist to find: ")
        artist = Artist.find_by_name(name)

        if artist:
            print(f"Artist found:\n 🎤{artist.name}🎤")
            
            # Display artist's songs
            artist_songs = Artist.artists_songs(artist)
            if artist_songs:
                print("----------Artist's songs----------")
                for song in artist_songs:
                    print(f"🎶{song.title}")
            else:
                print("No songs found for this artist.")

        else:
            print(f"No artist found with the name: {name}")

    except Exception as e:
        print(f"Error finding artist by name: {e}")

def find_song_by_title():
    try:
        title = input("Enter the title of the song to find: ")
        song = Song.find_by_title(title)

        if song:
            print(f"Song found: 🎶{song.title}🎶")
            if song.artist:
                print(f"Artist: 🎤{song.artist.name}🎤")
            else:
                print("Oh no.. Artist information not available. 😢")
        else:
            print(f"Uh oh! No song found with the title: {title} 😢")

    except Exception as e:
        print(f"Error finding song by title: {e}")