#!/usr/bin/python3
"""
    file: app.py
    purpose: Holds the view for the Flask web application and handling of the
             database.
"""

import os
print(os.getcwd())

from .config import Config
import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, make_response, send_file
import os
from .simulation_settings import SimulationSettingsForm
import sqlite3
import threading


app = Flask(__name__)
app.config.from_object(Config)

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


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.cli.command('initdb')
def initdb_handler():
    """
    Make a call to initialize the database.
    """
    initializeDatabase()
    print("Initialized the " + __name__ + " database.")


@app.route('/', methods=['GET', 'POST'])
def command_console():
    """
    This function loads the resources into the HTML template for the GUI for
    using the web server.
    """
    form = SimulationSettingsForm()
    if form.validate_on_submit():
        danger = form.danger.data
        environment = form.environment.data
        return redirect('/configure', user_input=(danger, environment))
    return render_template('view.html', form=form)


@app.route('/configure', methods=['POST'])
def configure_simulation_from_gui(user_input):
    """
    Captures the form submission into the database. Needs the POST method for
    form submission.
    """
    backend_database = getDatabase(app.config['DATABASE'])
    cursor = backend_database.execute("""select state from settings
                                         order by time_set desc
                                         limit 1""")
    current_state = cursor.fetchall()
    print(current_state)
    # currently this will break because we don't have an initial setting of the state, which should be to STOPPED
    # TODO: Add route for setting the state
    backend_database.execute("""insert into settings
                                (time_set, danger, environment, state)
                                values (?, ?, ?, ?)""",
                             [datetime.datetime.now(),
                              user_input[0],
                              user_input[1],
                              current_state])


@app.route('/image_stream')
def most_recent_image():
    """
    This function opens the database to grab the most recent image taken to push
    to the client.
    """
    backend_database = getDatabase(app.config['DATABASE'])
    cursor = backend_database.execute('select image_path from images order by time_taken desc')
    image_data = cursor.fetchall()
    path_to_image = image_data[0][0]
    return send_file(path_to_image, attachment_filename='stream-latest.jpg')

@app.route('/add_image')
def add_image_in_db_for_prototyping():
    """
    Adds a hardcoded image to the database for testing purposes.
    """
    IMAGE_PATH = os.path.join(os.sep, 'home', 'ssnover', 'develop', 'msd-p18542', 'asar-pi-applications', 'asar_web_server', 'asar_web_server', 'static', 'hondas2000.jpg')
    backend_database = getDatabase(app.config['DATABASE'])
    backend_database.execute("""insert into images 
                                (image_path, time_taken) 
                                values (?, ?)""",
                             [IMAGE_PATH, datetime.datetime.now()])
    return redirect('/')


def main():
    """
    Runs the application on localhost:5000.
    """
    APP_WORKER_THREAD.start()


if __name__ == "__main__":
    main()
