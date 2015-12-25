#!/usr/bin/env python3
from gi.repository import Gtk
import os

#http://gnipsel.com/glade/glade05a.html

class Buglump:
  def on_window_main_destroy(self, object, data=None):
    print ("quit with cancel")  #FIXME
    Gtk.main_quit()

  def on_gtk_quit_activate(self, menuitem, data=None):
    print ("quit from menu")  #FIXME
    Gtk.main_quit()

  def on_gtk_about_activate(self, menuitem, data=None):
    print ("help about selected")
    self.response = self.aboutdialog.run()
    self.aboutdialog.hide()

  def on_push_status_activate(self, menuitem, data=None):
    self.status_count += 1
    self.statusbar.push(self.context_id, "Message number {0}".format(str(self.status_count)))

  def on_pop_status_activate(self, menuitem, data=None):
    self.status_count -= 1
    self.statusbar.pop(self.context_id)

  def on_clear_status_activate(self, menuitem, data=None):
    while (self.status_count > 0):
      self.statusbar.pop(self.context_id)
      self.status_count -= 1

  def __init__(self):
    self.builder = Gtk.Builder()
    self.builder.add_from_file('layout/docker.glade')
    self.builder.connect_signals(self)
    self.window = self.builder.get_object('window_main')
    self.aboutdialog = self.builder.get_object('dialog_about')
    self.statusbar = self.builder.get_object('status_bar')
    self.context_id = self.statusbar.get_context_id('status')
    self.window.show()
    self.status_count = 0


if __name__ == "__main__":
  main = Buglump()
  Gtk.main()

# class DialogAddDockerHandler:
#   def on_delete_dialog(self, *args):
#     print ('end')
#     #FIXME Gtk.main_quit(*args)

#   def on_clicked_add(self, button):
#     print('Add new conf, close dialog')

#   def on_clicked_cancel(self, button):
#     print('Cancel new conf, close dialog')


# class MyWindow(Gtk.Window):
#   def __init__(self):
#     Gtk.Window.__init__(self, title='Docker localhost')
#     self.set_border_width(4)

#     self.notebook = Gtk.Notebook()
#     self.add(self.notebook)

#     # Status (Main) tab
#     self.p_list = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
#     self.p_list.set_border_width(10)
#     l_status = Gtk.Label('Config / Add new')
#     l_status.set_halign(Gtk.Align.START)
#     self.p_list.pack_start(l_status, False, False, 0)
#     self.notebook.append_page(self.p_list, Gtk.Label('Status'))

#     box_footer = Gtk.Box()
#     self.p_list.pack_end(box_footer, False, False, 0)
#     btn_add_docker = Gtk.Button.new_with_label('Add docker')
#     btn_add_docker.connect('clicked', self.on_click_add_docker)
#     box_footer.pack_start(btn_add_docker, False, False, 0)

#     # Proccess tab
#     self.p_list = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
#     self.p_list.set_border_width(10)
#     p = os.popen('docker ps -a')
#     line = True
#     s_ps = ''
#     while line:
#       line = p.readline()
#       s_ps = s_ps + line
#     l_proccess = Gtk.Label(s_ps)
#     l_proccess.set_halign(Gtk.Align.START)
#     self.p_list.pack_start(l_proccess, False, False, 0)
#     self.notebook.append_page(self.p_list, Gtk.Label('Proccess'))

#     # Images tab
#     self.p_images = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
#     self.p_images.set_border_width(10)
#     p = os.popen('docker images')
#     line = True
#     images = ''
#     while line:
#       line = p.readline()
#       images = images + line
#     l_images = Gtk.Label(images)
#     l_images.set_halign(Gtk.Align.START)
#     self.p_images.pack_start(l_images, False, True, 0)
#     self.notebook.append_page(self.p_images, Gtk.Label('Images'))

#     # About tab
#     self.p_about = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
#     self.p_about.set_border_width(10)
#     p = os.popen('docker version')
#     line = True
#     version = ''
#     while line:
#       line = p.readline()
#       version = version + line
#     l_version = Gtk.Label(version)
#     l_version.set_halign(Gtk.Align.START)
#     self.p_about.pack_start(l_version, False, False, 0)
#     self.notebook.append_page(self.p_about, Gtk.Label('About'))

#   def on_click_add_docker(self, button):
#     builder = Gtk.Builder()
#     builder.add_from_file('layout/add_docker.glade')
#     builder.connect_signals(DialogAddDockerHandler())
#     dialog = builder.get_object('dialog_add_docker')
#     dialog.show()


# win = MyWindow()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()
