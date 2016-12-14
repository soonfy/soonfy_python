#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider middleware.'

__author__ = 'soonfy'

from bs4 import BeautifulSoup
import urllib.request as urllib

class UA(object):
  def get_ua():
    """get ua from web"""
    ua_url = 'http://www.useragentstring.com/pages/useragentstring.php?name=All'
    _user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'
    headers = {'User-Agent': _user_agent}
    req = urllib.Request(ua_url, headers = headers)
    res = urllib.urlopen(req)
    body = res.read()
    # print(body)
    soup = BeautifulSoup(body, 'html.parser')
    tag_lis = soup.find_all('li')
    uas = []
    for tag in tag_lis:
      tag_a = tag.find('a')
      uas.append(tag.string)
    return uas
  
  def update_ua():
    """update ua from file"""
    