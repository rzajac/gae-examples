#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
webhandlers.py

This file is an example code for presentation I gave for GDG Krakow.
Slides are available here: http://rzajac.github.io/gaeslides/#1

@author: Rafal Zajac rzajac<at>gmail<dot>com
@copyright: Copyright 2007-2013 Rafal Zajac rzajac<at>gmail<dot>com. All rights reserved.
@license: Licensed under the MIT license
'''

import webapp2

class MainPage(webapp2.RequestHandler):
    '''Main page handler'''

    def get(self):
        self.response.write('Hello World')
