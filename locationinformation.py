import requests

class LocationInformation() :
    def __init__(self, ip_list) :
        self.ipinfodb_key = 'ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586'
        self.ip_list = ip_list
        self.ip_dictionary = {}
        self.get_location_information()

    def get_location_data(self, ip):
        base_url = 'http://api.ipinfodb.com/v3/ip-city/'
        params = {'key': self.ipinfodb_key, 'ip':ip, 'format':'json'}
        resp = requests.get(url=base_url, params=params)
        return resp.json()

    def get_location_information(self):
        for ip in self.ip_list:
            self.ip_dictionary[ip] = self.get_location_data(ip)
 
