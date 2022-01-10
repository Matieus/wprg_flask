from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "fdfyhsdiydf8dfyfdfgrtysfdfinlandfyfyudfoy"


@app.route("/loguot", methods=('GET', 'POST'))
def logout():
    ...


@app.route("/login", methods=('GET', 'POST'))
def login():
    login = request.form['login']
    password = request.form['pass']
    if password == "abc":

        ...
    else:
        return render_template('index.html', value=writtenlog, value1='Incorrect Password')


@app.route("/")
@app.route("/home")
def home():
    return render_template(...)


@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route("/index")
def index_page():
    return render_template('index.html')


@app.route('/zad1', methods=('GET', 'POST'))
def zad1():
    return 'You said:{}'.format(request.form['freetext'])


@app.route('/zad2', methods=('GET', 'POST'))
def zad2():
    a = float(request.form['firstnumber'])
    b = float(request.form['secondnumber'])
    char = (request.form['znaki'])
    result = 0
    if char == 'dodawanie':
        result = a + b
    elif char == 'odejmowanie':
        result = a - b
    elif char == 'mnozenie':
        result = a * b
    elif char == 'dzielenie' and b != 0:
        result = a / b
    elif char == 'dzielenie' and b == 0:
        result = 'error'
    return str(result)


@app.route('/zad3', methods=('GET', 'POST'))
def zad3():
    correctpass = "abc"
    writtenlog = request.form['login']
    writtenpass = request.form['pass']
    if correctpass == writtenpass:
        return render_template('index2.html')
    else:
        return render_template('index.html', value=writtenlog, value1='Incorrect Password')


if __name__ == '__main__':
    app.run()