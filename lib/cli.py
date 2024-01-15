import sys
sys.path.append('.')

from models.artist import Artist
from models.song import Song
from lib import helpers

from lib.helpers import (
    exit_program,
    add_artist,
    list_all_artists,
    remove_artist,
    add_song,
    remove_song,
    list_all_songs,
    find_artist_by_input,
    find_song_by_id,
)

def main():
    while True:
        menu()
        try:
            choice = input(">>> ")
            if choice == "0":
                exit_program()

            elif choice == "1":
                add_artist()
            elif choice == "2":
                list_all_artists()
            elif choice == "3":
                remove_artist()
            elif choice == "4":
                add_song()
            elif choice == "5":
                remove_song()
            elif choice == "6":
                list_all_songs()
            elif choice == "7":
                find_artist_by_input()
            elif choice == "8":
                find_song_by_id()
            else:
                print("Invalid choice. Please enter a number between 0 and 12.")
        except Exception as ex:
            print(f"🛑Whoaaaa! Unexpected error!🛑: {ex}")

def menu():
    print("----------Please select an option----------")
    print("1. Add an Artist ➕🧑‍🎤")
    print("2. List all Artists 📄")
    print("3. Remove an Artist ➖🎶")
    print("4. Add a Song ➕🎶")
    print("5. Remove a Song ➖🎶")
    print("6. List all Songs 📄")
    print("7. Find an Artist by ID 🔍")
    print("8. Find a Song by ID 🔍")

    print("Enter 0 to Exit 🚀")

if __name__ == "__main__":
    main()