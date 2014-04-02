"""

Author: Robert Duffner
Date: January 14, 2013
Email: rjduffner@gmail.com

locationinformation.py

"""
from pyramid.view import view_config
import pygeoip
import os

here = os.path.dirname(__file__)

CITY_DB = os.path.join(here, '..', 'ipdata' ,"GeoLiteCity.dat")
geo = pygeoip.GeoIP(CITY_DB, pygeoip.MEMORY_CACHE)

def get_location_from_file(ip):
    return geo.record_by_addr(ip)

@view_config(route_name='location_information', renderer='json')
def get_location_data_pyinfodb(request):
    ip = request.matchdict['ip']
    return {'status': 0, 'data' : get_location_from_file(ip)}
