#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider start crawl user.'

__author__ = 'soonfy'

# modules
from bs4 import BeautifulSoup
from fs import file_ready
from urllib.parse import urlencode
from urllib import request
import http.cookiejar
import os
import re

url_login = 'https://www.douban.com/accounts/login'
_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/54.0.2840.100 Safari/537.36'

def login():
  """
  get users from douban
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
  print('login success...')
  return request

def get_users(request, userid):
  """
  get users from douban
  """
  ua_file = os.path.abspath(r'./spider_douban/douban_user/%s.txt' % userid)
  url_user_con = 'https://www.douban.com/people/%s/contacts' % userid
  url_user_revcon = 'https://www.douban.com/people/%s/rev_contacts' % userid
  # headers = {
  #   'User-Agent': _user_agent,
  #   'Content-Type': 'text/html; charset=utf-8',
  #   'Referer': url_user_con,
  #   'Host': 'www.douban.com',
  #   'Origin': 'https://www.douban.com'
  # }
  body = request.urlopen(url_user_con).read().decode('utf-8')
  print(body)
  soup = BeautifulSoup(body, 'html.parser')
  tag_dls = soup.find_all('dl')
  users = []
  userids = []
  for tag in tag_dls:
    tag_a = tag.dd.a
    user_url = tag_a['href']
    user_name = tag_a.string
    user_con = 'contacts'
    user = '%s\t%s\t%s' % (user_con, user_name, user_url)
    users.append(user)
    m = re.search(r'/people/(\w+)/', user_url)
    if m:
      userids.append(m.group(1))
  body = request.urlopen(url_user_revcon).read().decode('utf-8')
  print(body)
  soup = BeautifulSoup(body, 'html.parser')
  tag_dls = soup.find_all('dl')
  for tag in tag_dls:
    tag_a = tag.dd.a
    user_url = tag_a['href']
    user_name = tag_a.string
    user_con = 'rev_contacts'
    user = '%s\t%s\t%s' % (user_con, user_name, user_url)
    users.append(user)
    m = re.search(r'/people/(\w+)/', user_url)
    if m:
      userids.append(m.group(1))
  if file_ready(ua_file):
    ua_str = '\r\n'.join(users)
    file_obj = open(ua_file, 'w')
    file_obj.write(ua_str)
    file_obj.close()
    print('%s已写入文件...' % userid)
  
  return userids