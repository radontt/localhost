#!/usr/bin/env python3
import hosts

insert = [{ 'ip' : '10.10.10.10', 'sites': 'test.cm1'}, { 'ip' : '10.10.10.11', 'sites': 'test1.cm2 test2.cm2'}]
hosts.resave_hosts('tmp/hosts', insert)
