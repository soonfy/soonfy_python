#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'douban spider: login or nologin.'

__author__ = 'soonfy'

# modules
import os

from urllib import request
from urllib.parse import urlencode
from http import cookiejar

from spider_middleware.ua import read_ua

def spider_login():
  """
  login douban spider  
  @return opener  
  """
  url_login = 'https://www.douban.com/accounts/login'
  param = {
    "source": 'None',
    "redir": 'https://www.douban.com/people/67492098/contacts',
    "form_email": 'soonfy@163.com',
    "form_password": 'soonfy163',
    "login": '登录'
  }
  data = urlencode(param).encode('utf-8')
  headers = {
    'User-Agent': read_ua(),
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.douban.com/people/67492098/contacts',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }
  req = request.Request(url_login, data, headers)
  filename = os.path.abspath(r'./crawl_douban/spider_middleware/cookie.txt')
  FileCookieJar= cookiejar.MozillaCookieJar(filename)
  FileCookieJar.save()
  handler = request.HTTPCookieProcessor(FileCookieJar)
  opener = request.build_opener(handler)
  request.install_opener(opener)
  res = request.urlopen(req)
  body = res.read().decode('utf-8')
  FileCookieJar.save()
  print('login spider success...')
  return opener

def spider_nologin():
  """
  nologin douban spider  
  @return opener  
  """
  header = {
    'User-Agent': read_ua(),
    'Referer': 'https://www.douban.com/',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }
  headers = []
  for key, value in header.items():
    elem = (key, value)
    headers.append(elem)
  cj = cookiejar.CookieJar()
  handler = request.HTTPCookieProcessor(cj)
  opener = request.build_opener(handler)
  request.install_opener(opener)
  opener.addheaders = headers
  print('spider success...')
  return opener
