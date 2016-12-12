#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from PIL import Image
im = Image.open('demo.jpg')
w, h = im.size
print('jpg size is %s %s' % (w, h))