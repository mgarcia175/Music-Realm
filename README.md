# Music Realm Creator

## Description
Hello! Welcome to my Music Realm Creator. Your very own way to organize all of your music-related things!

From adding your own artist, songs and adding them to your control to your music, just got better!

## Visuals

Project Introduction - YouTube

https://youtu.be/PxmwFVl4YiE

## Instructions

Run `pipenv install` to create your virtual environment and `pipenv shell` to enter the virtual environment.

Type in `python lib/cli.py` to start the main menu.

Take a look at the directory structure:

```console
.
├── CONTRIBUTING.md
├── LICENSE
├── LICENSE.md
├── Pipfile
├── Pipfile.lock
├── README.md
├── lib
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── helpers.cpython-38.pyc
│   │   └── util.cpython-38.pyc
│   ├── cli.py
│   ├── debug.py
│   ├── helpers.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   ├── artist.cpython-38.pyc
│   │   │   ├── favorites.cpython-38.pyc
│   │   │   └── song.cpython-38.pyc
│   │   ├── artist.py
│   │   └── song.py
│   └── util.py
└── music_libr.db
```
---
## Usage

***Music Realm Creat*** is a fun and interactive program that:

+ Allows the user to add, list, and remove their known songs
+ Allows the user to add, list, and remove their known artists
+ Allows the user to customize these submission by removing, adding and assigning their songs to the song's corresponding artist
+ Allows the user to update the song's/artist's information, if needed

Let's go through it!

---
## `cli.py`

Here we have the command line interface for our Realm Creator, whic ultimately comes from our file, `lib/cli.py`!

Once we run `python lib/cli.py`, we are given a menu, with 10 options to choose from:

```
----------Please select an option----------
1. Add an Artist ➕🧑‍🎤
2. List all Artists 📄
3. Remove an Artist ➖🎶
4. Add a Song ➕🎶
5. List all Songs 📄
6. Remove a Song ➖🎶
7. Find an Artist by name 🔍
8. Find a Song by title 🔍

Enter 0 to Exit 🚀
```
These options and actions derive their logic and functionality from our `lib/helpers.py file`. We will visit them now.

## helpers.py

```1. Add an Artist ➕🧑‍🎤```

Option 1 allows the user to add an artist of their choice. Once the option is chosen, the user will be prompted to enter the artist's name for submission, which will then create the desired artist!:
```
>>> 1
---------🌟Adding artist🌟---------
Artist Name (Or enter 0 to go back): Michael Jackson
✅Nice! 🎤'Michael Jackson'🎤 has been successfully added!✅
----------Please select an option----------
1. Add an Artist ➕🧑‍🎤
2. List all Artists 📄
3. Remove an Artist ➖🎶
4. Add a Song ➕🎶
5. List all Songs 📄
6. Remove a Song ➖🎶
7. Find an Artist by name 🔍
8. Find a Song by title 🔍

Enter 0 to Exit 🚀
```

```2. List all Artists 📄```

Option 2 will list all of the created artists for the user. However, remember that there is an option which will remove an artist/song, which we will cover shortly. But if a song/artist is removed, the said song/artist will not be shown any longer, unless added again.:
```
> 2
---------🌟Available Artists🌟---------
🥁🎹🎸Michael Jackson (ID: 35)🎸🎹🥁
🥁🎹🎸Greenday (ID: 36)🎸🎹🥁
🥁🎹🎸Miley Cyrus (ID: 37)🎸🎹🥁
----------Please select an option----------
1. Add an Artist ➕🧑‍🎤
2. List all Artists 📄
3. Remove an Artist ➖🎶
4. Add a Song ➕🎶
5. List all Songs 📄
6. Remove a Song ➖🎶
7. Find an Artist by name 🔍
8. Find a Song by title 🔍

Enter 0 to Exit 🚀
>>>
```

```3. Remove an Artist```

Option 4 will allow the user to remove one of their submitted Artists. For convenience, the user will be informed on all of the available Artists, along with their IDs. The user will then be prompted to enter the Artist's ID. Once this is done, the user will be informed that the Artist has been removed.:

```
----------Please select an option----------
1. Add an Artist ➕🧑‍🎤
2. List all Artists 📄
3. Remove an Artist ➖🎶
4. Add a Song ➕🎶
5. List all Songs 📄
6. Remove a Song ➖🎶
7. Find an Artist by name 🔍
8. Find a Song by title 🔍
Enter 0 to Exit 🚀
>>> 3
---------❌Removing Artist❌---------
---------🌟Available Artists🌟---------
🥁🎹🎸Michael Jackson (ID: 15)🎸🎹🥁
Please enter the Artist's ID to remove (Or 0 to go back): 15
Done. ❌Michael Jackson has now been removed.❌
```

```4. Add a Song ➕🎶```

Option 4 will allow the user to add a song. The user will be prompted to enter the name od the desired song. Once this is done, the user will also be given the ability to assign the song to an artist, if so desired, by entering the artist's ID. If not, simply enter 'NA'.:

