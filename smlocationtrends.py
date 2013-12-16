"""
"""

from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify

from surveyinformation import SurveyInformation 

# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE='/tmp/flaskr.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

'''
@app.route('/', methods=['GET'])
def index():
    pages = 0
    question_dict = {}
    survey_id = None
    if 'survey_id' in request.args.keys():
        survey_id = request.args['survey_id']
        si = SurveyInformation()
        pages = si.get_number_of_pages(survey_id)
        question_dict = {}
        for page in range(pages):
            questions =  si.get_number_of_questions_on_page(survey_id, page)
            question_dict[page] = questions
        print question_dict
        message = 'surveyfound!'
    else:
        message = 'Hello'
    return render_template('index.html', message=message, pages=pages, questions=question_dict, survey_id=survey_id)
'''

@app.route('/', methods=['GET'])
def index():
    pages = 0
    question_dict = {}
    survey_id = None
    if 'survey_id' in request.args.keys():
        survey_id = request.args['survey_id']
        si = SurveyInformation()
        pages = si.get_number_of_pages(survey_id)
        question_dict = {}
        for page in range(pages):
            questions =  si.get_number_of_questions_on_page(survey_id, page)
            question_dict[page] = questions
        print question_dict
        message = 'surveyfound!'
    else:
        message = 'Hello'
    return render_template('index.html', message=message, pages=pages, questions=question_dict, survey_id=survey_id)

@app.route('/question/<survey_id>/<page>/<question>', methods=['GET'])
def survey_information(survey_id, page, question):
    si = SurveyInformation()
    information = si.get_survey_question(survey_id, int(page), int(question))
    return render_template('survey.html', information=information)

if __name__ == '__main__':
    init_db()
    app.run()
