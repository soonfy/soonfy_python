#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from html import application

httpd = make_server('', 9999, application)
print('wsgi server on port 9999...')
httpd.serve_forever()