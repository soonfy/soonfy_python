#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'douban spider: login or nologin.'

__author__ = 'soonfy'

# modules
from bs4 import BeautifulSoup
from fs import file_ready
from urllib.parse import urlencode
from urllib import request
import http.cookiejar
import os

url_login = 'https://www.douban.com/accounts/login'
_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/54.0.2840.100 Safari/537.36'

def spider_login():
  """
  login douban spider
  """
  print('start login...')
  param = {
    "source": 'None',
    "redir": 'https://www.douban.com/people/67492098/contacts',
    "form_email": 'soonfy@163.com',
    "form_password": 'soonfy163',
    "login": '登录'
  }
  data = urlencode(param).encode('utf-8')
  headers = {
    'User-Agent': _user_agent,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.douban.com/people/67492098/contacts',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }
  req = request.Request(url_login, data, headers)

  filename = os.path.abspath(r'./spider_douban/cookie.txt')
  FileCookieJar= http.cookiejar.MozillaCookieJar(filename)
  FileCookieJar.save()
  handler = request.HTTPCookieProcessor(FileCookieJar)

  opener = request.build_opener(handler)
  request.install_opener(opener)

  res = request.urlopen(req)
  body = res.read().decode('utf-8')
  print(body)
  FileCookieJar.save()
  print('login spider success...')
  return request

def spider_nologin():
  """
  common douban spider
  """
  header = {
    'User-Agent': _user_agent,
    'Referer': 'https://www.douban.com/',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }
  headers = []
  for key, value in header.items():
    elem = (key, value)
    headers.append(elem)
  cj = http.cookiejar.CookieJar()
  opener = request.build_opener(request.HTTPCookieProcessor(cj))
  opener.addheaders = headers
  print('nologin spider success...')
  return opener