#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider ua.'

__author__ = 'soonfy'

# modules
import os
from urllib import request
from urllib.parse import urlencode
from bs4 import BeautifulSoup

from util.fs import file_ready

url_ua = 'http://www.useragentstring.com/pages/useragentstring.php?name=All'

def get_ua():
  """
  get ua list from web  
  ex:
    'http://www.useragentstring.com/pages/useragentstring.php?name=All'
  """
  print('get ua list from web...')
  req = request.Request(url_ua)
  try:
    res = request.urlopen(req)
  except urllib.URLError as e:
    print(e)
  body = res.read()
  soup = BeautifulSoup(body, 'html.parser')
  tag_lis = soup.find_all('li')
  uas = []
  for tag in tag_lis:
    tag_a = tag.find('a')
    uas.append(tag.string)
  print(uas)
  return uas

def write_ua(filepath = './crawl_douban/spider_middleware/ua.txt'):
  """
  write ua list to file  
  """
  uas = get_ua()
  if file_ready(filepath):
    ua_str = '\r\n'.join(uas)
    file_obj = open(filepath, 'w')
    file_obj.write(ua_str)
    file_obj.close()
    print('最新UA已写入文件...')

def read_ua():
  """
  read ua list from file
  """
  pass

write_ua()