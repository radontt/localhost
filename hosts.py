#!/usr/bin/env python3

def resave_hosts(file_path, insert = None, mark = None) :
  if mark is None :
    mark = { 'start': '### auto_hosts-start', 'end' : '### auto_hosts-end' }

  a_share_hosts = []
  a_my_hosts = []
  f_curr = 'share'

  # File loads.
  for s_line in open(file_path, 'r') :
    s_line = s_line.strip()
    if len(s_line) > 1 :
      if s_line == mark['start'] :
        f_curr = 'my'
        continue
      if s_line == mark['end'] :
        f_curr = 'share'
        continue

    if f_curr == 'share' :
      a_share_hosts.append(s_line)
    else:
      if len(s_line) > 1:
        a_my_hosts.append(s_line)

  # File saves.
  f_hosts = open(file_path, 'w')
  i_br = 0
  for s_line in a_share_hosts :
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
