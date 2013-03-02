#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
webhandlers.py
'''

# App imports

# GAE imports
import webapp2

# MyApp imports
from pipelines import CreatePipeline, EditPipelineRoot

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

        job = EditPipelineRoot()
        job.start(queue_name="Stations")

        return self.response.out.write('Edit stations pipeline started.')
