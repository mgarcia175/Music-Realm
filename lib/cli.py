import sys
sys.path.append('.')

from models.artist import Artist
from models.song import Song

from lib.helpers import (
    exit_program,
    add_artist,
    list_all_artists,
    add_song,
    remove_song,
    list_all_songs,
    add_song_to_favorites,
    remove_favorited_song,
    list_favorited_songs
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
                add_song_to_favorites()
            elif choice == "7":
                remove_favorited_song()
            elif choice == "8":
                list_favorited_songs()

            else:
                print("Invalid choice. Please enter a number between 0 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")

def menu():
    print("Please select an option:")
    print("0. Exit")
    print("1. Add an Artist +🧑‍🎤")
    print("2. List all Artists 📄")
    print("3. Add a Song +🎶")
    print("4. Remove a Song -🎶")
    print("5. List all Songs 📄")
    print("6. Add song to your Favorites +🎼")
    print("7. Remove Favorited song -🎼")
    print("8. List all Favorited songs 📄")

if __name__ == "__main__":
    main()