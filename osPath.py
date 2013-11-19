#!/usr/bin/python
# Filename: osPath.py

import os
from os.path import join, getsize

rootdir = '/Users/lidian/Downloads/'

file = {}

for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        name = join(parent, filename)
        size = getsize(name)
        file[name] = size

file = sorted(file.items(), key=lambda f:f[1], reverse=True)

for item in file:
    size = item[1] / 1024.0
    if (size / 1024 / 1024) >= 1:
        print 'file %s size is =======> %.2fG' % (item[0], size / 1024 / 1024)
    elif (size / 1024) >= 1:
        print 'file %s size is =======> %.1fM' % (item[0], size / 1024)
    else:
        print 'file %s size is =======> %dk' % (item[0], size)
