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
    routes.RedirectRoute(r'/create-pipeline', handler='webhandlers.CreateStations'),
    routes.RedirectRoute(r'/edit-pipeline', handler='webhandlers.EditStations'),
]

app = webapp2.WSGIApplication(url_mapping)
