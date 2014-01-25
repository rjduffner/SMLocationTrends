"""

Author: Robert Duffner
Date: January 14, 2013
Email: rjduffner@gmail.com

smlocationtrends.py

"""
from pyramid.view import view_config

from surveyinformation import SurveyInformation
from surveyresults import SurveyResults
from locationinformation import LocationInformation


SM_API_KEY='pcpuk2dfxdwggu6gfssxqa6t'
SM_ACCESS_TOKEN='UFHR1aBDl2QjFoOzyDhoj91aM1Q3Atp-HtOvcI8kBk.HIBEdrGLtGKLnbSmHGcE-cNkJnPOaR1t-jiJqrE3iqUwObKHbg3NuTB-u5W6w9bg='

@view_config(route_name='home', renderer='templates/index.jinja2')
def index(request):
    print dir(request)
    '''
    if 'survey_id' in request.args.keys():
        return redirect(url_for('survey', survey_id=request.args['survey_id']))
    '''
    #return render_template('index.jinja2')
    return {'project': 'smlocationtrends'}

@view_config(route_name='survey', renderer='templates/survey.jinja2')
def survey(request):
    si = SurveyInformation(SM_API_KEY, SM_ACCESS_TOKEN)
    pages, question_dict = si.get_survey_page_count_and_questions(survey_id)
    return render_template('survey.jinja2', pages=pages, questions=question_dict, survey_id=survey_id)

@view_config(route_name='trends', renderer='templates/trends.jinja2')
def survey_information(request):
    si = SurveyInformation(SM_API_KEY, SM_ACCESS_TOKEN)
    information = si.get_survey_question(survey_id, int(page), int(question))
    sr = SurveyResults(SM_API_KEY, SM_ACCESS_TOKEN, survey_id)
    respondents = sr.respondent_dictionary
    ip_list = []
    for i in respondents:
        ip_list.append(i['ip_address'])
    li = LocationInformation(ip_list)
    locations = li.ip_dictionary
    return render_template('trends.jinja2', information=information, respondents=respondents, locations=locations)

