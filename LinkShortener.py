# -*- coding: <utf-8> -*-
from flask import Flask, request, redirect, render_template, session
from werkzeug.debug import DebuggedApplication

# app_url = '/okraskaj/urlshortener'
app_url = ''
app = Flask(__name__)
app.secret_key = '$a&*F*Gd#!s#(FGH&*@#DSc'

app.debug = True
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

links = {}
users = {'admin': 'admin'}


@app.route(app_url + '/')
def index():
    session.pop('username', None)
    if 'username' not in session:
        return redirect(app_url + "/login")
    else:
        username = session['username']
        return render_template('login_success', username=username)


@app.route('/mojelinki', methods=['GET', 'POST'])
def moje_linki():
    request.get_data()
    return render_template('moje_linki.html', links=linki_usera)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        session.pop('username', None)

    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        global links
        links[username] = {}
        # tworzymy uzytkownikowi slownik jego linkow

        if username not in session:
            if username in users:
                if users[username] == password:
                    session[username] = username
                    return render_template('login_succes.html', username=username)
                else:
                    return render_template('login_failure.html',username=username, reason= 'pass')
            else:
                return render_template('login_failure.html',username= username, reason = 'username')




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username not in users:
            #rejestracja
            users[username]= password
            #logowanie
            session[username] = username
            render_template('register_succes.html', username=username)
        else:
            return render_template('register_failure.html', username=username)



    return render_template('register.html')


if __name__ == '__main__':
    app.run()
