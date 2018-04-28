"""
    file: config.py
    purpose: The location from which the application's configuration can be
             modified to be received downstream for all usages.
"""

import os

class GUI_CONSTANTS(object):
    DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'asar-runtime.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asar'

DANGER = {
    'SAFE'              : 1,
    'PRECARIOUS'        : 2,
    'IMPENDING DOOM'    : 3,
}

ENVIRONMENT = {
    'FOREST FIRE'  : 1,
    'BLIZZARD'     : 2,
}

STATE = {
    'STOPPED'   : 0,
    'RUNNING'   : 1,
    'PAUSED'    : 2,
}
