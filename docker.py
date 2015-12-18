#!/usr/bin/env python3
from gi.repository import Gtk
import os

class MyWindow(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self, title='Docker server')
    self.set_border_width(10)
    box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.add(box_vert)

    box_header = Gtk.Box(spacing=4)
    box_vert.pack_start(box_header, True, True, 0)

    p = os.popen ('docker -v')
    self.server_status = Gtk.Label(p.readline())
    box_header.pack_start(self.server_status, False, True, 0)

win = MyWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
