"""

Author: Robert Duffner
Date: April 1, 2014
Email: rjduffner@gmail.com

auth.py

"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
import json

import logging
logger = logging.getLogger(__name__)


@view_config(route_name='auth', renderer='json')
def auth(request):
    # Key and Token
    api_key = request.POST.get('api_key')
    access_token = request.POST.get('access_token')

    response = Response(content_type='application/json')
    response.set_cookie('api_key', api_key, max_age=31536000)
    response.set_cookie('access_token', access_token, max_age=31536000)
    response.body = json.dumps({'hello': 'world'})
    return response
