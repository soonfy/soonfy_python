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
  """
  update ua from web
  """
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
  """
  get ua from file
  """
  pass

def get_cookie():
  """
  get cookie from douban
  """
  print('get cookie...')
  param = {
    "source": 'None',
    "redir": 'https://www.douban.com/people/67492098/contacts',
    "form_email": 'soonfy@163.com',
    "form_password": 'soonfy163',
    "login": '登录',
    "captcha-id": 'KmmXq1YRh3d7pr9fiytBdjXY:en',
    "captcha-solution": 'produce'
  }
  data = urlencode(param).encode('utf-8')
  header = {
    'User-Agent': _user_agent,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.douban.com/people/67492098/contacts',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }

  req = request.Request(url_login, data, header)

  cookie = http.cookiejar.CookieJar()
  handler = request.HTTPCookieProcessor(cookie)
  # proxy_support = request.ProxyHandler({'https': '114.231.242.248:8088'})
  opener = request.build_opener(handler)
  # opener = request.build_opener(proxy_support)
  request.install_opener(opener)
  res = request.urlopen(req)

  body = res.read()
  print(body.decode('utf-8'))
  print(cookie)