```
>>> 4
---------🎶Adding song🎶---------
Enter song title (Or enter 0 to go back): Billy Jean
---------🌟Available Artists🌟---------
🥁🎹🎸Michael Jackson (ID: 35)🎸🎹🥁
Enter the ID of the artist to assign your song!(`NA` if not assigning): 35
Song Title:Billy Jean, Assigned Artist: Michael Jackson
✅Nicely done! Song added: 🎶Billy Jean🎶 and assigned to 🎤Michael Jackson (ID: 35)🎤!✅
----------Please select an option----------
1. Add an Artist ➕🧑‍🎤
2. List all Artists 📄
3. Remove an Artist ➖🎶
4. Add a Song ➕🎶
5. List all Songs 📄
6. Remove a Song ➖🎶
7. Find an Artist by name 🔍
8. Find a Song by title 🔍
Enter 0 to Exit 🚀
>>>
```

```5. List all Songs 📄```

Option 5 will list all of the available songs. Similar to the songs, remember that there is an option which will remove an artist/song, which we will cover shortly. But if a song/artist is removed, the said song/artist will not be shown any longer, unless added again. For the purposes of the example, I have added more songs, for listing!:

```
>>> 5
---------🎹Available Songs🎹---------
🎶American Idiot (ID: 12🎶)
🎶Smooth Criminal (ID: 13🎶)
🎶Party in the USA (ID: 14🎶)
----------Please select an option----------
1. Add an Artist ➕🧑‍🎤
2. List all Artists 📄
3. Remove an Artist ➖🎶
4. Add a Song ➕🎶
5. List all Songs 📄
6. Remove a Song ➖🎶
7. Find an Artist by name 🔍
8. Find a Song by title 🔍
Enter 0 to Exit 🚀
>>>
```

```6. Remove a Song ➖🎶```

Option 6 will prompt the user to enter a song's ID, for removal. Please keep in mind that this cannot be undone, once processed. If the song is desired again, it will have to be added again, manually.:

```
>>> 6
---------❌Removing Song❌---------
---------🎹Available Songs🎹---------
🎶Billy Jean (ID: 16🎶)
Please enter the song's ID to remove (Or enter 0 to go back): 6
Done. ❌Billy Jean❌ has now been removed.
----------Please select an option----------
1. Add an Artist ➕🧑‍🎤
2. List all Artists 📄
3. Remove an Artist ➖🎶
4. Add a Song ➕🎶
5. List all Songs 📄
6. Remove a Song ➖🎶
7. Find an Artist by name 🔍
8. Find a Song by title 🔍
Enter 0 to Exit 🚀
>>>
```

```7. Find an Artist by name 🔍```

Option 7 will find a specific artist you are looking for. Once the name is provided, the Artist's full name will be provided. Along with this, the command is meant to also be an avenue for the user to update the Artist. If the user needs to correct a typo, they will be prompted to enter the Artist name again for updating.

```
>>> 7
----------Please select an option----------
1. Add an Artist ➕🧑‍🎤
2. List all Artists 📄
3. Remove an Artist ➖🎶
4. Add a Song ➕🎶
5. List all Songs 📄
6. Remove a Song ➖🎶
7. Find an Artist by name 🔍
8. Find a Song by title 🔍
Enter 0 to Exit 🚀
>>> 7
Enter the name of the artist: 20
----------🎤Found Artist🎤----------
Details:
Artist Name: 🌟Micahall Jackson (ID: 20)🌟
Would you like to update the artist's name? (Y/N?): y
Enter the updated artist name: Michael Jackson
✅ Nice! You have successfully updated the Artist name to 'Michael Jackson'! ✅
>>>
```

```8. Find a Song by title 🔍 ```

Option 8 will populate the of a song's information such as it's tile, id, and assigned artist (if one is assigned), once it's title is provided! Along with this, once the song information has populated, the user will be given the option to update the song's title, if so desired.
```
----------Please select an option----------
1. Add an Artist ➕🧑‍🎤
2. List all Artists 📄
3. Remove an Artist ➖🎶
4. Add a Song ➕🎶
5. List all Songs 📄
6. Remove a Song ➖🎶
7. Find an Artist by name 🔍
8. Find a Song by title 🔍
Enter 0 to Exit 🚀
>>> 8
Enter the title of the song: 20
----------🎶Found Song🎶----------
Details:
- Title: Smoothhh cRiminal
- Song ID: 20
- Artist: Michael Jackson
Would you like to udpate the song's title? (Y/N?): y
Enter the updated Title: Smooth Criminal
✅ Nice! You have successfully updated your Song to 'Smooth Criminal'! ✅
```

```Enter 0 to Exit 🚀```

Lastly, if the user would like to leave the application, entering 9 will close the progam.:

```
----------Please select an option----------
1. Add an Artist ➕🧑‍🎤
2. List all Artists 📄
3. Remove an Artist ➖🎶
4. Add a Song ➕🎶
5. List all Songs 📄
6. Remove a Song ➖🎶
7. Find an Artist by name 🔍
8. Find a Song by title 🔍
Enter 0 to Exit 🚀
>>> 0
Exiting menu.. Goodbye!
```

# Support

For any and all questions, concerns, or comments, please do not hesitate to reach out to me via email!

:envelope:: **martingarcia804@yahoo.com**

## Authors and acknowledgment

Many thanks go to the many communities online and the technical support agents from Flatiron, who were a tremendous help. And I am sure I speak for many programmers when I also say thank you to Google!