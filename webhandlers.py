#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
webhandlers.py
'''

import webapp2

class MainPage(webapp2.RequestHandler):
    '''Main page handler'''

    def get(self):
        self.response.write('Hello World')
