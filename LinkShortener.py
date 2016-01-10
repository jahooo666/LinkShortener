# -*- coding: <utf-8> -*-
import random
from flask import Flask, request, redirect, render_template, session
from werkzeug.debug import DebuggedApplication

app_url = '/okraskaj/urlshortener'
#app_url = ''
app = Flask(__name__)
app.secret_key = '$a&*F*Gd#!s#(FGH&*@#DSc'

app.debug = True
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

links = {}
users = {'admin': 'admin'}
users_links={}
users_links['admin'] = {}

@app.route(app_url + '/', methods=['POST','GET'])
def index():
    if 'username' not in session:
        return redirect(app_url + "/login")
    else:
        username = session['username']
        if request.method == 'POST':
            long = request.form.get('long')
            short = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPRSTUWXYZabcdefghijklmnoprstuwxyz') for i in range(6))
            while(short in links.keys()):
                short = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPRSTUWXYZabcdefghijklmnoprstuwxyz') for i in range(6))
            print short
            links[short]=long
            users_links[username][short]=long
            return render_template('shortener.html', username=username, links=users_links[username])
        elif request.method== 'GET':
            return render_template('shortener.html', username=username, links=users_links[username])

    #session.pop('username', None)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # global links
        # links[username] = {}
        # tworzymy uzytkownikowi slownik jego linkow
        if username in users:
            if users[username] == password:
                session['username'] = username
                return render_template('login_succes.html',username= username)
            else:
                return render_template('login_failure.html',username=username, reason='pass')
        else:
            return render_template('login_failure.html',username=username, reason='username')




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username not in users:
            # rejestracja
            users[username] = password
            users_links[username]={}
            # logowanie
            session[username] = username
            render_template('register_succes.html', username=username)
        else:
            return render_template('register_failure.html', username=username)

    return render_template('register.html')

@app.route(app_url+'/<url_code>',methods=['GET','POST'])
def redirect_link(url_code):
    link = links[url_code]
    return redirect(link)


if __name__ == '__main__':
    app.run()