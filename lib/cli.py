import sys
sys.path.append('.')

from models.artist import Artist
# from models.song import Song
from lib import helpers

from lib.helpers import (
    exit_program,

    list_all_artists,

    list_all_songs,

)

def main():
    while True:
        menu()
        try:
            choice = input(">>> ")
            if choice == "0":
                exit_program()

            elif choice == "2":
                list_all_artists()

            elif choice == "5":
                list_all_songs()

            else:
                print("Invalid choice. Please enter a number between 0 and 8.")
        except Exception as ex:
            print(f"🛑Whoaaaa! Unexpected error!🛑: {ex}")

def menu():
    print("----------Please select an option----------")
    print("1. Add an Artist ➕🧑‍🎤")
    print("2. List all Artists 📄")
    print("3. Remove an Artist ➖🎶")
    print("4. Add a Song ➕🎶")
    print("5. List all Songs 📄")
    print("6. Remove a Song ➖🎶")
    print("7. Find an Artist by ID 🔍")
    print("8. Find a Song by ID 🔍")

    print("Enter 0 to Exit 🚀")

if __name__ == "__main__":
    main()