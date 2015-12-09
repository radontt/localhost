#!/usr/bin/env python3

mark = { 'start': '### auto_hosts-start', 'end' : '### auto_hosts-end' }
pos = { 'start': 0, 'end': 0 }

insert = [{ 'ip' : '10.10.10.10', 'test.cm1'}, { 'ip' : '10.10.10.11', 'test1.cm2 test2.cm2'}]

a_file = []
i = 0
for s_line in open('hosts', 'r'):
  if len(s_line) > 1 :
    if pos['start'] == 0 and s_line == mark['start'] :
      pos['start'] = i
    if pos['end'] == 0 and s_line == mark['end'] :
      pos['end'] = i
    print ('{0} - {1}'.format(i, s_line[:-1]))
  i += 1
  a_file.append(s_line)

print ('Start = {0}; End = {1}'.format(pos['start'], pos['end']))
print (a_file)





# 'Last:\n{0} ({5})\n{1}\n\nAll answer - {2}\nError - {3}\nRight - {4}'.format(last, status)
