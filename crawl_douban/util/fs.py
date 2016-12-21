#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'file system.'

__author__ = 'soonfy'

# modules
import os

def file_ready(filepath):
  """
  judge filepath exists  
  @param filepath  
  @return boolean  
  """
  try:
    if os.path.exists(os.path.split(filepath)[0]):
      if os.path.isfile(filepath):
        print('file exists...')
      else:
        print('no file...')
    else:
      os.mkdir(os.path.split(filepath)[0])
      print('no file dir...')
    return True
  except Exception as e:
    print(e)
    return False
  