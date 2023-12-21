# lib/cli.py
from models.artist import Artist
from models.song import Song

from helpers import (
    exit_program,
    add_artist,
    remove_artist,
    find_artist_by_id,
    list_all_artists,
    add_song,
    remove_song,
    find_song_by_id,
    list_all_songs,
    add_song_to_favorites,
    remove_favorited_song,
    list_favorited_songs
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()

        elif choice == "1":
            add_artist()
        elif choice == "2":
            find_artist_by_id()
        elif choice == "3":
            remove_artist()
        elif choice == "4":
            list_all_artists()
        elif choice == "5":
            add_song()
        elif choice == "6":
            find_song_by_id()
        elif choice == "7":
            remove_song()
        elif choice == "8":
            list_all_songs()
        elif choice == "9":
            add_song_to_favorites()
        elif choice == "10":
            remove_favorited_song()
        elif choice == "11":
            list_favorited_songs()

        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add an Artist")
    print("2. Find an Artist by ID")
    print("3. Remove an Artist")
    print("4. List all Artists")
    print("5. Add a Song")
    print("6. Find Song by ID")
    print("7. Remove a Song")
    print("8. List all Songs")
    print("9. Add song to your Favorites")
    print("10. Remove Favorited song")
    print("11. List all Favorited songs")

if __name__ == "__main__":
    main()