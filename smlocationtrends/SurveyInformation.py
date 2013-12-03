'''

'''

import pyipinfodb
import api_service
import simplemapplot
import requests
import ratelimit

class SurveyInformation():
    def __init__(self):
        self.sm_api_key = 'pcpuk2dfxdwggu6gfssxqa6t'
        self.sm_access_token = 'UFHR1aBDl2QjFoOzyDhoj91aM1Q3Atp-HtOvcI8kBk.HIBEdrGLtGKLnbSmHGcE-cNkJnPOaR1t-jiJqrE3iqUwObKHbg3NuTB-u5W6w9bg='
        self.ipinfodb_key = 'ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586'
        self.api = api_service.ApiService(self.sm_api_key, self.sm_access_token)
       
    def get_survey_answer_choices(self, survey_id, page_number, question_number):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            print response['data']['pages'][page_number-1]['questions'][question_number-1]['answers']
        else:
            print "Error with status code :" + str(response['status'])


    def get_survey_questions(self):
        pass

    def get_survey_pages(self):
        pass

    def get_survey_questions_by_page(self, survey_id):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            resp = response['data']['pages']
            for page in resp:
                questions = page['questions']
                for question in questions:
                    print question
                    print
                print
                print
                print
        else:
            print "Error with status code :" + str(response['status'])


#si = SurveyInformation('45533333')
si = SurveyInformation('46460327')
si.get_survey_questions_by_page()
