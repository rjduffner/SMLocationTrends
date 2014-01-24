"""

Author: Robert Duffner
Date: January 14, 2013
Email: rjduffner@gmail.com

surveyinformation.py

"""

import pyipinfodb
import api_service
import simplemapplot
import requests
import ratelimit

class SurveyInformation():
    def __init__(self, sm_api_key, sm_access_token):
        self.sm_api_key = sm_api_key
        self.sm_access_token = sm_access_token
        self.api = api_service.ApiService(self.sm_api_key, self.sm_access_token)

    def get_survey_answer_choices(self, survey_id, page_number, question_number):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            print response['data']['pages'][page_number]['questions'][question_number]['answers']
        else:
            print "Error with status code :" + str(response['status'])

    def get_number_of_pages(self, survey_id):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            resp = response['data']['pages']
        else:
            resp = []
        return len(resp)

    def get_number_of_questions_on_page(self, survey_id, page_number):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            resp = len(response['data']['pages'][page_number]['questions'])
        else:
            resp = None
        return resp

    def get_survey_question(self, survey_id, page_number, question_number):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            resp = response['data']['pages'][page_number]['questions'][question_number]
        else:
            resp = "Error with status code :" + str(response['status'])
        return resp

    def get_survey_pages(self, survey_id):
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            resp = response['data']['pages']
            return resp
        else:
            print "Error with status code :" + str(response['status'])
            return None

    def get_survey_page_count_and_questions(self, survey_id):
        pages_dict = {}
        pages = 0
        response = self.api.get_survey_details({'survey_id': survey_id})
        if response['status'] == 0:
            pages = response['data']['pages']
            for page in range(len(pages)):
                pages_dict[page] = len(response['data']['pages'][page]['questions'])
        return len(pages), pages_dict

