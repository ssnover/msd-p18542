#!/usr/bin/python3
"""
    file: app.py
    purpose: Holds the view for the Flask web application and handling of the
             database.
"""

from .gui_constants import GUI_CONSTANTS, DANGER, ENVIRONMENT, STATE
import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, make_response, send_file
import os
from .simulation_settings import SimulationSettingsForm
import sqlite3
import threading


app = Flask(__name__)
app.config.from_object(GUI_CONSTANTS)
SAMPLE_IMAGE_PATH = os.path.join(os.sep, 'home', 'ssnover', 'develop', 'msd-p18542', 'asar_pi_applications', 'asar_web_server', 'asar_web_server', 'static', 'hondas2000.jpg')
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
    # Initial settings for application state
    update_settings(DANGER['SAFE'], ENVIRONMENT['FOREST FIRE'], STATE['STOPPED'])


@app.route('/', methods=['GET', 'POST'])
def command_console():
    """
    This function loads the resources into the HTML template for the GUI for
    using the web server.
    """
    form = SimulationSettingsForm(request.form)

    if request.method == 'POST':
        # get the current settings and replace with form submission
        settings = get_current_settings()
        if (settings[2] == STATE['STOPPED']):
            update_settings(form.danger.data, form.environment.data, settings[2])
        else:
            print("Invalid: User tried to change settings during simulation.")

    return render_template('view.html', form=form)


@app.route('/set_state', methods=['POST'])
def update_simulation_state():
    """
    Update the state of the simulation in the database.
    """
    button_clicked = request.form['button_clicked']
    settings = get_current_settings()
    # assume the state won't change by default
    new_state = settings[2]

    if (settings[2] == STATE['STOPPED']):
        if button_clicked == 'play':
            new_state = STATE['RUNNING']
    elif (settings[2] == STATE['RUNNING']):
        if button_clicked == 'stop':
            new_state = STATE['STOPPED']
        elif button_clicked == 'pause':
            new_state = STATE['PAUSED']
    elif (settings[2] == STATE['PAUSED']):
        if button_clicked == 'play':
            new_state = STATE['RUNNING']
        elif button_clicked == 'stop':
            new_state = STATE['STOPPED']

    update_settings(settings[0], settings[1], new_state)
    return redirect('/')


@app.route('/get_state', methods=["GET"])
def get_current_state():
    """
    """
    settings = get_current_settings()
    state = "error"
    if settings[2] == STATE['STOPPED']:
        state = "stopped"
    elif settings[2] == STATE['RUNNING']:
        state = "running"
    elif settings[2] == STATE['PAUSED']:
        state = "paused"
    return state


@app.route('/image_stream')
def most_recent_image():
    """
    This function opens the database to grab the most recent image taken to push
    to the client.
    """
    image_path = get_most_recent_image()
    if image_path:
        print("Sending off the most recent image.")
        return send_file(image_path, mimetype='image/jpeg')
    else:
        print("Sending the default image.")
        return send_file(SAMPLE_IMAGE_PATH, mimetype='image/jpeg')


@app.route('/add_image')
def add_image_in_db_for_prototyping():
    """
    Adds a hardcoded image to the database for testing purposes.
    """
    IMAGE_PATH = os.path.join(os.sep, 'home', 'ssnover', 'develop', 'msd-p18542', 'asar-pi-applications', 'asar_web_server', 'asar_web_server', 'static', 'hondas2000.jpg')
    add_image_to_database(IMAGE_PATH)
    return redirect('/')


def update_settings(danger, environment, state):
    """
    Utility method for setting values in the database.
    """
    print("Updating the settings for the simulation.")
    backend_database = getDatabase(app.config['DATABASE'])
    backend_database.execute("""insert into settings
                                (time_set, danger, environment, state)
                                values (?, ?, ?, ?)""",
                             [datetime.datetime.now(),
                              danger,
                              environment,
                              state])
    backend_database.commit()


def get_current_settings():
    """
    Utility method to retrieve a tuple of the current simulation settings.

    Returns: The settings in order of (danger, environment, state)
    """
    backend_database = getDatabase(app.config['DATABASE'])
    cursor = backend_database.execute("""select danger, environment, state from settings
                                         order by time_set desc
                                         limit 1""")
    current_settings = cursor.fetchall()[0]
    return current_settings


def add_image_to_database(path_to_image):
    """
    Utility method for adding image to database.
    """
    backend_database = getDatabase(app.config['DATABASE'])
    backend_database.execute("""insert into images
                                (image_path, time_taken)
                                values (?, ?)""",
                             [path_to_image, datetime.datetime.now()])
    backend_database.commit()


def get_most_recent_image():
    """
    Utility method grabbing the most recent image from the database.
    """
    backend_database = getDatabase(app.config['DATABASE'])
    cursor = backend_database.execute("""select image_path from images
                                         order by time_taken desc
                                         limit 1""")
    result = cursor.fetchall()
    if len(result) > 0:
        return result[0][0]
    else:
        return None


def main():
    """
    Runs the application on localhost:5000.
    """
    #APP_WORKER_THREAD.start()
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()
