import pyipinfodb
import api_service
import simplemapplot
import requests
import ratelimit

class ReadRespondentInformation():
    def __init__(self, survey_id):
        self.sm_api_key = 'pcpuk2dfxdwggu6gfssxqa6t'
        self.sm_access_token = 'UFHR1aBDl2QjFoOzyDhoj91aM1Q3Atp-HtOvcI8kBk.HIBEdrGLtGKLnbSmHGcE-cNkJnPOaR1t-jiJqrE3iqUwObKHbg3NuTB-u5W6w9bg='
        self.ipinfodb_key = 'ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586'
        self.api = api_service.ApiService(self.sm_api_key, self.sm_access_token)
        
        self.get_respondents(survey_id)
        self.get_responses(survey_id)

    def get_respondents(self, survey_id):
        self.respondent_dictionary = self.api.get_respondent_list({'survey_id': survey_id, 'fields':['ip_address']})['data']
    
    @ratelimit.RateLimited(2)
    def get_response(self, survey_id, respondent_id):
        try:
            response = self.api.get_responses({'survey_id': survey_id, 'respondent_ids': respondent_id})

            print response['status']
            print response
            print
            resp = {'Error': 'BAD INFO'}
        except:
            resp = {'Error': 'BAD INFO'}
        return resp
    
    def get_responses(self, survey_id):
        respondent_list = []
        for respondent in self.respondent_dictionary[:9]:
            respondent_list.append(str(respondent['respondent_id']))
        print respondent_list
        questions = self.get_response(survey_id, respondent_list)
        #respondent.update(questions)


        '''

        for respondent in self.respondent_dictionary:
            questions = self.get_response(survey_id, respondent['respondent_id'])
            respondent.update(questions)
        '''

smlt = ReadRespondentInformation('45533333')
#smlt = ReadRespondentInformation('46460327')


print smlt.respondent_dictionary

#for i in smlt.respondent_dictionary:
#    print i



