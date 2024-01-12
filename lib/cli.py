import sys
sys.path.append('.')

from models.artist import Artist
from models.song import Song
from lib import helpers

from lib.helpers import (
    exit_program,
    add_artist,
    list_all_artists,
    add_song,
    remove_song,
    list_all_songs,
    list_artists_songs,
    add_song_to_favorites,
    remove_favorited_song,
    list_favorited_songs,
    find_artist_by_id,
    find_song_by_id,
    find_favorited_song_by_id
)

def main():
    while True:
        menu()
        try:
            choice = input("> ")
            if choice == "0":
                exit_program()

            elif choice == "1":
                add_artist()
            elif choice == "2":
                list_all_artists()
            elif choice == "3":
                add_song()
            elif choice == "4":
                remove_song()
            elif choice == "5":
                list_all_songs()
            elif choice == "6":
                list_artists_songs()
            elif choice == "7":
                add_song_to_favorites()
            elif choice == "8":
                remove_favorited_song()
            elif choice == "9":
                list_favorited_songs()
            elif choice == "10":
                find_artist_by_id()
            elif choice == "11":
                find_song_by_id()
            elif choice == "12":
                find_favorited_song_by_id()
            else:
                print("Invalid choice. Please enter a number between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 9.")

def menu():
    print("----------Please select an option----------")
    print("1. Add an Artist ➕🧑‍🎤")
    print("2. List all Artists 📄")
    print("3. Add a Song ➕🎶")
    print("4. Remove a Song ➖🎶")
    print("5. List all Songs 📄")
    print("6. List an artist's assigned songs🕺🎶")
    print("7. Add song to your Favorites ➕🎼")
    print("8. Remove Favorited song ➖🎼")
    print("9. List all Favorited songs 📄")
    print("10. Find an Artist by ID 🔍")
    print("11. Find song by ID 🔍")
    print("12. Find Favorited Song by ID 🔍")

    print("Enter 0 to Exit 🚀")

if __name__ == "__main__":
    main()