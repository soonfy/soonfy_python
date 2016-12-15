#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider middleware.'

__author__ = 'soonfy'

from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib import request
import http.cookiejar

url_ua = 'http://www.useragentstring.com/pages/useragentstring.php?name=All'
url_login = 'https://www.douban.com/accounts/login'
_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/54.0.2840.100 Safari/537.36'

def update_ua():
  """update ua from web"""
  print('update ua...')
  req = request.Request(url_ua)
  req.add_header('User-Agent', _user_agent)
  try:
    res = request.urlopen(req)
  except urllib.URLError as e:
    print(e)
  body = res.read()
  # print(body)
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
  data = {
    "source": 'index_nav',
    "form_email": 'soonfy@163.com',
    "form_password": 'soonfy163'
  }
  cookie = http.cookiejar.CookieJar()
  cjhdr  =  request.HTTPCookieProcessor(cookie)
  opener = request.build_opener(cjhdr)
  req = request.Request(url_login)
  req.add_header('User-Agent', _user_agent)
  req.add_header('Content-Type', 'application/x-www-form-urlencoded')
  req.add_header('Content-Length', str(len(data)))
  param = urlencode(data)
  print(param)
  # res = request.urlopen(req, param.encode('utf-8'))
  res = opener.open(url_login, param)
  body = res.read()
  print(body.decode('utf-8'))
