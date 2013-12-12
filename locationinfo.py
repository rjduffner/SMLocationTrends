'''

'''

import pyipinfodb
import api_service
import simplemapplot
import requests

from SurveyResults import SurveyResults

class SMLocationTrends() :
    def __init__(self, survey_id, question_number=0) :
        self.sm_api_key = 'pcpuk2dfxdwggu6gfssxqa6t'
        self.sm_access_token = 'UFHR1aBDl2QjFoOzyDhoj91aM1Q3Atp-HtOvcI8kBk.HIBEdrGLtGKLnbSmHGcE-cNkJnPOaR1t-jiJqrE3iqUwObKHbg3NuTB-u5W6w9bg='
        self.ipinfodb_key = 'ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586'
        self.api = api_service.ApiService(self.sm_api_key, self.sm_access_token)

        self.respondent_list = None
        self.questions = None


        self.respondent_info = ReadRespondentInfo(survey_id)

        #self.add_ip_location_info()
        self.get_answer_choices(survey_id, 1, 1)

    def get_survey_results(self, survey_id):
        return self.respondent_info.self.respondent_dictionary

    def get_answer_choices(self, survey_id, page_number, question_number):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            print response['data']['pages'][page_number-1]['questions'][question_number-1]['answers']
        else:
            print "Error with status code :" + str(response['status'])

    def add_ip_location_info(self):
        for respondent in self.respondent_list:
            resp = self.get_location_data(respondent['ip_address'])
            for key in resp.keys():
                 respondent[key] = resp[key]
    
    def get_location_data(self, ip):
        base_url = 'http://api.ipinfodb.com/v3/ip-city/'
        params = {'key': self.ipinfodb_key, 'ip':ip, 'format':'json'}
        resp = requests.get(url=base_url, params=params)
        return resp.json()
































smlt = SMLocationTrends('45533333')
#for i in smlt.respondent_list:
#    print i
#    print


'''
#a = api.get_survey_list()
#for x in a['data']:
#print x

data = api.get_survey_details({'survey_id': '45533333'})
#print data
print data['data']['title']['text']
responses = api.get_respondent_list({'survey_id': '45533333', 'fields':['ip_address']})
#url = responses['data'][3]['ip_address']

for url in responses['data']:
    print url['ip_address']
    
    #ip_location = 'http://api.hostip.info/get_json.php?ip=' + url['ip_address'] + '&position=true'

    ip_location = 'http://api.ipinfodb.com/v3/ip-city/?key=ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586&ip=' + url['ip_address'] + '&format=json'

    #ip_location = 'http://www.geody.com/geoip.php?ip=' + url['ip_address']   
    resp = requests.get(url=ip_location, params=None)
    #print resp.content
    print resp.json()


#ids = []
#ids.append(responses['data'][0]['respondent_id'])
#print ids
#print api.get_responses({'survey_id': '45533333', 'respondent_ids': ids})

#print api.get_respondent_list({'survey_id': '45533333'})

example_colors = ["#FC8D59","#FFFFBF","#99D594"]
state_value = {"TX":2, "WI":1, "IL":1, "AK":0, "MI":0, "HI":2}
make_us_state_map(data=state_value, colors=example_colors)



example_colors = ["#FC8D59","#FFFFBF","#99D594"]
country_value = {"us":1, "au":2, "gb":0}
make_world_country_map(data=country_value, colors=example_colors)



        #ip_location = 'http://api.hostip.info/get_json.php?ip=' + url['ip_address'] + '&position=true'
        #ip_location = 'http://api.ipinfodb.com/v3/ip-city/?key=ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586&ip=' + ip_list[0] + '&format=json'
        #ip_location = 'http://www.geody.com/geoip.php?ip=' + url['ip_address']
        #resp = requests.get(url=ip_location, params=None)

