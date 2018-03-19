"""
    file: config.py
    purpose: The location from which the application's configuration can be
             modified to be received downstream for all usages.
"""

import os

class Config(object):
    DATABASE = os.path.join(os.path.realpath(__file__), '..', 'asar-runtime.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asar'