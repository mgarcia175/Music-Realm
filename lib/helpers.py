import sqlite3
from models.artist import Artist
from models.favorites import Favorited_Song
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
    for artist in Artist.all_artists:
        if str(artist.artist_id) == str(artist_id):
            return artist

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

    song_title = input('Enter song title (Or enter 0 to go back): ')

    if song_title == "0":
        return
    
    existing_song = next((song for song in Song.all_songs if song.title.lower() == song_title.lower()), None)

    if existing_song:
        print(f"🛑Wait a gosh darn second! {existing_song} already exists!🛑")
    else:
        list_all_artists()

        handle_id_or_na = input("Enter the Artist's ID for assignment. ('NA' to add New Artist, 0 to go back): ")

        if handle_id_or_na == 0:
            artist = None

        if handle_id_or_na.lower() == 'na':
            artist_name = input("Enter new artist's name: ")
            new_artist = Artist(name=artist_name)

            newly_added_song = Song(song_id=song_title.lower().replace(" ", "_"), title=song_title)
            new_artist.add_song(newly_added_song)

            newly_added_song.add_song_instance(new_artist)

            Artist.all_artists.append(new_artist)
            newly_added_song.assign_to_artist(new_artist)

            newly_added_song.save_to_db()

            print(f"✅Nicely done! Song added: 🎶{newly_added_song}🎶 and assigned to 🎤{new_artist}🎤!✅")

        #Line to go back if user chooses 0
        elif handle_id_or_na == '0':
            return
        
        else:
            artist = find_artist_by_id(handle_id_or_na)

            if artist:
                print(f"Nice! Found them! 🌟{artist.name} (ID: {artist.artist_id})🌟")
            else:
                print(f"Uh oh.. Looks like there isn't an Artist with that ID. 😢")
                return

            #If the artist was found with the provided ID, create a new instance of a Song
            newly_added_song = Song(song_id=song_title.lower().replace(" ", "_"), title=song_title)

            #Add the song to the matching artist
            artist.add_song(newly_added_song)

            newly_added_song.assign_to_artist(artist)

            newly_added_song.save_to_db()

            assigned_artist_name = newly_added_song.artist.name if newly_added_song.artist else 'Not Assigned'
            print(f"✅Nicely done! Song added: 🎶{newly_added_song.title}🎶 and assigned to 🎤{assigned_artist_name}🎤!✅")

def remove_song():
    print("---------❌Removing Song❌---------")
    list_all_songs()

    while True:
        deleted_song_id = input("Please enter the song's ID to remove (Or enter 0 to go back): ")

        if deleted_song_id == 0:
            return

        removed_song = Song.find_song_by_id(deleted_song_id)

        if removed_song:
            try:
                Song.remove_song_from_db(removed_song.song_id)
                Song.all_songs.remove(removed_song)
                print(f"Done. ❌{removed_song}❌ has now been removed.")
                return
            except Exception as ex:
                print(f"🛑Uh oh! Error occurred while removing!🛑: {ex}")
        else:
            print("Uh oh. It seems there is no song by that ID. 🙁")

def list_all_songs():
    try:
        Song.load_all_songs()
        print("---------🎹Available Songs🎹---------")

        for song in Song.all_songs:
            assigned_artist_id = song.artist.artist_id if song.artist else 'Not Assigned'
            assigned_artist_name = song.artist.name if song.artist else 'Not Assigned'

            print(f"🎶{song.title} (ID: {song.song_id})🎶")

        if not Song.all_songs:
            print("Oh no! There are currently no existing songs.. 😢")
            return
    except ValueError as ve:
        print(f"Error: {ve}")

def find_song_by_id(song_id):
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

    selected_artist_id = input("Enter the artist's ID (Or 0 to exit): ")

    # if selected_artist_id == '0':
    #     return
    selected_artist = find_artist_by_id(selected_artist_id)

    if selected_artist:
        #Checking for songs under the desired artist
        if selected_artist.songs:
            print(f"Songs by 🌟{selected_artist.name}🌟")
            for song in selected_artist.songs:
                print(f"🎶{song.title} (ID: {song.song_id})🎶")
        else:
            print(f"Uh oh. This artist doesn't have any songs assigned right now. 🙁")
    else:
        print(f"Uh oh. There doesn't seem to be an artist with that ID. 🙁")



def add_song_to_favorites():
    print("---------❤️Adding song to your favorites❤️---------")

    list_all_songs()

    needed_song_id = input("Enter your desired song's ID (Or enter 0 to go back): ")

    try:
        needed_song_id = int(needed_song_id)
    except ValueError:
        print("🛑Err! Not a valid and numeric ID!🛑")

    song_to_be_favorited = find_song_by_id(needed_song_id)

    if needed_song_id == '0':
        return

    if song_to_be_favorited:
        try:
            favorited_song_instance = Favorited_Song(song=song_to_be_favorited)
            Favorited_Song.add_favorited_song_to_db(favorited_song_instance)
            print(f"✅Success! 🎶{song_to_be_favorited.title}🎶 now favorited:✅")
        except Exception as e:
            print(f"🛑Uh oh! Stop right there! Error has occurred: {e}🛑")

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
        print("🛑Err! Stop right there! The inputted ID is not valid.🛑")