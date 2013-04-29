#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
main.py

This file is an example code for presentation I gave for GDG Krakow.
Slides are available here: http://rzajac.github.io/gaeslides/#1

@author: Rafal Zajac rzajac<at>gmail<dot>com
@copyright: Copyright 2007-2013 Rafal Zajac rzajac<at>gmail<dot>com. All rights reserved.
@license: Licensed under the MIT license
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
