#!/usr/bin/env python3
from gi.repository import Gtk
import hosts
import load_conf


class MyWindow(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self, title='Localhost server')

    self.set_border_width(10)
    box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.add(box_vert)

    box_header = Gtk.Box(spacing=4)
    box_vert.pack_start(box_header, True, True, 0)

    self.server_status = Gtk.Label('Server: ' + 'Offline')
    box_header.pack_start(self.server_status, False, True, 0)

    switch = Gtk.Switch()
    switch.connect('notify::active', self.on_switch_activated)
    switch.set_active(False)
    box_header.pack_end(switch, False, True, 0)

    # IP + site
    # Line 1
    box_l1 = Gtk.Box(spacing=4)
    box_vert.pack_start(box_l1, True, True, 0)

    text_l1 = Gtk.Label('192.168.11.10')
    box_l1.pack_start(text_l1, False, True, 0)
    btnc_l1 = Gtk.CheckButton()
    box_l1.pack_end(btnc_l1, False, False, 0)

    # Line 2
    box_l2 = Gtk.Box(spacing=4)
    box_vert.pack_start(box_l2, True, True, 0)

    text_l2 = Gtk.Label('       ' + 'drupal7.lc')
    box_l2.pack_start(text_l2, False, True, 0)
    btnc_l2 = Gtk.CheckButton()
    box_l2.pack_end(btnc_l2, False, False, 0)

    # Line 3
    box_l3 = Gtk.Box(spacing=4)
    box_vert.pack_start(box_l3, True, True, 0)

    text_l3 = Gtk.Label('       ' + 'test.lc')
    box_l3.pack_start(text_l3, False, True, 0)
    btnc_l3 = Gtk.CheckButton()
    box_l3.pack_end(btnc_l3, False, False, 0)

  def on_switch_activated(self, switch, gparam):
    if switch.get_active():
      state = 'on'
    else:
      state = 'off'


win = MyWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()


##########################################
# conf = load_conf.load_conf('tmp/main-sites.conf')
# insert = load_conf.get_conf_hosts(conf)
# hosts.resave_hosts('tmp/hosts', insert)
