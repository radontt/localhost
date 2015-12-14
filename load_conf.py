#!/usr/bin/env python3
import yaml

def load_conf(file_path) :
  with open('tmp/main-sites.conf', 'r') as stream :
    conf = yaml.load(stream)
  return conf

def get_conf_hosts(conf) :
  a_hosts = []
  for ip in conf :
    if 'status' not in conf[ip] or conf[ip]['status'] == 1 :
      a_sites = conf[ip]['sites']
      site_list = []
      for item in a_sites :
        if 'status' not in a_sites[item] or a_sites[item]['status'] == 1 :
          site_list.append(item)
      if len(site_list) :
        a_hosts.append({'ip': ip, 'sites': site_list})
  return a_hosts
