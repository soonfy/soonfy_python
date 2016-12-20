#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider start crawl user.'

__author__ = 'soonfy'

# modules
import re

from util.fs import file_ready

def get_users(soup, relation):
  """
  get users from douban
  """
  tag_dls = soup.find_all('dl')
  users = []
  userids = []
  for tag in tag_dls:
    tag_a = tag.dd.a
    user_url = tag_a['href']
    user_name = tag_a.string
    user = '%s\t%s\t%s' % (relation, user_name, user_url)
    users.append(user)
    m = re.search(r'/people/(\w+)/', user_url)
    if m:
      userids.append(m.group(1))
  return users, userids

def write_users(users, userid):
  """
  写入用户的关注与被关注文件
  """
  user_file = r'./crawl_douban/douban_user/users/%s.txt' % userid
  if file_ready(user_file):
    user_str = '\r\n'.join(users) + '\r\n'
    file_obj = open(user_file, 'a')
    file_obj.write(user_str)
    file_obj.close()
  print('users write success...')

def write_userids(userids):
  """
  写入所有用户ids文件
  """
  user_file = r'./crawl_douban/douban_user/users.txt'
  if file_ready(user_file):
    user_str = '\r\n'.join(userids) + '\r\n'
    file_obj = open(user_file, 'a')
    file_obj.write(user_str)
    file_obj.close()
    print('userids write success...')
