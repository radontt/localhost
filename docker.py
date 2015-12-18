#!/usr/bin/env python3
from gi.repository import Gtk
import os

class MyWindow(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self, title="Simple Notebook Example")
    self.set_border_width(4)

    self.notebook = Gtk.Notebook()
    self.add(self.notebook)

    self.p_list = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.p_list.set_border_width(10)
    p = os.popen('docker ps -a')
    line = True
    s_ps = ''
    while line:
      line = p.readline()
      s_ps = s_ps + line
    self.p_list.pack_start(Gtk.Label(s_ps), False, False, 0)
    self.notebook.append_page(self.p_list, Gtk.Label('Status'))

    self.p_images = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.p_images.set_border_width(10)
    p = os.popen('docker images')
    line = True
    images = ''
    while line:
      line = p.readline()
      images = images + line
    self.p_images.pack_start(Gtk.Label(images), False, True, 0)
    self.notebook.append_page(self.p_images, Gtk.Label('Images'))

    self.p_about = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.p_about.set_border_width(10)
    p = os.popen('docker version')
    line = True
    version = ''
    while line:
      line = p.readline()
      version = version + line
    self.p_about.pack_start(Gtk.Label(version), False, False, 0)
    self.notebook.append_page(self.p_about, Gtk.Label('About'))

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
