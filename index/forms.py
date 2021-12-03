"""
File         : forms.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 03-Dec-2021
"""

from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms import RadioField
from wtforms import SubmitField


# ---------------------------------------------------------------------------------------------------------------------

class SimpleForm(FlaskForm):
    name = TextField('Name')
    gender = RadioField('Gender', choices=[('M', 'male'), ('F', 'female')])
    submit = SubmitField('Send')
