#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
main.py
"""

# Python imports

# GAE imports
import webapp2
from webapp2_extras import routes

url_mapping = \
[
    routes.RedirectRoute(r'/', handler='webhandlers.MainPage'),
]

app = webapp2.WSGIApplication(url_mapping)
