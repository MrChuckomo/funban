"""
File         : routes.py
Description  :

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 02-Dec-2021
"""

from index import app
from flask import url_for
from flask import redirect
from flask import render_template
from tinydb import TinyDB


# ---------------------------------------------------------------------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    db = TinyDB(f'{app.config["RES_FOLDER"]}config.json')

    boards = db.table('boards')
    profiles = db.table('profiles')

    return render_template(
        'home.html',
        app_title='Funban Home',
        active_home='active',
        all_boards=boards.all(),
        profile=profiles.get(doc_id=1),
    )

@app.route('/setup', methods=['GET'])
def setup():
    return render_template(
        'setup.html',
        app_title='Funban Setup',
        active_setup='active',
    )
