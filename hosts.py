#!/usr/bin/env python3
import os
import os.path

class Hosts:
  a_share_hosts = []
  a_my_hosts = []
  file_path = '/etc/hosts'
  errors = []
  mark = { 'start': '### auto_hosts-start', 'end' : '### auto_hosts-end' }

  def __init__(self, file_path = None, mark = None):
    if file_path is not None:
      self.file_path = file_path
    if mark is not None:
      self.mark = mark

    load()

  # Hosts file load.
  def load(self, file_path = None):
    self.a_share_hosts = []
    self.a_my_hosts = []
    f_curr = 'share'

    tmp_path = file_path if file_path is not None else self.file_path
    if os.path.isfile(tmp_path) == False or os.access(tmp_path, os.R_OK):
      self.errors.append({'file_not_exists': 'File "hosts" not exists'})
      return False


    if file_path is not None:
      self.file_path = file_path

    # File loads.
    for s_line in open(self.file_path, 'r') :
      s_line = s_line.strip()
      if len(s_line) > 1 :
        if s_line == mark['start'] :
          f_curr = 'my'
          continue
        if s_line == mark['end'] :
          f_curr = 'share'
          continue

      if f_curr == 'share' :
        self.a_share_hosts.append(s_line)
      else:
        if len(s_line) > 1:
          self.a_my_hosts.append(s_line)
    return True

  # Hosts file save.
  def save(self, insert = None) :
    f_hosts = open(self.file_path, 'w')
    i_br = 0
    for s_line in self.a_share_hosts :
      i_br = 0 if len(s_line) > 1 else i_br + 1
      if i_br < 3 :
        f_hosts.write(s_line + '\n')

    if insert is not None :
      if i_br < 3 :
        f_hosts.write('\n')
      f_hosts.write(mark['start'] + '\n')
      for s_line in insert :
        f_hosts.write(s_line['ip'] + '  ' + ' '.join(s_line['sites']) + '\n')
      f_hosts.write(mark['end'] + '\n')

    f_hosts.close()
