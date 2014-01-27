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
from locationinformation import LocationInformation


SM_API_KEY='pcpuk2dfxdwggu6gfssxqa6t'
SM_ACCESS_TOKEN='UFHR1aBDl2QjFoOzyDhoj91aM1Q3Atp-HtOvcI8kBk.HIBEdrGLtGKLnbSmHGcE-cNkJnPOaR1t-jiJqrE3iqUwObKHbg3NuTB-u5W6w9bg='

@view_config(route_name='home', renderer='templates/index.jinja2')
def index(request):
    params = dict(request.GET)
    if 'survey_id' in params:
        return HTTPFound(location='/survey/'+ request.GET['survey_id'])
    return {'project': 'smlocationtrends'}

@view_config(route_name='survey', renderer='templates/survey.jinja2')
def survey(request):
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
    
    survey_id = request.matchdict['survey_id']
    page = request.matchdict['page']
    question = request.matchdict['question']

    si = SurveyInformation(SM_API_KEY, SM_ACCESS_TOKEN)
    information = si.get_survey_question(survey_id, int(page), int(question))
    
    sr = SurveyResults(SM_API_KEY, SM_ACCESS_TOKEN, survey_id)
    respondents = sr.respondent_dictionary

    return {
            'information': information, 
            'respondents': respondents
            }

