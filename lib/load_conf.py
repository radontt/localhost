#!/usr/bin/env python3
import yaml

class Config:
  conf = []
  file_path = ''

  def __init__(self, file_path):
    self.load(file_path)

  # Configuration file load.
  def load(self, file_path = None):
    if file_path is not None:
      self.file_path = file_path

    with open(self.file_path, 'r') as f_conf:
      self.conf = yaml.load(f_conf)

  # Get hosts from configuration.
  def get_hosts(self):
    a_hosts = []
    for ip in self.conf:
      if 'status' not in self.conf[ip] or self.conf[ip]['status'] == 1 :
        a_sites = self.conf[ip]['sites']
        site_list = []
        for item in a_sites:
          if 'status' not in a_sites[item] or a_sites[item]['status'] == 1 :
            site_list.append(item)
        if len(site_list):
          a_hosts.append({'ip': ip, 'sites': site_list})
    return a_hosts
