#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider middleware.'

__author__ = 'soonfy'

from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib import request
import http.cookiejar

url_ua = 'http://www.useragentstring.com/pages/useragentstring.php?name=All'
url_login = 'https://accounts.douban.com/login'
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
    "source": 'None',
    "redir": 'https://www.douban.com/people/67492098/',
    "form_email": 'soonfy@163.com',
    "form_password": 'soonfy163',
    "login": '登录'
  }
  param = urlencode(data)

  cookie = http.cookiejar.CookieJar()
  handler = request.HTTPCookieProcessor(cookie)
  opener = request.build_opener(handler)
  opener.addheaders = [('User-Agent', _user_agent), ('Content-Type', 'application/x-www-form-urlencoded'), ('Content-Length', str(len(param))), ('Referer', 'https://www.douban.com/people/67492098/contacts'), ('Host', 'accounts.douban.com'), ('Origin', 'https://www.douban.com'), ('Cookie', 'bid=tGfHl4Pl38E; gr_user_id=b7f2ee17-989a-4f3e-8147-f54e10feb238; ll="108288"; viewed="1148282_26821461_25862578_26872990_25863515_26593179_26820855_24703171_2297786"; ps=y; _ga=GA1.2.1412101783.1474446904; _vwo_uuid_v2=3B609F95BC383BF840E4B0619CE0915F|0a060be832758ffb66cd8099c7cf2b87; push_noty_num=0; push_doumail_num=0; ap=1; __utmt=1; __utma=30149280.1412101783.1474446904.1481865548.1481870624.14; __utmb=30149280.1.10.1481870624; __utmc=30149280; __utmz=30149280.1479435389.8.7.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=%E5%AE%89%E8%A3%85PIL; __utmv=30149280.15504; as="https://www.douban.com/people/146905195/"')]
  
  # req = request.Request(url_login, param)
  # req.add_header('User-Agent', _user_agent)
  # req.add_header('Content-Type', 'application/x-www-form-urlencoded')
  # req.add_header('Content-Length', str(len(param)))
  # req.add_header('Referer', 'https://www.douban.com/people/67492098/contacts')
  # req.add_header('Cookie', 'bid=tGfHl4Pl38E; gr_user_id=b7f2ee17-989a-4f3e-8147-f54e10feb238; ll="108288"; viewed="1148282_26821461_25862578_26872990_25863515_26593179_26820855_24703171_2297786"; ps=y; _ga=GA1.2.1412101783.1474446904; _vwo_uuid_v2=3B609F95BC383BF840E4B0619CE0915F|0a060be832758ffb66cd8099c7cf2b87; push_noty_num=0; push_doumail_num=0; ap=1; __utmt=1; __utma=30149280.1412101783.1474446904.1481865548.1481870624.14; __utmb=30149280.1.10.1481870624; __utmc=30149280; __utmz=30149280.1479435389.8.7.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=%E5%AE%89%E8%A3%85PIL; __utmv=30149280.15504; as="https://www.douban.com/people/146905195/"')
  # req.add_header('Host', 'accounts.douban.com')
  # req.add_header('Origin', 'https://www.douban.com')

  # res = opener.open(url_login, data = param.encode('utf-8'))
  res = opener.open('https://www.douban.com/people/67492098/contacts')
  body = res.read()
  print(body.decode('utf-8'))
  print(cookie)
