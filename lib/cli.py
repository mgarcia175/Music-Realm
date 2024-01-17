import sys
sys.path.append('.')

from lib.helpers import (
    exit_program,
    add_an_artists,
    remove_an_artist,
    list_all_artists,
    add_a_song,
    list_all_songs,
    remove_a_song,
    find_artist_by_name,
    find_song_by_title
)

def main():
    while True:
        menu()
        try:
            choice = input(">>> ")
            if choice == "0":
                exit_program()
            elif choice ==  "1":
                add_an_artists()
            elif choice == "2":
                list_all_artists()
            elif choice ==  "3":
                remove_an_artist()
            elif choice ==  "4":
                add_a_song()
            elif choice == "5":
                list_all_songs()
            elif choice ==  "6":
                remove_a_song()
            elif choice ==  "7":
                find_artist_by_name()
            elif choice ==  "8":
                find_song_by_title()

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
    print("7. Find an Artist by name 🔍")
    print("8. Find a Song by title 🔍")

    print("Enter 0 to Exit 🚀")

if __name__ == "__main__":
    main()