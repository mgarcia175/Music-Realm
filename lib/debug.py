#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.song import Song

import ipdb


Artist.drop_table()
Artist.create_table()

Song.drop_table()
Song.create_table()



# Create artists
michael_jackson = Artist.create("Michael Jackson")
greenday = Artist.create("Green Day")

# Create songs for artists
smooth_criminal = Song.create("Smooth Criminal", michael_jackson)
boulevard_of_broken_dreams = Song.create("Boulevard of Broken Dreams", greenday)






ipdb.set_trace()