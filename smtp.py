#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# smtp
# email构造邮件
# smtplib发送邮件
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.utils import parseaddr, formataddr
from email.header import Header
import smtplib

def _format_addr(s):
  name, addr = parseaddr(s)
  return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input('from:')
# from_pass = input('pass:')
# to_addr = input('to:')
# smtp_server = input('smtp server:')
from_addr = 'kzdwqjsnjd@sina.com'
from_pass = 'qpzm1234'
to_addr = 'soonfy@163.com'
smtp_server = 'smtp.sina.com'

# msg = MIMEText('email from python...', 'plain', 'utf-8')
# msg = MIMEText('<html><h1>miss</h1><p><a href="http://www.baidu.com" target="_blank">baidu</p></html>', 'html', 'utf-8')
msg = MIMEMultipart()
msg.attach(MIMEText('<html><h1>miss</h1><p><a href="http://www.baidu.com" target="_blank">baidu</p><img src="cid:0"></html>', 'html', 'utf-8'))

msg['from'] = _format_addr('sf <%s>' % from_addr)
msg['to'] = _format_addr('qw <%s>' % to_addr)
msg['subject'] = Header('miss...', 'utf-8').encode()

with open('demo.jpg', 'rb') as f:
  mime = MIMEBase('image', 'jpg', filename = 'demo.jpg')
  mime.add_header('Content-Disposition', 'attachment', filename = 'demo.jpg')
  mime.add_header('Content-Id', '<0>')
  mime.add_header('X-Attachment-Id', '0')
  mime.set_payload(f.read())
  encoders.encode_base64(mime)
  msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, from_pass)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
