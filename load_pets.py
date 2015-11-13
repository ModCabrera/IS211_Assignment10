#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Load pet database"""

import sqlite3 as lite
import sys

con = lite.connect('pets.db', isolation_level=None)

person = (
    ('1', 'James', 'Smith', 41),
    ('2', 'Diana', 'Greene', 23),
    ('3', 'Sara', 'White', 27),
    ('4', 'William', 'Gibson', 23)
)

pet = (
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
)

person_pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
)

with con:
    cur = con.cursor()
    cur.executemany('INSERT INTO person VALUES(?, ?, ?, ?)', PERSON)
    cur.executemany('INSERT INTO pet VALUES(?, ?, ?, ?, ?)', PET)
    cur.executemany('INSERT INTO person_pet VALUES(?, ?)', PERSON_PET)
