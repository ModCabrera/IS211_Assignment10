#!/urs/bin/env python
# -*- coding: utf-8 -*-
"""Query Pets db"""

import sqlite3 as lite
import sys

con = lite.connect('pets.db')

with con:
    while True:
        user_input = raw_input("Enter Person's ID: ")
        if user_input == '0':
            continue
        if user_input != '-1':
            con.row_factory = lite.Row
            cur = con.cursor()
            cur.execute('SELECT p.first_name, p.last_name, p.age, pt.name, '
                        'pt.breed, pt.age as pt_age, pt.dead '
                        'FROM person as p, pet as pt, person_pet as perpet '
                        'WHERE p.id=? AND perpet.person_id == p.id '
                        'AND pt.id == perpet.pet_id', (user_input))
            data = cur.fetchall()
            output = '{} owns / owned {}, a {}, that is/was {} years old.'
            for info in data:
                name = info['first_name']+' '+info['last_name']
                pet_name = info['name']
                breed = info['breed']
                age = info['pt_age']
                print output.format(name, pet_name, breed, age)
        else:
            raise sys.exit(-1)
