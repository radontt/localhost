#!/usr/bin/env python3
import yaml

def load_conf(file_path) :
  with open('tmp/main-sites.conf', 'r') as stream :
    conf = yaml.load(stream)

  

##########################################
load_conf('tmp/main-sites.conf')
