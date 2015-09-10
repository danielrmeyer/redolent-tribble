from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash
from sqlalchemy import create_engine, Table, Column, Integer, String, \
MetaData, ForeignKey
from sqlalchemy.sql import select

DATABASE = 'demodb'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'dbuser'
PASSWORD = 'dbpass'
DBHOST = '10.0.0.10'
DBPORT = '5432'
CONNECTION_STRING = \
    'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}'.format(
    username=USERNAME,password=PASSWORD,host=DBHOST,port=DBPORT,db=DATABASE
)

engine = create_engine(CONNECTION_STRING, echo=True)

metadata = MetaData()
entries = Table('entries', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('text', String, nullable=False)
    )

metadata.create_all(engine)

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_entries():
    with engine.connect() as conn:
        s = select([entries])
        result = conn.execute(s)
        rows = [row for row in result]
        return str(rows)


@app.route('/add', methods=['POST'])
def add_entry():
    with engine.connect() as conn:
        ins = entries.insert()
        result = conn.execute(ins, title=request.form['title'],
            text=request.form['text'])
        flash("new entry was successfully posted")
        return redirect(url_for('show_entries'))

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
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == "__main__":
    app.debug = DEBUG
    app.run(host='0.0.0.0', port=80)
