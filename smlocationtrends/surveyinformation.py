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

    def get_number_of_pages(self, survey_id):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            resp = response['data']['pages']
        return len(resp)

    def get_number_of_questions_on_page(self, survey_id, page_number):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            resp = len(response['data']['pages'][page_number-1]['questions'])
        else:
            resp = None
        return resp

    def get_survey_question(self, survey_id, page_number, question_number):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            print response['data']['pages'][page_number-1]['questions'][question_number-1]
        else:
            print "Error with status code :" + str(response['status'])

    def get_survey_pages(self, survey_id):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            resp = response['data']['pages']
            return resp
        else:
            print "Error with status code :" + str(response['status'])
            return None


si = SurveyInformation()



#print si.get_number_of_pages('45533333')
#pages = si.get_number_of_pages('46460327')
#pages = 2
#print pages
#for i in range(pages):
#    print i+1
#    print si.get_number_of_questions_on_page('46460327', i+1)


#print si.get_survey_question('46460327',2,4)

print si.get_survey_questions_by_page('46460327')
#print si.get_survey_questions_by_page('45533333')
#si.get_survey_pages('46460327')
#print si.get_survey_pages('45533333')
