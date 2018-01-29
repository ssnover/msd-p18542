"""
    file: app.py
    purpose: Holds the view for the Flask web application and handling of the
             database.
"""

from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import os
import sqlite3


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, '..', 'asar-runtime.db')
))
app.config.from_envvar('ASAR_SETTINGS', silent=True)


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


@app.cli.command('initdb')
def initdb_handler():
    """
    Make a call to initialize the database.
    """
    initializeDatabase()
    print("Initialized the " + __name__ + " database.")


@app.route('/')
def command_console():
    """
    This function loads the resources into the HTML template for the GUI for
    using the web server.
    """
    return "Hello world!"


def main():
    """
    Runs the application on localhost:5000.
    """
    app.run()


if __name__ == "__main__":
    main()