#!/usr/bin/env python3
from gi.repository import Gtk
import os
import os.path
import sqlite3

curr_dir = 'tmp/root'
curr_id = 1
con = sqlite3.connect('test.db')
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS dirs")
cur.execute("DROP TABLE IF EXISTS files")

cur.execute('CREATE TABLE files ("fid" INTEGER PRIMARY KEY AUTOINCREMENT, "did" INTEGER NOT NULL, "name" TEXT NOT NULL)')
cur.execute('CREATE TABLE dirs ("did" INTEGER PRIMARY KEY AUTOINCREMENT, "path" TEXT, "name" TEXT)')
cur.execute('INSERT INTO dirs VALUES(NULL, "root", "")')

con.commit()

with con:
  while curr_dir:
    for item in os.listdir(curr_dir):
      if os.path.isfile(curr_dir + '/' + item):
        cur.execute("INSERT INTO files VALUES(NULL, ?, ?)", (curr_id, item))
      else:
        cur.execute("INSERT INTO dirs VALUES(NULL, ?, ?)", (curr_dir, item))
    con.commit()
    curr_id = curr_id + 1
    cur.execute('SELECT * FROM dirs WHERE did = :id', {'id': curr_id})
    result = cur.fetchone()
    if result:
      curr_dir = result[2] if result[1] == '' else result[1] + '/' + result[2]
    else:
      curr_dir = ''

