#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pipelines.py
"""

# Python imports
import logging
import string
import random

# GAE imports
from google.appengine.ext import ndb
from google.appengine.datastore.datastore_query import Cursor

# MyApp imports
import pipeline
from models import Station


class CreatePipeline(pipeline.Pipeline):

    def run(self, counter_start=0):

        logging.info('Running pipeline starting at counter = %s' % str(counter_start))

        if counter_start < 100:
            logging.info(' -> STARTING ANOTHER PIPELINE!')
            yield CreatePipeline(counter_start + 5)

        stations = []
        for counter in range(counter_start, counter_start + 5):
            station = Station()
            station.callsign = self.id_generator()

            stations.append(station)

        logging.info(' -> saving %s stations' % str(len(stations)))
        ndb.put_multi(stations)

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))


class EditPipeline(pipeline.Pipeline):

    def run(self, cursor=None, counter=0):

        logging.info('Running EditPipeline -> %s ...' % str(counter))

        cursor = Cursor(urlsafe=cursor)
        stations, next_cur, more = Station.query().fetch_page(10, start_cursor=cursor)

        if more and next_cur:
            yield EditPipeline(cursor=next_cur.urlsafe(), counter=counter + 1)

        for station in stations:
            station.some_value += 1

        ndb.put_multi(stations)
