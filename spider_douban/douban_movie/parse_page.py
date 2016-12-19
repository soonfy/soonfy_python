#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'parse douban page data page.'

__author__ = 'soonfy'


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