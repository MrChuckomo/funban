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
from flask import request
from flask import render_template
from tinydb import TinyDB

from index.forms import BoardForm
from index.forms import ProfileForm


# ---------------------------------------------------------------------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    board_id = request.args.get('board_id')

    if board_id:
        board_id = int(board_id)
    else:
        board_id = 1

    db = TinyDB(f'{app.config["RES_FOLDER"]}config.json')
    boards = db.table('boards')
    profiles = db.table('profiles')

    return render_template(
        'home.html',
        app_title='Funban Home',
        active_home='active',
        all_boards=boards.all(),
        active_board=boards.get(doc_id=board_id),
        profile=profiles.get(doc_id=boards.get(doc_id=board_id)['profile_id']),
    )

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    db = TinyDB(f'{app.config["RES_FOLDER"]}config.json')
    boards = db.table('boards')
    profiles = db.table('profiles')

    board_form = BoardForm()
    profile_form = ProfileForm()

    if request.method == 'POST' and 'submit_board' in request.form:
        print(board_form.name.data)
        print(board_form.profile.data)
        print(board_form.task_color.data)

    for profile in profiles.all():
        board_form.profile.choices.append((profile.doc_id, profile['name']))

    return render_template(
        'setup.html',
        app_title='Funban Setup',
        active_setup='active',
        all_boards=boards.all(),
        all_profiles=profiles.all(),
        board_form=board_form,
        profile_form=profile_form
    )


# ---------------------------------------------------------------------------------------------------------------------
# NOTE: Redirect Links

@app.route('/add_issue', methods=['GET'])
def add_issue():
    lane = request.args.get('lane')
    board_id = request.args.get('board_id')

    return redirect(
        url_for('home', board_id=board_id)
    )
