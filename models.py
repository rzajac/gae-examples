#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
models.py
'''

# GAE imports
from google.appengine.ext import ndb


class User(ndb.Model):
    login_name = ndb.StringProperty()
    password = ndb.StringProperty()


class LoginCounter(ndb.Model):
    count = ndb.IntegerProperty(default=0, indexed=False)
