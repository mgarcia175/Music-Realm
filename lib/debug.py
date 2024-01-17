#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.artist import Artist

import ipdb


Artist.drop_table()
Artist.create_table()

# artistMichael = Artist.create("Michael Jackson")
# print(artistMichael)

# rock_artist = Artist.create("Greenday")
# print(rock_artist)


# artistMichael.name = "MJ"
# rock_artist.name = "GD"
# artistMichael.update()
# rock_artist.update()

# print(artistMichael, rock_artist)


# print("Delete artistMichael and rock_artist")
# artistMichael.delete()
# rock_artist.delete()
# print(artistMichael, rock_artist)



Artist.create("Michael Jackson")
Artist.create("Queen")





ipdb.set_trace()