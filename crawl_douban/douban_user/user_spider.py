#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'user spider class.'

__author__ = 'soonfy'

# modules
from bs4 import BeautifulSoup

class UserSpider(object):
  """
  douban user spider
  relation: contacts, rev_contacts
  """
  def __init__(self, userid, opener):
    self.userid = userid
    self.opener = opener
    self.contacts = 'https://www.douban.com/people/%s/contacts' % userid
    self.rev_contacts = 'https://www.douban.com/people/%s/rev_contacts' % userid

  def crawl_contacts(self):
    """
    关注
    """
    opener, contacts = self.opener, self.contacts
    print(contacts)
    body = opener.open(contacts).read()
    soup = BeautifulSoup(body, 'html.parser')
    return soup, 'contacts'

  def crawl_rev_contacts(self):
    """
    被关注
    """
    opener, rev_contacts = self.opener, self.rev_contacts
    print(rev_contacts)
    body = opener.open(rev_contacts).read()
    soup = BeautifulSoup(body, 'html.parser')
    return soup, 'rev_contacts'
