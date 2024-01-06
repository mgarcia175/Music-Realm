import sys
sys.path.append('.')

from models.artist import Artist
from models.song import Song

from lib.helpers import (
    exit_program,
    add_artist,
    remove_artist,
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
                remove_artist()
            elif choice == "3":
                list_all_artists()
            elif choice == "4":
                add_song()
            elif choice == "5":
                remove_song()
            elif choice == "6":
                list_all_songs()
            elif choice == "7":
                add_song_to_favorites()
            elif choice == "8":
                remove_favorited_song()
            elif choice == "9":
                list_favorited_songs()

            else:
                print("Invalid choice. Please enter a number between 0 and 11.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 11.")



def menu():
    print("Please select an option:")
    print("0. Exit")
    print("1. Add an Artist")
    print("2. Remove an Artist")
    print("3. List all Artists")
    print("4. Add a Song")
    print("5. Remove a Song")
    print("6. List all Songs")
    print("7. Add song to your Favorites")
    print("8. Remove Favorited song")
    print("9. List all Favorited songs")

if __name__ == "__main__":
    main()