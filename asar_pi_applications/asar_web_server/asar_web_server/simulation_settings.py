"""
    file: simulation_settings.py
    purpose: Defines a Flask WTForm for setting up and submitting user settigns
             from the web GUI.
"""

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class SimulationSettingsForm(FlaskForm):
    danger = SelectField('Danger',
                         choices=[(1, 'Safe'), (2, 'Precarious'), (3, 'Impending Doom')])
    environment = SelectField('Simulation',
                              choices=[(1, 'Forest Fire'), (2, 'Blizzard')])
    submit = SubmitField('Configure')