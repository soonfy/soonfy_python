#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider middleware.'

__author__ = 'soonfy'

from bs4 import BeautifulSoup
from urllib import request

url_ua = 'http://www.useragentstring.com/pages/useragentstring.php?name=All'
url_login = 'https://accounts.douban.com/login'
_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/54.0.2840.100 Safari/537.36'

def update_ua():
  """update ua from web"""
  print('update ua...')
  req = request.Request(url_ua)
  req.add_header('User-Agent', _user_agent)
  res = request.urlopen(req)
  body = res.read()
  print(body)
  soup = BeautifulSoup(body, 'html.parser')
  tag_lis = soup.find_all('li')
  uas = []
  for tag in tag_lis:
    tag_a = tag.find('a')
    uas.append(tag.string)
  return uas

def get_ua():
  """get ua from file"""
  pass

def get_cookie():
  """get cookie from douban"""
  print('get cookie...')
  headers = {
    'User-Agent': _user_agent
  }
  data = {
    "source": None,
    "redir": 'https://www.douban.com/people/135422939/',
    "form_email": 'soonfy@163.com',
    "form_password": 'soonfy163',
    "login": '登录'
  }
  req = urllib.Request(url_login, data, headers = headers)
  res = urllib.urlopen(req)
  body = res.read()
  print(body)
