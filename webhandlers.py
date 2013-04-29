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
from models import LoginCounter, User

# GAE imports
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import taskqueue


class MainPage(webapp2.RequestHandler):
    '''Main page handler'''

    def get(self):
        '''Display login form'''

        self.response.write('''
        <html>
            <body>
                <form action="/" method="POST">
                    <p>Login <input type="text" name="login_name"></p>
                    <p>Password <input type="password" name="password"></p>
                    <p><button type="submit">Login</button>
                </form>
            </body>
        </html>
        ''')

    def post(self):
        '''Login user'''

        login_name = self.request.get('login_name')
        password = self.request.get('password')

        user = self.authenticate(login_name, password)

        if user:
            user_id = user.key.id()
            # Add the task to the queue.
            taskqueue.add(url='/user-analytics', queue_name='LoginCounter', params={'user_id': user_id})
            return self.redirect('/profile/%s' % user_id)

        self.redirect('/')

    def authenticate(self, login_name, password):
        '''Authenticate user in the system'''

        user = User.query(User.login_name == login_name).get()

        if user and user.password == password:
            return user
        else:
            return None


class ProfilePage(webapp2.RequestHandler):
    '''Profile handler'''

    def get(self, user_id):

        user = User.get_by_id(int(user_id))

        if user:
            login_name = user.login_name

            key_name = 'user_login_counter:%s' % str(user.key.id())
            counter = ndb.Key(LoginCounter, key_name).get()

            if counter:
                login_count = counter.count
            else:
                login_count = 0
        else:
            login_name = 'Unknown!!!'
            login_count = 0

        self.response.write('Profile page for: <b>%s</b>,<br> Login count: <b>%s</b>' % (login_name, str(login_count)))


class SetupHandler(webapp2.RequestHandler):
    '''Setup test user'''

    def get(self, login_name):

        user = User.gql('WHERE login_name = :1', login_name).get()

        if user is None:

            user = User()
            user.login_name = login_name
            user.password = 'test123'
            user.put()

            self.response.write('Test user created')
        else:
            self.response.write('Test user already existed!')


class LoginCounterHandler(webapp2.RequestHandler):

    def post(self):
        user_id = self.request.get('user_id')

        @ndb.transactional
        def txn():
            key_name = 'user_login_counter:%s' % str(user_id)

            counter = LoginCounter.get_or_insert(key_name)
            counter.count += 1
            counter.put()

        txn()
