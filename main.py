#!/usr/bin/env python3
import hosts
import load_conf




##########################################
conf = load_conf.load_conf('tmp/main-sites.conf')
insert = load_conf.get_conf_hosts(conf)
hosts.resave_hosts('tmp/hosts', insert)
