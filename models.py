#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
models.py
'''

# GAE imports
from google.appengine.ext import ndb


class Station(ndb.Model):
    callsign = ndb.StringProperty()
    some_value = ndb.IntegerProperty(default=0)
