#! coding: utf-8

# For small applications it’s a possibility to drop the configuration directly into the module which we will be doing here. However a cleaner solution would be to create a separate .ini or .py file and load that or import the values from there.

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True  # If set to true, user can execute code on server.
SECRET_KEY = 'development key'  # Intend to keep client-side session secure, should be complex
USERNAME = 'admin'
PASSWORD = 'default'

# create our Little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Alternative for from_object to read from config files stored in var FLASKR_SETTINGS
# slient=True means if FLASKR_SETTINGS var doesn't exists, don't through error
app.config.from_envvar("FLASKR_SETTINGS", silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


# create sql_db with python libs
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()  # g object works well for threaded environments


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')  # I guess this does the url mapping job like rules in nginx.
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')  # This is sqlite query statement?
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


# Be sure to use question marks when building SQL statements, as done in the example below. Otherwise, your app will be vulnerable to SQL injection when you use string formatting to build SQL statements.
# TODO 下面函数里SQL语句里的`? ?`是如何防止了SQL注入的？
@app.route('/add', methods=['POST'])  # Accept specified HTTP method only
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    # it seems ? ? in below statement refers to requst.form['title'] and requst.form['text']
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()  # TODO what does commit do?
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))  # This seems could find the url in the app.route decorator for specified function names


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You were logged out")
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
