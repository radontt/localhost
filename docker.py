#!/usr/bin/env python3
from gi.repository import Gtk
import os

class MyWindow(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self, title="Simple Notebook Example")
    self.set_border_width(4)

    self.notebook = Gtk.Notebook()
    self.add(self.notebook)

    self.p_list = Gtk.Box()
    self.p_list.set_border_width(10)
    self.p_list.add(Gtk.Label('List of dockers'))
    self.notebook.append_page(self.p_list, Gtk.Label('Status'))

    self.p_images = Gtk.Box()
    self.p_images.set_border_width(10)
    self.p_images.add(Gtk.Label('List of images'))
    self.notebook.append_page(self.p_images, Gtk.Label('Images'))

    self.p_about = Gtk.Box()
    self.p_about.set_border_width(10)
    p = os.popen('docker version')
    line = True
    version = ''
    while line:
      line = p.readline()
      version = version + line
    self.p_about.add(Gtk.Label(version))
    self.notebook.append_page(self.p_about, Gtk.Label('About'))

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
