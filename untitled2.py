from flask import Flask,session,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    a = {'short': 'krotki1', 'full': 'dlugi1'}
    b = {'short': 'krotki2', 'full': 'dlugi2'}
    c = {'short': 'krotki3', 'full': 'dlugi3'}
    linki = [a,b,c]
    return render_template('shortener.html',links = linki)


if __name__ == '__main__':
    app.run()
