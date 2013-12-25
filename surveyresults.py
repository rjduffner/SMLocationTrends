'''

'''

import pyipinfodb
import api_service
import simplemapplot
import requests
import ratelimit

class SurveyResults():
    def __init__(self, sm_api_key, sm_access_token, survey_id):
        self.DEBUG = False
        self.sm_api_key = 'pcpuk2dfxdwggu6gfssxqa6t'
        self.sm_access_token = 'UFHR1aBDl2QjFoOzyDhoj91aM1Q3Atp-HtOvcI8kBk.HIBEdrGLtGKLnbSmHGcE-cNkJnPOaR1t-jiJqrE3iqUwObKHbg3NuTB-u5W6w9bg='
        self.ipinfodb_key = 'ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586'
        self.api = api_service.ApiService(self.sm_api_key, self.sm_access_token)
        
        self.get_survey_respondent_information(survey_id)
        self.get_survey_results(survey_id)

    def __diff(self, d1, d2, key):
        if d1[key] != d2[key]:
            return d1
        new_keys = list(set(d2) - set(d1))
        for new_key in new_keys:
            d1[new_key] = d2[new_key]
        return d1

    def __join(self, l1, l2, key):
        l3 = l1
        for d2 in l2:
            l3 = map(lambda d1: self.__diff(d1, d2, key), l3)
        return l3

    @ratelimit.RateLimited(2)
    def __return_chunk_of_survey_results(self, survey_id, respondent_id):
        try:
            response = self.api.get_responses({'survey_id': survey_id, 'respondent_ids': respondent_id})
        except:
            response = {'Error': 'BAD INFO'}
        return response

    def get_survey_respondent_information(self, survey_id):
        self.respondent_dictionary = self.api.get_respondent_list({'survey_id': survey_id, 'fields':['ip_address']})['data']
    
    def get_survey_results(self, survey_id):
        responses = []

        # Chuck respondent ids into 10
        #
        for i in range(0, len(self.respondent_dictionary), 10):
            respondent_list = []
            chunk = self.respondent_dictionary[i:i + 10]
            for respondent in chunk:
                respondent_list.append(respondent['respondent_id'])

            # For each set of 10, add the answer information
            #
            for item in self.__return_chunk_of_survey_results(survey_id, respondent_list)['data']:
                responses.append(item)

        # Merge dictionaries by respondent id.
        #
        self.__join(self.respondent_dictionary, responses, 'respondent_id')
