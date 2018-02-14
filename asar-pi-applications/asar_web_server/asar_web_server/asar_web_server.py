"""
    file: app.py
    purpose: Holds the view for the Flask web application and handling of the
             database.
"""

import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, make_response
from functools import wraps, update_wrapper
import os
import sqlite3
import threading


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, '..', 'asar-runtime.db')
))
app.config.from_envvar('ASAR_SETTINGS', silent=True)

APP_WORKER_THREAD = threading.Thread(target=app.run, name="ASAR Web Application Server Thread")


def connectDatabase(db_path):
    """
    Connects to the application database.
    """
    rv = sqlite3.connect(db_path)
    rv.row_factory = sqlite3.Row
    return rv


def getDatabase(db_path):
    """
    Opens a new database connection if one is not open yet from the application globals.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connectDatabase(db_path)
    return g.sqlite_db


@app.teardown_appcontext
def closeDatabase(error):
    """
    Closes the database again at the end of the request.
    """
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def initializeDatabase():
    db = getDatabase(app.config['DATABASE'])
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def nocache(view):
    """
    https://arusahni.net/blog/2014/03/flask-nocache.html
    """
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)


@app.cli.command('initdb')
def initdb_handler():
    """
    Make a call to initialize the database.
    """
    initializeDatabase()
    print("Initialized the " + __name__ + " database.")


@app.cli.command('run')
def run_handler():
    """
    Make a call to run the application.
    """
    print("Initializing and running the ASAR Web Server...")
    APP_WORKER_THREAD.start()
    return


@app.cli.command('stop')
def stop_handler():
    """
    Make a call to stop the application from running.
    """
    print("Tearing down the ASAR Web Server...")
    print("Done.")
    return


@app.route('/')
@nocache
def command_console():
    """
    This function loads the resources into the HTML template for the GUI for
    using the web server.
    """
    return render_template('view.html')


def main():
    """
    Runs the application on localhost:5000.
    """
    APP_WORKER_THREAD.start()


if __name__ == "__main__":
    main()
