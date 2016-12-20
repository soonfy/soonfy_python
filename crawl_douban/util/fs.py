#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'file system.'

__author__ = 'soonfy'

import os

def file_ready(filepath):
  try:
    if os.path.exists(os.path.split(filepath)[0]):
      if os.path.isfile(filepath):
        print('文件已存在...')
      else:
        open(filepath, 'w')
        print('不存在文件...')
    else:
      os.mkdir(os.path.split(filepath)[0])
      print('文件夹不存在，已新建...')
    return True
  except Exception as e:
    print(e)
    return False
  