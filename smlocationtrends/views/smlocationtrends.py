"""

Author: Robert Duffner
Date: January 14, 2013
Email: rjduffner@gmail.com

smlocationtrends.py

"""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from surveyinformation import SurveyInformation
from surveyresults import SurveyResults

from collections import Counter

import logging
logger = logging.getLogger(__name__)


@view_config(route_name='home', renderer='templates/index.jinja2')
def index(request):
    params = dict(request.GET)
    if 'survey_id' in params:
        return HTTPFound(location='/survey/'+ request.GET['survey_id'])
    return {'project': 'smlocationtrends'}

@view_config(route_name='survey', renderer='templates/survey.jinja2')
def survey(request):
    SM_API_KEY = request.registry.settings['sm_api_key']
    SM_ACCESS_TOKEN = request.registry.settings['sm_access_token']
    survey_id = request.matchdict['survey_id']


    si = SurveyInformation(SM_API_KEY, SM_ACCESS_TOKEN)
    pages, questions = si.get_survey_page_count_and_questions(survey_id)

    return {'project': 'smlocationtrends',
            'pages': pages,
            'questions': questions,
            'survey_id': survey_id
            }

@view_config(route_name='trends', renderer='templates/trends.jinja2')
def survey_information(request):
    SM_API_KEY = request.registry.settings['sm_api_key']
    SM_ACCESS_TOKEN = request.registry.settings['sm_access_token']

    survey_id = request.matchdict['survey_id']
    page = request.matchdict['page']
    question = request.matchdict['question']


    si = SurveyInformation(SM_API_KEY, SM_ACCESS_TOKEN)
    information = si.get_survey_question(survey_id, int(page), int(question))
    
    sr = SurveyResults(SM_API_KEY, SM_ACCESS_TOKEN, survey_id)
    respondents = sr.respondent_dictionary
    
    city = []
    state = []
    for respondent in respondents:
        city.append(respondent['location'].get('city', None))
        state.append(respondent['location'].get('region_code', None))

    cities_count = dict(Counter(city))
    states_count = dict(Counter(state))
    
    return {
            'information': information, 
            'respondents': respondents,
            'cities': cities_count,
            'states': states_count
            }

