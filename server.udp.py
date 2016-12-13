#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('this is a udp server. waiting for connection...')

def udplink(s, data, addr):
  print('a new connection from %s:%s' % addr)
  print('data is %s' % data.decode('utf-8'))
  s.sendto(('hello %s...' % data.decode('utf-8')).encode('utf-8'), addr)

while True:
  data, addr = s.recvfrom(1024)
  t = threading.Thread(target = udplink, args = (s, data, addr))
  t.start()