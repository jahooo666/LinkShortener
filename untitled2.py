from flask import Flask,session,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    a = {'krotki1': 'dlugi1'}
    a = {'krotki2': 'dlugi2'}
    a = {'krotki3': 'dlugi3'}
    return render_template('shortener.html', links = a)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
