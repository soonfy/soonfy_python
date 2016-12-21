#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider ua.'

__author__ = 'soonfy'

# modules
import os
import random

from urllib import request
from bs4 import BeautifulSoup

from util.fs import file_ready

def spider_origin():
  """
  origin spider  
  @return opener  
  """
  header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Host': 'www.useragentstring.com',
    'Origin': 'www.useragentstring.com'
  }
  headers = []
  for key, value in header.items():
    elem = (key, value)
    headers.append(elem)
  opener = request.build_opener()
  opener.addheaders = headers
  print('origin spider success...')
  return opener

def get_ua():
  """
  get ua list from web  
  @return uas  
  ex:
    'http://www.useragentstring.com/pages/useragentstring.php?name=All'
  """
  url_ua = 'http://www.useragentstring.com/pages/useragentstring.php?name=All'
  print('get ua list from web...')
  opener = spider_origin()
  body = opener.open(url_ua).read()
  soup = BeautifulSoup(body, 'html.parser')
  tag_lis = soup.find_all('li')
  uas = []
  for tag in tag_lis:
    tag_a = tag.find('a')
    uas.append(tag.string)
  return uas

def write_ua(filepath = r'./crawl_douban/spider_middleware/ua.txt'):
  """
  write ua list to file  
  @param filepath  
  """
  uas = get_ua()
  if file_ready(filepath):
    ua_str = '\n'.join(uas) + '\n'
    file_obj = open(filepath, 'w')
    file_obj.write(ua_str)
    file_obj.close()
    print('new UA write success...')

def read_ua(filepath = r'./crawl_douban/spider_middleware/ua.txt'):
  """
  read ua from file  
  @param filepath  
  @return ua  
  """
  if file_ready(filepath):
    file_obj = open(filepath, 'r')
    ua_str = file_obj.read()
    file_obj.close()
    uas = ua_str.split('\n')
    ua = random.choice(uas)
    print('new ua...')
    print(ua)
    return ua
