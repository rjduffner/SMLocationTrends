"""

Author: Robert Duffner
Date: January 14, 2013
Email: rjduffner@gmail.com

locationinformation.py

"""
import requests

class LocationInformation(object) :
    def __init__(self, ipinfodb_key) :
        self.ipinfodb_key = ipinfodb_key 
        #self.ip_list = ip_list
        self.ip_dictionary = {}
        #self.get_location_information()

    def get_location_data(self, ip):
        base_url = 'http://api.ipinfodb.com/v3/ip-city/'
        params = {'key': self.ipinfodb_key, 'ip':ip, 'format':'json'}
        resp = requests.get(url=base_url, params=params)
        print resp.json()
        if resp.status_code == 200:
            data = resp.json()
        else:
            data = None
        return data

    def get_location_information(self):
        for ip in self.ip_list:
            self.ip_dictionary[ip] = self.get_location_data(ip)
 