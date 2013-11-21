import pyipinfodb
import api_service
import simplemapplot
import requests
import time


class ReadRespondentInformation():
    def __init__(self, survey_id):
        self.sm_api_key = 'pcpuk2dfxdwggu6gfssxqa6t'
        self.sm_access_token = 'UFHR1aBDl2QjFoOzyDhoj91aM1Q3Atp-HtOvcI8kBk.HIBEdrGLtGKLnbSmHGcE-cNkJnPOaR1t-jiJqrE3iqUwObKHbg3NuTB-u5W6w9bg='
        self.ipinfodb_key = 'ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586'
        self.api = api_service.ApiService(self.sm_api_key, self.sm_access_token)
        
        self.get_respondents(survey_id)
        self.get_responses(survey_id)

    def get_respondents(self, survey_id):
        self.respondent_list = self.api.get_respondent_list({'survey_id': survey_id, 'fields':['ip_address']})['data']
   
    def get_responses(self, survey_id):
        for i in self.respondent_list:
            try:
                questions = self.api.get_responses({'survey_id': survey_id, 'respondent_ids': [i['respondent_id']]})['data'][0]
            except:
                questions = {}
            i.update(questions)


smlt = ReadRespondentInformation('45533333')

for i in smlt.respondent_list:
    print i





