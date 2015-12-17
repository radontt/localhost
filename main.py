#!/usr/bin/env python3
from gi.repository import Gtk
import hosts
import load_conf

class MyWindow(Gtk.Window):
  c_conf = None

  def __init__(self):
    self.c_conf = load_conf.Config('tmp/main-sites.yml')

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

    for ip in self.c_conf.conf:
      box = Gtk.Box(spacing=4)
      box_vert.pack_start(box, True, True, 0)

      text = Gtk.Label(ip)
      box.pack_start(text, False, True, 0)
      btnc = Gtk.CheckButton()
      if 'status' not in self.c_conf.conf[ip] or self.c_conf.conf[ip]['status'] == 1:
        btnc.set_active(True)
      # FIXME connect event
      box.pack_end(btnc, False, False, 0)

      a_sites = self.c_conf.conf[ip]['sites']
      for item in a_sites:
        box = Gtk.Box(spacing=4)
        box_vert.pack_start(box, True, True, 0)

        text = Gtk.Label('       ' + item)
        box.pack_start(text, False, True, 0)
        btnc = Gtk.CheckButton()
        if 'status' not in a_sites[item] or a_sites[item]['status'] == 1:
          btnc.set_active(True)
        box.pack_end(btnc, False, False, 0)

    box_footer = Gtk.Box(spacing=4)
    box_vert.pack_start(box_footer, True, True, 0)

    btn_reload = Gtk.Button.new_with_label('Reload')
    btn_reload.connect('clicked', self.on_click_reload_conf)
    box_footer.pack_start(btn_reload, True, True, 0)


    btn_save = Gtk.Button.new_with_label('Save configuration')
    box_footer.pack_start(btn_save, True, True, 0)


  def on_click_reload_conf(self, button):
    print ('Click')

  def on_switch_activated(self, switch, gparam):
    if switch.get_active():
      state = 'on'
    else:
      state = 'off'


win = MyWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()

# c_conf = load_conf.Config('tmp/main-sites.yml')
# insert = c_conf.get_hosts()
# c_hosts = hosts.Hosts('tmp/hosts')
# c_hosts.save(insert)
