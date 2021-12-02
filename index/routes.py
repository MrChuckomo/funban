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


# ---------------------------------------------------------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template(
        'base.html',
        app_title='Template App'
    )
