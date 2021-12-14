"""
File         : forms.py
Description  :

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 03-Dec-2021
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import RadioField
from wtforms import SelectField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms.widgets import ColorInput


# ---------------------------------------------------------------------------------------------------------------------

class BoardForm(FlaskForm):
    name = StringField('Board Name')
    profile = SelectField('Profile', choices=[])
    task_color = StringField('Task Color')
    submit_board = SubmitField('Apply')

class ProfileForm(FlaskForm):
    name = StringField('Profile Name')
    lane_name = StringField('Lane Name')
    lane_icon = RadioField('Lane Icon', choices=[('one', 'one'), ('two', 'two')])
    is_archive_lane = BooleanField('Is Archive Lane')
    submit_profile = SubmitField('Apply')
