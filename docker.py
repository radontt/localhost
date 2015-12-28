#!/usr/bin/env python3
from gi.repository import Gtk
import os, time


class DockerHost:
  d_tabs = {
    #'Status': '',
    'Proccess': 'ps -a',
    'Images': 'images',
    'Info': 'version'
  }

  def __init__(self):
    self.builder = Gtk.Builder()
    self.builder.add_from_file('layout/docker.glade')
    self.builder.connect_signals(self)

    self.window = self.builder.get_object('window_main')
    self.about_dialog = self.builder.get_object('dialog_about')
    self.add_docker_dialog = self.builder.get_object('dialog_add_docker')

    self.statusbar = self.builder.get_object('status_bar')
    self.context_id = self.statusbar.get_context_id('status')
    self.window.show()
    self.statusbar.push(0, "Refreshed - {0}".format(time.ctime()))
    self.notebook = self.builder.get_object('notebook1')
    self.on_notebook1_switch_page(self.notebook, '', 0)


  def on_window_main_destroy(self, object, data=None):
    #FIXME quit with cancel
    Gtk.main_quit()

  def on_gtk_quit_activate(self, menuitem, data=None):
    #FIXME "quit from menu"
    Gtk.main_quit()

  def on_gtk_about_activate(self, menuitem, data=None):
    self.response = self.about_dialog.run()
    self.about_dialog.hide()

  def on_gtk_add_docker_activate(self, menuitem, data=None):
    self.response = self.add_docker_dialog.run()
    self.add_docker_dialog.hide()

  def on_notebook1_switch_page(self,  notebook, page, page_num, data=None):
    tab_content = notebook.get_nth_page(page_num)
    name_label = notebook.get_tab_label(tab_content).get_label()

    if name_label in self.d_tabs:
      tab_content.set_halign(Gtk.Align.START)
      tab_content.set_text(self.get_docker_command(self.d_tabs[name_label]))

  def get_docker_command(self, command):
    output = ''
    p = os.popen('docker ' + command)
    line = True
    while line:
      line = p.readline()
      output = output + line
    return output


if __name__ == "__main__":
  main = DockerHost()
  Gtk.main()
