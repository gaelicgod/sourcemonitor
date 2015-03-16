from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.pymongo import PyMongo

import json, urllib, datetime 

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
DB_NAME = 'source-control'


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.name = 'source-control'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/'
#app.config['MONGO_DBNAME'] = 'source-control'

client = PyMongo(app)

#users = client.db.users
#projects = client.db.projects


@app.route('/')
def index():
    if 'username' in session:
        return render_template('source_list.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = client.db.users.find_one({ "username": username })

        if(user is not None):
            if(user["password"] == password):
                print(user)
                session['username'] = user["username"]
                session['email'] = user['email']
                flash('Login successful')
                return redirect(url_for('index'))
            else:
                error = "Invalid Password!"
        else:
            error = "Invalid Username!"
    
    return render_template('show_login.html', error=error)
    

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
