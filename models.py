#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
models.py

This file is an example code for presentation I gave for GDG Krakow.
Slides are available here: http://rzajac.github.io/gaeslides/#1

@author: Rafal Zajac rzajac<at>gmail<dot>com
@copyright: Copyright 2007-2013 Rafal Zajac rzajac<at>gmail<dot>com. All rights reserved.
@license: Licensed under the MIT license
'''

# GAE imports
from google.appengine.ext import ndb


class User(ndb.Model):
    login_name = ndb.StringProperty()
    password = ndb.StringProperty()


class LoginCounter(ndb.Model):
    count = ndb.IntegerProperty(default=0, indexed=False)
