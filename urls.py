#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from handlers.api import APIHandler

from handlers.home import HomeHandler
from handlers.search import SearchHandler
from handlers.detail import DetailHandler
from handlers.update import UpdateHandler
from handlers.download import DownloadHandler

url_patterns = [
    (r'/',HomeHandler),
    (r'/search',SearchHandler),
    (r'/detail/(.+)',DetailHandler),
    (r'/download/(.+)',DownloadHandler),
    (r'/update',UpdateHandler),
    (r'/api/.*', APIHandler),
    (r'.*',BaseHandler),
]