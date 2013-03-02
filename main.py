#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
main.py
"""

# Python imports

# GAE imports
import webapp2
from webapp2_extras import routes

url_mapping = \
[
    routes.RedirectRoute(r'/', handler='webhandlers.MainPage'),

    routes.RedirectRoute(r'/setup/<login_name:\w+>', handler='webhandlers.SetupHandler'),

    routes.RedirectRoute(r'/profile/<user_id:\d+>', handler='webhandlers.ProfilePage'),

    routes.RedirectRoute(r'/user-analytics', handler='webhandlers.LoginCounterHandler'),
]

app = webapp2.WSGIApplication(url_mapping)
