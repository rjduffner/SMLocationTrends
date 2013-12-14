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

@app.route('/', methods=['GET'])
def index():
    pages = 0
    if 'survey_id' in request.args.keys():
        survey_id = request.args['survey_id']
        si = SurveyInformation()
        pages = si.get_number_of_pages(survey_id)
        message = 'surveyfound!'
    else:
        message = 'Hello'
    return render_template('index.html', message=message, pages=pages)

@app.route('/survey/pages/<survey_id>/<nonsense>', methods=['GET'])
def get_survey_pages(survey_id, nonsense):
    si = SurveyInformation()
    pages = si.get_number_of_pages(survey_id)
    print nonsense
    return jsonify({ 'pages': pages })


@app.route('/add_keys', methods=['POST'])
def add_keys():
    db = get_db()
    db.execute('insert into keys (text) values (?)', [request.form['key']])
    db.commit()
    #flash('New entry was successfully posted')
    return redirect(url_for('home_page'))

    
'''
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
'''

if __name__ == '__main__':
    init_db()
    app.run()
