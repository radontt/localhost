#!/usr/bin/env python3
import os

def parse_console_command(command):
  output = []
  p = os.popen(command)
  line = True
  while line:
    line = p.readline().strip()
    if line:
      output.append(line)

  str = output[0]

  find = 'char'
  index = 0
  result_index = []
  for ch in str:
    if find == 'char':
      if ch != ' ':
        result_index.append(index)
        find = 'string'
        space = 0
    else:
      if ch == ' ':
        space += 1
        if space > 1:
          find = 'char'
      else:
        space = 0
    index += 1

  result = []
  for str in output:
    result.append(explode_by_index(str, result_index))
  return result


def explode_by_index(str, index):
  fields = []
  count = len(index)
  for i in range(count):
    if i < count - 1:
      fields.append(str[index[i]:index[i + 1]].strip())
    else:
      fields.append(str[index[i]:].strip())
  return fields


if __name__ == "__main__":
  print (parse_console_command('docker images'))
