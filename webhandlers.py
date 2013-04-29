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

# App imports

# GAE imports
import webapp2

# MyApp imports
from pipelines import CreatePipeline, EditPipeline

class MainPage(webapp2.RequestHandler):
    '''Main page handler'''

    def get(self):
        '''Display login form'''

        self.response.write('''
        <html>
            <body>
                <h1>Index page. Nothing to show here!</h1>
            </body>
        </html>
        ''')

class CreateStations(webapp2.RequestHandler):
    '''Create stations'''

    def get(self):

        job = CreatePipeline()
        job.start(queue_name="Stations")

        return self.response.out.write('Create stations pipeline started.')

class EditStations(webapp2.RequestHandler):
    '''Edit stations'''

    def get(self):

        job = EditPipeline()
        job.start(queue_name="Stations")

        return self.response.out.write('Edit stations pipeline started.')
